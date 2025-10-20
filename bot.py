from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ⚠️⚠️⚠️ ඔබගේ TikTok Login තොරතුරු මෙහි ඇතුළත් කරන්න ⚠️⚠️⚠️
TIKTOK_USERNAME = "your_test_tiktok_username"  
TIKTOK_PASSWORD = "your_test_tiktok_password" 
COMMENT_TEXT = "Wow! Great video! This bot is powerful! #automated" # නව comment එක

def promote_video(video_url):
    print(f"\n--- Starting Bot for: {video_url} ---")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15) # Wait time eka 15s walata wadi kalath hondayi.

    try:
        # --- 1. TikTok Login වීමට උත්සාහ කිරීම (Login Attempt) ---
        print("1. Attempting to login...")
        driver.get("https://www.tiktok.com/login")
        
        # Login page eke elements sitema wenas wenna puluwan!
        try:
             # Username/Email field එක සොයා data ඇතුල් කිරීම
             login_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Use phone / email / username")]')))
             login_option.click()
             
             username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
             username_field.send_keys(TIKTOK_USERNAME)
             
             password_field = driver.find_element(By.NAME, "password")
             password_field.send_keys(TIKTOK_PASSWORD)
             
             login_btn = driver.find_element(By.XPATH, '//button[@data-e2e="login-button"]')
             login_btn.click()
             
             print("Login credentials sent. Waiting for page load...")
             time.sleep(10) 
        except Exception as e:
            print(f"Login failed (Could not find elements or security check). Continuing...")
            # Login wenne nathuwa actions karanna amaru wenawa.
        
        # --- 2. වීඩියෝව විවෘත කිරීම (Open Video) ---
        print(f"2. Opening target video: {video_url}")
        driver.get(video_url)
        time.sleep(5) 

        
        # --- 3. Action 1: Video එක Like කිරීම (Action 1: Like Video) ---
        try:
            # Like button එකේ XPATH එක සොයාගෙන Click කරයි
            like_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@data-e2e="like-icon"]')))
            like_btn.click()
            print("Action 1: ✅ Successfully sent 'Like' action.")
            time.sleep(1) 
        except:
            print("Action 1: ❌ Failed to find or click 'Like' button.")
        
        
        # --- 4. Action 2: Comment එකක් Post කිරීම (Action 2: Post Comment) ---
        try:
            print("Action 2: Attempting to post comment...")
            
            # Comment input field එක සොයා ගැනීම
            comment_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')))
            comment_box.send_keys(COMMENT_TEXT)
            
            time.sleep(2)
            
            # Comment Post Button එක සොයා Click කිරීම
            post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Post"]')))
            post_button.click()
            
            print("Action 2: ✅ Comment posted successfully!")
            time.sleep(2)
        except:
            print("Action 2: ❌ Failed to post comment.")
            
            
        # --- 5. Action 3: User ව Follow කිරීම (Action 3: Follow User) ---
        try:
            # Follow Button එක සොයා ගැනීම. මේක ගොඩක් වෙලාවට 'follow-button' e2e attribute ekata allan thiyenawa.
            follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-e2e="follow-button"]')))
            
            # Button eke text eka "Follow" da balanna (denatath follow karalada nadda balanna)
            if follow_button.text.strip().lower() == "follow":
                 follow_button.click()
                 print("Action 3: ✅ Successfully clicked 'Follow' button.")
            else:
                 print("Action 3: 🟡 Already following this user. Skipping Follow.")
            time.sleep(1)
        except:
            print("Action 3: ❌ Failed to find or click 'Follow' button.")

            
    except Exception as e:
        print(f"\n!!! An unexpected error occurred: {e}")

    finally:
        driver.quit()
        print(f"--- Bot execution finished for: {video_url} ---")
