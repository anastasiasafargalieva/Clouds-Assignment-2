# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

#installed azure identity: pip install azure-storage-blob azure-identity 

import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

#added environment variable with export AZURE_STORAGE_CONNECTION_STRING="<connection_string>"
#connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
def main(inputtext: str) -> list:
    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=mapreduceanastasia;AccountKey=8i4KRWlTso7CrqDA/1o8PuWeI1vGQs0XHkVF+F6XBVCkaNBMQsgrsrLM24Sltrrc+tvbvjte0ZAj+AStG5vnAA==;EndpointSuffix=core.windows.net")

    #get container
    container_client = blob_service_client.get_container_client(container=inputtext)
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    result = []
    for blob in blob_list:
        #read input texts
        text = container_client.download_blob(blob.name).readall()
        #split into lines
        split_lines = text.splitlines() 
        ordered_lines = []
        k = 0
        for each in split_lines:
            k = k + 1
            ordered_lines.append((k, str(each)))
        result.extend(ordered_lines)
    return result


