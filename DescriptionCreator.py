from google import genai
import config

def createGeneratedDescription(title, description):
    client = genai.Client(api_key=config.google_api_key)

    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=[f'Here is a title for a news story {title} and a description for the same story {description}. Use them to create a captivating instagram caption that explains the key details of story. Write as if you are a news page that posts recent events and make sure to not include any placeholders. If the news story resembles a true news story that is currently breaking, draw additional details from that event.']
    )

    return response.text