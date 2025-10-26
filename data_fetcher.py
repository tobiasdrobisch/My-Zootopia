import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """
    Fetch animal data from the API Ninjas Animal API.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of animal dictionaries, each containing:
            {
                'name': str,
                'taxonomy': dict,
                'locations': list,
                'characteristics': dict
            }
        Returns an empty list if the request fails or no data is found.
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(api_url, headers=headers)
    except requests.RequestException as error:
        print("Error while fetching data:", error)
        return []

    if response.status_code == requests.codes.ok:
        return response.json()

    print("Error:", response.status_code, response.text)
    return []
