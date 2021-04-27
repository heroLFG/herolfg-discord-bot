import discord
import os
import json

client = discord.Client()

# @client.event
# async def on_socket_raw_receive(message):
#     print('on socket raw receive')
#     print(message)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_raw_reaction_add(payload):
    print('on raw reaction add')
    print(payload)

@client.event
async def on_raw_reaction_remove(payload):
    print('on raw reaction remove')
    print(payload)

@client.event
async def on_message(message):
    print(f'client.user:{client.user}')
    print(f'message.author:{message.author}')
    print(f'message.reference:{message.reference}')
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!hello'):
        await message.reply('Hello!', mention_author=True)
    if message.content.startswith('!log'):
        messages = await message.channel.history().flatten()
        for msg in messages:
            print(f'{msg.author} said: {msg.content} with reactions {msg.reactions}')
            for reaction in msg.reactions:
                print(client.get_emoji(reaction))
    if message.content.startswith('!react'):
        messages = await message.channel.history().flatten()
        for msg in messages:
            emoji = '\N{Hundred Points Symbol}'
            await msg.add_reaction(emoji)
    # if message.content.startswith('!delete'):
    #     messages = await message.channel.history().flatten()
    #     for msg in messages:
    #         await msg.delete()

@client.event
async def on_message_edit(before, after):
    print('on message edit')
    fmt = f'**{before.author}** edited their message:\n{before.content} -> {after.content}'
    print(fmt)
    # await before.channel.send(fmt.format(before, after))

@client.event
async def on_message_delete(message):
    print('on message delete')
    fmt = f'{message.author} has deleted the message: {message.content}'
    print(fmt)

token = os.getenv('TOKEN')
if token:
    client.run(os.getenv('TOKEN'))
else:
    print('token not found')
