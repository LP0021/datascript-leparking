
import os
import glob
from datetime import datetime, timedelta
import csv
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.common.exceptions import InvalidArgumentException


def find_recent_files(suffix, days=20):
    current_date = datetime.now()
    cutoff_date = current_date - timedelta(days=days)
    matched_files = []

    os.chdir('D:\\Oct_leparking\\scripts\\')  # Change to your specific directory if necessary


    print(f"Checking in directory: {os.getcwd()}")  # Debug: Print the directory being checked

    # Debug: List all files in the directory
    all_files = glob.glob('*.*')
    print(f"All files in directory: {all_files}")


    for file in glob.glob(f"*{suffix}*.csv"):
        print(f"Checking file: {file}")  # Debug: print each file name
        try:
            file_date_str = file.split('_')[-1].replace('.csv', '')
            file_date = datetime.strptime(file_date_str, '%Y%m%d')
            print(f"Extracted date: {file_date}")  # Debug: print extracted date

            if file_date > cutoff_date:
                matched_files.append((file, file_date))
                print(f"Matched File: {file} with Date: {file_date_str}")
        except ValueError as e:
            print(f"Date parsing error for file {file}: {e}")

    # Sort files by date closest to current
    matched_files.sort(key=lambda x: x[1], reverse=True)
    if matched_files:
        print(f"Most recent file: {matched_files[0][0]}")
        return matched_files[0][0]
    else:
        print("No recent files found.")
        return None
def extract_last_valid_url(file_path):
    df = pd.read_csv(file_path)
    valid_urls = df[df['URL'].str.len() > 80]
    if not valid_urls.empty:
        return valid_urls.iloc[-1]['URL']
    return None

def find_url_row_in_list(url, url_list_file):
    df = pd.read_excel(url_list_file)
    match = df[df['lot_url'] == url]
    if not match.empty:
        return match.index[0] + 1
    return None




def setup_driver(retries=3):
    driver_path = "C:\\Users\\paule\\AppData\\Local\\geckodriver.exe"
    firefox_binary = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    options = Options()
    options.binary_location = firefox_binary
    options.headless = True  # Enable headless mode

    while retries > 0:
        try:
            service = Service(executable_path=driver_path)
            driver = webdriver.Firefox(service=service, options=options)
            return driver
        except WebDriverException as e:
            print(f"Failed to start WebDriver: {e}")
            retries -= 1
            print(f"Retrying... {retries} attempts left.")
            time.sleep(5)  # Wait for 5 seconds before retrying

    raise Exception("Failed to initialize WebDriver after several attempts.")



def extract_data(driver, url):
    data = []
    try:
        titles = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1) > span:nth-child(1)")
        sub_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1) > span:nth-child(2)")
        sub_links2 = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(1) > a:nth-child(1) > span:nth-child(3)")
        sub_links3 = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3)")
        price = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)")
        price2 = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1)")
        price3 = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > s:nth-child(2)")
        price4 = driver.find_elements(By.CSS_SELECTOR, "li.clearfix:nth-child(12) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
        location = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > span:nth-child(2)")
        fuel_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1)")
        km_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1)")
        year_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(3) > div:nth-child(1)")
        tx_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1)")
        zip_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(5) > div:nth-child(1)")
        weblisted1_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1) > a:nth-child(1)")
        weblisted2_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1) > a:nth-child(2)")
        weblisted3_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1) > a:nth-child(3)")
        weblisted4_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1) > a:nth-child(4)")
        weblisted5_links = driver.find_elements(By.CSS_SELECTOR, "section:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > p:nth-child(1) > a:nth-child(5)")



        hits_elements = driver.find_elements(By.CSS_SELECTOR, ".hits span")

        hits_values = [hit.text if hit.text.isdigit() else "" for hit in hits_elements]  # Handling complex and potentially empty hits
        
        for index, title in enumerate(titles):
            item = {
                "URL": url,
                "Title": title.text if titles else "",
                "Sublinks": sub_links[index].text if index < len(sub_links) else "",
                "Sublinks2": sub_links2[index].text if index < len(sub_links2) else "",
                "Sublinks3": sub_links3[index].text if index < len(sub_links3) else "",
                "Price": price[index].text if index < len(price) else "",
                "Price2": price2[index].text if index < len(price2) else "",
                "Price3": price3[index].text if index < len(price3) else "",
                "Price4": sub_links2[index].text if index < len(price4) else "",
                "Location": location[index].text if index < len(location) else "",
                "Fuel_links": fuel_links[index].text if index < len(fuel_links) else "",
                "km_links": km_links[index].text if index < len(km_links) else "",
                "year_links": year_links[index].text if index < len(year_links) else "",
                "tx_links": sub_links2[index].text if index < len(tx_links) else "",
                "zip_links": zip_links[index].text if index < len(zip_links) else "",
                "weblisted1_links": weblisted1_links[index].text if index < len(weblisted1_links) else "",
                "weblisted2_links": weblisted2_links[index].text if index < len(weblisted2_links) else "",
                "weblisted3_links": weblisted3_links[index].text if index < len(weblisted3_links) else "",
                "weblisted4_links": weblisted4_links[index].text if index < len(weblisted4_links) else "",
                "weblisted5_links": weblisted5_links[index].text if index < len(weblisted5_links) else "",



                "Hits": ' '.join(hits_values)  # Combine all hit numbers into a single string

            }
            data.append(item)


    except NoSuchElementException:
        print("Element not found")
    except Exception as e:
        print(f"Error extracting data: {e}")
    # Check if data list is not empty before writing to CSV
    return data


