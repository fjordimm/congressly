import requests


congUrl: str = 'https://api.congress.gov/v3/'
congKey: str = 'ggK1rckfYBoQkmpvOZ4DZrdyj1uAIS7OAxDSbEyB'



def get_bills(numberOfBills):

    bills = {}


    response = requests.get(url=congUrl + "bill", params={"api_key": congKey, "limit": numberOfBills})
    jsonData = response.json()

    for bill in jsonData['bills']:
        bills[bill['number']] = {'congressNumber': bill['congress'], 
                                 'originChamber': bill['originChamber'],
                                 'title': bill['title'],
                                 'type': bill['type'],
                                 'number': bill['number']
                                 }
        
    numberOfBills -= 250
    offset = 250
        
    while numberOfBills > 0:
        response = requests.get(url=congUrl + "bill", params={"api_key": congKey, "limit": numberOfBills, "offset": offset})
        jsonData = response.json()

        for bill in jsonData['bills']:
            bills[bill['number']] = {'congressNumber': bill['congress'], 
                                    'originChamber': bill['originChamber'],
                                    'title': bill['title'],
                                    'type': bill['type'],
                                    'number': bill['number']
                                    }
            
        numberOfBills -= 250
        offset += 250

    # print(bills)
    return bills

def get_full_text(bills):
    for billNumber in bills:
        bill = bills[billNumber]
        fullUrl = congUrl + f"bill/{bill['congressNumber']}/{bill['type']}/{billNumber}/text"
        # print(fullUrl)
        response = requests.get(url=fullUrl, params={"api_key": congKey})
        jsonData = response.json()
        if 'error' not in jsonData:
            print(jsonData)


# billInfo = get_bills(501)
# print(billInfo.keys())