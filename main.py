import discord
from discord.ext import commands
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, HardwareType
import random
import datetime
import sys
import os
from time import sleep
import requests
from random import randint
import json



intents = discord.Intents.default()
intents.members = True

client = commands.Bot(description="", command_prefix=",", case_insensitive=True, intents=intents)
client.remove_command("help")

def is_owner(ctx):
    return ctx.message.author.id == 366106745396920322, 366106745396920322
    


def is_haxer(ctx):
    return ctx.message.author.id == 750607871649120340, 679859331600089098



                



snipes = dict()

def snipe_embed(context_channel, message, user):
    if message.author not in message.guild.members or message.author.color == discord.Colour.default():
        embed = discord.Embed(description = message.content, timestamp = message.created_at)
    else:
        embed = discord.Embed(description = message.content, color = message.author.color, timestamp = message.created_at)
    embed.set_author(name = str(message.author), icon_url = message.author.avatar_url)
    if message.attachments:
        embed.add_field(name = 'Attachment(s)', value = '\n'.join([attachment.filename for attachment in message.attachments]))
        embed.set_image(url=message.attachments[0].url)

    if message.channel != context_channel:
        embed.set_footer(text = 'Sniped By: ' + str(user) + ' | in channel: #' + message.channel.name)
    else:
        embed.set_footer(text = 'Sniped By: ' + str(user))
    return embed

guild_ids = [834636547571187743] # Put your server IDs in this array.


@client.event
async def on_ready():
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1
    
    activity = discord.Game(name = f'with {members} members')
    await client.change_presence(status=discord.Status.dnd, activity=activity)

    print('We have logged in as {0.user}'.format(client))
r = requests.head("https://api.github.com")
if r.ok:
    print ('Connected to github api')
else:
    print ('Uhh Github Api Is not connecting!')
    


@client.event
async def on_member_join(member):
    a = ["Welcome To 6ix.", "Enjoy Your Stay At 6ix.", "Hey Cutie"]
    channel = discord.utils.get(member.guild.channels, name='v')
    if channel is not None:
        embed = discord.Embed(
        title=f"**6ix - New Member**", color=000000,
        description=f"**{member} Is Our {member.guild.member_count} Member \nReact With 🖤 To Get Access To The Rest Of The Server.**"
    )
    embed.set_footer(text=f"6ix", icon_url="https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif")
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
    await channel.send(f"{member.mention}, " + random.choice(a), delete_after=7)
    message = await channel.send(embed=embed, delete_after=7)
    await message.add_reaction("🖤")

@client.event
async def on_reaction_add(reaction, user):
        if reaction.emoji == "🖤":
            await user.add_roles(discord.utils.get(user.guild.roles, name="6ix"))


@client.command()
async def github(ctx, user):
    githuburl = requests.get(f"https://api.github.com/users/{user}") 
    githubjson = json.loads(githuburl.text)    
    embed = discord.Embed(title="Github", description=f"{user}'s Profile", color=000000)
    embed.add_field(name="Name", value=githubjson["name"], inline=True)
    embed.add_field(name="Location", value=githubjson["location"], inline=True)
    embed.add_field(name="Website", value=githubjson["blog"], inline=True)
    embed.add_field(name="Twitter", value=githubjson["twitter_username"], inline=True)
    embed.add_field(name="Gists", value=githubjson["public_gists"], inline=True)
    embed.add_field(name="Followers", value=githubjson["followers"], inline=True)
    embed.add_field(name="following", value=githubjson["following"], inline=True)
    embed.add_field(name="Bio: ", value=githubjson["bio"], inline=True)
    embed.add_field(name="Repos", value=githubjson["public_repos"], inline=True)
    embed.add_field(name="Gists", value=githubjson["public_gists"], inline=True)
    embed.set_thumbnail(url=githubjson["avatar_url"])
    await ctx.send(embed=embed)

@client.command()
async def repo(ctx, search):
    abcc = requests.get(f"https://api.github.com/search/repositories?q={search}&page,per_page,sort,order") 
    githubjsony = json.loads(abcc.text)    
    embed = discord.Embed(title="Repos", description=f"Top 5 Repos Found For {search}", color=000000)
    embed.add_field(name="Repo 1", value=githubjsony["items"][0]["html_url"]
, inline=False)
    embed.add_field(name="Repo 2", value=githubjsony["items"][1]["html_url"]
, inline=False)
    embed.add_field(name="Repo 3", value=githubjsony["items"][2]["html_url"]
, inline=False)
    embed.add_field(name="Repo 4", value=githubjsony["items"][3]["html_url"]
, inline=False)
    embed.add_field(name="Repo 5", value=githubjsony["items"][4]["html_url"]
, inline=False)
    await ctx.send(embed=embed)



