from moduleImport import importPackage

importPackage()

import requests

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
        response = upload_images_to_ipfs(image, api_url)
        if response != None:
            CIDs[image]=get_cid_from_daemon_response(response)

    return CIDs
    