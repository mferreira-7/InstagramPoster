import requests
from PIL import Image

def processImage(filename, url):
    with open(filename, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

    im = Image.open(filename)
    im.save(f'{filename}.jpg')