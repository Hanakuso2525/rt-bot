# RT Chan - Info

from discord import commands
import discord


class Info(commands.Cog):

    INVITE_URL = "https://discord.com/api/oauth2/authorize?client_id=888635684552863774&permissions=172339022401&scope=bot%20applications.commands"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(slash_command=True, aliases=["info", "about"])
    async def invite(self, ctx):
        await ctx.reply(
            embed=discord.Embed(
                title="������",
                description="""[Discord�̑��@�\Bot�ł���RT](https://rt-bot.com/)�̉��y�Đ��Ɠǂݏグ�����g����悤�ɂ����T�uBot�̂����I
���@�\Bot��RT�͉��y�Đ���ǂݏグ�̑��ɂ��T�[�o�[�X�e�[�^�X�₢�����ɗ��郁�b�Z�[�W�ȂǗl�X�ȋ@�\�������I
��������������Ȃ�[����](https://rt-bot.com)�ɂ��ď��҂�����T�|�[�g�T�[�o�[�ɍs���Ă݂悤�I
���͂���RT�ɂ��鉹�y�Đ��Ɠǂݏグ�𓯎��Ɏg�p�������Ƃ����l�̂��߂ɐ��܂ꂽ��B
�����T�[�o�[�ɏ��҂������l��[����](self.INVITE_URL)���N���b�N�I"""
            )
        )

    @commands.command(slash_command=True, aliases=["h"])
    async def help(self, ctx):
        await ctx.reply(
            "���y�Đ��̃w���v�Fhttps://rt-bot.com/help.html?g=music\n�ǂݏグ�̃w���v�Fhttps://rt-bot.com/help.html?g=entertainment&c=tts\n����Bot�ɂ���/���҃����N�F`rt#info`"
        )
