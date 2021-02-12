import requests
import math
import os
from twilio.rest import Client
from keys import *



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]



stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
closing_price = stock_data['Global Quote']['05. price']
print(closing_price)
print(stock_data)
#TODO 2. - Get the day before yesterday's closing stock price
last_closing_price = stock_data['Global Quote']['08. previous close']
print(last_closing_price)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
absolute_difference = abs(float(closing_price) - float(last_closing_price))
print(absolute_difference)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_changed = absolute_difference / float(closing_price) * 100
print(percent_changed)

emoji_ticker = ""
if closing_price > last_closing_price:
    emoji_ticker = "🔺"
else:
    "🔻"
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_changed > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_articles = news_response.json()['articles'][:3]
    my_articles = []
    for i in range(0, 3):
        headline = news_articles[i]['title']
        brief = news_articles[i]['description']
        print(f"this is i {i}\nheadline: {headline}\nbrief: {brief}")
        my_articles.append(f"TSLA: {emoji_ticker}{math.floor(percent_changed)}%\nHeadline: {headline}\nBrief: {brief}")

    for article in my_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=article,
            from_='+15039804541',
            to=MY_PHONE
        )

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

