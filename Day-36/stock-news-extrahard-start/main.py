import requests
import pytz
from datetime import datetime,timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key1=api_key1
api_url1=api_url"
stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "apikey":api_key1

}

api_key2=api_key2
api_url2=api_url2
today=datetime.now()

iso_yesterday=(today - timedelta(days = 1)).isoformat()
iso_previous_day=(today - timedelta(days = 2)).isoformat()
news_parameters={
    "apiKey":api_key2,
    "q":COMPANY_NAME,
    "language":"en",
    "from":iso_previous_day,
    "to":iso_yesterday

}


news_response=requests.get(url=api_url2,params=news_parameters)
news_response.raise_for_status()
news_data=news_response.json()


stock_response=requests.get(url=api_url1,params=stock_parameters)
stock_response.raise_for_status()
stock_data=stock_response.json()



#Adjusting the time zone
time_zone = pytz.timezone('US/Eastern')
now = datetime.now()
current_date= time_zone.localize(now)

yesterday=str(current_date - timedelta(days = 1))[:10]
previous_day=str(current_date - timedelta(days = 2))[:10]

yesterday_closing=float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
previous_day_closing=float(stock_data["Time Series (Daily)"][previous_day]["4. close"])

stock_change= ((yesterday_closing-previous_day_closing)/previous_day_closing)*100

if stock_change==5 or stock_change==-5:
    for i in range(0,3):
        headline = news_data["articles"][i]["title"]
        description = news_data["articles"][i]["description"]
        print(f"Headline: {headline}\nDescription: {description}\n")

else:
    print("Nothing important happend")
    for i in range(0,3):
        headline = news_data["articles"][i]["title"]
        description = news_data["articles"][i]["description"]
        print(f"Headline: {headline}\nDescription: {description}\n")




