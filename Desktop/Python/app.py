from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>Local Lab - Marker Form</title>
</head>
<body>
  <h1>Local Lab Form</h1>
  <form action="/submit" method="post">
    <label for="input">Enter text:</label>
    <input id="input" name="input" type="text" />
    <button type="submit">Send</button>
  </form>
  <p>Use marker strings like <code>TEST_SQL_1</code> or <code>TEST_XSS_1</code>.</p>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(INDEX_HTML)

@app.route("/submit", methods=["POST"])
def submit():
    value = request.form.get("input", "")
    ts = datetime.utcnow().isoformat()
    # log to stdout (visible in your terminal)
    print(f"[{ts}] Received form submission: {value}")
    # echo a safe response
    return f"Received: {value}", 200

if __name__ == "__main__":
    # host=127.0.0.1 binds to localhost only (safe)
    app.run(host="127.0.0.1", port=5000, debug=False)
