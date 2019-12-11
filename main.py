from flask import Flask, render_template, request
from weather import getWeather

app = Flask("MyApp")

@app.route("/")
def base():
    return render_template("index.html")

# We need a route to handle the form data coming from the html pack
# Need to make sure the methods match and the / route matches the action in the form
@app.route("/lookup", methods=['POST'])
def lookup():
    # Pull the form data from the request object
    form_data = request.form
    print(form_data)
    # That form data is a dictonary object
    # So can access parts of it in the usual way
    city = form_data["search"]
    print(city)
    # Call all our API function with our form value
    x = getWeather(city)
    # Now we have the weather, we want to pass through to the html file
    # We are doing this in a json object to make it easy to pass through
    # multiple values in one 'package', so first we put together the object
    result = {"city": city, "weather": x}
    return render_template("index.html", result=result)

app.run(debug=True)
