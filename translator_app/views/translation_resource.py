from aiohttp import web
from core.translator import get_translator


async def translation_handler(request: web.BaseRequest) -> web.Response:
    """ 
    Handle GET translation request

    Find translator according to passed `translation_type` parameter.
    And return translated text as json response.

    """
    translator = get_translator(request["translation_type"])
    translated_text = await translator.translate(text_to_translate=request.query["text"])
    response = {"translated_text": translated_text}
    return web.json_response(response)
