from flask import Flask, render_template, request, redirect
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


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

@app.before_request
def force_https():
    if request.headers.get('X-Forwarded-Proto', 'http') != 'https':
        return redirect(request.url.replace('http://', 'https://', 1), code=301)


if __name__ == "__main__":
    app.run(debug=True)
