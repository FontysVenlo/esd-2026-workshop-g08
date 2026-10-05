import json

def hello(event, context):
    # 'event' contains all the HTTP request data
    body = {
        "message": "Welcome to the Serverless Workshop!",
        "status": "Success"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

# requirements.txt completely empty for now. Will add later