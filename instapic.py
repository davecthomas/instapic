import argparse
import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os


def extract_image_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    img_tag = soup.find('img')
    if img_tag and 'src' in img_tag.attrs:
        return img_tag['src']
    return None


def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded as {filename}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract image URL from HTML img tag.")
    parser.add_argument('input', type=str,
                        help="HTML img tag as a string")
    args = parser.parse_args()

    input_data = args.input

    # Assume it's an HTML img tag
    img_url = extract_image_url(input_data)
    if img_url:
        print(f"Image URL: {img_url}")
        webbrowser.open(img_url)

        # Determine the file extension
        file_extension = img_url.split('?')[0].split('.')[-1]
        if file_extension not in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp']:
            file_extension = 'jpg'  # default to jpg if the extension is not recognized

        # Create the filename
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"instapic-{date_str}.{file_extension}"

        # Get the current user's Downloads directory
        downloads_folder = os.path.join(
            os.path.expanduser('~'), 'Downloads')
        filepath = os.path.join(downloads_folder, filename)

        # Download the image
        download_image(img_url, filepath)
    else:
        print("No valid image URL found.")


if __name__ == "__main__":
    main()
