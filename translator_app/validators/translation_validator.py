from typing import Dict

from aiohttp.web_request import Request

from core.translator import TranslatorTypeEnum


def validate_translation_request(request: Request) -> Dict:
    """
    Valite request params.

    Check:
        - `translation_type` param converts to `TranslatorTypeEnum` object
        - query string pararameter `text` exists in URL

    Example of valid URL:
        http://host:port/translation/eng_to_pig_latin?text=hello
    
    """
    errors = {}
    try:
        request["translation_type"] = TranslatorTypeEnum(
            request.match_info.get("translation_type")
        )
    except ValueError as e:
        errors["translation_type"] = str(e)

    if request.query.get("dialect"):
        request["dialect"] = request.query["dialect"]
    else:
        errors["dialect"] = "required query string param is missed"

    if request.query.get("text") is None:
        errors["text"] = "required query string param is missed"

    return errors
