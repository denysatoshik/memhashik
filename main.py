import time
import asyncio
from datetime import datetime, timedelta, timezone
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from aiogram import Bot, Dispatcher, types
from config import TOKEN, URL

# Telegram bot setup
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

screenshot_path = "screenshot.png"
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(URL)


def capture_screenshot():
    """Creates a screenshot of the page."""
    try:
        driver.save_screenshot(screenshot_path)
    except Exception as e:
        print(f"Error creating screenshot: {e}")


def click_button():
    """Clicks a button on the page."""
    try:
        time.sleep(10)  # Waiting for the page to load
        element = driver.find_element(By.TAG_NAME, "body")  # Specify the required selector
        action = ActionChains(driver)
        action.move_to_element_with_offset(element, 0, -65).click().perform()
    except Exception as e:
        print(f"Error clicking: {e}")


async def wait_and_click_continuous():
    """Click once and then keep the program running."""
    print(f"Starting mining in a few seconds...")
    click_button()  # Perform the click once
    print("\033[32mMining started!\033[0m")
    while True:
        print("\033[32mMining...\033[0m")
        await asyncio.sleep(60)  # Keeps the program running without clicking
        

async def wait_and_click_with_mining_recharge(mining_duration: int, recharge_duration: int):
    """Handles mining and recharging cycle, including stopping mining after the mining duration."""
    while True:
        # Start mining
        print(f"Starting mining for {mining_duration} seconds...")
        click_button()  # Perform the click to start mining
        print("\033[32mMining started!\033[0m")

        # Wait for the mining duration
        await asyncio.sleep(mining_duration)

        # Stop mining by clicking again
        print(f"Mining finished. Stopping mining...")
        click_button()  # Perform the click to stop mining
        print("\033[31mMining stop!\033[0m")

        # Start recharging
        print(f"Starting recharge for {recharge_duration} seconds...")
        print("\033[32mRecharging...\033[0m")

        # Wait for the recharge duration
        await asyncio.sleep(recharge_duration)

        print("Recharge finished. Starting next mining cycle...")

def display_time_conversion():
    """Displays a table of time conversions from seconds to minutes for specific intervals."""
    intervals = [5, 10, 15, 25, 30, 35, 40, 45, 50, 60]  # Specific intervals in minutes
    print("\nTime Conversion (Seconds to Minutes):")
    print(f"{'Seconds':<10}{'Minutes'}")
    print("="*20)
    for minutes in intervals:
        seconds = minutes * 60
        print(f"{seconds:<10}{minutes} min")
    print("="*20)


@dp.message_handler(commands=['screen'])
async def send_screenshot(message: types.Message):
    """Sends a screenshot in response to the /screen command."""
    capture_screenshot()
    await message.answer("Creating screenshot, please wait...")
    await message.answer_document(open(screenshot_path, 'rb'))


async def main():
    """Main asynchronous function to run the bot and clicks."""
    print("\nChoose an option to run the bot:")
    print("1. Run the bot continuously.")
    print("2. Start mining for a specified duration, then recharge.\n")

    # Prompt the user to select the mode
    option = input("Enter option (1 or 2): \n")

    if option == "1":
        # Option 1: Run the bot continuously.
        asyncio.create_task(wait_and_click_continuous())
    elif option == "2":
        # Display time conversion table
        display_time_conversion()

        # Option 2: Ask the user for mining and recharge durations.
        mining_duration = int(input("\nEnter mining duration in seconds: \n"))
        recharge_duration = int(input("Enter recharge duration in seconds: \n"))
        asyncio.create_task(wait_and_click_with_mining_recharge(mining_duration, recharge_duration))
    else:
        print("\033[31mInvalid option selected.\033[0m")
        return

    # Start the bot polling
    print("\033[32m\nBot is running...\n\033[0m")
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())  # Start the main event loop
