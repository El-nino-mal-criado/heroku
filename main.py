from flask import Flask, render_template #render_template poskrbi,da spletno stran vrne prav (npr. encoding, bla bla bla)
import datetime

#s tem ustvarimo aplikacijo
app = Flask(__name__) #flask je server program - deluje kao kot simple streznik

#ko poklicemo aplikacijo, bo pognal tudi to funkcijo
@app.route("/")
def index():
    trenutni_cas = datetime.datetime.now()
    datum = datetime.date.day
    return f"<h1>Moja prva spletna stran</h1><p>{trenutni_cas}</p><br> <button><a href=about>About</a></button>"

@app.route("/about") #to se bo zagnalo, ko pride človek na about
def on_about():
    #preberemo datoteko
    '''with open("index.html") as html_datoteka:
        vsebina = html_datoteka.read()
    return vsebina'''
    #return render_template("index.html")
    return render_template("Boogle_login.html")

if __name__ == "__main__":
    app.run()