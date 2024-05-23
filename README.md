# TrendAnalyzerApp: Dive into Hashtag Trends with Ease!

Welcome to TrendAnalyzerApp, your gateway to exploring the ever-changing landscape of social media trends! Whether you're a marketer seeking insights or just a curious soul intrigued by what's buzzing online, this app has got you covered. Let's dive in and uncover the magic of hashtags together!

## What is TrendAnalyzerApp?

TrendAnalyzerApp is a powerful tool for tracking and analyzing trending hashtags. This app is very helpful for individuals, marketers, and businesses to gain insights into hashtag popularity and engagement, enabling them to leverage trends for increased visibility and reach on social media platforms.

## How does it work?

Behind the scenes, TrendAnalyzerApp utilizes cutting-edge technologies to fetch, process, and visualize hashtag data. Here's a brief overview of how it all comes together:

- **Frontend with Streamlit**: The user interface is built using Streamlit, a user-friendly framework for creating web applications with Python. With its intuitive interface, you can easily interact with the app, post your thoughts and explore hashtag trends effortlessly.
- **Backend with AWS Lambda**: When you enter a content to post it, the request is sent to AWS Lambda, a serverless computing service provided by Amazon Web Services (AWS). Lambda processes the data, performs analysis, and prepares the results for display.
- **Data Storage with DynamoDB**: The analyzed data is stored in DynamoDB, a fully managed NoSQL database service provided by AWS. DynamoDB ensures fast and reliable storage of hashtag trends, allowing for quick retrieval and visualization.
- **Deployment with AWS SAM**: The entire infrastructure is deployed using AWS SAM (Serverless Application Model), a framework for building and deploying serverless applications on AWS. SAM simplifies the deployment process, making it easy to set up and manage the application.

## Getting Started

Excited to get started? Here's how you can dive into hashtag analysis with TrendAnalyzerApp:

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- AWS CLI (Amazon Web Services Command Line Interface)
- AWS SAM CLI (Serverless Application Model Command Line Interface)
- Streamlit (Python library for building web applications)

### Installation

1. **Clone the Repository**: Start by cloning the TrendAnalyzerApp repository to your local machine:
    ```bash
    git clone https://github.com/RiyaMary1512/trendanalyzerapp.git
    ```
2. **Navigate to the Project Directory**: Once cloned, navigate to the project directory:
    ```bash
    cd trendanalyzerapp
    ```
3. **Install Dependencies**: Install the required Python dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
    
### AWS Configuration

To deploy and run TrendAnalyzerApp, you'll need an AWS account and appropriate permissions. Here's what you need to do:

1. **Create an AWS Account**: If you don't already have one, sign up for an AWS account at [aws.amazon.com](https://aws.amazon.com).
2. **Configure AWS CLI**: Set up the AWS Command Line Interface (CLI) with your AWS credentials:
    ```bash
    aws configure
    ```
3. **Configure AWS SAM**: Set up the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) using below command:
    ```bash
    sam init
    ```
### Deployment

Ready to deploy TrendAnalyzerApp? Follow these steps to deploy the application on AWS:

1. **Build the Code**: The necessary AWS configurations have been given in 'template.yaml' file. Navigate to my-app directory & build the code using sam:
    ```bash
    sam build
    ```
2. **Deploy the Code**: Once the code is build successfully, deploy the code using sam. Make your own choices for the prompted questions during guided deployment:
    ```bash
    sam deploy --guided
    ```
    
### Running the Application

Once deployed, go to AWS console & navigate to API gateway. Choose POST method & edit the integration response. Add the below template to it. 
```bash
#set($inputRoot = $input.path('$'))
{
    "statusCode": $statusCode,
    "body": $input.json('$'),
    "headers": {
        "Content-Type": "application/json"
    }
}
```
This helps in proper handling and displaying of response code received from backend to frontend. 

Copy the API gateway URL and update it in streamlit.py file at line no 50. You should also update the region name in line no 12. Now you can run TrendAnalyzerApp locally by navigating to trendanalyzerapp directory & running the python code for streamlit app:
```bash
streamlit run streamlit.py
```
This will start the Streamlit server, and you can access the application through your web browser at [http://localhost:8501](http://localhost:8501).

## Usage

Using TrendAnalyzerApp is a breeze! Here's how to use this app:

- **Write a post**: In the app's interface home page, click on the 'Write a post!' button. You will be directed to post page & there you can write your thoughts and add hashtags if required.
- **Trending Hashtags**: When you click on 'Show Trending Hashtags' button, you can see the top 10 trending hashtags based on previous post inputs from user. The number of times those hashtags have been previously used will be also displayed along with each hashtag.
- **Post your thoughts**: Once you have completed writing down your thoughts, you can post it by clickiing on 'Post' button. This will send the post content to dynamo DB table for storage purpose. The hashtags & their count will be updated based on each content posted through app interface.
- **Write a new post**: If you need to post a new content, you can click on 'Go Back' button. This will redirect you to home page where you can click on 'Write a post!' button to start writing down your new thoughts.

## Contributing

We welcome contributions from the community! Whether it's fixing bugs, adding new features, or improving documentation, your contributions are valuable. Here's how you can contribute:

1. **Fork the Repository**: Start by forking the TrendAnalyzerApp repository on GitHub.
2. **Make Changes**: Make your desired changes to the codebase.
3. **Submit a Pull Request**: Once your changes are ready, submit a pull request, and we'll review it as soon as possible.

## Acknowledgements

We'd like to express our gratitude to the following:

- **Streamlit**: For providing an intuitive framework for building web applications with Python.
- **Amazon Web Services (AWS)**: For offering robust cloud infrastructure services that power TrendAnalyzerApp.
- **Open Source Community**: For their continuous support and contributions to the world of technology.

