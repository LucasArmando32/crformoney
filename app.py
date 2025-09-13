from flask import Flask, render_template, request

app = Flask(__name__)

TOTAL_DONATION_CHF=20

@app.route("/")
def home():
    return render_template('home.html',total_chf=TOTAL_DONATION_CHF)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/play")
def play():
    return render_template('play.html')

@app.route("/dates")
def dates():
    player = request.args.get("player")  # Spieler aus dem Button
    return render_template('dates.html', player=player)

@app.route("/payment")
def payment():
    player = request.args.get("player")
    return render_template("pay.html", player=player)

@app.route("/consent")
def consent():
    return render_template('consent.html')

@app.route("/donations")
def donations():

    return render_template("donations.html", total_chf=TOTAL_DONATION_CHF)





if __name__ == "__main__":
    app.run(debug=True)
