from flask import Flask, render_template, request
import os

# start the app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    greeting = ""
    if request.method == "POST":
        user_input = request.form['username']
        greeting = f"Hello {user_input}, Welcome to this app for Docker demonstration"
    
    return f'''
        <html>
        <body>
            <h1>
                <form action="/" method="POST">
                    Enter your name: <input type="text" name="username">
                    <input type="submit" value="Submit">
                </form>
            </h1>
            <h2>{greeting}</h2>
        </body>
        </html>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)