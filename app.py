import json
from extract.crypto_api import fetch_crypto_data
from load.load_db import insert_crypto

def main(): 
    data = fetch_crypto_data()
    print(json.dumps(data,indent=4))
    
    insert_crypto(data)
    print("Data inserted Successfully!")

if __name__ == "__main__":
    main()