from flask import Flask, render_template, request

app = Flask(__name__)

# 1️⃣ Login page
@app.route("/")
def login():
    return render_template("login.html")

# 2️⃣ Skills page
@app.route("/skills")
def skills():
    return render_template("skills.html")

# 3️⃣ Result page (button triggers this)
@app.route("/result", methods=["POST"])
def result():
    user_skills = request.form.get("skills")

    # backend logic (can be simple for now)
    jobs = ["AI Engineer", "Data Scientist", "ML Engineer"]
    gaps = ["Deep Learning", "NLP", "Deployment"]

    return render_template(
        "result.html",
        jobs=jobs,
        gaps=gaps
    )

if __name__ == "__main__":
    app.run(debug=True)
