import requests
from bs4 import BeautifulSoup

# GitHub Trending URL
url = "https://github.com/trending"

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all trending repositories
repos = soup.select("h2 a")  # Repo names are inside <h2> -> <a> tags

# Print total repositories found
print(f"Total repositories found: {len(repos)}\n")

# Print the top 15 trending GitHub repositories
print(" Top 15 Trending GitHub Repositories:\n")
for i, repo in enumerate(repos[:15], start=1):  
    repo_name = repo.get_text(strip=True).replace("\n", "").replace(" ", "")  # Clean text
    repo_link = "https://github.com" + repo['href']  # Construct full URL
    print(f"{i}. {repo_name}\n   {repo_link}\n")
