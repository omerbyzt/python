# -*- coding: utf-8 -*-

r"""
git-hub follower bot
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

TARGET_ACCOUNT = "caglartoklu"

driver = webdriver.Chrome()
driver.get("https://github.com/" + TARGET_ACCOUNT + "?tab=followers")
counts = driver.find_elements_by_css_selector(".text-bold.text-gray-dark")

followers_count = int(counts[0].text)
following_count = int(counts[1].text)

def main():
    
    print("son")

main()