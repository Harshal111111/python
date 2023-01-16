import requests
from bs4 import BeautifulSoup as bs

github_profile = input('Paste profile url here: ')
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)