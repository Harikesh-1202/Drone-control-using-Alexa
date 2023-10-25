import json
import boto3

def lambda_handler(event, context):
    print(event)
    print("recieved...")
    dynamo=boto3.client('dynamodb')
    URL="https://4ademiw456.execute-api.us-east-1.amazonaws.com/dev"
    client=boto3.client("apigatewaymanagementapi", endpoint_url=URL)
    resp=dynamo.scan(TableName="cids")
    for connection in resp["Items"]:
        resp=client.post_to_connection(ConnectionId=connection["cid"]["S"], Data=json.dumps(event))
    return{
        'statusCode':200,
        'body': json.dumps()
    }