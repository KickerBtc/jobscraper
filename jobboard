from selenium import webdriver
from bs4 import BeautifulSoup
import csv
# you must install selenium and beautifulsoup4 first // pip install selenium beautifulsoup4 #
#to do: check days since job posting#
#append new column for dates#
#also write results to .txt file#
#search for website or linkedin link#
#append new column if link found#
def scrape_jobs(url):
    # Set up the webdriver
    driver = webdriver.Firefox()
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Get the HTML content of the website
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find all job listings
    job_listings = soup.find_all(class_='card')

    # Extract the job titles and companies
    jobs = []
    for job in job_listings:
        # Find h2 and h3 tags
        title = job.find('h2').get_text()
        company = job.find('h3').get_text()
        jobs.append((title, company))

    # Close the webdriver
    driver.quit()

    return jobs

# Scrape the jobs from the website
url = "https://cryptocurrencyjobs.co/remote/"
jobs = scrape_jobs(url)

# Write the results to a CSV file
with open('jobs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Company'])
    for job in jobs:
        writer.writerow(job)

# Print the number of results
print(f"Number of results: {len(jobs)}")