def save_data_to_csv(data):
    if data:
        # Generate filename with the current date
        current_date = datetime.now().strftime("%Y%m%d")
        output_file = f"leparking_part1_output_data_{current_date}.csv"
        
        with open(output_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            if file.tell() == 0:  # Write header only if the file is empty
                writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {output_file}")
    else:
        print("No data to write to file.")

def navigate_to_next_page(driver):
    # List of CSS selectors that could potentially be the 'Next' button.
    possible_selectors = [
        "#paginations_top > li:nth-child(3)",
        "#paginations_top > li:nth-child(4)",
        "#paginations_top > li:nth-child(5)",
        "#paginations_top > li:nth-child(6)",
        "#paginations_top > li:nth-child(7)",
        "#paginations_top > li:nth-child(8)",
        "#paginations_top > li:nth-child(9)"
    ]

    for selector in possible_selectors:
        try:
            # Try to find the element with the current selector
            element = driver.find_element(By.CSS_SELECTOR, selector)
            # Check if the text of the element is 'Suivant'
            if "Suivant" in element.text:
                element.click()
                time.sleep(3)  # Wait for the page to load after clicking
                return True
        except NoSuchElementException:
            # If the element doesn't exist with the current selector, continue to the next
            continue
        except WebDriverException as e:
            print(f"Error navigating to next page with {selector}: {e}")
            return False

    print("No 'Suivant' button found.")
    return False



def main():
    print("Running main")
    url_list_file = "D:\\Oct_leparking\\scripts\\URL_park_long_part1.xlsx"
    fallback_url_list_file = "D:\\Oct_leparking\\URL_park_long_part1.xlsx"  # Path to fallback URL list
    suffix = "part1"
    recent_file = find_recent_files(suffix)

    start_row = None  # Initialize start_row
    url_list_df = pd.read_excel(url_list_file, sheet_name="Audi")

    if recent_file:
        print("Found recent URL file:", recent_file)
        last_url = extract_last_valid_url(recent_file)
        if last_url:
            print("Found last valid URL:", last_url)
            start_row = find_url_row_in_list(last_url, url_list_file)
        else:
            print("No valid URLs found in the recent file.")
    
    if start_row is not None:
        print(f"Restarting from row: {start_row}")
        url_list = url_list_df['lot_url'].iloc[start_row-1:].tolist()
    else:
        print("No recent files matched or valid starting point not found. Defaulting to predefined URL list.")
        # Load the fallback URL list from the beginning
        fallback_df = pd.read_excel(fallback_url_list_file, sheet_name="Audi")
        url_list = fallback_df['lot_url'].iloc[1:6900].tolist()  # Specify the rows you need

    driver = setup_driver()
    output_file = f"leparking_part1_output_data_{datetime.now().strftime('%Y%m%d')}.csv"  # One file per day

    for url in url_list:
        if not isinstance(url, str) or not url.strip():
            print(f"Invalid URL skipped: {url}")
            continue

        print(f"Attempting to access URL: {url}")
        try:
            driver.get(url)
        except (InvalidArgumentException, WebDriverException) as e:
            print(f"Error accessing URL {url}: {e}. Skipping to next URL.")
            continue

        # Try to handle the cookie pop-up
        css_cookie_selector = '#sd-cmp.sd-cmp-1EpGs.sd-cmp-ziEj0 div.sd-cmp-2jVB1 div.sd-cmp-2QK_B.sd-cmp-32o6S.sd-cmp-O521Y div.sd-cmp-1ZnvE div.sd-cmp-kOZlP div.sd-cmp-3Mcwk div.sd-cmp-NBjy7 div.sd-cmp-2yAVI div.sd-cmp-inD2m button.sd-cmp-1bquj span.sd-cmp-1jLDJ.sd-cmp-fuQAp.sd-cmp-W8q3F'
        try:
            element_cookie = driver.find_element(By.CSS_SELECTOR, css_cookie_selector)
            element_cookie.click()
        except NoSuchElementException:
            print("Cookie pop-up not found")

        data = extract_data(driver, url)
        save_data_to_csv(data)

        while navigate_to_next_page(driver):
            additional_data = extract_data(driver, driver.current_url)
            save_data_to_csv(additional_data)

    driver.quit()
    print("Scraping complete. Data saved to", output_file)


if __name__ == "__main__":
    main()





