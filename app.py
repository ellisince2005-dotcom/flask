from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome!</h1>
    <p>This is a simple Flask site.</p>
    <a href='/about'>Go to About</a>
    """

@app.route("/about")
def about():
    return """
    <h1>About Page</h1>
    <p>This is all in one file 😄</p>
    <a href='/'>Back Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)