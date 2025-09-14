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



from flask import request, redirect

@app.before_request
def canonicalize_host_and_scheme():
    host = request.host.split(':', 1)[0].lower()
    # Pfad inkl. Query beibehalten (ohne nacktes '?')
    path = request.full_path[:-1] if request.full_path.endswith('?') else request.full_path
    # Upstream-Scheme (Render/Proxy) respektieren
    scheme = request.headers.get('X-Forwarded-Proto', 'http')

    # 1) Root-Domain -> immer auf www weiterleiten, Scheme beibehalten (kein extra HTTPS)
    if host == 'crformoney.com':
        return redirect(f"{scheme}://www.crformoney.com{path}", code=301)

    # 2) www-Host -> immer HTTPS erzwingen
    if host == 'www.crformoney.com' and scheme != 'https':
        return redirect(f"https://www.crformoney.com{path}", code=301)



if __name__ == "__main__":
    app.run(debug=True)
