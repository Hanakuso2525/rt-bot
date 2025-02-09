# RT.cogs.music.cogs - SoundCloud ... SouncCloudの音楽のAudioSourceなどを取得するためのモジュールです。

from copy import copy
import discord
import asyncio

from .youtube import (
    FLAT_OPTIONS, _make_get_source, _get,
    MusicData, MusicRawData, UploaderData
)


COPIED_FOPTIONS = copy(FLAT_OPTIONS)
del COPIED_FOPTIONS["cookiefile"]
SC_OPTIONS = copy(COPIED_FOPTIONS)
SC_OPTIONS["noplaylist"] = True


def _make_music_raw_data(
    loop: asyncio.AbstractEventLoop, data: dict, url: str
) -> MusicRawData:
    return MusicRawData(
        url=url, title=data["title"], thumbnail=data["thumbnail"],
        duration=data["duration"], uploader=UploaderData(
            name=data["uploader"], url=data["uploader_url"]
        ), get_source=_make_get_source(loop, data["url"], SC_OPTIONS)
    )


async def get_music(
    url: str, author: discord.Member,
    loop: asyncio.AbstractEventLoop
) -> MusicData:
    return MusicData(
        _make_music_raw_data(
            loop, await _get(loop, url, COPIED_FOPTIONS), url
        ), author
    )
