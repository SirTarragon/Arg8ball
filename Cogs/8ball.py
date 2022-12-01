import discord
import random
from discord.ext import commands

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.slash_command(name="8ball ask")
    async def ask(ctx, *, arg):
        embed = discord.Embed(
            title = f"\"{str(arg)}\"",
            description=f"```{ball_response()}```")
        await ctx.send(embed=embed)
        
    @staticmethod
    def ball_response() -> str:
        responses = ["It is certain.", "It is decidedly so.",
                     "Without a doubt. Yes definitely.,
                     "You may rely on it.", "As I see it, yes.",
                     "Most likely.", "Outlook good.", "Yes.",
                     "Signs point to yes.", "Reply hazy, try again.",
                     "Ask again later.", "Better not tell you now.",
                     "Cannot predict now.", "Concentrate and ask again.",
                     "Don't count on it.", "My reply is no.",
                     "My sources say no.", "Outlook not so good.",
                     "Very doubtful."]
        return responses[random.randint(0, len(responses) - 1)]

    
async def setup(bot):
    await bot.add_cog(EightBall(bot))
