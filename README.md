# Sentiment-Analysis-Dash-NLP


Sentiment Analysis using Dash and NLP
This repository contains the code for a sentiment analysis model built using Dash and NLP techniques. The model is trained on a dataset of jewellery reviews scraped from esty.com.

## Data
The dataset used in this project was scraped from esty.com using web scraping techniques. The data is preprocessed and cleaned to remove any irrelevant information.

## Model
The sentiment analysis model is built using Tfidf Transformer and Count Vectorizer. These natural language processing techniques are used to convert the text data into numerical representations that can be used as input for machine learning models. The model is then trained using this preprocessed data.

## Deployment
The model is deployed using Dash, a web application framework for building analytical applications. The Dash application allows users to input their own text and receive a sentiment analysis of the text in real-time.

## Usage
To use this repository, you will need to have Python and the following libraries installed: <br>

1.Dash <br>
2.NLTK <br>
3.Sklearn <br>
4.Pandas <br>
5.Selenium <br>
6.BeautifulSoup <br> 

Clone the repository and navigate to the directory in your command line. Then run the following command to start the Dash application:

<code>python sentiment_analysis.py</code> {The file is located in solo_development folder}

Then open the http://127.0.0.1:8050/ in your browser to see the deployed model.

Note: You may also need to install chromedriver depending on your chrome version.

Feel free to use and modify the code as needed for your own projects. If you have any questions or encounter any issues, please open an issue in the repository.
