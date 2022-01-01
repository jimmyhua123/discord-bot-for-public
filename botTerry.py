import discord
from discord.ext import commands
import json
import random
import os
intents = discord.Intents.all()#dicord1.5 更新 
from googleapiclient.discovery import build


with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json
api_key="hi"
bot = commands.Bot(command_prefix='//',intents=intents)#呼叫前要打的






@bot.event #自動觸發事件
async def on_ready():   #函式 重新定義
    print(">>Bot is online<<")
    #channel = bot.get_channel(int(jdata["test_channel"]))
    #await channel.send('>>Bot is online<<')
    

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded{extension} done')


@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded{extension} done')

#reload暫時壞了不知道為啥 可能跟我打help會出現2個一樣
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded{extension} done')

@bot.command(aliases=["show"])
async def showpic(ctx,*,search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="020feebf5412510ee", searchType="image").execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search})  work?")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)

for Filename in os.listdir('./cmds'): #./=相對路徑
    if Filename.endswith('.py'):
        print(Filename)
        bot.load_extension(f'cmds.{Filename[:-3]}') #-3 = 把.py三個字變不見


if __name__ == "__main__":

  bot.run(jdata['TOKEN'])#需要string形式=''




