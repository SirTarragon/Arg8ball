import discord
import random
from discord.ext import commands
from discord import app_commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(aliases=["coinflip", "flipcoin"])
    async def flip(self, ctx):
        """
        Flips a coin.
        """
        heads_img = "https://media.discordapp.net/attachments/810007261530685461/1048046478293209138/heads.png"
        tails_img = "https://media.discordapp.net/attachments/810007261530685461/1048046478767169556/tails.png"
        rand = random.randint(0, 1)
        text = 'Heads' if rand == 0 else 'Tails'
        img = heads_img if rand == 0 else tails_img
        embed = discord.Embed(
            title="Coin Flip",
            description=f"You flipped a coin and got **{text}**!",
            color=discord.Color.blue()).set_image(
            url=img)
        await ctx.send(embed=embed)

    @commands.hybrid_command(aliases=["diceroll", "rolldice"])
    @app_commands.describe( # this is for slash commands
        dice="The dice to roll. Format: [number of dice]d[number of sides]"
    )
    async def roll(self, ctx, *, dice: str = commands.parameter(description="The dice to roll. Format: [number of dice]d[number of sides]")):
        """
        Rolls a (or multiple) dice.
        """
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception as e:
            raise commands.BadArgument("Format has to be in NdN!") from e

        if rolls > 500 or limit > 5000: # Prevents abuse
            msg = f"You can't roll with {'500 dice' if rolls > 500 else 'more than 5000 sides'}!"
            raise commands.BadArgument(msg)

        results = [random.randint(1, limit) for r in range(rolls)]
        embed = discord.Embed(
            title=f"Dice Roll {dice}",
            description=f"You rolled and got **{', '.join(str(result) for result in results)}**!\n" + \
            f"Total: **{sum(results)}**",
            color=discord.Color.blue())
        await ctx.send(embed=embed)

    @staticmethod
    def __ball_response() -> str:
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

    @commands.hybrid_command(aliases=["8ball", "8-ball", "eightball", "eight-ball"])
    @app_commands.describe( # this is for slash commands
        question="The question to ask the magic 8-ball."
    )
    async def ask(self, ctx, *, question: str = commands.parameter(description="The question to ask the magic 8-ball.")):
        """
        Asks the magic 8-ball a question.
        """
        image="https://emojipedia-us.s3.amazonaws.com/thumbs/120/twitter/134/billiards_1f3b1.png"
        try:
            embed = discord.Embed(
                title = f"\"{str(question)}\"",
                description=f"```{self.__ball_response()}```",
                color=discord.Color.blue()).set_image(
                url=image)
            await ctx.send(embed=embed)
        except Exception as e:
            raise commands.BadArgument("Please ask a question!") from e

    @staticmethod
    def __cardinal_response() -> str:
        responses = ["North", "East", "South", "West", "North-East", "North-West", "South-East", "South-West"]
        return responses[random.randint(0, len(responses) - 1)] # random.randint seems more random than random.choice

    @commands.hybrid_command()
    async def cardinal(self, ctx):
        """
        Gives a random cardinal direction.
        """
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Cardinal_with_raspberries.jpg/120px-Cardinal_with_raspberries.jpg"
        embed = discord.Embed(
            title=f"**{self.__cardinal_response()}**",
            color=discord.Color.blue()).set_image(
            url=image)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(
                title=":x: Error",
                description="Missing required argument(s).",
                color=discord.Color.red()))
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(
                title=":x: Error",
                description=str(error),
                color=discord.Color.red()))


async def setup(bot):
    await bot.add_cog(Fun(bot))
