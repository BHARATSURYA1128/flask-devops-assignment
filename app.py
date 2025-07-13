import bugsnag
from bugsnag.flask import handle_exceptions
from flask import Flask

# Configure bugsnag
bugsnag.configure(
  api_key="1301d2fe80bc2664053777d009aaa0f1",
  project_root="/path/to/your/app",
)

# Attach bugsnag to Flask's exception handler
app = Flask(__name__)
handle_exceptions(app)

@app.route("/")
def hello():
    return "Hello from Flask app with Bugsnag!"

@app.route("/crash")
def crash():
    raise RuntimeError("This is a test error for Bugsnag!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
