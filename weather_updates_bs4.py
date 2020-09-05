
__author__ : "@rockdevu"

import requests		# pip install requests

from bs4 import BeautifulSoup as bs 	# pip install bs4

search = "Weather in" + input("Enter the city name : ")

url = f"https://www.google.com/search?&q={search}"

request = requests.get(url)

soup = bs(request.text, "html.parser")
update = soup.find("div", class_="BNeawe").text

print(update)