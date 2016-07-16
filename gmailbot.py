from bs4 import BeautifulSoup
import argparse, os, time
import urlparse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def ViewBot(browser):
	page = BeautifulSoup(browser.page_source,"html.parser")
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if '/mail' in url:
				browser.get(url)
	time.sleep(5)
	browser.find_element_by_xpath("//div[text()='COMPOSE']").send_keys(Keys.RETURN)
	time.sleep(6)
	browser.find_element_by_xpath("//textarea[@name='to']").send_keys("lappy176@gmail.com")
	browser.find_element_by_xpath("//input[@name='subjectbox']").send_keys("Hello")
	time.sleep(1)
	browser.find_element_by_xpath("//div[@class='Ar Au']//div").send_keys("This is an auto generated mail")
	time.sleep(1)
	browser.find_element_by_xpath("//div[contains(text(),'Send')]").click()
	time.sleep(3)
	print "Messege sent successfully"
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if '/Logout' in url:
				browser.get(url)
	time.sleep(5)
	print "Logged out successfully"
	browser.close()

def main():
	email = raw_input("Enter the email id\n")
	password = raw_input("Enter the password\n")

	browser = webdriver.Firefox()
	browser.get("https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.co.in/%3Fclient%3Dfirefox-b-ab#identifier")

	emailElement = browser.find_element_by_id("Email")
	emailElement.send_keys(email)
	emailElement.submit()
	time.sleep(2) ##necessary so that the page can load otherwise gives an error.
	passElement = browser.find_element_by_name("Passwd")
	passElement.send_keys(password)
	passElement.submit()
	print "Successfully logged in"

	os.system('cls')
	ViewBot(browser)
	

if __name__ == '__main__':
	main()
