import logging

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_middlewares import _Handler as Handler

from core.errors import BaseTranslationError
from validators.translation_validator import validate_translation_request


@web.middleware
async def validation_middleware(request: Request, handler: Handler) -> web.StreamResponse:
    """
    Validate request for each endpoint

    return `{"error": "error_message"}` if unhandled error happens

    """
    if request.app.router.get("translation"):
        errors = validate_translation_request(request)
        if errors:
            return web.json_response({"error": errors}, status=400)

    return await handler(request)


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
    except BaseTranslationError as e:
        logging.exception("validation error")
        # err_message = f"validation_error. {e}."
        return web.json_response({"error": e.error_text}, status=e.code)
    except Exception as e:
        logging.exception("Unhandled error")
        err_message = "Unhandled_error. Please, check logs."
        return web.json_response({"error": err_message}, status=500)

