from flask import Flask, render_template

# webserver gateway interface

aap=Flask(__name__)


@aap.route("/")
def index():
    return render_template("layout.html")


if __name__=="__main__":
    aap.run(debug=True)