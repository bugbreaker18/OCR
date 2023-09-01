import requests
from bs4 import BeautifulSoup
import json

# Define the URL of the HTML page you want to parse
url = "https://example.com"

# Send an HTTP GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Create a dictionary to store the data you want to extract
data = {}

# Example: Extract the title and store it in the dictionary
data['title'] = soup.title.string

# Example: Extract all the links on the page and store them in a list
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
data['links'] = links

# Convert the data dictionary to JSON format
json_data = json.dumps(data, indent=4)

# Print or save the JSON data
print(json_data)

# If you want to save the JSON data to a file, you can use the following:
# with open('output.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)