@client.command()
async def code(ctx, *, text):
        fart = ("https://cancer-co.de/upload")
        a = {
           "text": f"{text}"
           }
        r = requests.post(fart, data=a)
        b = (r.text)
        c = (r)
        data = r.json()

        aya = data['url']
        embed = discord.Embed(title="6ix", description=f"Text Uploader", color=000000)
        embed.add_field(name='URL:',value=f"{aya}")
        await ctx.send(embed=embed)




@client.event
async def on_message_delete(message):
        if message.guild and not message.author.bot:
            try:
                snipes[message.guild.id][message.channel.id] = message
            except KeyError:
                snipes[message.guild.id] = {message.channel.id: message}

@client.command(aliases=["s"])
async def snipe(ctx, channel: discord.TextChannel = None):
        if not channel:
            channel = ctx.channel

        try:
            sniped_message = snipes[ctx.guild.id][channel.id]
        except KeyError:
            await ctx.send(embed=discord.Embed(description=f":x: No messages to be sniped! {ctx.author.mention}", colour=000000), )
        else:
            await ctx.send(embed = snipe_embed(ctx.channel, sniped_message, ctx.author))


@client.command(name="clear", aliases=["c"])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=999):
    embed = discord.Embed(color=000000)
    embed.add_field(name='Purge',value=f"{ctx.author}  ***cleared***  {amount}  ***messages in***  {ctx.message.channel} ")

    await ctx.channel.purge(limit=amount)
    await ctx.send(embed=embed)

@client.command(aliases=["ui"])
async def userinfo(ctx, *, member: discord.Member):
    embed=discord.Embed(
        color=discord.Color.from_rgb(000, 000, 00)
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Name:", value=member.name, inline=False)
    embed.add_field(name="tag:", value=f"#{member.discriminator}", inline=False)
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Created:", value=member.created_at.strftime("%B %d %Y,\n%H:%M:%S %p"), inline=False)
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%B %d %Y,\n%H:%M:%S %p"), inline=False)
    embed.add_field(name="Highest Role:", value=member.top_role, inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['servericon'])
async def guildicon(ctx): # b'\xfc'
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@client.command()
async def loyal(ctx, user: discord.Member = None, number=100):
      '''
      Rates A Loyalty In The Server
      '''
      if user is None:
          user = ctx.author
      embed=discord.Embed(
          colour=0x2f3136,
          timestamp=datetime.datetime.utcnow(),
          title="Loyalty", 
          description=f"Ooou **{user}** saying they loyal...", color=000000)
      embed.set_footer(text=f"{ctx.guild.name}")
          
      await ctx.send(embed=embed)
      sleep(1)
      embed=discord.Embed(
          colour=0x2f3136,
          timestamp=datetime.datetime.utcnow(),
          title="Loyalty", 
          description=f"Turns Out They're  {randint(1, number)}%  Loyal!", color=000000)
      embed.set_footer(text=f"{ctx.guild.name}")
          
      await ctx.send(embed=embed)
  

@client.command(name="cinfo", aliases=["ci"])
async def channelinfo(ctx, *, channel_or_category: str=None):
        if not channel_or_category:
            channel = ctx.channel
        else:
            channel = arg.get_voice_channel(ctx, channel_or_category)
        if not channel:
            channel = arg.get_text_channel(ctx, channel_or_category)
        if not channel:
            channel = arg.get_category(ctx, channel_or_category)
        if not channel:
            return await ctx.send("Invalid channel/category :trident:")
        perms = "\n".join(list(map(lambda x: x[0].replace("_", " ").title(), filter(lambda x: x[1] == True, channel.permissions_for(ctx.author)))))
        if isinstance(channel, discord.TextChannel):
            s=discord.Embed(colour=000000, description=ctx.channel.topic)
            s.set_author(name=channel.name, icon_url=ctx.guild.icon_url)
            s.set_thumbnail(url=ctx.guild.icon_url)
            s.add_field(name="ID", value=channel.id)
            s.add_field(name="NSFW Channel", value="Yes" if channel.is_nsfw() else "No")
            s.add_field(name="Channel Position", value=channel.position + 1)
            s.add_field(name="Slowmode", value="{} {}".format(channel.slowmode_delay, "second" if channel.slowmode_delay == 1 else "seconds") if channel.slowmode_delay != 0 else "Disabled")
            s.add_field(name="Channel Category", value=channel.category.name if channel.category else "None")
            s.add_field(name="Members", value=len(channel.members))
            s.add_field(name="Author Permissions", value=perms if perms else "None", inline=False)
        elif isinstance(channel, discord.VoiceChannel):
            s=discord.Embed(colour=000000, description=ctx.channel.topic)
            s.set_author(name=channel.name, icon_url=ctx.guild.icon_url)
            s.set_thumbnail(url=ctx.guild.icon_url)
            s.add_field(name="ID", value=channel.id)
            s.add_field(name="Channel Position", value=channel.position + 1)
            s.add_field(name="Channel Category", value=channel.category.name if channel.category else "None")
            s.add_field(name="Members Inside", value=len(channel.members))
            s.add_field(name="User Limit", value="Unlimited" if channel.user_limit == 0 else channel.user_limit)
            s.add_field(name="Bitrate", value="{} kbps".format(round(channel.bitrate/1000)))
            s.add_field(name="Author Permissions", value=perms if perms else "None", inline=False)
        elif isinstance(channel, discord.CategoryChannel):
            channels = "\n".join(map(lambda x: x.mention if isinstance(x, discord.TextChannel) else x.name, channel.channels))
            s=discord.Embed(colour=000000, description=ctx.channel.topic)
            s.set_author(name=channel.name, icon_url=ctx.guild.icon_url)
            s.set_thumbnail(url=ctx.guild.icon_url)
            s.add_field(name="ID", value=channel.id)
            s.add_field(name="NSFW Category", value="Yes" if channel.is_nsfw() else "No")
            s.add_field(name="Category Position", value=channel.position + 1, inline=False)
            s.add_field(name="Author Permissions", value=perms if perms else "None", inline=True)
            s.add_field(name="Channels", value=channels if channels else "None", inline=True)
        await ctx.send(embed=s)

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    channel_info = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])

