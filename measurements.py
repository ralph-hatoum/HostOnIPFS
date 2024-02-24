# Let's measure how long data is cached at the gateway

"""

Strategy : 

1) create a new file, upload it on the network
2) request it from gateway until it is succesfully retrieved
3) wait for an increasingly long amount of time until request is not succesful anymore

"""

from host import upload_file_to_ipfs

api_url = 'http://127.0.0.1:5001/api/v0/add'

def create_file(file_name, file_size):
    with open(file_name, 'w') as f:
        f.write("0"*file_size)



    