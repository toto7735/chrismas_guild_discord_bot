import discord
import os
from discord.ext import tasks
from discord.utils import get

intents = discord.Intents.all()  # All but the two privileged ones
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(client.user.id)
    print("준비 완료!")

    game = discord.Game("하이픽셀 크리스마스 길드 디스코드 채팅")
    await client.change_presence(status=discord.Status.online, activity=game)
    edit_total_member_channel_name.start()
    edit_online_member_channel_name.start()


@client.event
async def on_message(message):
    if not isinstance(message.channel, discord.channel.DMChannel):
        if message.channel.id == 833187276526845972:
            if message.author == client.user:
                return
            if message.reference:
                msg = await client.get_channel(message.channel.id).fetch_message(message.reference.message_id)
                await message.channel.send(msg.embeds.description)
        else:
            if message.author == client.user:
                return
            if message.channel.id != 832982685944905771 and not await has_role("연산자", message.author, message):
                return

            if message.content.startswith('/도움말'):
                await send_help_message(message)
            elif message.content.startswith('/문의'):
                await send_inquiry_help_message(message)
            elif message.content.startswith('/말하기'):
                if not await has_role("연산자", message.author, message):
                    await message.channel.send("아쉽게도 권한이 없어서 안되겠네요. **연산자**")
                    return
                if len(message.content) < 6:
                    await message.channel.send(embed=custom_help_message("말하기", "/말하기 [내용]", "연산자", discord.Colour.orange()))
                    return
                await message.delete()
                await message.channel.send(message.content[4:])
    elif isinstance(message.channel, discord.channel.DMChannel):
        if message.author == client.user:
            return
        embed = discord.Embed(colour=discord.Colour.green(), title="문의가 접수되었습니다!",
                              description="관리진이 확인 후 1주일 내로 처리됩니다.\n더 하실말씀이 있다면 계속 적어주세요.")
        await message.channel.send(embed=embed)
        admin_embed = discord.Embed(colour=discord.Colour.gold(), title="문의 내용", description=message.content)
        await client.get_channel(833187276526845972).send(message.author.mention + "**님의 문의** (처리하려면 이 메시지에 답변)")
        await client.get_channel(833187276526845972).send(embed=admin_embed)


async def send_help_message(message):
    await message.channel.send('**__크리스마스 길드 디스코드 봇 도움말__**')
    await message.channel.send('**[/도움말]** - 봇 도움말을 확인해요.')
    await message.channel.send('**[/음악]** - 음악 관련 도움말를 확인해요. (준비중)')
    await message.channel.send('**[/문의]** - 문의 관련 도움말를 확인 해요.')
    await message.channel.send('**[/처벌]** - 처벌 관련 도움말을 확인 해요. (준비중)')


async def send_inquiry_help_message(message):
    await message.channel.send('**문의 관련 도움말**')
    await message.channel.send('문의 (유저 신고, 관리자 신청, 기타 관리자와 소통)은 **저**(DM)를 통해 받고 있습니다. 저에게 메시지를 보내시면 최대한 빨리 처리해 드리겠습니다!')


@client.event
async def on_raw_reaction_add(payload):
    if payload.message_id != 833332871615610902:
        return
    if payload.emoji.name == "💖":
        guild = client.get_guild(payload.guild_id)
        role = get(guild.roles, id=833190627897638943)
        await payload.member.add_roles(role)
    elif payload.emoji.name == "🍨":
        guild = client.get_guild(payload.guild_id)
        role = get(guild.roles, id=833697054605180929)
        await payload.member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id != 833332871615610902:
       return
    if payload.emoji.name == "💖":
        guild = client.get_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = get(guild.roles, id=833190627897638943)
        await member.remove_roles(role)
    elif payload.emoji.name == "🍨":
        guild = client.get_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        role = get(guild.roles, id=833697054605180929)
        await member.remove_roles(role)


async def has_role(role, user, message):
    role = discord.utils.find(lambda r: r.name == role, message.guild.roles)
    if role in user.roles:
        return True
    else:
        return False


def custom_help_message(command, usage, permission, color):
    embed = discord.Embed(colour=color, title="**" + command + "** 도움말", description=usage + " - **" + permission + "** 권한이 필요해요.")
    return embed


@tasks.loop(seconds=600)
async def edit_total_member_channel_name():
    total_member_channel = client.get_channel(833592614535561247)
    total_members = sum(not member.bot for member in client.get_all_members())
    await total_member_channel.edit(name="🌎 총 인원 : " + str(total_members) + "명")


@tasks.loop(seconds=600)
async def edit_online_member_channel_name():
    online_members = sum(member.status != discord.Status.offline and not member.bot for member in client.get_all_members())
    online_member_channel = client.get_channel(833698038245359677)
    await online_member_channel.edit(name="⚽ 온라인 인원 : " + str(online_members) + "명")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
