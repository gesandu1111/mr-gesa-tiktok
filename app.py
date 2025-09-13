from flask import Flask, render_template, request
from bot import promote_video  # Selenium bot function

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    video_url = request.form["video_url"]
    promote_video(video_url)  # Call Selenium bot
    return f"Promotion started for: {video_url}"

if __name__ == "__main__":
    app.run(debug=True)
