class Response:
    """Response class"""
    def ResponseModel(data, code , message):
        return {
            "data": [data],
            "code": code,
            "message": message,
        }


    def ErrorResponseModel(error, code, message):
        return {"error": error, "code": code, "message": message}