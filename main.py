import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
print(type(bot))
print(bot)
version = (discord.__version__)

@bot.event
async def on_ready():
	print('Bot initiated.')

@bot.event
async def on_message(message):
	print(message.author)
	print(type(message.author))
	if message.author == bot.user:
		return 
														
	if message.content.startswith("on"):
		await message.channel.send('Yo there!')

	if message.content.startswith("!members"):
		guild = bot.guilds[0]
		await message.channel.send("Here are all the members of this server:")
		async for member in guild.fetch_members(limit=10000):
		    await message.channel.send(member.name)
		await message.channel.send("These are all the members of this server.")

		


with open('token.txt', 'r') as text:
	token = text.read()

bot.run(token)

