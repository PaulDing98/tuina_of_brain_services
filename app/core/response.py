from app.schemas.common import ApiResponse
def success_response(data=None, message=None, code="OK", details=None):
    return ApiResponse(
        data=data,
        message=message,
        code=code,
        details=details
    )