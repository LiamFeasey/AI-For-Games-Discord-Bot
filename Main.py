import os
import io
import discord
import re
import requests

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True


# Create a new Discord client instance
client = discord.Client(intents=intents)

#General Chat room: 230718477172867072
#Bot testing chat room: 1078680465801760780

# Define a function to send a message
async def send_message(targetChannel, message):
    channel = client.get_channel(int(targetChannel))  # Replace with the ID of the channel you want to send the message to
    if channel == None:
        channel = client.get_channel(1078680465801760780)
        message = "Channel Not Found"
        print("Channel not found!")
    await channel.send(message)


# Define an event listener for when a message is sent in a server
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #Put the prompts you want the bot to reply to here, they must be in lower case to make it easier to parse the incoming messages!!
    response = 'I don\'t understand!'

    target_channel = message.channel.id
    
    
    
    #Handle text only input and reply with only text
    if 'hello' in message.content.lower():
        response = 'Hello! I am currently under development so expect limited features!'
    elif 'goodbye' in message.content.lower():
        authorName = message.author.name
        response = f'Goodbye {authorName}!'
    elif 'what are you for?' in message.content.lower():
        authorName = message.author.name
        response = f'I am just a test to help my author learn how to create discord bots!'
    elif message.content == "Dan":
        channel = message.channel
        file = discord.File("C:/Users/30005249/Documents/Artificial Intelligence for Games/Assignment 1/dan.png")
        await channel.send(file=file)
        response = 'Available to a good home for £20'

    #Sends a message to a specific channel of your choice
    if message.content.startswith('!sendmessage'):
        commandContents = message.content.split(' ')

        #ChanelID is the 2nd item in the list, remove everything that isn't a number
        channelID = commandContents[1]
        channelID = re.sub(r'[^\d]+', '', channelID)
        
        #Remove the first 2 items in the list, then join the remaining message contents back into one string
        commandContents = commandContents[2:]    
        messangeContent = ' '.join(commandContents)

        if channelID.isnumeric() != True:
            target_channel = message.channel.id
            response = "Target channel not set"
        else:
            target_channel = channelID
            response = messangeContent


    if message.content.startswith('!image'):
        commandContents = message.content.split(' ')

        for image in commandContents:
            if image.lower() == "dan1":
                image_url  = "https://cdn.glitch.global/4db1c3ad-7267-4525-b242-66b292b16f9f/Dan1.jpg?v=1677266745194"
                imageName = "dan1.jpg"
            elif image.lower() == 'artur1':
                image_url  = "https://cdn.glitch.global/4db1c3ad-7267-4525-b242-66b292b16f9f/Artur1.jpg?v=1677267150992"
                imageName = "artur1.jpg" 
            elif image.lower() == 'dartur1':
                image_url  = "https://cdn.glitch.global/4db1c3ad-7267-4525-b242-66b292b16f9f/Dartur1.jpg?v=1677267159363"
                imageName = "dartur1.jpg"
            else:
                image_url  = None

        image = requests.get(image_url, stream=True)

        file = discord.File(io.BytesIO(image.content), filename=imageName)

        if file != None:
            channel = message.channel
            await channel.send(file=file)
        else:
            send_message(target_channel, "Image not found!")     

        
    
    print("Message Contents: " + message.content.lower())
    # Replace "Hello, world!" with the message you want to send
    await send_message(target_channel, response)

@client.event
async def on_reaction_add(reaction, user):
    # Do something when a reaction is added
    print(f"{user} added {reaction.emoji} to {reaction.message}")
    await send_message(reaction.channel, f"{user} added {reaction.emoji} to \"{reaction.message.content}\"")

# Start the Discord bot
client.run('BOT_TOKEN_GOES_HERE')  # Replace with your bot's token

if client:
  print("Running")
  