@client.command(aliases=["massunban"])
@commands.has_permissions(ban_members=True)
@commands.cooldown(1,60, commands.BucketType.guild)
async def unbanall(ctx):
    bans = 0 
    unbanned = 0
    banlist = await ctx.guild.bans()
    idktbh = len(banlist)
    if idktbh == 0:
      await ctx.send("There is no banned users in this server for me to unban!")
      return
    else:
      embed = discord.Embed(title='Unbanall', color=000000, description=f'Unbanning Users...', delete_after=7)
      embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
      msg = await ctx.send(embed=embed)

      for users in banlist:
        bans += 1
        await ctx.guild.unban(user=users.user) 
        unbanned += 1
      embed1 = discord.Embed(title='Unbanall', color=000000, description=f'**Unbanned {unbanned} Members!**')
      embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
      await ctx.send(embed=embed1)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason = None):
    if reason == None:
        await member.kick(reason=f'Kicked By {ctx.author} With No Reason Provided...')
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Successfully Kicked {member} With No Reason Provided.`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Please Provide A Member To Kick...`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)
    else:
        await member.kick(reason=reason)
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Successfully Kicked {member} For {reason}.`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason = None):
    if reason == None:
        await member.ban(reason=f'Banned By {ctx.author} With No Reason Provided...')
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Successfully Banned {member} With No Reason Provided.`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Please Provide A Member To Ban...`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)


@client.command()
@commands.check(is_owner)
async def unban(ctx, member_id:discord.User
 = None):
    if member_id == None:
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Please Provide A Member ID To Unban...`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)
    else:
        await ctx.guild.unban(user=member_id)
        embed = discord.Embed(title='6ix', color=000000, description=f'**`Successfully Unbanned {member_id}!`**')
        embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif')
        await ctx.send(embed=embed)


