from dotenv import load_dotenv
import os

load_dotenv()

my_username = os.environ['LINKEDIN_USERNAME']
my_password = os.environ['LINKEDIN_PASSWORD']

file_name = 'results.csv' # file where the results will be saved

query = 'site:linkedin.com/in/ AND "Web" AND "Javascript"'
