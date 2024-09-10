import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Nipon lambda with New STUFF v2 by Github action!')
    }