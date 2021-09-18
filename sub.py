"""RT Backend (C) 2020 RT-Team
LICENSE : ./LICENSE
README  : ./readme.md
"""

desc = r"""
������ - (C) 2020 RT-Team
�����N����..."""
print(desc)

from discord.ext import commands
import discord

from asyncio import sleep
from os import listdir
from sys import argv
import ujson
import rtlib

from data import data, is_admin


# �ݒ�t�@�C���̓ǂݍ��݁B
with open("token.secret", "r", encoding="utf-8_sig") as f:
    secret = ujson.load(f)
TOKEN = secret["token"][argv[1]]


# ���̑��ݒ������B
prefixes = data["prefixes"][argv[1]]


# Backend�̃Z�b�g�A�b�v������B
def setup(bot):
    bot.admins = data["admins"]

    bot.session = ClientSession(loop=bot.loop)
    @bot.listen()
    async def on_close(loop):
        await bot.session.close()
        del bot.mysql


    # �G�N�X�e���V������ǂݍ��ށB
    rtlib.setup(bot)
    bot.load_extension("jishaku")

    async def setting_up():
        await sleep(3)
        await bot.change_presence(
            activity=discord.Game(
                name="�����N����..."
            ), status=discord.Status.dnd
        )

    bot._loaded = False

    @bot.event
    async def on_ready():
        # cogs�t�H���_�ɂ���G�N�X�e���V������ǂݍ��ށB
        if not bot._loaded:
            for name in ("cogs.tts", "cogs.music", "cogs._sub"):
                bot.load_extension(name)
            bot.dispatch("full_ready")
            bot._loaded = True

    bot.loop.create_task(setting_up())

# �e�X�g���͕��ʂ�Backend��{�Ԃ̓V���[�h��Backend���`����B
intents = discord.Intents.default()
intents.typing = False
intents.guild_typing = False
intents.dm_typing = False
intents.members = True
args = (prefixes,)
kwargs = {
    "help_command": None,
    "on_init_bot": on_init,
    "intents": intents
}
bot = commands.Bot(command_prefix=data[])
bot.test = False


server = (eval(argv[2]) if len(argv) > 2 else True)


bot.data = data
bot.colors = data["colors"]
bot.is_admin = is_admin


# jishaku�̊Ǘ��҂��ǂ����m�F���邽�߂̃R���[�`���֐���p�ӂ���B
async def _is_owner(user):
    return bot.is_admin(user.id)
bot.is_owner = _is_owner
del is_admin, _is_owner


bot.run(TOKEN)
