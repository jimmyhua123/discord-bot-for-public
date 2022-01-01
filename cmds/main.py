from _typeshed import Self
import discord
from discord import file
from discord.ext import    commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json,random
import datetime

with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

class Main(Cog_Extension):
    @commands.command()
    async def online_list(self,ctx):#ctx.guild 所在私服器
        for member in ctx.guild.members:          
            if str(member.status) == 'online'and member.bot==False:#注意type
                await ctx.send(f'{member} 的狀態是 {member.status}')

    @commands.command()
    async def offline_list(self,ctx):#ctx.guild 所在私服器
        for member in ctx.guild.members:          
            if str(member.status) == 'offline'and member.bot==False:#注意type
                await ctx.send(f'{member} 的狀態是 {member.status}')  
    
    @commands.command()
    async def  jojo(self,ctx):#embed
        embed=discord.Embed(title="SHIZAAAAAAAA",url="https://www.youtube.com/watch?v=0-Kda5ZLN5s,color=0x4c712d")
        embed.set_author(name="Majaja")
        embed.add_field(name="test", value='1', inline=True)
        embed.add_field(name='2', value='3', inline=True)
        embed.add_field(name='4', value='5', inline=True)
        embed.set_footer(text='test123456')
        await ctx.send(embed=embed)
    
    @commands.command()#回話
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()#回話
    async def say10times(self,ctx,*,msg):
        await ctx.message.delete()
        for i in range(1,11):
            await ctx.send(msg)
    @commands.command()#清理
    async def cleanmsg(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.send(f'already cleaned ,{num} message')
    @commands.command()
    async def online_list(self,ctx):#ctx.guild 所在私服器
        for member in ctx.guild.members:          
            if str(member.status) == 'online'and member.bot==False:#注意type
                await ctx.send(f'{member} 的狀態是 {member.status}')

    @commands.command()
    async def offline_list(self,ctx):#ctx.guild 所在私服器
        for member in ctx.guild.members:          
            if str(member.status) == 'offline'and member.bot==False:#注意type
                await ctx.send(f'{member} 的狀態是 {member.status}')  
    
    @commands.command()
    async def rand_online_squad(self,ctx):#ctx.guild 所在私服器
       # print(ctx.guild.members)
        online =[]
        for member in ctx.guild.members:
            #print(member.status)
            #await ctx.send(f'{member} 的狀態是 {member.status}')
            if str(member.status) == 'online'and member.bot==False:#注意type
                online.append(member.name)#加入
        #print(online)
        random_online=[]
        random_online = random.sample(online,k=10)
        for squad in range(2):
            rlist = random.sample(random_online,k=5)#隨機挑n人放到list直到結束
            await ctx.send(f'第 {squad+1} 隊是 {rlist}')
            for name in  rlist:
                random_online.remove(name)

    @commands.command()
    async def rand_offline_squad(self,ctx):#ctx.guild 所在私服器
        offline =[]
        for member in ctx.guild.members:         
            if str(member.status) == 'offline'and member.bot==False:#注意type
                offline.append(member.name)#加入
        random_offline=[]
        random_offline = random.sample(offline,k=15)
        for squad in range(3):
            rlist = random.sample(random_offline,k=5)
            await ctx.send(f'第 {squad+1} 隊是 {rlist}')
            for name in  rlist:
                random_offline.remove(name)
        #for x in random.sample(offline,k=4):#sample == 不重複                          


    @commands.command()
    async def rand_offline_squad(self,ctx):#ctx.guild 所在私服器
        offline =[]
        for member in ctx.guild.members:         
            if str(member.status) == 'offline'and member.bot==False:#注意type
                offline.append(member.name)#加入
        random_offline=[]
        random_offline = random.sample(offline,k=15)
        for squad in range(3):
            rlist = random.sample(random_offline,k=5)
            await ctx.send(f'第 {squad+1} 隊是 {rlist}')
            for name in  rlist:
                random_offline.remove(name)
        #for x in random.sample(offline,k=4):#sample == 不重複                  
    
    @commands.command()
    async def load(self,ctx):
        await ctx.send('Shutting down...')
        db.commit()
        self.bot.scheduler.shutdown()
        await self.bot.logout()



def setup(bot):
    bot.add_cog(Main(bot))#呼叫 傳回init
