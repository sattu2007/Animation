from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Start the WebDriver and open the HTML page
service = Service(executable_path='/usr/local/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://github.com/sattu2007/Animation/")  # Update this with the path to your HTML file

time.sleep(2)  # Adding a delay to see the result

# Assert some condition to verify the result
assert "My Animation" in driver.title

# Close the WebDriver
driver.close()
