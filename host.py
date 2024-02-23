from moduleImport import importPackage

importPackage()

import requests
import os

# IPFS API endpoint
api_url = 'http://127.0.0.1:5001/api/v0/add'


def upload_file_to_ipfs(file_path, api_url):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(api_url, files=files)
    if response.status_code == 200:

        return response.json()
    else:
        print('Error:', response.text)
        return None
    
def get_cid_from_daemon_response(response):
    return response['Hash']

def upload_images_to_ipfs(images_paths, api_url):
    CIDs = {}
    for image in images_paths:
        response = upload_file_to_ipfs(image, api_url)
        if response != None:
            CIDs[image]=get_cid_from_daemon_response(response)

    return CIDs

def get_all_paths(directory):
    """
    Get paths to all elements (files and subdirectories) in the specified directory.
    
    Args:
    - directory (str): The directory to search for elements.
    
    Returns:
    - List[str]: A list of paths to all elements found.
    """
    all_paths = []

    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        all_paths.append(full_path)

    return all_paths

images = get_all_paths("images")

CIDs = upload_images_to_ipfs(images, api_url)

print(CIDs)