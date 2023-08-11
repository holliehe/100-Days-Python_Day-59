from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    response = requests.get('https://api.npoint.io/a89260239d50fb21145b')
    blogs = response.json()
    print(blogs)
    return render_template("index.html", blogs=blogs)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:number>')
def blog(number):
    response = requests.get('https://api.npoint.io/a89260239d50fb21145b')
    blogs = response.json()
    print(blogs[number]['title'])
    return render_template("post.html", blog=blogs[number])


if __name__ == "__main__":
    app.run(debug=True)