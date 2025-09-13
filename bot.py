from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def promote_video(video_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open video
    driver.get(video_url)
    time.sleep(5)

    # Example: Like the video
    try:
        like_btn = driver.find_element(By.XPATH, '//span[@data-e2e="like-icon"]')
        like_btn.click()
        print(f"Liked video: {video_url}")
    except:
        print("Like failed")

    # Close browser
    driver.quit()
