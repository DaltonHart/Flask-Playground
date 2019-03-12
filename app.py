# Import Flask class from flask library. (Note the upper/lowercase convention.)
from flask import Flask, render_template

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
# Could be instead "my-website.com/about" or anything - more on this later.


@app.route('/')
def home():
    return render_template("index.html", greeting="Hello World!")


@app.route('/template')
def temp():
    return render_template("injectedTemp.html")


@app.route('/sayhi/<username>')  # When someone goes here...
def hello(username):  # Do this.
    return f"Hello {username}"


# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
