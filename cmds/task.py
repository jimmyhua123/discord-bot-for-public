
import discord
from discord import file
from discord.ext import    commands
from discord.ext.commands.core import command
from core.classes import Cog_Extension
import json,asyncio,datetime


with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

#指定/間隔 時間執行指令 - 異步執行/協程概念
class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):#**==可變參數  def __init__()==格式化 https://www.youtube.com/watch?v=dBeC-SM-DNw&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=14&t=14s&ab_channel=Proladon
        super().__init__(*args,**kwargs)#super.__init__ => 再重新繼承#不用加裝飾器


        self.counter=0
        async def interval():
            await self.bot.wait_until_ready() #等bot開好
            self.channel = self.bot.get_channel(int(jdata["test_channel"]))
            while not self.bot.is_closed():#whilenotclose
                pass
                #await self.channel.send('hi bot is running')
                #await asyncio.sleep(2)#單位:秒

        #self.bg_task=self.bot.loop.create_task(interval())

        async def time_task():
            await self.bot.wait_until_ready() #等bot開好
            self.channel = self.bot.get_channel(888174408026456114)
            while not self.bot.is_closed():#while bot not close
                now_time=datetime.datetime.now().strftime("%H%M")#只有 小時 分鐘
                with open('setting.json','r',encoding='utf8')as jFile:
                    jdata=json.load(jFile)
                if now_time == jdata['time'] and self.counter==0:
                    self.counter = 1
                    await self.channel.send("task working")
                    await asyncio.sleep(2)
                #elif now_time != jdata['time'] and self.counter==0:
                #    self.counter = 1
                #    await self.channel.send("task not working")
                #    await asyncio.sleep(2)
                else:
                    await asyncio.sleep(2)
                    pass


        self.bg_task=self.bot.loop.create_task(time_task())

        
    @commands.command()
    async def set_channel(self,ctx,ch:int): #ch:int 宣告int
        self.channel=self.bot.get_channel(ch)
        await ctx.send(f'Set channel:{self.channel.mention}')
    
    @commands.command()
    async def set_time(self,ctx, time): #
        self.counter = 0
        with open('setting.json','r',encoding='utf8')as jFile:
            jdata=json.load(jFile)
        jdata['time']=time
        with open('setting.json','w',encoding='utf8')as jFile:#w=>寫入
            json.dump(jdata,jFile,indent=4)#縮排4
        await ctx.send(f'Set time:{int(jdata["time"])}')
def setup(bot):
    bot.add_cog(Task(bot))

