import asyncio
from aiohttp import web

from translator import config


async def tran(parameter_list):
    pass


async def handle(request):
    name = request.match_info.get("name", "Anonymous")

    text = f"hi, {name}"
    return web.Response(text=text)


def run_app():
    app = web.Application()
    app.add_routes([web.get("/", handle), web.get("/{name}", handle)])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(web.run_app(app, path="test", port=config.SERVER_PORT))


if __name__ == "__main__":
    print("run app")
    asyncio.run(run_app())

