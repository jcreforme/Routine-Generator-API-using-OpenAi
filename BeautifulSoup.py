import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def fetch_exercises_with_selenium():
    """
    Fetches exercise data from the FitCron website using Selenium.

    Returns:
        list: A list of dictionaries containing exercise names and descriptions.
    """
    url = "https://fitcron.com/exercises/"
    
    # Initialize the Selenium WebDriver (make sure you have ChromeDriver installed)
    driver = webdriver.Chrome()  # Or use webdriver.Firefox() if you have FirefoxDriver
    driver.get(url)

    # Wait for the page to load (adjust as needed)
    driver.implicitly_wait(10)

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    exercises = []

    # Adjust the selectors based on the website's structure
    for exercise in soup.select(".view-item"):  # Update this selector
        name_element = exercise.select_one(".item-type")  # Update this selector
        description_element = exercise.select_one(".item-name")  # Update this selector
        image_element = exercise.select_one(".item-image img")  # Selector for the image

        if name_element and description_element and image_element:
            name = name_element.text.strip()
            description = description_element.text.strip()
            image_url = image_element["src"].strip()  # Extract the image URL
            exercises.append({
                "name": name,
                "description": description,
                "image_url": image_url
            })
    
    return exercises

def save_exercises_to_file(exercises, filename="exercises.json"):
    """
    Saves the fetched exercises to a JSON file.

    Args:
        exercises (list): List of exercise dictionaries.
        filename (str): The name of the file to save the exercises to.
    """
    with open(filename, "w") as f:
        json.dump(exercises, f, indent=4)

def load_exercises_from_file(filename="exercises.json"):
    """
    Loads exercises from a JSON file.

    Args:
        filename (str): The name of the file to load the exercises from.

    Returns:
        list: A list of exercise dictionaries.
    """
    with open(filename, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    try:
        # Fetch exercises from the website
        print("Fetching exercises...")
        exercises = fetch_exercises_with_selenium()
        print(f"Fetched {len(exercises)} exercises.")

        # Save exercises to a file
        print("Saving exercises to file...")
        save_exercises_to_file(exercises)
        print("Exercises saved to 'exercises.json'.")

        # Load exercises from the file and print them
        print("Loading exercises from file...")
        loaded_exercises = load_exercises_from_file()
        print(f"Loaded {len(loaded_exercises)} exercises.")
        for exercise in loaded_exercises[:5]:  # Print the first 5 exercises
            print(f"- {exercise['name']}: {exercise['description']}")
    except Exception as e:
        print(f"Error: {e}")