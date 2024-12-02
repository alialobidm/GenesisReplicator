import uuid

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
        # Validate inputs and session
        if not agentId or not isinstance(agentId, str):
            raise ValueError("Invalid agent ID")
        if not action or not isinstance(action, str):
            raise ValueError("Invalid action")
        if not self.session:
            raise PermissionError("No active session")

        # Define valid operations similar to admin interface
        valid_actions = {
            "query": "Query agent status and data",
            "compute": "Request computation task",
            "transfer": "Transfer data or assets",
            "deploy": "Deploy new configuration",
            "update": "Update agent settings"
        }

        if action not in valid_actions:
            raise ValueError(f"Invalid action. Valid actions are: {', '.join(valid_actions.keys())}")

        # Prepare request with enhanced metadata
        request = {
            "agent_id": agentId,
            "action": action,
            "data": data,
            "session": self.session,
            "timestamp": "2024-01-01T00:00:00Z",
            "request_id": str(uuid.uuid4()),  # Generate unique request ID
            "client_info": {
                "version": "1.0.0",
                "platform": "standard"
            }
        }

        # Simulate agent interaction with detailed response
        response = {
            "status": "success",
            "request_id": request["request_id"],
            "agent_id": agentId,
            "action_result": f"Executed {action} successfully",
            "data": {
                "processed": True,
                "result": "Operation completed",
                "metadata": {
                    "agent_status": "active",
                    "execution_time": "100ms",
                    "resource_usage": {
                        "cpu": "10%",
                        "memory": "150MB"
                    },
                    "blockchain_status": {
                        "block_height": 1234567,
                        "synchronized": True
                    }
                }
            },
            "audit": {
                "timestamp": "2024-01-01T00:00:00Z",
                "user_id": self.session["user"],
                "action": action,
                "status": "completed"
            }
        }

        return response