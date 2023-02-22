import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = "Hello, I received your message: {}".format(message.content)
    await message.channel.send(response)

client.run('MTA3Nzk5ODQyOTA5NzE4MTE4NA.GZNTQE.mNmAOPGe8WSfGE3Pgo3AXPzGvm_02AagbHTZRA')