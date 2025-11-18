import requests
import config

def sendNotification(story_count):
    url = f"https://api.telegram.org/bot{config.bot_token}/sendMessage"
    payload = {"chat_id": config.chat_id, "text": f"{story_count} stories posted"}

    requests.post(url, data=payload)