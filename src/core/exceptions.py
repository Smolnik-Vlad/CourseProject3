class CustomBaseException(Exception):
    def __init__(self, detail="Custom Error"):
        self.status_code = 500  # Internal Server Error


class CustomException(CustomBaseException):
    def __init__(self, detail="Custom Error"):
        self.status_code = 400


class InfrastructureException(CustomBaseException):
    pass
