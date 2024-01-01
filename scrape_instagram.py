import pandas as pd
import os, re, time, asyncio
from dotenv import load_dotenv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(username, password):
    driver.get('https://www.instagram.com/')
    username_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
    pass_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, 'password'))
            )
    username_field.send_keys(username)
    pass_field.send_keys(password)
    print(f"Login to {username}'s instagram")
    pass_field.submit()
    time.sleep(10)
    
    return

def scrape_post(post_url):
    post_comments = []
    driver.get(post_url)
    WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'span.x5n08af'))
            )
    driver.implicitly_wait(5)
    comments = driver.find_elements(By.CSS_SELECTOR, 'span.x5n08af')
    for comment in comments:
        post_comments.append(comment.text)
        print(comment.text)

    return post_comments

if __name__ == '__main__':
    load_dotenv()
    username = os.getenv('IG_USERNAME')
    password = os.getenv('IG_PASS')
    posts = ['https://www.instagram.com/p/Cz8sjzavM0T/']
    post_comments = {}

    driver = webdriver.Chrome()
    login(username, password)
    for post in posts:
        comments = scrape_post(post)
        post_comments[post] = comments

        time.sleep(30)
    pd.DataFrame(post_comments).to_csv(f'results/{time.time()}.csv')

    # x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj
    # # x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft
    # # x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x10wh9bi x1wdrske x8viiok x18hxmgj
    # # _ap3a _aaco _aacw _aacx _aad7 _aade
    # x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1