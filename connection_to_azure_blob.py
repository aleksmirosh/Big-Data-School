import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

print(os.getcwd())

try:
  #  print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
   # print('TRUE 1')

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  #  print('TRUE 2')

    # Create a unique name for the container
    container_name = "miroshnychenko"
  #  print('TRUE 3')

    # Create the container
   # print('TRUE 3.2')
    container_client = blob_service_client.create_container(container_name)
  #  print('TRUE 4')
except Exception as ex:
    print('Exception:')
    print(ex)

    
#print('TRUE 5')
#new_container = blob_service_client.create_container("containerfromblobservice")
#properties = new_container.get_container_properties()
#print('TRUE 6')

# Create a file in local data directory to upload and download
local_path = "./blob-quickstart-v12/data"
local_file_name = "IndianFoodDatasetCSV.csv"
upload_file_path = os.path.join(local_path, local_file_name)
print('FILE EXIST')

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)

