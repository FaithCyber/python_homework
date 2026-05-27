
# Task 3: Import libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import json
import time


# Task 3: Load page


url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url)

time.sleep(5)

# Task 3: Find all book entries

book_entries = driver.find_elements(By.TAG_NAME, "li")

print("Total LI elements:", len(book_entries))

results = []


# Task 3: Main scraping loop

for book in book_entries:

    try:

        # Replace class names with actual ones from DevTools
        title = book.find_element(By.CLASS_NAME, "cp-title").text

        author_elements = book.find_elements(By.CLASS_NAME, "author-link")

        authors = []

        for author in author_elements:
            authors.append(author.text)

        author_text = "; ".join(authors)

        format_div = book.find_element(By.CLASS_NAME, "display-info-primary")

        format_year = format_div.text

        data = {
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        }

        results.append(data)

    except:
        pass


# Task 3: Create DataFrame

df = pd.DataFrame(results)

print(df)


# Task 4: Saved CSV

df.to_csv("get_books.csv", index=False)


# Task 4: Saved JSON


with open("get_books.json", "w") as file:
    json.dump(results, file, indent=4)

driver.quit()

print("Files created successfully.")