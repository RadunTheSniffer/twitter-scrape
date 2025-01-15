from bs4 import BeautifulSoup
import requests

def scrape_data(link):
    scraped_data = []
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        activity_descs = soup.find_all('div', class_='activity-descp')
        for desc in activity_descs:
            p_tag = desc.find('p')
            if p_tag:
                scraped_data.append(p_tag.get_text())
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    return scraped_data

# Test the function
link = "https://twstalker.com/search/tiktok%20ban"
scraped_data = scrape_data(link)
print(scraped_data)