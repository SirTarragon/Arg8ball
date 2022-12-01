import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(hidden=True, with_app_command=False)
    @commands.is_owner()
    async def sync(self, ctx):
        """
        Globally syncs all bot commands with Discord. Should be run after adding or removing commands.
        Args:
            ctx (discord.ext.Context): The message Context.
        """
        response = await ctx.bot.tree.sync() # if wanting to sync with a specific guild, include guild=ctx.guild
        return await ctx.send(f"Synced {len(response)} commands to Discord.")
      
async def setup(bot):
    await bot.add_cog(Owner(bot))
