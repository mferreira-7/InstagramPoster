import requests
import config

def getNewsFromBBC():
    news_data = []

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": config.news_api_key
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)

    for i in range(len(res.json()['articles'])):
        news_data.append([
            res.json()['articles'][i]['title'],
            res.json()['articles'][i]['description'],
            res.json()['articles'][i]['urlToImage']
        ])

    return news_data