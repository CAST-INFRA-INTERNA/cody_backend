"""
Response adapter: converts JSONResponse objects to dictionary format
Allows existing service-layer code to be compatible with Pydantic response models
"""
from typing import Any
from schemas.base import Success, Fail, SuccessExtra


def adapt_response(response: Success | Fail | SuccessExtra) -> dict[str, Any]:
    """
    Convert a JSONResponse object to dictionary format
    This function acts as a compatibility layer during the transition period,
    allowing existing service-layer code to work with the new Pydantic response models
    
    Args:
        response: A Success, Fail, or SuccessExtra instance
        
    Returns:
        A dictionary containing the response data
    """
    if hasattr(response, 'body'):
        # JSONResponse object: parse content from body
        import json
        return json.loads(response.body)
    else:
        # Return dictionary content directly
        return {
            "code": getattr(response, 'code', 200),
            "msg": getattr(response, 'msg', 'OK'),
            "data": getattr(response, 'data', None),
            "total": getattr(response, 'total', None),
            "page": getattr(response, 'page', None),
            "page_size": getattr(response, 'page_size', None),
        }