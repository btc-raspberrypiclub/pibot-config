import discord
from configparser import ConfigParser

# Repeat back to the user what they said
def command_echo(params: str, message: discord.Message, client: discord.Client, config: ConfigParser):
    if params == '':
        return None
    else:
        return params
