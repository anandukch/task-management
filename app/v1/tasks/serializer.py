def taskResponseSerializer(task):
    return {
        "id": task["id"],
        "title": task["title"],
        "is_completed": task["is_completed"],
    }


def tasksResponseSerializer(tasks):
    return {"tasks": [taskResponseSerializer(task) for task in tasks]}


def errorResponseSerializer(error):
    return {"error": error}
