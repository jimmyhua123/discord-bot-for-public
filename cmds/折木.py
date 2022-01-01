import discord
from discord.ext import    commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

class 折木(Cog_Extension):
    @commands.command()  
    async def 茶(self,ctx):#網路圖片
        await ctx.send(jdata['(茶'])
    @commands.command()  
    async def 折木1(self,ctx):#網路
        await ctx.send(jdata['折木奉太郎1'])
    @commands.command()  
    async def 折木2(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎2'])
    @commands.command()  
    async def 折木3(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎3'])
    @commands.command()  
    async def 折木4(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎4'])
    @commands.command()  
    async def 折木5(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎5'])
    @commands.command()  
    async def 折木6(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎6'])
    @commands.command()  
    async def 折木7(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎7'])
    @commands.command()  
    async def 折木8(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎8'])
    @commands.command()  
    async def 折木9(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎9'])
    @commands.command()  
    async def 折木10(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎10'])
    @commands.command()  
    async def 折木11(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎11'])
    @commands.command()  
    async def 折木12(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎12'])
    @commands.command()  
    async def 折木13(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎13'])
    @commands.command()  
    async def 折木14(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎14'])
    @commands.command()  
    async def 折木15(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎15'])
    @commands.command()  
    async def 折木16(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎16'])
    @commands.command()  
    async def 折木17(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎17'])
    @commands.command()  
    async def 折木18(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎18'])
    @commands.command()  
    async def 折木19(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎19'])
    @commands.command()  
    async def 折木20(self,ctx):#網路圖片
        await ctx.send(jdata['折木奉太郎20'])

def setup(bot):
    bot.add_cog(折木(bot))#呼叫 傳回init