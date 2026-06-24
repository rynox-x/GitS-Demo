from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")

    # XSS
    return render_template_string(
        "<h1>Hello %s</h1>" % name
    )

@app.route("/debug")
def debug():
    # Debug enabled
    app.debug = True
    return "debug"

if __name__ == "__main__":
    app.run(debug=True)

