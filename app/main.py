from flask import Flask, jsonify

app = Flask(__name__)

# ── Routes ──────────────────────────────────────────────

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my CI/CD demo app!",
        "status": "running"
    })


@app.route("/health")
def health():
    """Health check — used by Render & the pipeline to verify the app is alive."""
    return jsonify({"status": "ok"}), 200


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    """Simple addition endpoint — easy to write tests for."""
    return jsonify({"result": a + b}), 200


@app.route("/reverse/<string:text>")
def reverse(text):
    """Reverses a string — another testable endpoint."""
    return jsonify({"result": text[::-1]}), 200


# ── Entry point ─────────────────────────────────────────

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)