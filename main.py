import discord, os, colour, sys
colour.autoreset = True
from aioconsole.stream import ainput
import uuid
TOKEN = open("token.txt","r").read()
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

PREFIX = ".."

class Util:
    
    def __init__(self) -> None:
        self.commands = [
            [["m", "mention"], "Mention a user. Will bring up a prompt when executed. No arguments."],
            [["r", "reply"], "Reply to a message. Will bring up a prompt when executed. No arguments."],
            [["uid", "userid"], "Produces a user's ID. Will bring up a prompt when executed. No arguments."],
            [["gid", "guildid"], "Produce a guilds ID. Will produce ID of current guild. No arguments."],
            [["cid", "channelid"], "Produces a channel's ID. Will produce ID of current channel. No arguments."],
            [["mc", "membercount"], "Produces the member count of a guild. Will produce the member count of the current guild. No arguments."],
            [["e", "q", "quit", "exit"], "Exits clicord. No arguments."],
            [["h", "help"], "Produces this prompt. No arguments."],
            [["clm", "dlm", "deletelastmessage"], "Deletes your last message. No arguments."],
            [["cmm", "dmm", "clearmymessages"], "Deletes all of your messages within the last 250. Edit the limit manually within the main.py (limit). No arguments."],
            [["nuke"], "Attempts to cause as much havoc as possible. USE AT OWN RISK. FOR EXPERIMENTAL PURPOSES ONLY. Carries out on current guild. No arguments."],
            [["spam"], "Spams a random string of characters in all channels in a guild. USE AT OWN RISK. FOR EXPERIMENTAL PURPOSES ONLY. Carries out on current guild. No arguments."],
            [["cc", "changechannel"], "Allows you to change guild/channel. Will bring up a prompt when executed. No arguments"]

            
            
        ]
    
    async def selectChannel(self) -> list:
        count = 0
        print()
        print(colour.green("[console]"),colour.yellow("Please select a guild:"))   
        print()     
        for i in clicord.guilds:
            print(colour.green(f"[{count+1}]"),colour.yellow(f"{i}"))
            count += 1
        try:
            choice = await ainput("--> ")
            guild = clicord.guilds[int(choice)-1]
            count = 0
            print()
            print(colour.green("[console]"),colour.yellow("Please select a channel:"))
            print()
            for i in guild.text_channels:
                print(colour.green(f"[{count+1}]"),colour.red("#")+colour.yellow(f"{i}"))
                count += 1
            choice = await ainput("--> ")
            channel = guild.text_channels[int(choice)-1]
            print(colour.green(f"[success]"),colour.yellow(f"Successfully joined"), colour.red(f"#{channel}"), colour.yellow("of"), colour.red(f"{guild}."))
            return [True, [guild, channel]]
        except Exception as e:
            print(e)
            print(colour.red("[error] Invalid guild or channel. Please try again."))
            return [False, [0, 0]]
                
    async def cin(self, guild, channel) -> list:
        inp = await ainput("--> ")
        if inp.strip().startswith(PREFIX):
            command = inp.split(PREFIX)[1].split(" ")[0]
            args = []
            try:
                args = inp.split(" ")[1:]
                #print(command, args)
            except:
                pass
            if command == "changechannel" or command == "cc":
                rGC = await Util().selectChannel()
                while (not rGC[0]):
                    rGC = await Util().selectChannel()
                return rGC
            elif command == "mention" or command == "m":
                try:
                    await channel.send(f"<@{await self.mention(guild, channel)}>")
                    return [True, [guild, channel]]
                except Exception as e:
                    #print(e)
                    print(colour.red("[error] Invalid user."))
                    return [True, [guild, channel]]
                    
                return [True, [guild, channel]]
            elif command == "uid" or command == "userid":
                try:
                    print(colour.red(f"[console]"),colour.yellow(f"USER ID: {await self.mention(guild, channel)}"))
                    return [True, [guild, channel]]
                except Exception as e:
                    print(colour.red("[error] Invalid user."))
                    return [True, [guild, channel]]
                
            elif command == "mc" or command == "membercount":
                try:
                    print(colour.red(f"[console]"),colour.yellow(f"MEMBER COUNT: {len(guild.members)}"))
                    return [True, [guild, channel]]
                except Exception as e:
                    return [True, [guild, channel]]
                
            elif command == "gid" or command == "guildid":
                try:
                    print(colour.red(f"[console]"),colour.yellow(f"GUILD ID: {guild.id}"))
                    return [True, [guild, channel]]
                except Exception as e:
                    return [True, [guild, channel]]
                
            elif command == "cid" or command == "channelid":
                try:
                    print(colour.red(f"[console]"),colour.yellow(f"CHANNEL ID: {channel.id}"))
                    return [True, [guild, channel]]
                except Exception as e:
                    return [True, [guild, channel]]
           
            elif command == "exit" or command == "quit" or command == "q" or command == "e":
                print(colour.red("[console]"),colour.yellow("Exitting..."))
                try:
                    sys.exit()
                except:
                    sys.exit()
           
           
            elif command == "r" or command == "reply":
                try:
                    print(colour.green("[console]"),colour.yellow("Choose a message to reply to: "))
                    m = [i async for i in channel.history(limit=16)]
                    count = 0
                    for i in m:
                        if i.content:
                            print(colour.green(f"{count+1}."), colour.red("'")+colour.yellow(f"{i.content}")+colour.red("'"),colour.red("by"),colour.yellow(f"{i.author}"))
                            count += 1
                    choice = await ainput("--> ")
                    print(colour.green("[console]"),colour.yellow("Write your reply: "))
                    await m[int(choice)-1].reply(await ainput("--> "))
                    return [True, [guild, channel]]
                except Exception as e:
                    raise
                    print(colour.red("[error] Invalid message. Has it been deleted?"))
                    return [True, [guild, channel]]

            
            elif command == "dmm" or command == "cmm" or command == "clearmymessages":
                try:
                    m = [i async for i in channel.history(limit=250)]
                    for i in m:
                        if i.author.id == clicord.user.id:
                            await i.delete()
                            print(colour.red("[console]"),colour.yellow("Successfully deleted message") ,colour.red(str(i.content)))
                        else:
                            continue
                    return [True, [guild, channel]]
                except:
                    print(colour.red("[error] Unable to delete. Are you missing permissions?"))
                    return [True, [guild, channel]]


            elif command == "dlm" or command == "clm" or command == "deletelastmessage":
                try:
                    m = [i async for i in channel.history(limit=1)]
                    for i in m:
                        if i.author.id == clicord.user.id:
                            await i.delete()
                            print(colour.red("[console]"),colour.yellow("Successfully deleted message") ,colour.red(str(i.content)))
                        
                        else:
                            continue
                    return [True, [guild, channel]]

                except Exception as e:
                    print(e)
                    print(colour.red("[error] Unable to delete. Are you missing permissions?"))
                    return [True, [guild, channel]]
           
                
            elif command == "help" or command == "h":
                for i in self.commands:
                    currC = ""
                    for t in i[0]:
                        currC += colour.red("[")+colour.yellow(f"{PREFIX}{t}")+colour.red("] ")
                    print(currC,colour.red("-"),colour.yellow(i[1]))
                return [True, [guild, channel]]
                

            
            elif command == "spam":
                print(colour.red("[console] CTRL+Z TO STOP"))
                while True:
                    try:
                        for i in guild.text_channels:
                            await i.send(str(uuid.uuid4()))
                            await i.send("@everyone")
                    except Exception as e:
                        print(e) 
                        print(colour.red("[error] Failed."))
                        return [True, [guild, channel]]

                return [True, [guild, channel]]

            elif command == "nuke":
                print(colour.red("[console] CTRL+Z TO STOP"))
                try:
                    if len(guild.text_channels) > 0:
                        for i in guild.text_channels:
                            await i.delete()
                    else: pass
                except Exception as e:
                    #print(e)
                    print(colour.red("[console] MISSING PERMISSIONS TO DELETE CHANNELS. ATTEMPTING TO SPAM."))
                    while True:
                        for i in guild.text_channels:
                            await i.send(str(uuid.uuid4()))
                            await i.send("@everyone")
                while True:
                    try:
                        
                        try:
                            await guild.create_text_channel(str(uuid.uuid4()))
                        except Exception as e:
                            raise
                            print(colour.red("[console] MISSING PERMISSIONS TO CREATE CHANNELS. ATTEMPTING TO SPAM."))
                            while True:
                                for i in guild.text_channels:
                                    await i.send(str(uuid.uuid4()))
                                    await i.send("@everyone")
                        for i in guild.text_channels:
                            await i.send(str(uuid.uuid4()))
                            await i.send("@everyone")
                        
                    except Exception as e:
                        print(e) 
                        print(colour.red("[error] Failed."))
                        return [True, [guild, channel]]

                return [True, [guild, channel]]



            else:
                print(colour.red(f"[error] Invalid command. Please try {PREFIX}help."))
                return [True, [guild, channel]]
            
    

                

        else:
            try:
                await channel.send(inp)
                return [True, [guild, channel]]
            except:
                print(colour.red("[error] Empty message or invalid permissions to send a message here."))
                return [True, [guild, channel]]

    async def mention(self, guild, channel) -> int:
        count = 0
        try:
                print(colour.green("[console]"),colour.yellow("Please select a user:"))   
                for i in guild.members:
                    print(colour.green(f"[{count+1}]"),colour.yellow(f"{i}"),colour.cyan("[bot]" if i.bot else ""))
                    count += 1
                choice = await ainput("--> ")
                return guild.members[int(choice)-1].id
        except Exception as e:
            raise
    
            
            
            
            
class Clicord(discord.Client):

    async def on_ready(self):
        self.ready = False
        print(colour.green("[login]"),colour.yellow("Logged in as"),colour.red(str(clicord.user)))
        rGC = await Util().selectChannel()
        while (not rGC[0]):
            rGC = await Util().selectChannel()
        self.guild = rGC[1][0]
        self.channel = rGC[1][1]
        self.ready = True
        while True:
            rGC = await Util().cin(self.guild, self.channel)
            self.guild = rGC[1][0]
            self.channel = rGC[1][1]
            
    async def on_message(self, message):
        try:
            if message.channel.id == self.channel.id and self.ready:
                print(colour.green("[message]"), "||",colour.cyan(f"[{message.guild}]"),"||",colour.blue(f"[#{message.channel}]"),"||", colour.yellow(f"[{str(message.author)}]"),">",message.content)
            #print("--> ",end="")
            #await Util().cin(self.guild, self.channel)
            else:
                pass
        except:
            pass
try: 
    clicord = Clicord(intents=intents)
    clicord.run(TOKEN)
except Exception as e:
    print(e)
    print(colour.red("[error] Invalid token OR user quit OR ran into fatal error. See above."))
