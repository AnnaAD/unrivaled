import requests
from bs4 import BeautifulSoup
import csv



url = "https://www.unrivaled.basketball/schedule"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print(f"Failed to fetch URL: {response.status_code}")
    exit()

s = BeautifulSoup(html_content, "html.parser")
print(s.find_all("a"))
game_list = ["https://www.unrivaled.basketball" + l["href"] for l in s.find_all("a") if "box-score" in l["href"]]
print(game_list)

data = []
# Step 1: Fetch the HTML content from the URL
for url in game_list:
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
    else:
        print(f"Failed to fetch URL: {response.status_code}")
        exit()

    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    # Step 3: Locate the table
    for table in soup.find_all("table", {"class": "w-100"}):

        # Step 4: Extract table headers and rows
        headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]
        rows = table.find("tbody").find_all("tr")

        # Step 5: Accumulate stats per player
        for row in rows:
            cells = row.find_all("td")
            if cells:  # Ignore empty rows
                player_data = [cell.get_text(strip=True) for cell in cells]
                player_data.extend([""] * (14 - len(player_data)))
                data.append(player_data)

# Step 6: Save the data to a CSV file
csv_file = "basketball_stats.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Write headers to the CSV file
    writer.writerows(data)  # Write data to the CSV file

print(f"Data has been saved to {csv_file}")
