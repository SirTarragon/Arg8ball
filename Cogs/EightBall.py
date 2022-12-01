import discord
import random
from discord.ext import commands

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @staticmethod
    def ball_response(self) -> str:
        responses = ["It is certain.", "It is decidedly so.",
                     "Without a doubt. Yes definitely.",
                     "You may rely on it.", "As I see it, yes.",
                     "Most likely.", "Outlook good.", "Yes.",
                     "Signs point to yes.", "Reply hazy, try again.",
                     "Ask again later.", "Better not tell you now.",
                     "Cannot predict now.", "Concentrate and ask again.",
                     "Don't count on it.", "My reply is no.",
                     "My sources say no.", "Outlook not so good.",
                     "Very doubtful."]
        return responses[random.randint(0, len(responses) - 1)]

        
    @commands.hybrid_command(alias="8ball ask")
    async def ask(self, ctx, *, arg):
        """
        Runs the 8ball command.
        Args:
            ctx (discord.ext.Context): The message Context.
            arg (str): The question to ask the 8ball.
        """
        embed = discord.Embed(
            title = f"\"{str(arg)}\"",
            description=f"```{self.ball_response()}```")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(EightBall(bot))
