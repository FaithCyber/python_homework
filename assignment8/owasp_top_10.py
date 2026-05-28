# Task 6: OWASP Top 10 Scraper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


# open browser


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Launch OWASP Top 10 page


url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

# Wait for page to run
time.sleep(5)


# correction Improved XPath targeting: 
# Focus ONLY on the ordered list (Top 10 section)


items = driver.find_elements(
    By.XPATH,
    "//main//ol//li//a"
)

print("Items found:", len(items))


# Extract data

results = []

for item in items:

    try:
        title = item.text.strip()
        link = item.get_attribute("href")

        if title and link:
            results.append({
                "Title": title,
                "Link": link
            })

    except Exception as e:
        print("Skipped item:", e)


# Convert to DataFrame


df = pd.DataFrame(results)

print(df)


# Save CSV


df.to_csv("owasp_top_10.csv", index=False)


# Close browser


driver.quit()

print("OWASP Top 10 data saved successfully.")