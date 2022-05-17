import user_handler, random, discord, datetime, time, asyncio, log_handler, encryption
from discord.ext import commands

token_password = input("Enter the token password: ")
client = commands.Bot(command_prefix = "!")
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("!help"))
    print("ready")

@client.command()
async def hello(ctx):
    log_handler.log(ctx.author.name, "Hello")
    embed = discord.Embed(title = "Hello", colour = discord.Colour.blurple())
    embed.add_field(name = "this is a test command", value = "Lorem ipsum dolor sit amet.", inline = True)
    await ctx.send(embed = embed)

client.run(encryption.decrypt(open("token.txt", "rb").read().decode("utf-8"), token_password))