import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

version = (discord.__version__)
# Remember to use repr when debugging using the print function.

@bot.event
async def on_ready():
	print('Bot initiated.')

@bot.event
async def on_message(message):
	
	if message.author == bot.user:
		return 
														
	if message.content.startswith("on"):
		await message.channel.send('Yo there!')

	if message.content.startswith("!members"):
		guild = bot.guilds[0] # Type is discord.guild.Guild.
		members = guild.members # A list containing items of type discord.member.Member.
		print(type(members))
		for member in members:
			await message.channel.send(member)
			await message.channel.send(type(member))
		# await message.channel.send(guild.owner)
		# if message.author == guild.owner:
		# 	await message.channel.send("The owner of this server has sent this message.")

with open('token.txt', 'r') as text:
	token = text.read()

bot.run(token)

'''
 result of members

[<Member id=440043419813937152 name='Awesome_Adnan' discriminator='8895' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=664111533407731735 name='Asiwardo' discriminator='0958' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=712704356356718643 name='GudFoNuttin' discriminator='0730' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=778864510613192704 name='mahbubmahin46' discriminator='6724' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=787380235800543232 name='BeastSlayer' discriminator='5819' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=788775920689086504 name='JAMES_BHAI' discriminator='3905' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=795304480051691531 name='mahin93' discriminator='5498' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=829569402034585631 name='dibase' discriminator='0027' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=857319268805509152 name='parvezshahnoor' discriminator='4504' bot=False nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>, <Member id=859428375482073118 name='Chakor' discriminator='9547' bot=True nick=None guild=<Guild id=829425226202218526 name="GudFoNuttin's server" shard_id=None chunked=True member_count=10>>]

'''