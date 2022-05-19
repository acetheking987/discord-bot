import user_handler, random, discord, log_handler, encryption
from PIL import Image, ImageColor
import lorem as lorem_ipsum
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
    user_handler.add_exp(str(ctx.author.id), 10)
    log_handler.log(ctx.author.name, "Hello")
    embed = discord.Embed(title = "Hello", colour = discord.Colour.blurple())
    embed.add_field(name = "this is a test command", value = "Lorem ipsum dolor sit amet.", inline = True)
    await ctx.send(embed = embed)

@client.command()
async def lorem(ctx):
    user_handler.add_exp(str(ctx.author.id), 10)
    log_handler.log(ctx.author.name, "Lorem")
    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.add_field(name = "Lorem ipsum", value = lorem_ipsum.paragraph(), inline = True)
    await ctx.send(embed = embed)

@client.command()
async def bal(ctx, user: discord.User = None):
    log_handler.log(ctx.author.name, f"Bal  |  {user}")
    user_handler.add_exp(str(ctx.author.id), 10)

    if user == None:
        user = ctx.author

    userid = str(user.id)
    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.set_author(name = user, icon_url = user.avatar_url)
    embed.add_field(name = "Balance", value = str(user_handler.get_bal(userid)), inline = True)
    embed.add_field(name = "Level", value = str(user_handler.get_lvl(userid)), inline = True)
    await ctx.send(embed = embed)

@client.command()
async def embed(ctx,  title = "", *, description = ""):
    log_handler.log(ctx.author.name, f"Embed  |  {title}  |  {description}")
    user_handler.add_exp(str(ctx.author.id), 10)

    embed = discord.Embed(title = title, description = description, colour = discord.Colour.blurple())
    await ctx.send(embed = embed)

@client.command()
async def dice(ctx):
    log_handler.log(ctx.author.name, "Dice")
    user_handler.add_exp(str(ctx.author.id), 10)

    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.add_field(name = "Dice", value = str(random.randint(1, 6)), inline = True)
    await ctx.send(embed = embed)

@client.command()
async def rate(ctx, user : discord.User = None):
    log_handler.log(ctx.author.name, f"Rate  |  {user}")
    user_handler.add_exp(str(ctx.author.id), 10)

    if user == None:
        user = ctx.author

    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.set_author(name = user, icon_url = user.avatar_url)
    embed.add_field(name = "rate", value = f"{user} is {random.randint(1, 100)} on the rate scale", inline = True)
    await ctx.send(embed = embed)

@client.command()
async def colour(ctx):
    log_handler.log(ctx.author.name, "Colour")
    user_handler.add_exp(str(ctx.author.id), 10)
    colour_hex = hex(random.randint(0, 16777215))
    colour_rgb = ImageColor.getcolor(str(colour_hex).replace("0x", "#"), "RGB")
    image = Image.new("RGB", (200, 200), colour_rgb)
    image.save("colour.png")

    embed = discord.Embed(title = f"Colour", colour = discord.Colour(int(colour_hex, 16)))
    embed.add_field(name = "Hex", value = str(colour_hex).replace("0x", "#"), inline = True)
    embed.add_field(name = "RGB", value = f"{colour_rgb[0]} {colour_rgb[1]} {colour_rgb[2]}", inline = True)
    embed.set_image(url = "attachment://colour.png")
    await ctx.send(file = discord.File("colour.png"), embed = embed)

@client.command()
async def ping(ctx):
    log_handler.log(ctx.author.name, "Ping")
    user_handler.add_exp(str(ctx.author.id), 10)

    embed = discord.Embed(colour = discord.Colour.blurple())
    embed.add_field(name = "pong", value = str(round(client.latency * 1000)) + "ms", inline = True)
    await ctx.send(embed = embed)

@client.command()
async def gamble(ctx, amount = 0):
    log_handler.log(ctx.author.name, f"Gamble  |  {amount}")
    user_handler.add_exp(str(ctx.author.id), 10)

    if amount == 0:
        embed = discord.Embed(title = "Gamble", colour = discord.Colour.blurple())
        embed.add_field(name = "Gamble", value = "You must enter an amount to gamble", inline = True)
        await ctx.send(embed = embed)
    elif amount > user_handler.get_bal(str(ctx.author.id)):
        embed = discord.Embed(title = "Gamble", colour = discord.Colour.blurple())
        embed.add_field(name = "Gamble", value = "You do not have enough money to gamble", inline = True)
        await ctx.send(embed = embed)
    else:
        multiplyer = random.randint(-20, 10)
        if multiplyer == 0:
            multiplyer = 1
        elif multiplyer < 0:
            multiplyer = -1

        bal = user_handler.get_bal(str(ctx.author.id))
        user_handler.set_bal(str(ctx.author.id), (bal - amount) + (amount * multiplyer))    
        embed = discord.Embed(title = "Gamble", colour = discord.Colour.blurple())
        embed.add_field(name = "Gamble", value = "You have gambled " + str(amount) + " coins", inline = True)
        embed.add_field(name = "Multiplyer", value = str(multiplyer), inline = True)
        if multiplyer < 0:
            embed.add_field(name = "Result", value = "You lost " + str(amount * multiplyer) + " coins", inline = True)
        else:
            embed.add_field(name = "Result", value = "You won " + str(amount * multiplyer) + " coins", inline = True)
        await ctx.send(embed = embed)

    log_handler.log(ctx.author.name, "Gamble")
    user_handler.add_exp(str(ctx.author.id), 10)

@client.command()
async def help(ctx):
    log_handler.log(ctx.author.name, "Help")
    user_handler.add_exp(str(ctx.author.id), 10)

    embed = discord.Embed(title = "help", colour = discord.Colour.blurple())
    embed.add_field(name = "!hello", value = "Sends a hello message", inline = True)
    embed.add_field(name = "!lorem", value = "Sends a lorem ipsum paragraph", inline = True)
    embed.add_field(name = "!bal", value = "Sends your balance", inline = True)
    embed.add_field(name = "!embed", value = "Sends an embed", inline = True)
    embed.add_field(name = "!dice", value = "Sends a dice roll", inline = True)
    embed.add_field(name = "!rate", value = "Sends a rate", inline = True)
    embed.add_field(name = "!colour", value = "Sends a random colour", inline = True)
    embed.add_field(name = "!ping", value = "Sends your ping", inline = True)
    embed.add_field(name = "!help", value = "Sends this message", inline = True)
    await ctx.send(embed = embed)

client.run(encryption.decrypt(open("token.txt", "rb").read().decode("utf-8"), token_password))