from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Setup folders
image_folder = "latex_images"
output_base_folder = "screenshots"
os.makedirs(output_base_folder, exist_ok=True)

# Generate Q1.png to Q100.png
#image_names = [f"Q{i}.png" for i in range(1, 101)]
image_names = [f"Q{i}.png" for i in range(71, 81)]


# Chrome options with logging
options = Options()
options.add_argument("--start-maximized")
options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

driver = webdriver.Chrome(options=options)

for name in image_names:
    question_id = name.replace(".png", "")
    image_path = os.path.abspath(os.path.join(image_folder, name))

    # Create a subfolder for the current question
    question_folder = os.path.join(output_base_folder, question_id)
    os.makedirs(question_folder, exist_ok=True)

    for attempt in range(1, 10):  # Run 9 times
        try:
            screenshot_name = f"{question_id}.{attempt}_solution.png"
            screenshot_path = os.path.abspath(os.path.join(question_folder, screenshot_name))

            print(f"\n🔁 Processing: {name} (Attempt {attempt}/9)")
            driver.get("https://metamersive-math-dse.vercel.app/")
            driver.execute_script("document.body.style.zoom='120%'")
            time.sleep(2)

            # Upload file
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(image_path)
            print("⏳ Waiting for 'Solution Response'...")

            # Wait for console output
            found = False
            timeout = 150
            start_time = time.time()

            while time.time() - start_time < timeout:
                logs = driver.get_log("browser")
                for entry in logs:
                    if "Solution Response" in entry["message"]:
                        print("✅ Detected 'Solution Response'. Capturing screenshot...")
                        driver.save_screenshot(screenshot_path)
                        print(f"📸 Saved: {screenshot_path}")
                        found = True
                        break
                if found:
                    break
                time.sleep(1)

            if not found:
                print(f"⚠️ Timeout. No solution found for {name} (Attempt {attempt})")

        except Exception as e:
            print(f"❌ Error processing {name} (Attempt {attempt}): {e}")

driver.quit()
