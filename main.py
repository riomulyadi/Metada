import json

dicts = {
  "file_path": "C:/Users/riomu/OneDrive/Documents/1.png", #Path folder NFT nya, nama file harus 1.png - XX.png
  "nft_name": "#1", #Nama NFT-nya
  "external_link": "",
  "description": "Collection", #Deskripsi
  "collection": "Collections", #Nama Collection
  "properties": [
    
  ],
  "levels": [
    
  ],
  "stats": [
    
  ],
  "unlockable_content": [
    
  ],
  "explicit_and_sensitive_content": "",
  "supply": 1,
  "blockchain": "Polygon",
  "price": 0.005, #Harga NFT nya
  "quantity": 1 
}

for x in range(6000):
    dicts["file_path"] = "C:/Users/riomu/OneDrive/Documents/NFT/gen/outputs/HelloWorld/"+str(x)+".png"
    dicts["nft_name"] = "#"+str(x)
    with open('result.json','a')as outfile:
        json.dump(dicts, outfile)


