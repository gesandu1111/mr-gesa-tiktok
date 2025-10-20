from flask import Flask, render_template, request
from bot import promote_video  # 'bot.py' file eken promote_video function eka import karanawa

# Flask application eka hadanawa
app = Flask(__name__)

# මුල් පිටුව (Home Page) - http://127.0.0.1:5000/
@app.route("/")
def index():
    # 'templates' folder eke thiyena 'index.html' file eka load karanawa.
    return render_template("index.html")

# Form eka submit kalama POST request eka me route ekata enawa.
@app.route("/submit", methods=["POST"])
def submit():
    # HTML form eke 'name="video_url"' eken ena data eka gannawa.
    video_url = request.form["video_url"]
    
    # bot.py file eke thiyena promote_video function eka call karanawa.
    # Note: promote_video function eka weda karaddi browser window ekak open wewi.
    promote_video(video_url)
    
    # User ta result eka peenwanawa.
    return f"Promotion process initiated for: <strong>{video_url}</strong>. Check your terminal/console for bot status updates!"

# Web Server eka patan gannawa.
if __name__ == "__main__":
    # debug=True nisa, code eka wenas kaloth server eka auto restart wenawa.
    app.run(debug=True)
