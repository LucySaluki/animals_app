from flask import Flask, Blueprint, request, render_template, redirect
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository
from models.animal import Animal
from models.owner import Owner


app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/animals')

@app.route('/animals')
def animals():
    animals = animal_repository.select_all()
    return render_template('index.html', animals=animals)

@app.route("/animals/new")
def new_animal():
    owners = owner_repository.select_all()
    return render_template('new.html', owners = owners)


@app.route("/animals", methods = ["POST"])
def create_animal():
    name = request.form["name"]
    species = request.form["species"]
    breed = request.form["breed"]
    owner_id = request.form["owner_id"]
    owner = owner_repository.select(owner_id)
    new_animal = Animal(name, species, breed, owner)
    animal_repository.save(new_animal)
    return redirect("/animals")

@app.route("/animals/<id>")
def show_animal(id):
    animal = animal_repository.select(id)
    return render_template("/show.html", animal=animal)

if __name__ == '__main__':
    app.run(debug=True)
