#this is my old file i saved code here this is not important
# import os
# import re
# import snscrape.modules.twitter as sntwitter
# from bs4 import BeautifulSoup
# from facebook_scraper import get_posts
# import instaloader
# import praw
# import tweepy
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # Function to extract email and phone number
# def extract_contact_details(text):
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     phone_pattern = r'\+?\d[\d -]{8,12}\d'
#     emails = re.findall(email_pattern, text) if text else []
#     phones = re.findall(phone_pattern, text) if text else []
#     return emails, phones

# # --- Instagram Scraper ---
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

# # --- Facebook Scraper - API Method (facebook_scraper) ---
# def scrape_facebook_api(page_name):
#     try:
#         posts = []
#         for post in get_posts(page_name, pages=1):
#             emails, phones = extract_contact_details(post.get('text', ''))
#             posts.append({
#                 'title': post.get('text', None),
#                 'url': post.get('post_url', None),
#                 'contact': post.get('username', None),
#                 'email': emails or None,
#                 'phone': phones or None
#             })
#         return posts
#     except Exception as e:
#         print(f"Facebook API scraping error: {e}")
#         return []

# # --- Facebook Scraper - snscrape Method ---
# def scrape_facebook_snscrape(page_url):
#     command = f"snscrape facebook-page {page_url} > facebook_posts.txt"
#     os.system(command)
#     with open('facebook_posts.txt', 'r') as file:
#         data = file.read()
#     soup = BeautifulSoup(data, 'html.parser')
#     posts = []
#     for post in soup.find_all('div', class_='post'):
#         emails, phones = extract_contact_details(post.text)
#         posts.append({
#             'title': post.text,
#             'url': post.find('a')['href'],
#             'contact': post.find('span', class_='username').text,
#             'email': emails,
#             'phone': phones
#         })
#     return posts

# # --- Twitter Scraper - API Method (tweepy) ---
# # def scrape_twitter_api(username):
# #     try:
# #         auth = tweepy.OAuth1UserHandler('924dwylHJBwTBWtCH7zeF3lE0',
# #                                           'FxciPLZQmQUtlFbGGQxXluOfJDKEdWV7ttL6fFazPnIsPO7pda', 
# #                                           '1832493701416767488-OIbMeaG3kLu9lvrib4NITjVksOPO4E',
# #                                             'dKtK5BYl5N1qHgkcBV65tkDh2a2YT881YAfLJnHF9mjX4')
# #         api = tweepy.API(auth)
# #         tweets = api.user_timeline(screen_name=username, count=10)
# #         posts = []
# #         for tweet in tweets:
# #             emails, phones = extract_contact_details(tweet.text)
# #             posts.append({
# #                 'title': tweet.text or None,
# #                 'url': f"https://twitter.com/{username}/status/{tweet.id}" or None,
# #                 'contact': username or None,
# #                 'email': emails or None,
# #                 'phone': phones or None
# #             })
# #         return posts
# #     except Exception as e:
# #         print(f"Twitter API scraping error: {e}")
# #         return []

# # --- Twitter Scraper - snscrape Method ---
# # def scrape_twitter_snscrape(keyword):
# #     tweets = []
# #     for tweet in sntwitter.TwitterSearchScraper(f'{keyword}').get_items():
# #         emails, phones = extract_contact_details(tweet.content)
# #         tweets.append({
# #             'title': tweet.content,
# #             'url': tweet.url,
# #             'contact': tweet.user.username,
# #             'email': emails,
# #             'phone': phones
# #         })
# #         if len(tweets) >= 50:
# #             break
# #     return tweets

# # --- LinkedIn Scraper using Selenium ---
# def scrape_linkedin(profile_url):
#     try:
#         driver = webdriver.Chrome(executable_path='path_to_chromedriver')
#         driver.get('https://www.linkedin.com/login')
#         username = driver.find_element_by_name('session_key')
#         password = driver.find_element_by_name('session_password')
#         username.send_keys('professordhar69@gmail.com')  # Replace with your LinkedIn email
#         password.send_keys('forgotpassword')  # Replace with your LinkedIn password
#         password.send_keys(Keys.RETURN)
#         driver.get(profile_url)
#         name = driver.find_element_by_css_selector('h1').text or None
#         posts = [{
#             'title': name,
#             'url': profile_url,
#             'contact': name,
#             'email': None,
#             'phone': None
#         }]
#         driver.quit()
#         return posts
#     except Exception as e:
#         print(f"LinkedIn scraping error: {e}")
#         return []

# # --- Reddit Scraper using PRAW ---
# def scrape_reddit(subreddit_name):
#     try:
#         reddit = praw.Reddit(client_id='9FU-6d330ZoDkytgzwfwBg', client_secret='J1Ijclx4730k0lydnA6TcPXc1k_A_Q', user_agent='user_agent')
#         subreddit = reddit.subreddit(subreddit_name)
#         posts = []
#         for post in subreddit.hot(limit=10):
#             emails, phones = extract_contact_details(post.title)
#             posts.append({
#                 'title': post.title or None,
#                 'url': post.url or None,
#                 'contact': post.author.name if post.author else None,
#                 'email': emails or None,
#                 'phone': phones or None
#             })
#         return posts
#     except Exception as e:
#         print(f"Reddit scraping error: {e}")
#         return []

# # --- Main Function to Collect Posts from All Platforms ---
# def scrape_posts(industry, keywords, country):
#     posts = []
    
#     # Twitter Scraping (Both API and snscrape)
#     if len(keywords) > 0:
#         # posts += scrape_twitter_api(keywords[0])  # Twitter API
#         # posts += scrape_twitter_snscrape(keywords[0])  # snscrape

#     # Facebook Scraping (Both API and snscrape)
#      if country.lower() == "usa" and len(keywords) > 1:
#         posts += scrape_facebook_api(keywords[1])  # Facebook API
#         posts += scrape_facebook_snscrape("https://www.facebook.com/page_name")  # snscrape

#     # Instagram Scraping
#     posts += scrape_instagram('instagram_handle')

#     # LinkedIn Scraping
#     posts += scrape_linkedin('linkedin_profile_url')

#     # Reddit Scraping
#     posts += scrape_reddit('subreddit_name')

#     return posts




