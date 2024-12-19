from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def get_secret():
    secret = os.getenv("SECRET_PASSWORD", "No secret found")
    return f"SECRET_PASSWORD: {secret}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)