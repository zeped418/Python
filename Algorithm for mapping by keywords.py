# Librerías necesarias para manejar datos, expresiones regulares, interfaz gráfica y operaciones matemáticas
import pandas as pd  # Para manejar estructuras de datos tipo DataFrame
import numpy as np  # Para operaciones numéricas y dividir bloques
import re  # Para limpieza de texto usando expresiones regulares
import os  # Para manipular rutas y archivos
import time  # Para medir duración del proceso
import tkinter as tk  # Para interfaz gráfica de usuario
from tkinter import filedialog, messagebox, ttk  # Módulos específicos para GUI
from math import ceil  # Redondeo hacia arriba para dividir en bloques

# -----------------------------
# FUNCIÓN PRINCIPAL
# -----------------------------
def buscar_regla_V2_batch(df_datos, df_mapeo, progress_label=None):
    """
    Esta función procesa datos financieros y aplica reglas de mapeo para clasificar registros.
    Utiliza coincidencias por código (OU, CC, CTA) y palabras clave para encontrar la mejor regla
    y asignar clasificaciones a cada registro de entrada.
    """

    # --------------------------------
    # ETAPA 1: LIMPIEZA DE DATOS
    # --------------------------------

    # Elimina espacios en los nombres de columnas para evitar errores de coincidencia
    df_mapeo.columns = df_mapeo.columns.str.strip()
    df_datos.columns = df_datos.columns.str.strip()

    # Estándariza nombres de columnas clave para que coincidan en ambos DataFrames
    df_mapeo.rename(columns={'Centro de coste': 'CC', 'Clase de coste': 'CTA'}, inplace=True)
    df_datos.rename(columns={'Centro de coste': 'CC', 'Clase de coste': 'CTA'}, inplace=True)

    # Limpieza y conversión de valores clave a texto uniforme para evitar errores de tipo
    for col in ['OU', 'CC', 'CTA']:
        # Convierte a string, elimina espacios y reemplaza valores faltantes
        df_mapeo[col] = df_mapeo[col].astype(str).str.strip().replace(['nan', 'NaN', 'None', ''], '')
        df_mapeo[col] = df_mapeo[col].apply(lambda x: str(int(float(x))) if x.replace('.', '', 1).isdigit() and float(x).is_integer() else x)

        df_datos[col] = df_datos[col].astype(str).str.strip().replace(['nan', 'NaN', 'None', ''], '')
        df_datos[col] = df_datos[col].apply(lambda x: str(int(float(x))) if x.replace('.', '', 1).isdigit() and float(x).is_integer() else x)

    # Limpieza de palabras clave (keywords): se convierten a minúsculas, se quitan espacios extra
    keywords_cols = ['Keyword 1', 'Keyword 2', 'Keyword 3']
    for col in keywords_cols:
        df_mapeo[col] = df_mapeo[col].fillna('').astype(str).apply(lambda x: re.sub(r'\s+', ' ', x.strip().lower())).str.strip()
        # re.sub(r'\s+', ' ', x.strip().lower()) reemplaza uno o más espacios en blanco consecutivos por un solo espacio ' '
        # después de quitar espacios al principio y al final con x.strip() y convertir a minúsculas con .lower().

    # Renombra los campos destino para distinguirlos de los datos de entrada
    target_cols = ['Vendor', 'Concept', 'MainExpenseType', 'Type2', 'Exp2', 'Exp1',
                   'Layer', 'PL3', 'HQ_MU', 'Scope', 'Acc_Name', 'Funding_Bucket', 'Project',
                   'Function', 'Area', 'Resp', 'IT_Lead', 'Bucket2', 'Smart_Spending', 'Adj_Type']
    df_mapeo = df_mapeo.rename(columns={col: f"{col}_map" for col in target_cols})

    # Crea un campo de texto combinado para análisis semántico usando columnas relevantes
    campos_texto = ['Denominación del objeto', 'Denom.clase de coste', 'Texto de pedido',
                    'Texto de cabecera de documento', 'Denominación', 'Denom.cuenta contrapartida',
                    'Denominacion cuenta contrapartida', 'Denominación del objeto del interlocutor',
                    'Objeto', 'Proveedor', 'Asignacion', 'Texto', 'Referencia', 'Objeto del interlocutor']
    campos_texto = [col for col in campos_texto if col in df_datos.columns]
    df_datos['input_text'] = df_datos[campos_texto].fillna('').astype(str).agg(' '.join, axis=1).str.lower()

    # --------------------------------
    # ETAPA 2: PROCESAMIENTO EN BLOQUES
    # --------------------------------

    resultados = []
    # Divide el dataset en bloques de 1000 registros para mejorar el rendimiento
    bloques = np.array_split(df_datos, ceil(len(df_datos) / 1000))
    total_bloques = len(bloques)

    # Procesa cada bloque de forma iterativa
    for i, bloque in enumerate(bloques):
        if progress_label:
            progress_label.config(text=f"Procesando bloque {i+1} de {total_bloques}...")
            progress_label.update()

        bloque_resultados = []

        # Procesa fila por fila dentro del bloque
        for _, fila in bloque.iterrows():
            input_ou = fila.get('OU', '')
            input_cc = fila.get('CC', '')
            input_cta = fila.get('CTA', '')
            input_text = fila.get('input_text', '')

            # Filtra reglas que coinciden con la OU actual o estén vacías (genéricas) con isin(lista de palabras)
            df_filtrado = df_mapeo[
                (df_mapeo['OU'].isin(['', input_ou])) &
                (df_mapeo['CC'].isin(['', input_cc])) &
                (df_mapeo['CTA'].isin(['', input_cta]))
            ].copy()

            # Define cómo se calcula la puntuación de coincidencia
            def puntaje_coincidencia(row):
                score = 0  # Puntos acumulados

                # Limpieza individual de cada palabra clave
               
                def clean_keyword(value):
                    try:
                        if pd.isna(value): # celdas vacías las devuelve como ''
                            return ''
                        f = float(value)
                        return str(int(f)) if f.is_integer() else str(f) # los cecos o cuentas se conviernten en texto
                    except:
                        return str(value).strip().lower()  # de los textos se remueven espacios y convierte en minúsculas

                # Lista de palabras clave limpias
                keywords = [clean_keyword(row.get(k)) for k in keywords_cols]

                # Revisa si las keywords están presentes en el texto de entrada
                for k in keywords:
                    if k in input_text and k:
                        score += 2
                    elif k:
                        score -= 2

                # Coincidencia por código OU
                row_ou = str(row.get('OU', '')).strip()
                if row_ou == '':
                    score += 1  # genérica cuando en el catálogo esta vacío
                elif row_ou == input_ou:
                    score += 2

                # Coincidencia por código CC (más fuerte)
                row_cc = str(row.get('CC', '')).strip()
                if row_cc == '':
                    score += 1
                elif row_cc == input_cc:
                    score += 3
                else:
                    return 0  # si no coincide exactamente, se descarta

                # Coincidencia por código CTA (más fuerte aún)
                row_cta = str(row.get('CTA', '')).strip()
                if row_cta == '':
                    score += 1
                elif row_cta == input_cta:
                    score += 5
                else:
                    return 0 # si no coincide exactamente, se descarta

                return score

            # Aplica la función de puntuación a todas las reglas filtradas
            df_filtrado['Score'] = df_filtrado.apply(puntaje_coincidencia, axis=1)

            # Se quedan solo reglas con score > 3
            df_filtrado = df_filtrado[df_filtrado['Score'] > 3].copy()
            # df_filtrado['Points'] = df_filtrado['Score'].apply(lambda s: s // 2)

            # Si hay coincidencias, se toma la mejor
            if not df_filtrado.empty:
                fila_match = df_filtrado.sort_values(by='Score', ascending=False).iloc[0]
                resultado = {
                    'OU': input_ou,
                    'CC': input_cc,
                    'CTA': input_cta,
                    'input_text': input_text,
                    'Score': fila_match.get('Score'),
                    'Rule_ID': fila_match.get('Rule_ID', ''),
                    'Vendor': fila_match.get('Vendor_map', ''),
                    'Concept': fila_match.get('Concept_map', ''),
                    'MainExpenseType': fila_match.get('MainExpenseType_map', '')
                    # ...
                    # Se agrega el resto de columas con su valor
                }
            else:
                # Si no hay coincidencias, se llena con valores por defecto
                resultado = {
                    'OU': input_ou,
                    'CC': input_cc,
                    'CTA': input_cta,
                    'input_text': input_text,
                    'Points': 0,
                    'Rule_ID': 'No match',
                    'Vendor': '',
                    'Concept': '',
                    'MainExpenseType': ''
                    # ...
                    # Se agrega el resto de columas vacías
                }

            # Se agrega el resultado individual al bloque
            bloque_resultados.append(resultado)

        # Se agregan todos los resultados del bloque al total general
        resultados.extend(bloque_resultados)

    # Devuelve el DataFrame completo con los resultados de clasificación
    return pd.DataFrame(resultados)


