class APIGateway:
    def __init__(self):
        self.routes = {}

    def register_route(self, route, handler):
        self.routes[route] = handler

    def handle_request(self, route, request_data):
        if route not in self.routes:
            return {"error": "Route not found"}
        return self.routes[route](request_data)