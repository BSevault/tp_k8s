from flask import Flask, render_template, send_from_directory
import requests

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

@app.route("/")
def home():
    try:
        # Appel au backend via le service Kubernetes
        response = requests.get("http://backend-service:5000/api/data")
        # response = requests.get("http://localhost:5000/api/data")
        data = response.json()
        message = data.get("message", "No message received from backend")

    except requests.exceptions.RequestException as e:
        # Capture et affiche les détails de l'erreur en cas d'échec
        message = f"Error while connecting to backend: {str(e)}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
