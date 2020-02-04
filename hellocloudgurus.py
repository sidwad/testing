def lambda_handler(event, context):
    print("In lambda handler")
    print("here")

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Ryan Kroonenburg"
    }

    return resp