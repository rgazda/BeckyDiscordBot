# bot.py
import os
import random
import datetime
from git import Repo
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth) # Create GoogleDrive instance with authenticated GoogleAuth instance

#initialize pic lists
ab_list = []
arm_list = []
leg_list = []
tiddy_list = []
fs_list = []

#Git Repo link 
repo = Repo("/Users/caitl/Documents/pythonFiles/DiscordBot/BeckyDiscordBot/BeckyDiscordBot")
assert not repo.bare


def get_Pics():
    # Auto-iterate through all files in the root folder.
    ab_file_list = drive.ListFile({'q': "'1Hh_4YWVkNVaprArjRIPrHA8KS_lSVbuD' in parents and trashed=false"}).GetList()
    for file1 in ab_file_list:
        urlValue = 'https://drive.google.com/uc?id=' + file1['id']
        if urlValue not in ab_list:
            ab_list.append(urlValue)

    fs_file_list = drive.ListFile({'q': "'1G5I1ITUxPhxq26akocFF30p4_wXwsqzE' in parents and trashed=false"}).GetList()
    for file1 in fs_file_list:
        urlValue = 'https://drive.google.com/uc?id=' + file1['id']
        if urlValue not in fs_list:
            fs_list.append(urlValue)

    arm_file_list = drive.ListFile({'q': "'1zVEJC3SJKTvWioZ_EL5yQ57UnbYJYQDQ' in parents and trashed=false"}).GetList()
    for file1 in arm_file_list:
        urlValue = 'https://drive.google.com/uc?id=' + file1['id']
        if urlValue not in arm_list:
            arm_list.append(urlValue)

    leg_file_list = drive.ListFile({'q': "'1bHNWPc_BWjgyq6aKvUzSjRy71ICC9HdW' in parents and trashed=false"}).GetList()
    for file1 in leg_file_list:
        urlValue = 'https://drive.google.com/uc?id=' + file1['id']
        if urlValue not in leg_list:
            leg_list.append(urlValue)

    tiddy_file_list = drive.ListFile({'q': "'16qDAwpUMnOIDXSQzsGDRShWKHur09jRP' in parents and trashed=false"}).GetList()
    for file1 in tiddy_file_list:
        urlValue = 'https://drive.google.com/uc?id=' + file1['id']
        if urlValue not in tiddy_list:
            tiddy_list.append(urlValue)

@bot.command(name='EVIL', help='displays the evil')
async def evil(ctx):
    lemonSeven = '🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋⁷'    
    await ctx.send(lemonSeven)

@bot.command(name='jikook', help='tells u what jikook is')
async def jikookcanon(ctx):
    await ctx.send('CANON.')

@bot.command(name='hiBecky', help='say hi to becky')
async def hiBecky(ctx):
    greetings = ['Whaddup bitch', 'sup br0 (is da ceilin)', 'Leave me aL0ne', 'ey', 'swiggity swooty im comin for dat b00ty', 'hey cutie ;3', 'u come here oft3n?', 'hi friendo', 'y0']
    response = random.choice(greetings)
    await ctx.send(response)

@bot.command(name='jk', help='have googie time uwu')
async def jkTime(ctx):
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    if current_hour > 7 and current_hour < 12:
        await ctx.send('koo morning uwu')
    elif current_hour > 11 and current_hour < 19:
        await ctx.send('googie day OwO')
    elif current_hour > 18 and current_hour < 23:
        await ctx.send('koo nite ~_~')
    else:
        await ctx.send('g00g the FUCK 2 sleep, psych0')

@bot.command(name='ping', help='test your connection/test becky\'s connection')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name='refreshPics', help='reload the images becky has taken from google drive')
async def reloadImages(ctx):
    get_Pics()
    await ctx.send('I did the thing, the thing is done OwO')

@bot.command(name='updates', help='get most recent commit message from becky\'s git repo')
async def getLatestCommit(ctx):
    commit = repo.head.commit
    await ctx.send('Latest update: ' + commit.message)

@bot.command(name='fs', help='display a random figure skater pic')
async def fsPic(ctx):
    if not fs_list:
        get_Pics()
    if not fs_list:
        await ctx.send("Fig Skater image repo is empty")
    else:
        response = random.choice(fs_list)
        await ctx.send(response)

@bot.command(name='ab', help='display a random ab pic...')
async def abPic(ctx):
    if not ab_list:
        get_Pics()
    if not ab_list:
        await ctx.send("ab image repo is empty")
    else:
        response = random.choice(ab_list)
        await ctx.send(response)

@bot.command(name='arm', help='display a random arm pic...')
async def armPic(ctx):
    if not arm_list:
        get_Pics()
    if not arm_list:
        await ctx.send("arm image repo is empty")
    else:
        response = random.choice(arm_list)
        await ctx.send(response)

@bot.command(name='leg', help='display a random leg pic...')
async def legPic(ctx):
    if not leg_list:
        get_Pics()
    if not leg_list:
        await ctx.send("leg image repo is empty")
    else:
        response = random.choice(leg_list)
        await ctx.send(response)

@bot.command(name='tiddy', help='display a random tiddy pic...')
async def tiddyPic(ctx):
    if not tiddy_list:
        get_Pics()
    if not tiddy_list:
        await ctx.send("tiddy image repo is empty")
    else:
        response = random.choice(tiddy_list)
        await ctx.send(response)

@bot.command(name='bts', help='give me the bts boi')
async def bts_boi(ctx):
    bois = ['joonie uwu', 'THX JIN', 'y00ngles', 'hobi :sunny:', 'park FUCKING jimin', 'tae tae :heart_eyes:', 'g00gie :pleading_face:']
    response = random.choice(bois)
    await ctx.send(response)

@bot.command(name='8ball', help='ask the 8ball wat to do, u can\'t make decisions anyway dumb cunt')
async def eightball(ctx):
    answers = ['no way u stupid bitch', 'Si, hijo de puta.', 'uh, fuck ye', 'hell yass hoe', '-mo voice- NO', 'booty', ':musical_note: ~ YES or YES ~ :musical_note:', 'fuckING No', 'YE', 'mebbe e_e', 'ask ur mom', 'try again later, lo0o0o0ser', 'i guess :|', 'y don\'t u fuckin zigazigAH', 'PROBS.', 'iDk nAn mOlLA']
    response = random.choice(answers)
    await ctx.send(response)

@bot.command(name='rollDice', help='Simulates rolling dice. Takes params # of dice, # of sides')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)