# -----------------------------
# GUI DE TKINTER
# -----------------------------
# Esta parte permite al usuario cargar archivos y ver el progreso sin necesidad de usar código.

if __name__ == "__main__":
    # Se inicializa la ventana de Tkinter sin mostrar la principal
    root = tk.Tk()
    root.withdraw()

    # Muestra ventana de progreso
    progress_win = tk.Toplevel()
    progress_win.title("Procesando")
    progress_label = ttk.Label(progress_win, text="Iniciando...")
    progress_label.pack(padx=20, pady=10)
    progress_bar = ttk.Progressbar(progress_win, mode='indeterminate')
    progress_bar.pack(padx=20, pady=10)
    progress_bar.start()
    progress_win.update()

    # Solicita al usuario seleccionar el archivo de Excel
    messagebox.showinfo("Inicio", "Selecciona el archivo Excel con las hojas 'KSB1' y 'Mapeo'")
    file_path = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Excel files", "*.xlsx *.xlsm")])
    if not file_path:
        messagebox.showerror("Error", "No se seleccionó ningún archivo.")
        exit()

    start_time = time.time()

    # Lee las hojas requeridas
    df_datos = pd.read_excel(file_path, sheet_name="KSB1")
    df_mapeo = pd.read_excel(file_path, sheet_name="Mapeo")

    # Ejecuta la función de búsqueda de reglas
    progress_label.config(text="Ejecutando búsqueda de reglas...")
    progress_win.update()

    df_resultado = buscar_regla_V2_batch(df_datos, df_mapeo, progress_label)

    # Guarda el resultado como un nuevo archivo Excel
    output_path = os.path.splitext(file_path)[0] + "_Resultado.xlsx"
    df_resultado.to_excel(output_path, index=False)

    # Cierra barra de progreso y muestra mensaje final
    progress_bar.stop()
    progress_win.destroy()

    duration = time.time() - start_time
    messagebox.showinfo("Completado", f"✅ Archivo generado:\n{output_path}\nTiempo: {duration:.2f} segundos")
