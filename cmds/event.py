import discord
from discord import file
from discord.ext import    commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8')as jFile: #r=read讀取as命名jfile
    jdata=json.load(jFile)#呼叫jdata=呼叫json

class Event(Cog_Extension):
    @commands.Cog.listener()  
    async def  on_member_join(self,member):#有人join
        #Wchannel = bot.get_channel(888173557828419606) #指定頻道
        Wchannel = self.bot.get_channel(int(jdata["welecome_channel"]))#要加int()因為在setting是string
        await Wchannel.send(f'{member}join!')#呼叫 協成->coroutine send 傳送文字

    @commands.Cog.listener()  
    async def  on_member_remove(self,member):#有人不見
        #Lchannel = bot.get_channel(888173601503723540)
        Lchannel = self.bot.get_channel(int(jdata["leave_channel"])) #指定頻道
        await Lchannel.send(f'{member}leave!')#呼叫 協成->coroutine
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['aqua','阿夸']
        #if msg.content =='aqua':#完全相同
        #if msg.content =='aqua'and msg.author!= self.bot.user:#防無限迴圈 bot回話自己
        #if  msg.content.endswith('aqua'):#句尾有
        #if  msg.content in keyword and msg.author!= self.bot.user:
        if   (jdata["keyword"]) in msg.content  and msg.author!= self.bot.user: 
            await msg.channel.send('我先Q走')


def setup(bot):
    bot.add_cog(Event(bot))#呼叫 傳回init