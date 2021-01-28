# -*- coding: utf-8 -*-

r"""
#python github_follower_control.py

github_follower_control.py

bizim follow ettiğimiz kişiler, bizi follow ediyor mu?
etmeyenleri tespit edelim.

https://anaconda.org/conda-forge/selenium
Anaconda prompt'da çalıştıralım:
    conda install -c conda-forge selenium

#login olmak istersek 

driver.get("https://github.com/login")

username = driver.find_element_by_name("login")
username.send_keys("deneme300")
time.sleep(2)

password = driver.find_element_by_name("password")
password.send_keys("Denemesifre123")
time.sleep(2)

login_btn = driver.find_element_by_name("commit")
login_btn.click()
"""

TARGET_ACCOUNT = "caglartoklu"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://github.com/" + TARGET_ACCOUNT + "?tab=followers")
time.sleep(2)
counts = driver.find_elements_by_css_selector(".text-bold.text-gray-dark")

followers_count = int(counts[0].text)
following_count = int(counts[1].text)

followers_page_count = 0
followings_page_count = 0

if followers_count % 50 == 0:
    followers_page_count = int(followers_count/50)
else:
    followers_page_count = int(followers_count/50) +1

if following_count % 50 == 0:
    followings_page_count = int(following_count/50)
else:
    followings_page_count = int(following_count/50) +1

followers_link = []
followings_link = []

print("FOLLOWERS")
print("-------------------------------")

for i in range(followers_page_count):
    driver.get("https://github.com/" + TARGET_ACCOUNT + "?page="+ str(i+1) + "&tab=followers")
    # https://github.com/caglartoklu?page=1&tab=followers

    followers = driver.find_elements_by_css_selector(".d-inline-block.no-underline.mb-1")
 
    for follower in followers:
        link = follower.get_attribute('href')
        followers_link.append(link)
    
count = 1
for e in followers_link:
    print(count, " -> ", e)
    count += 1

print("FOLLOWING")
print("-------------------------------")

for i in range(followings_page_count):
    driver.get("https://github.com/" + TARGET_ACCOUNT + "?page="+ str(i+1) + "&tab=following")
    # https://github.com/caglartoklu?page=2&tab=following

    followings = driver.find_elements_by_css_selector(".d-inline-block.no-underline.mb-1")
 
    for following in followings:
        link = following.get_attribute('href')
        followings_link.append(link)
    
count = 1
for e in followings_link:
    print(count, " -> ", e)
    count += 1


print("Followings - Followers")
print("----------------------------")

following_not_followers = set(followings_link) - set(followers_link)

count = 1
for e in following_not_followers:
    print(count, " -> ", e)
    count += 1


print("Followers - Followings")
print("----------------------------")

followers_not_following = set(followers_link) - set(followings_link)

count = 1
for e in followers_not_following:
    print(count, " -> ", e)
    count += 1