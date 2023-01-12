import requests
import json

# Set the base URL for the Dice API
base_url = "https://api.dice.com/jobs"

# Set the parameters for the search
# Replace YOUR_API_KEY with your Dice API key
params = {
  "q": "cryptocurrency",
  "sort": "relevance",
  "page": 1,
  "pageSize": 10
}

# Set the headers for the request
# Replace YOUR_API_KEY with your Dice API key
headers = {
  "Authorization": f"Bearer YOUR_API_KEY",
  "Content-Type": "application/json"
}

# Make a request to the Dice API
response = requests.get(base_url, params=params, headers=headers)

# Parse the response as JSON
data = response.json()

# Get the list of job postings from the response
postings = data["results"]

# Iterate through the list of job postings
for posting in postings:
  # Get the company's name and the job title
  company_name = posting["company"]["name"]
  job_title = posting["jobTitle"]

  # Print the company's name and the job title
  print(f"{company_name}: {job_title}")