import requests
import json

# Set the base URL for the RocketReach API
base_url = "https://api.rocketreach.co/v1/search/email"

# Set the parameters for the search
# Replace YOUR_API_KEY with your RocketReach API key
params = {
  "q": "fintech blockchain defi cryptocurrency executive",
  "limit": 10,
  "source": "linkedin"
}

# Set the headers for the request
# Replace YOUR_API_KEY with your RocketReach API key
headers = {
  "Authorization": f"Bearer YOUR_API_KEY",
  "Content-Type": "application/json"
}

# Make a request to the RocketReach API
response = requests.get(base_url, params=params, headers=headers)

# Parse the response as JSON
data = response.json()

# Get the list of people from the response
people = data["people"]

# Iterate through the list of people
for person in people:
  # Get the person's name and email
  name = person["name"]
  email = person["email"]
  
  # Get the list of job openings from the person's profile
  job_openings = person["jobs"]
  
  # Filter the list of job openings to only include those with more than 1 opening
  job_openings = [job for job in job_openings if job["openings"] > 1]
  
  # Print the person's name and email if they have more than 1 job opening
  if job_openings:
    print(f"{name}: {email}")