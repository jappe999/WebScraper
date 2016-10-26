import requests, json

IP = "http://127.0.0.1:420"

def main(ip):
    localQueue = []
    foundedURLs = ['google.com', 'google.de', 'google.nl', 'google.be', 'dmoz.com']
    #while True:
    getUrlData(foundedURLs, ip)
     #   getUrlData(foundedURLs, ip)
    

def getUrlData(data, ip):
    data = json.dumps(data)
    doc = requests.post(ip, data)
    print(doc.json())
    return doc.json()

if __name__ == "__main__":
    main(IP)

main(IP)
