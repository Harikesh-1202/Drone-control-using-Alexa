import json
import boto3

def lambda_handler(event, context):
    routeKey=event["requestContext"].get("routeKey")
    client = boto3.client("dynamodb")
    if(routeKey=='$connect'):
        client.put_item(TableName="cids" , Item={"cid" : {"S": event["requestContext"].get("connectionId")}})
    elif(routeKey=='$disconnect'):
        client.delete_item(TableName="cids" , Key={"cid" : {"S" : event["requestContext"].get("connectionId")}})
    return {
        'statusCode': 200,
        'body': json.dumps("hello!")
    }
