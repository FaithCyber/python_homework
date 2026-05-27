from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://owasp.org/www-project-top-ten/"

driver.get(url)

time.sleep(5)

results = []

# Example XPath — inspect page for exact structure
items = driver.find_elements(By.XPATH, "//a[contains(@href, 'A0')]")

for item in items:

    title = item.text
    link = item.get_attribute("href")

    results.append({
        "Title": title,
        "Link": link
    })

print(results)

df = pd.DataFrame(results)

df.to_csv("owasp_top_10.csv", index=False)

driver.quit()