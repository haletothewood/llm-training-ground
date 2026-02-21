"""
Flask HTTP layer — routes and request handling.

Note: input validation is intentionally absent on several endpoints.
This is the target for the Module 04 Scenario 03 exercise.
"""

from flask import Flask, jsonify, request

import storage
import tasks as task_lib

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def list_tasks():
    all_tasks = storage.load_tasks()

    status = request.args.get("status")
    priority = request.args.get("priority")

    if status:
        all_tasks = task_lib.filter_by_status(all_tasks, status)
    if priority:
        all_tasks = task_lib.filter_by_priority(all_tasks, priority)

    return jsonify(task_lib.sort_by_priority(all_tasks))


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # No validation: missing fields, invalid priority/status values,
    # or empty title are all silently accepted.
    task = task_lib.create_task(
        title=data.get("title"),
        description=data.get("description", ""),
        priority=data.get("priority", "medium"),
        status=data.get("status", "open"),
    )

    all_tasks = storage.load_tasks()
    all_tasks.append(task)
    storage.save_tasks(all_tasks)

    return jsonify(task), 201


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    all_tasks = storage.load_tasks()

    task = task_lib.get_task_by_id(all_tasks, task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    # No validation on the update payload either.
    task_lib.update_task(task, data)
    storage.save_tasks(all_tasks)

    return jsonify(task)


@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    all_tasks = storage.load_tasks()
    task = task_lib.get_task_by_id(all_tasks, task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    all_tasks = [t for t in all_tasks if t["id"] != task_id]
    storage.save_tasks(all_tasks)

    return jsonify({"deleted": task_id})


if __name__ == "__main__":
    app.run(debug=True)
