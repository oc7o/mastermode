# like this: rolegive <role>

import discord
from discord.ext import commands

from rolemanager.controller import RoleManagerController


class Rolemanager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.check(
        commands.is_owner()
    )  # check_any() is available too e.g. for commands.has_role("")
    async def rolegive(self, ctx, role):
        roles = [r.name for r in ctx.guild.roles]
        if role in roles:
            role_obj = discord.utils.get(ctx.guild.roles, name=role)
            embed = discord.Embed(
                title="Get Role",
                description="When commenting this message with :white_check_mark: you get the role "
                + role_obj.mention,
            )
            message = await ctx.send(embed=embed)
            rm = RoleManagerController()
            rm.add_message(message.id, role_obj.id)
        else:
            await ctx.send(f"Role {role} does not exist.")
            return

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        rm = RoleManagerController()
        messages = rm.fetch_messages()
        if reaction.message.id in messages.keys():
            if reaction.emoji == "✅":
                role_id = messages[reaction.message.id].role_id
                role_obj = discord.utils.get(user.guild.roles, id=role_id)
                await user.add_roles(role_obj)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        rm = RoleManagerController()
        messages = rm.fetch_messages()
        if reaction.message.id in messages.keys():
            if reaction.emoji == "✅":
                role_id = messages[reaction.message.id].role_id
                role_obj = discord.utils.get(user.guild.roles, id=role_id)
                await user.remove_roles(role_obj)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        rm = RoleManagerController()
        messages = rm.fetch_messages()
        if message.id in messages.keys():
            rm.remove_message(message.id)


def setup(bot):
    bot.add_cog(Rolemanager(bot))
