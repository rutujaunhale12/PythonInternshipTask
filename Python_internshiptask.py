import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

postings_container = soup.find("div", class_="bids-table-container")

postings = postings_container.find_all("div", class_="posting-row")


for i in range(min(5, len(postings))):
    posting = postings[i]

    est_value_notes = posting.find("div", class_="est-value-notes").text.strip()
    description = posting.find("div", class_="description").text.strip()
    closing_date = posting.find("div", class_="closing-date").text.strip()

    print("Posting", i+1)
    print("Est. Value Notes:", est_value_notes)
    print("Description:", description)
    print("Closing Date:", closing_date)
    print("---------------------------")
