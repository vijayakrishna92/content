import requests
from bs4 import BeautifulSoup
import json
import os

class WebSearchTools:

    @staticmethod
    def search_internet(query):
        search_url = f"https://www.google.com/search?q={query}&tbm=nws"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        
        for item in soup.find_all('div', attrs={'class': 'BVG0Nb'}):
            title = item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text()
            link = item.find('a')['href']
            snippet = item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text()
            results.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })
        
        return results

    @staticmethod
    def scrape_and_summarize_website(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([para.get_text() for para in paragraphs])
        return text

