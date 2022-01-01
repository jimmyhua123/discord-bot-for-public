import discord
from discord.ext import    commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

class React(Cog_Extension):
    @commands.command()
    async def 夸粉(self,ctx):#本機
        #pic = discord.File('C:\\Users\MochaMom\\Documents\\GitHub\\discord.bot\\pic\\821758945475297281.png')#可以用轉意+一個/
        pic = discord.File(jdata['aqua'])
        await ctx.send(file=pic)

    @commands.command()
    async def 隨機圖片(self,ctx):
        random_pic=random.choice(jdata['r_aqua'])
        rpic = discord.File(random_pic)
        await ctx.send(file=rpic)

    @commands.command()  
    async def bonk(self,ctx):#網路圖片
        pic=(jdata['url_bonk'])
        await ctx.send(pic)

    @commands.command()  
    async def gura_dance(self,ctx):#網路圖片
        pic=(jdata['gura_dance'])
        await ctx.send(pic)
        
    @commands.command()  
    async def conodio(self,ctx):#網路圖片
        pic=(jdata['url_dio'])
        await ctx.send(pic)

    @commands.command()  
    async def 不要瞎掰(self,ctx):#網路圖片
        pic=(jdata['nofucking'])
        await ctx.send(pic)

    @commands.command()  
    async def 窩不知道(self,ctx):#網路圖片
        pic=(jdata['窩不知道'])
        await ctx.send(pic)
   
    @commands.command()  
    async def 派耶(self,ctx):#網路圖片
        await ctx.send(jdata['派耶'])
    @commands.command()  
    async def 歪頭(self,ctx):#網路圖片
        await ctx.send(jdata['霍金歪頭'])
def setup(bot):
    bot.add_cog(React(bot))#呼叫 傳回init
