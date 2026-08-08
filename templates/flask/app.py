from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "Welcome to {project_name} API!",
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
