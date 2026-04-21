import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for item in soup.find_all("div", class_="quote"):
    quote = item.find("span", class_="text").text
    author = item.find("small", class_="author").text

    quotes.append(quote)
    authors.append(author)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

print(df)

df.to_csv("quotes_data.csv", index=False)

print("Exported to quotes_data.csv")
