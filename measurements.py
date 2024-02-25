# Let's measure how long data is cached at the gateway

"""

Strategy : 

1) create a new file, upload it on the network
2) request it from gateway until it is succesfully retrieved
3) wait for an increasingly long amount of time until request is not succesful anymore

"""

from host import upload_file_to_ipfs, get_cid_from_daemon_response
import requests
import time
import os

api_url = 'http://127.0.0.1:5001/api/v0/add'
gateway_url = "https://ipfs.io/ipfs/"
time_precision = 60 # in seconds

def create_file(file_name, file_size):
    """
    Create a file 

    Args:
    - file_name (str) : name of the file to create
    - file_size (int) : size of the file to create

    Returns:
    None
    """
    # We will create a files_generated directory to stores generated files
    # The directory is in the .gitignore to avoid pushing unnecessary stuff to github

    os.system("mkdir -p files_generated")

    with open("./files_generated/"+file_name, 'w') as f:
        f.write("0"*file_size)

def request_from_gateway(gateway_url, CID):
    """
    Request content from IPFS gateway through content's CID

    Args:
    - gateway_url (str) : url of the gateway 
    - CID (str) : CID of the content to request

    Returns : 
    - dict : response from IPFS gateway
    """
    URL = gateway_url+CID
    response = requests.get(URL)
    return response

def upload_and_make_available_at_gateway(file_name, file_size, gateway_url, api_url):
    """
    Create a file of given name and size, upload it to IPFS network, request it from IPFS gateway until it is available

    Args: 
    - file_name (str) : name of the file to create
    - file_size (int) : size of the file to create
    - gateway_url (str) : url of the IPFS gateway
    - api_url (str ) : url of IPFS daemon

    Returns : 
    - str : CID of file uploaded
    """
    create_file(file_name,file_size)
    server_response = upload_file_to_ipfs("./files_generated/"+file_name,api_url)
    CID = get_cid_from_daemon_response(server_response)
    response_code = request_from_gateway(gateway_url, CID).status_code
    while response_code!=200:
        print('File unavailable at gateway - trying again in 1 min ... ')
        time.sleep(60)
        response = request_from_gateway(gateway_url, CID)
        response_code = response.status_code
    
    print(f"File available at gateway, CID : {CID}")

    return CID

def main():

    file_name = "test.txt"
    file_size = 1024

    # Upload and make available at gateway 
    CID = upload_and_make_available_at_gateway(file_name, file_size, gateway_url, api_url)

    response_code = 0
    k=0
    while response_code != 504:
        k+=1
        time.sleep(time_precision*k)
        response_code = request_from_gateway(gateway_url, CID).status_code
        print("File still available at gateway ...")
    
    with open("results.txt","w") as f:
        f.write(f"File no longer available at gateway after {k*time_precision} seconds ")

main()

    

    