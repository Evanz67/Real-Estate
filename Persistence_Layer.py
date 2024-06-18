import json

class AccountBroker:

    textFile = "user.json"

    def serializeAccount(self, userData):
        jsonObj = json.dumps(userData, indent=4)

        with open(self.textFile, "w") as dataStorage:
            dataStorage.write(jsonObj)
    
    def deserializeAccount(self):
        with open(self.textFile, "r") as openFile:

            jsonObj = json.load(openFile)
        
        return jsonObj
    
class ApartmentBroker:

    textFile = "apartment.json"
    
    def deserializeApartmentData(self):
        with open(self.textFile, "r") as openFile:

            jsonObj = json.load(openFile)
        
        return jsonObj