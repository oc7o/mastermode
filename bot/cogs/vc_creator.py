import discord
from discord.ext import commands

# from utils import create_voice_channel, get_category_by_name

from vcmanager.controller import VCManagerController


class VCCreator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.bot:
            return

        vm = VCManagerController()
        if after.channel is not None:
            channel_name = member.name + " Session"
            if after.channel.name == "Sprachkanal erstellen" and channel_name not in [
                channel.name
                for channel in vm.get_category_by_name(
                    after.channel.guild, "Speech-Beach🔊🏖"  # in env
                ).channels
            ]:
                channel = await vm.start_session(after.channel.guild, member)
                if channel is not None:
                    await member.move_to(channel)
            elif after.channel.name == "Sprachkanal erstellen" and channel_name in [
                channel.name
                for channel in vm.get_category_by_name(
                    after.channel.guild, "Speech-Beach🔊🏖"
                ).channels
            ]:
                creator = False
                channel = None
                sessions = await vm.fetch_sessions()
                for s in sessions:
                    if s.creator == member.id:
                        creator = True
                        break
                if creator is True:
                    channel = await vm.start_session(after.channel.guild, member)
                    await member.move_to(channel)
                else:
                    await member.move_to(
                        vm.get_channel_by_name(after.channel.guild, channel_name)
                    )

            elif after.channel.id in [
                c.voicechannel for c in await vm.fetch_sessions()
            ]:
                await vm.update_session_permissions(after.channel, member)

        if before.channel is not None:
            if (
                before.channel.category.id
                == vm.get_category_by_name(before.channel.guild, "Speech-Beach🔊🏖").id
                and before.channel.name != "Sprachkanal erstellen"
            ):
                if len(before.channel.members) == 0:
                    await vm.delete_session(before.channel)
            elif before.channel.id in [
                c.voicechannel for c in await vm.fetch_sessions()
            ]:
                await vm.downdate_session_permissions(before.channel, member)


def setup(bot):
    bot.add_cog(VCCreator(bot))
