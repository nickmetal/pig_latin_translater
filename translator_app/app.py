import asyncio
from aiohttp import web

import config
from views import translation_handler
from middleware import validation_middleware, handle_errors_middleware


def init_router(app: web.Application):
    """apply routers to application"""
    app.router.add_get(
        "/translation/{translation_type}", translation_handler, name="translation"
    )


def run_app():
    middlewares = [handle_errors_middleware, validation_middleware]

    app = web.Application(middlewares=middlewares)
    init_router(app)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(web.run_app(app, port=config.SERVER_PORT))


if __name__ == "__main__":
    run_app()
