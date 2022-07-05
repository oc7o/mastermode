import discord

from .model import VCSession
from mastermode.settings import VC_CREATE_CHANNEL

sessions = {}


class VCManagerController:
    def __init__(self):
        pass

    async def fetch_sessions(self):
        return sessions

    async def start_session(self, guild, creator):
        text_channel_name = (creator.name + "s-session").lower()
        voice_channel_name = creator.name + " Session"
        category = self.get_category_by_name(guild, VC_CREATE_CHANNEL)
        voice_channel = await guild.create_voice_channel(
            voice_channel_name, category=category
        )
        text_channel = await guild.create_text_channel(
            text_channel_name, category=category
        )
        await text_channel.set_permissions(
            guild.default_role, view_channel=False, send_messages=False
        )
        await text_channel.set_permissions(
            creator, view_channel=True, send_messages=True
        )

        vs = VCSession(voice_channel, text_channel, creator)
        sessions[str(voice_channel.id)] = vs
        return voice_channel

    async def update_session_permissions(self, channel, user):
        vs = sessions[str(channel.id)]
        text_channel = vs.textchannel
        await text_channel.set_permissions(user, view_channel=True, send_messages=True)

    async def downdate_session_permissions(self, channel, user):
        vs = sessions[str(channel.id)]
        text_channel = vs.textchannel
        await text_channel.set_permissions(
            user, view_channel=False, send_messages=False
        )

    async def edit_session(self):
        pass

    async def delete_session(self, channel):
        vs = sessions[str(channel.id)]
        voice_channel = vs.voicechannel
        text_channel = vs.textchannel
        await voice_channel.delete()
        await text_channel.delete()
        sessions.pop(str(channel.id))

    def get_category_by_name(self, guild, category_name):
        category = None
        for c in guild.categories:
            if c.name == category_name:
                category = c
                break
        return category

    def get_channel_by_name(self, guild, channel_name):
        channel = None
        for c in guild.channels:
            if c.name == channel_name.lower():
                channel = c
                break
        return channel
