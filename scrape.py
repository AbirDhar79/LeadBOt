import os
import re
import snscrape.modules.twitter as sntwitter
from bs4 import BeautifulSoup
from facebook_scraper import get_posts
# import instaloader
import praw
# import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# Function to extract email and phone number
def extract_contact_details(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+?\d[\d -]{8,12}\d'
    emails = re.findall(email_pattern, text) if text else []
    phones = re.findall(phone_pattern, text) if text else []
    return emails, phones

# --- Instagram Scraper ---
# def scrape_instagram(username):
#     try:
#         bot = instaloader.Instaloader()
#         profile = instaloader.Profile.from_username(bot.context, username)
#         posts = []
#         for post in profile.get_posts():
#             emails, phones = extract_contact_details(post.caption)
#             posts.append({
#                 'title': post.caption or None,
#                 'url': post.url or None,
#                 'contact': profile.username or None,
#                 'email': emails or None,
#                 'phone': phones or None
#             })
#         return posts
#     except Exception as e:
#         print(f"Instagram scraping error: {e}")
#         return []

import requests
from bs4 import BeautifulSoup


def scrape_linkedin(industry, keywords, country):
    url = f"https://www.linkedin.com/search/results/content/?keywords={'+'.join(keywords)}&location={country}&industry={industry}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    
    posts = []
    for post in soup.find_all('div', class_='search-result__info'):
        post_data = {
            'title': post.find('span', class_='name actor-name').text.strip(),
            'description': post.find('p', class_='subline-level-1').text.strip(),
            'link': post.find('a', class_='search-result__result-link')['href']
        }
        posts.append(post_data)
    
    return posts

# --- Facebook Scraper - API Method (facebook_scraper) ---
def scrape_facebook_api(page_name):
    try:
        posts = []
        for post in get_posts(page_name, pages=1):
            emails, phones = extract_contact_details(post.get('text', ''))
            posts.append({
                'title': post.get('text', None),
                'url': post.get('post_url', None),
                'contact': post.get('username', None),
                'email': emails or None,
                'phone': phones or None
            })
        return posts
    except Exception as e:
        print(f"Facebook API scraping error: {e}")
        return []

# --- Facebook Scraper - snscrape Method ---
def scrape_facebook_snscrape(page_url):
    command = f"snscrape facebook-page {page_url} > facebook_posts.txt"
    os.system(command)
    with open('facebook_posts.txt', 'r') as file:
        data = file.read()
    soup = BeautifulSoup(data, 'html.parser')
    posts = []
    for post in soup.find_all('div', class_='post'):
        emails, phones = extract_contact_details(post.text)
        posts.append({
            'title': post.text,
            'url': post.find('a')['href'],
            'contact': post.find('span', class_='username').text,
            'email': emails,
            'phone': phones
        })
    return posts

# --- LinkedIn Scraper ---
def scrape_linkedin(profile_url):
    try:
        options = webdriver.ChromeOptions()
        # You can add any Chrome options here
        # driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)
        driver = webdriver.Chrome('/path/to/chromedriver')
        # Log in to LinkedIn
        driver.get('https://www.linkedin.com/login')
        username = driver.find_element_by_name('session_key')
        password = driver.find_element_by_name('session_password')
        username.send_keys('your_linkedin_email')  # Replace with your LinkedIn email
        password.send_keys('your_linkedin_password')  # Replace with your LinkedIn password
        password.send_keys(Keys.RETURN)
        
        # Navigate to the LinkedIn profile
        driver.get(profile_url)
        
        # Extract name and other information
        name = driver.find_element_by_css_selector('h1').text or None
        posts = [{
            'title': name,
            'url': profile_url,
            'contact': name,
            'email': None,
            'phone': None
        }]
        
        driver.quit()
        return posts

    except Exception as e:
        print(f"LinkedIn scraping error: {e}")
        return []


def scrape_reddit(subreddit_name):
    try:
        reddit = praw.Reddit(
            client_id=os.getenv('9FU-6d330ZoDkytgzwfwBg'),
            client_secret=os.getenv('J1Ijclx4730k0lydnA6TcPXc1k_A_Q'),
            user_agent=os.getenv('user_agent_me')
            
            
        )
        
        subreddit = reddit.subreddit(subreddit_name)
        posts = []
        for post in subreddit.hot(limit=10):
            emails, phones = extract_contact_details(post.title)
            posts.append({
                'title': post.title or None,
                'url': post.url or None,
                'contact': post.author.name if post.author else None,
                'email': emails or None,
                'phone': phones or None
            })
        return posts
    except Exception as e:
        print(f"Reddit scraping error: {e}")
        return []


# --- Main Function to Collect Posts from All Platforms ---
def scrape_posts(industry, keywords, country):
    posts = []

    # Twitter Scraping (Both API and snscrape)
    if len(keywords) > 0:
        # posts += scrape_twitter_api(keywords[0])  # Twitter API
        # posts += scrape_twitter_snscrape(keywords[0])  # snscrape

    # Facebook Scraping (Both API and snscrape)
     if country.lower() == "usa" and len(keywords) > 1:
        posts += scrape_facebook_api(keywords[1])  # Facebook API
        posts += scrape_facebook_snscrape("https://www.facebook.com/page_name")  # snscrape

    # Simplified LinkedIn Scraping with a single profile URL
    linkedin_posts = scrape_linkedin('https://www.linkedin.com/in/sample-profile/')
    posts += linkedin_posts

    # Reddit Scraping
    reddit_posts = scrape_reddit('subreddit_name')
    posts += reddit_posts

    return posts