@client.command(name='boosters')
async def boosters_send(ctx):
    await ctx.message.delete()
    guildName = ctx.guild.name
    boosters = ""
    for user in {ctx.guild.premium_subscription_count}:
        boosters = boosters+str(user)+","
    if len(boosters)<=0:
        boosters="None"
    container = discord.Embed(title=guildName, color=0x2f3136)
    container.add_field(name="Current boosters:" ,value=boosters ,inline=False)
    container.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=container)


@client.command()
@commands.has_permissions(manage_channels=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def unlock(ctx, channel: discord.TextChannel = None):

      overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(title='Radiant', description=f'Unlocked **{ctx.channel.name}**', color=000000)
      await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def lock(ctx, channel: discord.TextChannel = None):
      overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(title='Radiant', description=f'Locked **{ctx.channel.name}**', color=000000)
      await ctx.send(embed=embed)


@client.command()
async def help(ctx, category=None):
   if category is None:
        embed = discord.Embed(color=(000000))
        embed.title="help"
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/G0vTksm7UkAsFoklpfuc6Jov-8lnhRsTBbFhi9_o6Qg/%3Fsize%3D128/https/cdn.discordapp.com/icons/877552532543635458/a_e55204259216ed81382829e7f3a97ba5.gif")
        embed.description = f"6ix Cmds \n Ban \n Kick \n Unban \n Nuke \n Snipe \n loyal"
        embed.set_footer(text ='Usage ,help <Command>')
        await ctx.send(embed=embed, delete_after=25)
   elif str(category).lower() == "ban":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="ban", value="bans user from the guild", inline=False)
        embed.add_field(name="usage", value=" >ban @thief ", inline=False)
        embed.add_field(name="permissons required", value="admin, ban members.", inline=False)
        embed.set_footer(text ='Admin')
        await ctx.send(embed=embed)
   elif str(category).lower() == "kick":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="kick", value="kicks user from the guild", inline=False)
        embed.add_field(name="usage", value=" ,kick @thief ", inline=False)
        embed.add_field(name="permissons required", value="admin, kick members.", inline=False)
        embed.set_footer(text ='Admin')
        await ctx.send(embed=embed)    
   elif str(category).lower() == "mute":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="mute", value="mutes user from speaking in the guild", inline=False)
        embed.add_field(name="usage", value=" ,mute @thief ", inline=False)
        embed.add_field(name="permissons required", value="admin, mute members.", inline=False)
        embed.set_footer(text ='Admin')
        await ctx.send(embed=embed)     
   elif str(category).lower() == "unban":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="unban", value="unbans user from the guild", inline=False)
        embed.add_field(name="usage", value=" ,unban @thief ", inline=False)
        embed.add_field(name="permissons required", value="admin,", inline=False)
        embed.set_footer(text ='Admin')
   elif str(category).lower() == "nuke":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="nuke", value="Nukes A Channel", inline=False)
        embed.add_field(name="usage", value=" ,Nuke ", inline=False)
        embed.add_field(name="permissons required", value="Admin,", inline=False)
        embed.set_footer(text ='Stranded')
        await ctx.send(embed=embed)    
   elif str(category).lower() == "snipe":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="snipe", value="Snipes A Messgae", inline=False)
        embed.add_field(name="usage", value=" ,snipe <#channel> ", inline=False)
        embed.set_footer(text ='Stranded')
        await ctx.send(embed=embed)    
   elif str(category).lower() == "userinfo":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="userinfo", value="Gets A Users Info", inline=False)
        embed.add_field(name="usage", value=" ,userinfo <@user> ", inline=False)
        embed.set_footer(text ='Stranded')
        await ctx.send(embed=embed)    
   elif str(category).lower() == "loyal":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="loyal", value="Test a users loyalty", inline=False)
        embed.add_field(name="usage", value=" ,loyal <@user> ", inline=False)
        embed.set_footer(text ='Stranded')
        await ctx.send(embed=embed)   
   elif str(category).lower() == "cl":
        embed = discord.Embed(color=(000000))
        embed.add_field(name="clear", value="clears A Channel", inline=False)
        embed.add_field(name="usage", value=" ,clear <amount>", inline=False)
        embed.add_field(name="permissons required", value="Admin,", inline=False)
        embed.set_footer(text ='Stranded')
        await ctx.send(embed=embed)   



