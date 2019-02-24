from aiohttp import web
from core.translator import get_translator


async def translation_handler(request: web.BaseRequest) -> web.Response:
    """ 
    Handle GET translation request

    Find translator according to passed `translation_type` parameter.
    And return translated text as json response.

    """
    translation_type = request["translation_type"]
    dialect = request["dialect"]

    translator = get_translator(translation_type, dialect)
    translated_text = await translator.translate(request.query["text"])

    response = {"translated_text": translated_text}
    return web.json_response(response)
