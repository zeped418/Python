import requests

def get_pokemon_data(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Pokémon no encontrado. Verifica el nombre o número.")
        return None

def show_pokemon_info(data):
    name = data["name"].title()
    height = data["height"] / 10  # decímetros a metros
    weight = data["weight"] / 10  # hectogramos a kg
    types = [t["type"]["name"] for t in data["types"]]
    abilities = [a["ability"]["name"] for a in data["abilities"]]

    print(f"\n📛 Nombre: {name}")
    print(f"📏 Altura: {height} m")
    print(f"⚖️  Peso: {weight} kg")
    print(f"🔰 Tipo(s): {', '.join(types)}")
    print(f"✨ Habilidades: {', '.join(abilities)}")

def main():
    while True:
        pokemon = input("🔍 Ingresa el nombre o número del Pokémon (o escribe 'salir'): ")
        if pokemon.lower() == 'salir':
            break

        data = get_pokemon_data(pokemon)
        if data:
            show_pokemon_info(data)

if __name__ == "__main__":
    main()