@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def afk(ctx, reason : str=None, * , member: discord.Member=None):

    if reason == None:
        reason = 'No Reason Specifed'
    current_nick = ctx.author.nick
    embed = discord.Embed(color=000000)
    embed.title="AFK"
    embed.description=f"{ctx.author.mention} Is Now Afk | {reason}"
    await ctx.send(embed=embed)
    await ctx.author.edit(nick=f"[AFK] {reason}") 

    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    embed = discord.Embed(color=000000)
    embed.title="AFK"
    await ctx.author.edit(nick=current_nick)
    embed.description=f"{ctx.author.mention} u are no longer afk!"
    await ctx.send(embed=embed)
    while ctx.author is afk:
        if member.mentioned_in(msg):
          await ctx.send(f"{member.name} Is Afk | {reason}")



def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@client.command(name= 'restart')
@commands.check(is_owner)
async def restart(ctx):
  await ctx.send("Restarting bot...")
  restart_bot()


@client.command(name='eval')
async def my_command(ctx, *, arg):
    result = eval(arg)
    await ctx.send(result)




@client.command()
@commands.check(is_owner)
async def botinfo(ctx):
    proxie_list = []


    with open("https.txt", "r") as f:                   #USE HTTPS PROXIES ONLY
        for proxy in f.readlines():
            proxie_list.append(proxy.replace("\n", ""))
    proxies = {
      'https': random.choice(proxie_list)
    }
    url = "https://request-header-parser-microservice.freecodecamp.rocks/api/whoami"
    software_names = [SoftwareName.FIREFOX.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

    # Get list of user agents.
    user_agents = user_agent_rotator.get_user_agents()

    # Get Random User Agent String.
    user_agent = user_agent_rotator.get_random_user_agent()

    headers = {
    'User-Agent': user_agent
    }


    r = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    ipinfo = json.loads(r.text) 
    print(r.text)   
    print (ipinfo)
    print(r.json())
    verify = False
    embed = discord.Embed(color=(000000))
    embed.add_field(name="Bot IP", value=ipinfo['ipaddress'], inline=True)
    embed.add_field(name="Bot User Agent", value=ipinfo['software'], inline=True)
    await ctx.send(embed=embed)   

@client.command()
@commands.check(is_haxer)
async def rando(ctx):


    software_names = [SoftwareName.EDGE.value, SoftwareName.CHROME.value, SoftwareName.ANDROID.value, SoftwareName.CHROMIUM.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    operating_systems = [OperatingSystem.IOS.value, OperatingSystem.ANDROID.value, OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
 
    hardware_types = [HardwareType.MOBILE.value, HardwareType.SERVER.value, HardwareType.COMPUTER.value]    
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems,hardware_types=hardware_types, limit=100)

    # Get list of user agents.
    user_agents = user_agent_rotator.get_user_agents()

    # Get Random User Agent String.
    user_agent = user_agent_rotator.get_random_user_agent()
    embed = discord.Embed(color=(000000))
    embed.add_field(name="HAXER TOOL", value=user_agent, inline=True)
    await ctx.send(embed=embed)

@client.command()
@commands.check(is_haxer)
async def phaxer(ctx):
    url = "https://api.getproxylist.com/proxy"
    r = requests.get(url) 
    kok = json.loads(r.text)        
    embed = discord.Embed(color=(000000))
    embed.add_field(name="IP", value=kok['ip'], inline=False)
    embed.add_field(name="Port", value=kok['port'], inline=False)
    embed.add_field(name="Last Checked", value=kok['lastTested'], inline=False)
    embed.add_field(name="Proxy Type", value=kok['protocol'], inline=False)
    embed.add_field(name="Country", value=kok['country'], inline=False)
    embed.add_field(name="Speed", value=kok['connectTime'], inline=False)
    embed.add_field(name="Proxy Level", value=kok['anonymity'], inline=False)

    await ctx.send(embed=embed)

@client.command()
async def haxer(ctx):
    if ctx.message.author.id in (679859331600089098,877997042193006593):

      embed = discord.Embed(color=(000000))
      embed.add_field(name="rando", value='Sends A Random UserAgent',inline=False)
      embed.add_field(name="phaxer", value='Sends A Random Proxy',inline=False)
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(color=(000000))
      embed.add_field(name="It Seems You Have Found Our Secret Cmd add ឵឵x#0001 to get whitelisted ", value='Secret',inline=False)
      await ctx.send(embed=embed)

client.run("")
