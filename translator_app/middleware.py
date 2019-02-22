import logging

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_middlewares import _Handler as Handler

from core.errors import DataApiResponseError, TranslationTypeNotFoundError
from core.translator import TranslatorTypeEnum


@web.middleware
async def validate_translation_middleware(
    request: Request, handler: Handler
) -> web.StreamResponse:
    """
    Valite request params.

    Check:
        - `translation_type` param converts to `TranslatorTypeEnum` object
        - query string pararameter `text` exists in URL

    Example of valid URL:
        http://host:port/translation/eng_to_pig_latin?text=hello
    
    """
    error = {}
    try:
        request["translation_type"] = TranslatorTypeEnum(
            request.match_info.get("translation_type")
        )
    except ValueError as e:
        error["translation_type"] = str(e)

    if request.query.get("text") is None:
        error["text"] = "required query string param is missed"

    if error:
        return web.json_response({"error": error}, status=400)

    response = await handler(request)
    log_message = f'{request["translation_type"]}: {response._body}'
    logging.info(log_message)
    return response


@web.middleware
async def handle_errors_middleware(
    request: Request, handler: Handler
) -> web.StreamResponse:
    """
    Handle unhandled errors

    return `{"error": "error_message"}` if unhandled error happens

    """
    logging.info(request.path)
    try:
        return await handler(request)
    except TranslationTypeNotFoundError as e:
        logging.exception("validation error")
        err_message = f"validation_error. {e}."
        return web.json_response({"error": err_message}, status=e.code)
    except Exception as e:
        logging.exception("Unhandled error")
        err_message = "Unhandled_error. Please, check logs."
        return web.json_response({"error": err_message}, status=500)

