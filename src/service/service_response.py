class ServiceResponse:

    def __init__(self, success: bool, message: str, data = None, error = None):
        self.success = success
        self.message = message
        self.data = data
        self.error = error

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "error": self.error
        }