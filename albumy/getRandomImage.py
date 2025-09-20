import os
import random
import requests

# --- CONFIG ---
BASE_URL = "https://yavuzceliker.github.io/sample-images/image-{}.jpg" ## available open source from GitHub. Thanks to github.com/yavuzceliker.
NUM_IMAGES = 40
MAX_INDEX = 2000
SAVE_DIR = "./uploads/"

def download_file(url, save_path):
    """Download a single file."""
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)

def main():
    # pick 40 unique random numbers between 1 and MAX_INDEX
    random_indices = random.sample(range(1, MAX_INDEX + 1), NUM_IMAGES)

    for idx, n in enumerate(random_indices, start=1):
        url = BASE_URL.format(n)
        save_name = f"random_{idx}.jpg"
        save_path = os.path.join(SAVE_DIR, save_name)

        print(f"Downloading {url} -> {save_name}")
        try:
            download_file(url, save_path)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

if __name__ == "__main__":
    main()
