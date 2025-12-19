def lambda_handler(event, context):
    print("Full event:", event)

    request = event.get("request", {})
    body = request.get("body", {})
    user = body.get("user", {})

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

#the expected input structure
{
  "request": {
    "body": {
      "user": {
        "name": "Altroz"
      }
    }
  }
}
