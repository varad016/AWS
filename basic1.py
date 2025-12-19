import json

def lambda_handler(event, context):
    user = event.get("user", {})
    name = user.get("name")

    if not name:
        return {
            "success": False,
            "error": "Name missing"
        }

    return {
        "success": True,
        "message": f"Hello {name}"
    }
