import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TusharMusic import LOGGER, app, userbot
from TusharMusic.core.call import TUSHAR
from TusharMusic.misc import sudo
from TusharMusic.plugins import ALL_MODULES
from TusharMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("TusharMusic.plugins" + all_module)
    LOGGER("TusharMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await TUSHAR.start()
    try:
        await TUSHAR.stream_call("https://envs.sh/7aQ.mp4")
    except NoActiveGroupCall:
        LOGGER("TusharMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await TUSHAR.decorators()
    LOGGER("TusharMusic").info(
        "mhs music started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("TusharMusic").info("Stopping TUSHAR Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
