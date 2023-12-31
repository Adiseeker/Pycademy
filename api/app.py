from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__, template_folder='template')
obraz = "//sejf.png"

def generacja(level):
    if level == 1:
        return str(random.randrange(0,10))

@app.route('/')
def main():
    return render_template('index.html', obraz=obraz)

@app.route('/', methods=["POST"])
def check_code():
    global obraz
    if request.method == "POST":
        wpisany_kod = request.form.get("kod")
        kod_sejfu = generacja(1)
        licznik = 1
        while licznik <= 5:
            licznik += 1

            if kod_sejfu == wpisany_kod:
                return redirect("/ok.html")

            else:
                return redirect("/blad.html")
    return render_template("index.html", obraz=obraz)

@app.route('/ok.html')
def show_ok():
    return render_template("ok.html")

@app.route('/blad.html')
def show_error():
    return render_template("blad.html")

if __name__ == "__main__":
    app.run(debug=True)
