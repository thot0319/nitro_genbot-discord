
###################
#discord.py==1.4.0#
###################

import discord
import random
import string

client = discord.Client()


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!니트로'):
        ranNitro = ""
        for i in range(0, 16):
            ranNitro += str(random.choice(string.ascii_letters))
            NitroEmbed = discord.Embed(title='니트로 생성기', description='https://discord.gift/' + ranNitro)
        await message.channel.send(embed=NitroEmbed)
        
client.run('NzgzNzIzMDU4ODkxNDU2NTIy.X8e4-g.NsQzb4N5Y36OReBPL8hOjdKvmnU')
