import streamlit as st
import boto3
import requests
import json
import time
import logging

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

session = boto3.Session(region_name='AP-SOUTH-1')
lambda_client = session.client('lambda')


dynamodb = boto3.resource('dynamodb')
table_name = 'PostDataTable'
table = dynamodb.Table(table_name)

def home_page():
    st.title('Social Media Hashtag Trend Analyzer')
    logger.info('Home page loaded')
    if st.button('Write a post!'):
        st.session_state['page'] = 'post'
        logger.info('Navigated to post page')

def get_trending_hashtags():
    table = dynamodb.Table(table_name)
    response = table.scan()
    hashtags = {}
    for item in response['Items']:
        for hashtag in item['hashtags']:
            if hashtag in hashtags:
                hashtags[hashtag] += 1
            else:
                hashtags[hashtag] = 1
    trending_hashtags = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)[:10]
    return dict(trending_hashtags)

def post_page():
    st.title('Let your thoughts flow')
    post_content = st.text_area('Write your thoughts here..', '')
    logger.info('Post page loaded')
    if st.button('Post'):
        info_message = st.empty()
        logger.info('Post button clicked')
        info_message.success('Sit back & Enjoy! Your thoughts are posted successfully!')
        time.sleep(1)
        info_message.empty()
        api_url = 'https://bq2kv4mkki.execute-api.ap-south-1.amazonaws.com/Prod/trendanalyzer'
        try:
            response = requests.post(api_url, json={'post_content': post_content})
            logger.info('Post content sent to API: %s', post_content)
            if response.status_code == 200:
                logger.info('Content uploaded to AWS Lambda successfully!')
                info_message.success('Content uploaded to AWS lambda successfully!')
                time.sleep(1)
                info_message.empty()
            else:
                logger.error('Failed to upload content to AWS Lambda. Status code: %d', response.status_code)
                info_message.error(f'Failed to upload content to AWS Lambda. Status code: {response.status_code}. Please try again!')
                time.sleep(1)
                info_message.empty()
        except Exception as e:
            logger.error('Error occurred while uploading content to AWS Lambda: %s', str(e))
            info_message.error(f'An error occurred: {str(e)}')
    if st.button('Get Trending Hashtags'):
        trending_hashtags = get_trending_hashtags()
        st.write('Trending Hashtags:')
        for hashtag, count in trending_hashtags.items():
            st.write(f'#{hashtag}: {count}')
    if st.button('Go Back'):
        st.session_state['page'] = 'home'
        logger.info('Navigated back to home page')

# Initialize the session state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
    logger.info('Session state initialized to home')

# Display appropriate page based on session state
if st.session_state['page'] == 'home':
    home_page()
elif st.session_state['page'] == 'post':
    post_page()