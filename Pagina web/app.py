from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, mundo!"

@app.route("/saludar")
def saludar():
    nombre = request.args.get("nombre")
    if nombre:
        return f"¡Hola, {nombre}!"
    else:
        return "Por favor, introduce tu nombre en la URL como '?nombre=tu_nombre'"

@app.route("/calculadora", methods=["GET", "POST"])
def calculadora():
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacion = request.form["operacion"]
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            resultado = num1 / num2
        return render_template("resultado.html", resultado=resultado)
    else:
        return render_template("calculadora.html")

if __name__ == "__main__":
    app.run(debug=True)