import variables
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from parsel import Selector
from webdriver_manager.chrome import ChromeDriverManager



# Chrome driver install
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.linkedin.com/')
sleep(2)
# getting the variables name and login
username = driver.find_element(By.CLASS_NAME, 'input__input')
username.send_keys(variables.my_username) # username field

password = driver.find_element(By.NAME, 'session_password')
password.send_keys(variables.my_password) # password field
sleep(3)
log_in_button = driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button') # submit button
log_in_button.click() # click the submit button
sleep(2)
# Making the google query
driver.get('https://www.google.com/')
search_bar = driver.find_element(By.NAME, 'q')
search_bar.send_keys(variables.query)
search_bar.send_keys(Keys.ENTER) # Automating the enter key

# Saving the linkedin users urls in an array to do the scraping

linkedin_users_urls_list = driver.find_elements(By.XPATH, '//div[@class="yuRUbf"]/a[@href]')

profile_urls = []

# To check the list content we run the following command
[profile_urls.append(users.get_attribute("href")) for users in linkedin_users_urls_list]

fields = ['Name','Job Title','Company','University','Location','URL']
sel = Selector(text=driver.page_source)
# What we need from the profile


with open(variables.file_name, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(fields)
    for profiles in profile_urls:
        driver.get(profiles)
        sel = Selector(text=driver.page_source)
        sleep(3)
        name = sel.xpath('//*[starts-with(@class, "text-heading-xlarge")]/text()').extract_first()
        if name:
            name = name.strip()
        else:
            name = 'No Result'
        job_title = sel.xpath('//*[starts-with(@class, "text-body-medium")]/text()').extract_first()
        if job_title:
            job_title = job_title.strip()
        else:
            job_title = 'No Result'
        company = sel.xpath('//*[starts-with(@aria-label, "Current company")]/text()').extract_first()
        if company:
            company = company.strip()
        else:
            company = 'No Result'
        university = sel.xpath('//*[starts-with(@aria-label, "Education")]/text()').extract_first()
        if university:
            university = university.strip()
        else:
            university = 'No Result'
        location = sel.xpath('//*[starts-with(@class, "text-body-small")]/text()').extract_first()
        if location:
            location = location.strip()
        else:
            location = 'No Result'
        linkedin_url = driver.current_url
        writer.writerow([name, job_title, company, university, location, linkedin_url])

    
