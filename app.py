# respaldo[app.py](https://github.com/user-attachments/files/24431559/app.py)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
