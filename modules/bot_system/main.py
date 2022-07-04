import discord
from modules.bot_system.debug_utils import build_time



async def on_ready(bot: discord.Client):
    # 테스트용 빌드 문구
    btime = build_time() + ' 빌드 테스트'
    await bot.change_presence(activity=discord.Game(name=btime + ' 빌드 테스트'))
    print(btime + ' 빌드 테스트가 준비되었습니다.')