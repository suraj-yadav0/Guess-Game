import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

class NYTScraper:
    def __init__(self):
        self.base_url = "https://www.nytimes.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def get_soup(self, url):
        """Make request and return BeautifulSoup object"""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def get_article_data(self, article):
        """Extract data from article element"""
        data = {
            'title': '',
            'description': '',
            'url': '',
            'author': '',
            'date': ''
        }
        
        try:
            # Get title
            title_element = article.find('h2')
            if title_element:
                data['title'] = title_element.get_text().strip()
            
            # Get description
            desc_element = article.find('p', class_='css-1echdzn')
            if desc_element:
                data['description'] = desc_element.get_text().strip()
            
            # Get URL
            link_element = article.find('a')
            if link_element:
                data['url'] = self.base_url + link_element.get('href', '')
            
            # Get author
            author_element = article.find('span', class_='css-1n7hynb')
            if author_element:
                data['author'] = author_element.get_text().strip()
            
            # Get date
            date_element = article.find('span', class_='css-1dv1kvn')
            if date_element:
                data['date'] = date_element.get_text().strip()
                
        except Exception as e:
            print(f"Error extracting article data: {e}")
            
        return data

    def scrape_section(self, section_url, num_articles=10):
        """Scrape articles from a specific section"""
        soup = self.get_soup(section_url)
        if not soup:
            return []
        
        articles = []
        article_elements = soup.find_all('article', limit=num_articles)
        
        for article in article_elements:
            article_data = self.get_article_data(article)
            if article_data['title']:  # Only add if we got at least a title
                articles.append(article_data)
            
            # Be nice to the server
            time.sleep(1)
            
        return articles

    def save_to_csv(self, articles, filename):
        """Save scraped articles to CSV file"""
        if not articles:
            print("No articles to save")
            return
            
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=articles[0].keys())
                writer.writeheader()
                writer.writerows(articles)
            print(f"Successfully saved {len(articles)} articles to {filename}")
        except Exception as e:
            print(f"Error saving to CSV: {e}")

def main():
    scraper = NYTScraper()
    
    # Example usage: scrape the World news section
    section_url = "https://www.nytimes.com/section/world"
    articles = scraper.scrape_section(section_url, num_articles=5)
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nyt_articles_{timestamp}.csv"
    scraper.save_to_csv(articles, filename)

if __name__ == "__main__":
    main()