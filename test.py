# This is a test file to check if the APIs i was using are working or not i have commented everything for better understanding
import os
import re
import snscrape.modules.twitter as sntwitter
from bs4 import BeautifulSoup
from facebook_scraper import get_posts
import instaloader
import praw
import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# --- 1. Twitter Scraping (snscrape) ---
import ssl
import snscrape.modules.twitter as sntwitter

# Disable SSL verification (not recommended for production environments)
# ssl._create_default_https_context = ssl._create_unverified_context

# def test_twitter_scrape(keyword="Messi"):
#     query = f"{keyword} since:2020-01-01"
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
#         if i > 0:  # Limit to a single tweet for testing
#             break
#         print(f"Username: {tweet.user.username}")
#         print(f"Content: {tweet.content}")

# test_twitter_scrape()


# --- 2. Facebook Scraping ---
def test_facebook_scrape(page_name="FC Barcelona"):
    for post in get_posts(page_name, pages=1):
        return {'content': post['text'], 'post_url': post['post_url']}

# --- 3. Instagram Scraping (instaloader) ---
def test_instagram_scrape(username="leomessi"):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    for post in profile.get_posts():
        return {'content': post.caption, 'url': post.url}

# --- 4. Reddit Scraping (praw) ---
def test_reddit_scrape(subreddit_name="football"):
    reddit = praw.Reddit(
            client_id=os.getenv('9FU-6d330ZoDkytgzwfwBg'),
            client_secret=os.getenv('J1Ijclx4730k0lydnA6TcPXc1k_A_Q'),
            user_agent=os.getenv('user_agent_me')
            
            
        )
    
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.hot(limit=1):
        return {'title': post.title, 'url': post.url}

# --- 5. Twitter Scraping using Tweepy API ---
    # auth = tweepy.OAuth1UserHandler('924dwylHJBwTBWtCH7zeF3lE0',
    #                                       'FxciPLZQmQUtlFbGGQxXluOfJDKEdWV7ttL6fFazPnIsPO7pda', 
    #                                       '1832493701416767488-OIbMeaG3kLu9lvrib4NITjVksOPO4E',
    #                                          'dKtK5BYl5N1qHgkcBV65tkDh2a2YT881YAfLJnHF9mjX4')
    # api = tweepy.API(auth)
    # for tweet in tweepy.Cursor(api.search, q=keyword, lang='en').items(1):
    #     return {'username': tweet.user.screen_name, 'content': tweet.text}

# --- 6. Web Scraping with Selenium ---
def test_selenium_scrape(url="https://www.goal.com/en/player/lionel-messi/6t9l55yk33b1l45uvfjoej7i9"):
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path
    driver.get(url)
    element = driver.find_element_by_tag_name('h1')
    result = {'title': element.text}
    driver.quit()
    return result

# --- 7. Web Scraping with BeautifulSoup ---
def test_beautifulsoup_scrape(url="https://www.goal.com/en/player/lionel-messi/6t9l55yk33b1l45uvfjoej7i9"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return {'title': soup.find('h1').text}

if __name__ == "__main__":
    # # Twitter Scraping (snscrape) for Messi
    # twitter_result = test_twitter_scrape("Messi")
    # print("Twitter (snscrape):", twitter_result)

    # Facebook Scraping for Messi
    facebook_result = test_facebook_scrape('FC Barcelona')
    print("Facebook:", facebook_result)

    # Instagram Scraping for Messi
    instagram_result = test_instagram_scrape('leomessi')
    print("Instagram:", instagram_result)

    # Reddit Scraping for Messi
    reddit_result = test_reddit_scrape('football')
    print("Reddit:", reddit_result)

    # Tweepy API Scraping (if you have API keys, fill them in)
    # Uncomment and add API keys
    # tweepy_result = test_tweepy_scrape('API_KEY', 'API_KEY_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET', "Messi")
    # print("Twitter (Tweepy):", tweepy_result)

    # Selenium Web Scraping for Messi info from a webpage
    selenium_result = test_selenium_scrape('https://www.goal.com/en/player/lionel-messi/6t9l55yk33b1l45uvfjoej7i9')
    print("Selenium:", selenium_result)

    # BeautifulSoup Web Scraping for Messi info
    bsoup_result = test_beautifulsoup_scrape('https://www.goal.com/en/player/lionel-messi/6t9l55yk33b1l45uvfjoej7i9')
    print("BeautifulSoup:", bsoup_result)
