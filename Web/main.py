from flask import Flask, render_template, url_for
app = Flask(__name__)

# export FLASK_APP=main.py
# flask run

@app.route('/')
def index():
    return render_template("index.html", index=True)

@app.route('/<nm>')
def index_user(nm):
    return render_template("index.html", name=nm, index=True)

if __name__ == '__main__':
    app.run(debug=True)