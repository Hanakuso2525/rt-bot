# RT.cogs.music - Util

import discord


def check_dj(member: discord.Member) -> bool:
    # �n���ꂽ�����o�[���ꍇ�ɂ���Ă�DJ���K�v�ȃR�}���h�̂��߂�DJ�`�F�b�N������֐��ł��B
    return (
        len([m for m in member.voice.channel.members if not m.bot]) == 1
        or discord.utils.get(member.roles, name="DJ")
    )
