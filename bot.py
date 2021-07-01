''' We are going to create a discord bot using the discord.py library. '''

# Importing the library.
import discord # The main library we are using to create the bot. See discord rewrite for the complete documentation.
import os # This one allows us to use token from the .env file
import requests # This requests module allows the code to make http 
import json # Will allow us to work with our requested files easier.
import random # Using this module, the bot will be able to send random inspiring messages if it senses the presence of depression on a message.
from replit import db # Imports the data stored in the repl.it database.


client = discord.Client() # This client allows us to connect our code with the official discord server. You can say that this is our bot.
 
sad_words = ["sad", "unhappy", "depressed", "depression", "motivation", "cos2", "koshto", "hardship", "struggle", "crying", "miserable", "depressing"]
starter_encouragements = [
    "cheer up!", "Hang in there", "Times times don't last forever, tough people do", "Life is beautiful", "Don't lose hope mate!", "Don't be so miserable duh!", "We got your back dear.", "You are a great person!"
]

def get_quotes():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return ((quote))

def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements
    

@client.event 
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message_delete(message):
    await message.channel.send("A message was deleted by {0.author.mention}".format(message))

@client.event
async def on_raw_message_delete(message):
    await message.channel.send("A message was deleted.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith("$hello"):
        msg = "Hello {0.author.mention}".format(message)
        await message.channel.send(msg)
        await message.add_reaction('\N{THUMBS UP SIGN}')
    
    if message.content.startswith("$inspire"):
        quote = get_quotes()
        await message.channel.send(quote)
    
    if message.content.startswith("thanks bot"):
        await message.channel.send("Welcome Human!")

    options = starter_encouragements
    if "encouragements" in db.keys():
        options = options + db["encouragements"]

    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(options))

    if message.content.startswith("$new"):
        encouraging_message = message.content.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")
    
    if message.content.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = message.content.split()


@client.event
async def on_disconnect():
    general_channel = get_channel(789852733128572962)
    await (general_channel.send("Bye bye, I am going to sleep."))

client.run(os.getenv("TOKEN")) # This starts our bot/program.
