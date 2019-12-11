from flask import Flask, render_template, request
from marvel import getMarvelCharacter

app = Flask("MyApp")


@app.route("/")
def index():
    return render_template("index.html")


# We need a route to handle the form data coming from the html pack
# Need to make sure the methods match and the / route matches the action in the form
@app.route("/lookup", methods=['POST'])
def lookup():
    # Pull the form data from the request object
    form_data = request.form
    print(form_data)

    isHawkeye = form_data['arrows'] == 'yes'
    isIronman = form_data['iron'] == 'yes'
    isCaptainAmerica = form_data['america'] == 'yes'
    isTheHulk = form_data['temper'] == 'yes'

    if isHawkeye:
        name = "Hawkeye"
    elif isIronman:
        name = "Iron man"
    elif isCaptainAmerica:
        name = "Captain America"
    elif isTheHulk:
        name = "Hulk"
    else:
        name = "squirrel girl"

    character = getMarvelCharacter(name)

    result = {"imageUrl": character, "name":name}
    return render_template("character.html", result=result)


app.run(debug=True)
