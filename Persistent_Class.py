import json

class AccountBroker:

    def serializeAccount(self, userData):
        jsonObj = json.dumps(userData, indent=4)

        with open("user.json", "w") as dataStorage:
            dataStorage.write(jsonObj)
    
    def deserializeAccount(self):
        with open("user.json", "r") as openFile:

            jsonObj = json.load(openFile)
        
        return jsonObj
    
class ApartmentBroker:
    
    def deserializeAccount(self):
        with open("apartment.json", "r") as openFile:

            jsonObj = json.load(openFile)
        
        return jsonObj