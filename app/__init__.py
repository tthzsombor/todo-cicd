from flask import Flask, jsonify, request, render_template


def create_app():
    app = Flask(__name__)
    app.config["TODOS"] = []
    app.config["NEXT_ID"] = 1

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/api/todos")
    def list_todos():
        return jsonify(app.config["TODOS"])

    @app.post("/api/todos")
    def add_todo():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify(error="A 'title' mező kötelező"), 400
        todo = {"id": app.config["NEXT_ID"], "title": title, "done": False}
        app.config["NEXT_ID"] += 1
        app.config["TODOS"].append(todo)
        return jsonify(todo), 201

    @app.put("/api/todos/<int:todo_id>/toggle")
    def toggle_todo(todo_id):
        for t in app.config["TODOS"]:
            if t["id"] == todo_id:
                t["done"] = not t["done"]
                return jsonify(t)
        return jsonify(error="Nem található"), 404

    @app.delete("/api/todos/<int:todo_id>")
    def delete_todo(todo_id):
        before = len(app.config["TODOS"])
        app.config["TODOS"] = [t for t in app.config["TODOS"] if t["id"] != todo_id]
        if len(app.config["TODOS"]) == before:
            return jsonify(error="Nem található"), 404
        return "", 204

    return app
