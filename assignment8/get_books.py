#task1 robots.txt compliance
# Reviewed robots.txt compliance for Durham County
# and confirmed this scraping activity
# complies with the website's access policies.


# Task 3: Import libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import json
import time

# Task 1 note (required for grading)
# Reviewed Durham County Library robots.txt and confirmed compliance

# Task 3: Load page

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

time.sleep(5)

# Task 3: FIXED — only real search results
book_entries = driver.find_elements(
    By.CSS_SELECTOR,
    "li.cp-search-result-item"
)

print("Total search results found:", len(book_entries))

results = []

# Task 3: Main scraping loop

for book in book_entries:

    # Title
    title_elements = book.find_elements(By.CLASS_NAME, "cp-title")
    title = title_elements[0].text if title_elements else ""

    # Authors
    author_elements = book.find_elements(By.CLASS_NAME, "author-link")
    authors = [a.text for a in author_elements if a.text.strip() != ""]
    author_text = "; ".join(authors)

    # Format + Year
    format_elements = book.find_elements(By.CLASS_NAME, "display-info-primary")
    format_year = format_elements[0].text if format_elements else ""

    # Store data
    if title:
        results.append({
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        })

# Task 4: Create DataFrame

df = pd.DataFrame(results)
print(df)

# Task 4: Save CSV

df.to_csv("get_books.csv", index=False)

# Task 4: Save JSON

with open("get_books.json", "w") as file:
    json.dump(results, file, indent=4)

driver.quit()

print("Files created successfully.")