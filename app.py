from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
MONGO_URI = 'mongodb+srv://ashrarul0812:4yboyz6Agr5j46VN@ashcluster0.cvlnf9f.mongodb.net?retryWrites=true&w=majority&appName=ashCluster0'
client = MongoClient(MONGO_URI)
db = client["flask_app"]
collection = db["project_1"]

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        print(request)
        try:
            name = request.form.get("name")
            email = request.form.get("email")

            if not name or not email:
                return render_template("form.html", error="All fields are required.")

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            # Redirect on success
            return redirect(url_for("success"))
        except Exception as e:
            return render_template("form.html", error=str(e))

    return render_template("form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)



