from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ⚠️⚠️⚠️ ඔබගේ TikTok Login තොරතුරු මෙහි ඇතුළත් කරන්න ⚠️⚠️⚠️
# Remember to change these to your actual credentials for testing!
TIKTOK_USERNAME = "your_test_tiktok_username"  
TIKTOK_PASSWORD = "your_test_tiktok_password" 
COMMENT_TEXT = "Wow! Great video! Keep up the good work. #tiktokbot"

def promote_video(video_url):
    print(f"\n--- Starting Bot for: {video_url} ---")
    
    # Chrome Browser Settings
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Browser eka nopenwa wada karanna (Optional)
    options.add_argument("--start-maximized")
    
    # Chrome Driver eka install kara Browser eka open kirima
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Wait Object eka hadanna (Timeout: 10 seconds)
    wait = WebDriverWait(driver, 10)

    try:
        # 1. TikTok Login වීමට උත්සාහ කිරීම
        print("1. Attempting to navigate to TikTok and login...")
        driver.get("https://www.tiktok.com/login")
        time.sleep(3) # Wait for the initial page to load
        
        # 'Use phone/email/username' option එක click කරන්න (සාමාන්‍යයෙන් මුල්ම පියවර)
        # Note: TikTok login page elements change frequently! This might require updates.
        try:
             login_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Use phone / email / username")]')))
             login_option.click()
             print("Clicked login option.")
        except:
             print("Could not find or click 'Use phone/email/username' button. Proceeding.")


        # Username/Email field එක සොයා data ඇතුල් කිරීම
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys(TIKTOK_USERNAME)
        
        # Password field එක සොයා data ඇතුල් කිරීම
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(TIKTOK_PASSWORD)
        
        # Login Button එක click කිරීම
        login_btn = driver.find_element(By.XPATH, '//button[@data-e2e="login-button"]')
        login_btn.click()
        
        print("Login credentials sent. Waiting for page load...")
        time.sleep(10) # Login එක සනාථ වන තුරු වැඩිපුර වෙලාවක් නවතී (Captcha/security check එන්න පුළුවන්)
        
        
        # 2. වීඩියෝව විවෘත කිරීම
        print(f"2. Opening target video: {video_url}")
        driver.get(video_url)
        time.sleep(5) 

        
        # 3. Comment එකක් Post කිරීම
        print("3. Attempting to post comment...")
        
        # Comment input field එක සොයා ගැනීම
        comment_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')))
        
        # Comment එක ටයිප් කිරීම
        comment_box.send_keys(COMMENT_TEXT)
        print(f"Comment added: '{COMMENT_TEXT}'")
        
        time.sleep(2)
        
        # Comment Post Button එක සොයා Click කිරීම
        # Note: Post button එකේ XPATH එක නිතර වෙනස් වෙනවා!
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Post"]')))
        post_button.click()
        
        print("Comment posted successfully!")
            
    except Exception as e:
        print(f"\n!!! An error occurred during bot execution or element finding: {e}")
        print("The bot might have failed due to TikTok page changes or a security check.")

    finally:
        # Browser එක වසා දමයි
        driver.quit()
        print(f"--- Bot finished for: {video_url} ---")
