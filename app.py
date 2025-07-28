from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '🚀 Hello from Flask app deployed with GitHub Actions and AWS ECS.our group members are chathuni, nethmi and hiruni!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route("/health")
def health():
    return "OK", 200
