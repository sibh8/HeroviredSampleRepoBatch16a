from flask import Flask, render_template

app = Flask("Hello World")


@app.route("/")
def printHelloWorld():
    message = "Hello World"
    return render_template("helloworld.html", message=message)

app.run(debug=True, port=8088)