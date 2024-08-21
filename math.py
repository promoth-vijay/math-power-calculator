import json
import math
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Your Table Name')
#for time
time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    mathResult = math.pow(int(event['base']), int(event['exponent']))

    response = table.put_item(
        Item={
            'Val': str(mathResult),
            'LatestGreetingTime':time
            })

    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(mathResult))
    }
