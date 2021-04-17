import random
import discord
import typing

from redbot.core import checks, commands


class Pick(commands.Cog):
    """Picks a random user.
    **Output is a ping/mention.**."""

    __version__ = "1.2.0"

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, *, requester, user_id):
        # nothing to delete
        return

    def format_help_for_context(self, ctx: commands.Context) -> str:
        context = super().format_help_for_context(ctx)
        return f"{context}\n\nVersion: {self.__version__}"

    @commands.command()
    @commands.guild_only()
    @checks.mod_or_permissions(manage_roles=True)
    async def pickuser(self, ctx: commands.Context):
        """Pick a random user. It will ping them."""
        winner = random.choice(ctx.guild.members)
        await ctx.send(f"<@{winner.id}>")
