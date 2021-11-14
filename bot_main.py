# import discord
# import slash as slash
# from discord.ext import commands
# from discord.ext import tasks
# from discord.utils import get
# import requests, discord
# from discord.ext import commands
# from mojang import MojangAPI
# from discord_slash import SlashCommand, SlashContext
# from discord_slash.utils.manage_commands import create_choice, create_option
# client = commands.Bot(command_prefix="/")
# slash = SlashCommand(client,sync_commands=True)
# import os
#
#
# intents = discord.Intents.all()  # All but the two privileged ones
# client = commands.Bot(command_prefix='/', intents=intents)
#
#
# @client.event
# async def on_ready():
#     print(client.user.id)
#     print("준비 완료!")
#
#     game = discord.Game("하이픽셀 크리스마스 길드 디스코드 채팅")
#     await client.change_presence(status=discord.Status.online, activity=game)
#     edit_total_member_channel_name.start()
#     edit_online_member_channel_name.start()
#
#
#
# @client.command()
# async def 도움말(ctx):
#     await check_command_channel(ctx)
#     await ctx.send('**__크리스마스 길드 디스코드 봇 도움말__**')
#     await ctx.send('**[/도움말]** - 봇 도움말을 확인해요.')
#     await ctx.send('**[/음악]** - 음악 관련 도움말를 확인해요. (준비중)')
#     await ctx.send('**[/문의]** - 문의 관련 도움말를 확인 해요.')
#     await ctx.send('**[/처벌]** - 처벌 관련 도움말을 확인 해요. (준비중)')
#
#
# @client.command()
# async def 문의(ctx):
#     await ctx.send('**문의 관련 도움말**')
#     await ctx.send('문의 (유저 신고, 관리자 신청, 기타 관리자와 소통)은 **저**(DM)를 통해 받고 있습니다. 저에게 메시지를 보내시면 최대한 빨리 처리해 드리겠습니다!')
#
#
# @client.command()
# async def 말하기(message):
#     if not await has_role("연산자", message.author, message):
#         await message.channel.send("아쉽게도 권한이 없어서 안되겠네요. **연산자**")
#         return
#     if len(message.content) < 6:
#         await message.channel.send(embed=custom_help_message("말하기", "/말하기 [내용]", "연산자", discord.Colour.orange()))
#         return
#     await message.delete()
#     await message.channel.send(message.content[4:])
#
#
# @client.event
# async def on_message(message):
#     if not isinstance(message.channel, discord.channel.DMChannel):
#         if message.reference:
#             if message.author == client.user:
#                 return
#             if message.channel.id == 833187276526845972:
#                 try:
#                     msg = await client.get_channel(message.channel.id).fetch_message(message.reference.message_id)
#                     msg = str(msg.content)
#                     user = msg.replace("**님의 문의** (처리하려면 이 메시지에 답변)", "")
#                     user = user.replace("<", "")
#                     user = user.replace(">", "")
#                     user = user.replace("@", "")
#                     user = client.get_user(int(user))
#                     embed = discord.Embed(colour=discord.Colour.green(), title="답변이 왔습니다!", description=message.content)
#                     await user.send(embed=embed)
#                 except Exception:
#                     print("")
#         else:
#             if message.author == client.user:
#                 return
#             if message.channel.id != 832982685944905771 and not await has_role("연산자", message.author, message):
#                 return
#             elif message.content.startswith('/말하기'):
#                 if not await has_role("연산자", message.author, message):
#                     await message.channel.send("아쉽게도 권한이 없어서 안되겠네요. **연산자**")
#                     return
#                 if len(message.content) < 6:
#                     await message.channel.send(embed=custom_help_message("말하기", "/말하기 [내용]", "연산자", discord.Colour.orange()))
#                     return
#                 await message.delete()
#                 await message.channel.send(message.content[4:])
#             elif message.content.startswith('/채팅청소'):
#                 if not await has_role("연산자", message.author, message):
#                     await message.channel.send("아쉽게도 권한이 없어서 안되겠네요. **연산자**")
#                     return
#                 if len(message.content) < 7:
#                     await message.channel.send(embed=custom_help_message("채팅청소", "/채팅청소 [수]", "연산자", discord.Colour.green()))
#                     return
#                 await message.delete()
#                 i = int(message.content[5:])
#                 history_message = await message.channel.history(limit=i).flatten()
#                 for msg in history_message:
#                     await msg.delete()
#     elif isinstance(message.channel, discord.channel.DMChannel):
#         if message.author == client.user:
#             return
#         embed = discord.Embed(colour=discord.Colour.orange(), title="문의가 접수되었습니다!",
#                               description="관리진이 확인 후 1주일 내로 처리됩니다.\n더 하실말씀이 있다면 계속 적어주세요.")
#         await message.channel.send(embed=embed)
#         admin_embed = discord.Embed(colour=discord.Colour.gold(), title="문의 내용", description=message.content)
#         await client.get_channel(833187276526845972).send(message.author.mention + "**님의 문의** (처리하려면 이 메시지에 답변)")
#         await client.get_channel(833187276526845972).send(embed=admin_embed)
#
#
#
#
# @client.event
# async def on_raw_reaction_add(payload):
#     if payload.message_id != 833332871615610902:
#         return
#     if payload.emoji.name == "💖":
#         guild = client.get_guild(payload.guild_id)
#         role = get(guild.roles, id=833190627897638943)
#         await payload.member.add_roles(role)
#     elif payload.emoji.name == "🍨":
#         guild = client.get_guild(payload.guild_id)
#         role = get(guild.roles, id=833697054605180929)
#         await payload.member.add_roles(role)
#
#
# @client.event
# async def on_raw_reaction_remove(payload):
#     if payload.message_id != 833332871615610902:
#        return
#     if payload.emoji.name == "💖":
#         guild = client.get_guild(payload.guild_id)
#         member = await guild.fetch_member(payload.user_id)
#         role = get(guild.roles, id=833190627897638943)
#         await member.remove_roles(role)
#     elif payload.emoji.name == "🍨":
#         guild = client.get_guild(payload.guild_id)
#         member = await guild.fetch_member(payload.user_id)
#         role = get(guild.roles, id=833697054605180929)
#         await member.remove_roles(role)
#
#
# async def has_role(role, user, message):
#     role = discord.utils.find(lambda r: r.name == role, message.guild.roles)
#     if role in user.roles:
#         return True
#     else:
#         return False
#
#
# def custom_help_message(command, usage, permission, color):
#     embed = discord.Embed(colour=color, title="**" + command + "** 도움말", description=usage + " - **" + permission + "** 권한이 필요해요.")
#     return embed
#
#
# @tasks.loop(seconds=600)
# async def edit_total_member_channel_name():
#     total_member_channel = client.get_channel(833592614535561247)
#     total_members = sum(not member.bot for member in client.get_all_members())
#     await total_member_channel.edit(name="🌎 총 인원 : " + str(total_members) + "명")
#
#
# @tasks.loop(seconds=600)
# async def edit_online_member_channel_name():
#     online_members = sum(member.status != discord.Status.offline and not member.bot for member in client.get_all_members())
#     online_member_channel = client.get_channel(833698038245359677)
#     await online_member_channel.edit(name="⚽ 온라인 인원 : " + str(online_members) + "명")
#
#
# async def check_command_channel(message):
#     if message.channel.id != 832982685944905771:
#         return
#
# # aewolStart
# @slash.slash(name="verify",description="인증을 하는 명령어 시스템입니다.",guild_ids=[536526007906074624,879026494771462174],options=[create_option(name="nickname",description="자신의 닉네임을 입력해주세요.",required=True,option_type=3,choices=[])])
# async def verify(ctx:SlashContext, nickname:str):
#     ping = round(client.latency * 1000)
#     try:
#         # UUID
#         playeruuid = MojangAPI.get_uuid(nickname)
#         # Links
#         requestlink = str("https://api.hypixel.net/player?key="+API+"&uuid="+playeruuid)
#         guildrequest = str("https://api.hypixel.net/guild?key="+API+"&player="+playeruuid)
#         # datas
#         hydata = requests.get(requestlink).json()
#         guildhydata = requests.get(guildrequest).json()
#         playerdiscord = hydata["player"]["socialMedia"]["links"]["DISCORD"]
#         # name, guild
#         nickname = hydata["player"]["displayname"]
#         hyguild = guildhydata["guild"]
#         if hyguild=="None":
#             hyguild="❌"
#         else:
#             hyguild= guildhydata["guild"]["name"]
#             if hyguild == "Chrismas":
#                 role = discord.utils.get(ctx.guild.roles,name="Member")
#                 await ctx.author.add_roles(role)
#         if str(ctx.author) == str(playerdiscord):
#             verifieddiscord = "✅"
#             role = discord.utils.get(ctx.guild.roles,name="사람")
#             await ctx.author.add_roles(role)
#             await ctx.author.edit(nick=nickname)
#         else:
#             verifieddiscord = "❌"
#     except KeyError:
#         playerdiscord = "Not set"
#         await ctx.reply("하이픽셀 계정과 당신의 디스코드 계정을 연동해주세요!\nhttps://youtu.be/3_D32V0FUG4")
#         pass
#     except TypeError: await ctx.reply("올바르지 않은 닉네임입니다!")
#     except: pass
#     embed = discord.Embed(title=f"**`{nickname}`**", description="Chrismas 길드 전용 인증 디스코드 봇입니다!")
#     embed.set_thumbnail(url="https://mc-heads.net/avatar/"+playeruuid)
#     embed.add_field(name="**UUID**",value=f"{playeruuid}",inline=False)
#     embed.add_field(name="**디스코드**",value="`"+playerdiscord+"`",inline=True)
#     embed.add_field(name="**본인 여부**",value=verifieddiscord,inline=True)
#     embed.add_field(name="**길드**",value=hyguild,inline=True)
#     embed.set_footer(text=f"Ping: {ping}ms ㅣ 제작 Aewol#0001")
#     await ctx.reply(embed=embed)
#
# access_token = os.environ["BOT_TOKEN"]
# client.run(access_token)
