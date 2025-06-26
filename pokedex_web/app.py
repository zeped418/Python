from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def get_pokemon_data(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "id": data["id"],
            "name": data["name"].title(),
            "height": data["height"] / 10,
            "weight": data["weight"] / 10,
            "types": [t["type"]["name"] for t in data["types"]],
            "abilities": [a["ability"]["name"] for a in data["abilities"]],
            "sprite": data["sprites"]["front_default"]
        }
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon_data = None

    if request.method == "POST":
        if 'search' in request.form:
            query = request.form["pokemon"]
            pokemon_data = get_pokemon_data(query)
        elif 'next' in request.form:
            current = int(request.form["current_id"])
            pokemon_data = get_pokemon_data(current + 1)
        elif 'prev' in request.form:
            current = int(request.form["current_id"])
            if current > 1:
                pokemon_data = get_pokemon_data(current - 1)
    else:
        # Primera vez que se abre la página (GET)
        pokemon_data = get_pokemon_data(1)

    return render_template("index.html", pokemon=pokemon_data)
