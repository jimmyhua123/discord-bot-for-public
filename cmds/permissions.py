import discord
from discord import file
from discord.ext import    commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json,random
import datetime

with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

class permissions(Cog_Extension):
    def __init__(self,*args,**kwargs):#**==可變參數  def __init__()==格式化 https://www.youtube.com/watch?v=dBeC-SM-DNw&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=14&t=14s&ab_channel=Proladon
        super().__init__(*args,**kwargs)#super.__init__ => 再重新繼承    
        try:
            with open("./banlist.txt","r",encoding="utf-8")as f:
                self.banlist=[int(line.strip())for line in f.readlines()]
        except FileNotFoundError:
            self.banlist=[]
    
    
    
    @commands.command()#回話
    async def hii(self,ctx):
        await ctx.send('hello')

def setup(bot):
    bot.add_cog(permissions(bot))#呼叫 傳回init