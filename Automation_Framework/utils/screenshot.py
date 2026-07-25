import os 

from datetime import datetime 

def capturescreenshot(driver, test_name): 

    if not os.path.exists("screenshots"): 
        os.makedirs("screenshots") 

    time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S") # screenshot_20262507_020706.png

    file_name = f"{test_name}_{time_stamp}.png"  #test_login_20262507_020706.png

    file_path =os.path.join("screenshots", file_name) # screenshots/test_login_20262507_020706.png

    driver.save_screenshot(file_path) 

    return file_path