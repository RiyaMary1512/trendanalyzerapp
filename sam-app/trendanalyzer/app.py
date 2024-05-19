import boto3
import json
import re
import logging

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_hashtags(post_content):
    hashtags = re.findall(r"#(\w+)", post_content)
    return hashtags

def lambda_handler(event, context):
    logger.info('Received event: %s', json.dumps(event))
    post_content = event.get('post_content')
    if not post_content:
        error_message = 'Invalid input: post_content is required'
        logger.error(error_message)
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": error_message})
        }
        return response
    hashtags = extract_hashtags(post_content)
    logger.info('Extracted hashtags: %s', hashtags)
    dynamodb = boto3.resource('dynamodb')
    table_name = 'PostDataTable'
    table = dynamodb.Table(table_name)
    try:
        table.put_item(Item={
            'post_data': post_content,
            'hashtags': hashtags
        })
        success_message = 'Data uploaded successfully!'
        logger.info(success_message)
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": success_message})
        }
        return response
    except Exception as e:
        logger.error(f'Error uploading data to DynamoDB: {str(e)}')
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }
        return response

def get_trending_hashtags(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'PostDataTable'
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        hashtag_counts = {}
        for item in response['Items']:
            for hashtag in item['hashtags']:
                if hashtag in hashtag_counts:
                    hashtag_counts[hashtag] += 1
                else:
                    hashtag_counts[hashtag] = 1
        sorted_hashtag_counts = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
        trending_hashtags = [hashtag[0] for hashtag in sorted_hashtag_counts[:10]]
        response = {
            "statusCode": 200,
            "body": json.dumps({"trending_hashtags": trending_hashtags})
        }
        return response
    except Exception as e:
        logger.error(f'Error retrieving trending hashtags from DynamoDB: {str(e)}')
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal Server Error"})
        }
        return response