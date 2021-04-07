import random
import discord
import typing

from redbot.core import checks, commands


class Pick(commands.Cog):
    """Picks a random user.
    **Output is a ping/mention.**."""

    __author__ = "saurichable"
    __version__ = "1.2.0"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @checks.mod_or_permissions(manage_roles=True)
    async def pickuser(self, ctx: commands.Context):
        """Pick a random user. It will ping them."""
        winner = random.choice(ctx.guild.members)
        await ctx.send(f"<@{winner.id}>")
