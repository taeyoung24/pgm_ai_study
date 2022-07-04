import config
import os, atexit
import discord
from discord.ext import commands, tasks

import modules.bot_system.main as bot_manager

intents = discord.Intents.default() # 봇 의도 기본값
intents.members = True # 멤버 조회 오류 해결용

bot = commands.Bot('', intents=intents)

@bot.listen('on_ready')
async def on_ready():
    await bot_manager.on_ready(bot)
    print("클라이언트가 준비되었습니다.")
    
@bot.listen('on_member_update')
async def on_member_update(before: discord.Member, after: discord.Member):
    pass

@bot.listen('on_message')
async def on_message(message):
    pass

# @bot.listen('on_member_join')
# async def on_member_join(member):

# @bot.listen('on_member_remove')
# async def on_member_remove(member):

# @bot.listen('on_guild_join')
# async def on_guild_join(guild):

# @bot.listen('on_guild_remove')
# async def on_guild_remove(guild):


# 프로그램 종료시 (인터셉트)
def on_exit_app():
    print("프로그램이 종료되었습니다.")
atexit.register(on_exit_app)


bot.run(os.environ['BOT_TOKEN'])