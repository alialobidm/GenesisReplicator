class ClientSDK:
    def __init__(self) -> None:
        self.session = None

    def authenticate(self, credentials):
        if self.isUserCredentailValid(credentials):
            self.session = {"user": "uid"}
            return True
        return False
    
    def isUserCredentailValid(self, credentials):
        # simulate auth 
        return credentials.get("token") == "valid token"
    
    def interactWithAgent(self, agentId, action, data):
        if not self.session:
            raise PermissionError("User not authenticated")
        return self.callAgent(agentId, action, data)
        
    def callAgent(self, agentId, action, data):
        print('call agent with agentId, action and data')