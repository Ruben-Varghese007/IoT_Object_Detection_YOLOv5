import requests
from bs4 import BeautifulSoup
import os
import json

# Function to download images from Google Images
def download_images(search_term, num_images):
    # Create folder to store images
    folder_name = search_term.replace(" ", "_")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Prepare the URL for Google Images search
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_term}"
    
    # User agent to avoid blocking
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    count = 0
    for img_tag in img_tags:
        if count >= num_images:
            break
        try:
            img_url = img_tag['src']
            # Download the image
            img_data = requests.get(img_url).content
            with open(f"{folder_name}/{search_term}_{count}.jpg", 'wb') as handler:
                handler.write(img_data)
            count += 1
            print(f"Downloaded {search_term}_{count}.jpg")
        except Exception as e:
            print(f"Could not download image {count}: {e}")

    print(f"Downloaded {count} high-quality images of {search_term}.")

# Usage
download_images('arduino iot microcontroller', 50)  # Downloads 50 images of Arduino
download_images('iot servo motor', 50)   # Downloads 50 images of sensors
download_images('iot wires', 50)     # Downloads 50 images of wires
