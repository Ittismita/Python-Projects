import requests
from send_email import send_email

topic="tesla"
api_key="06ad38b7f40743348bbfb38f97bec284"
url="https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2023-06-01&sortBy=publishedAt&" \
    "apiKey=06ad38b7f40743348bbfb38f97bec284&" \
    "language=en"

#made a request
r = requests.get(url)

#initially was astring , used json , after this beacme a dictionary type
content=r.json()

#accessed the article titles and description
body=""
for article in content["articles"][:20]:
    body="Subject: Today's News "+\
         "\n"+body+article["title"]+\
         "\n"+article["description"]+\
         "\n"+ article["url"]+2*"\n"

body=body.encode("utf-8")
send_email(body)
