import discord
import asyncio
import requests
import league_requests
import league_wr
import praw
import league_summoner_wr
import python_json_write_to_file
import champ_counter

# zipcode and key are for requests for the weather api website
zipcode,key='48164','05dc89dd3fd81bfcc393477e92a0e8d7'

#start discord
client=discord.Client()
#riot api key
key="RGAPI-550295db-18c3-4600-898c-c5e1d71f0e04"
#timing vars
timer=0
timer_state=True

#reddit bot
token=open("apikey.env","r")
api_list=[]
for x in token:
    api_list.append(x.strip())
token.close()


reddit = praw.Reddit(client_id=api_list[0],
                     client_secret=api_list[1],
                     user_agent='description i believe')


#Someone reason on_ready and on_message have to be called like that and can't be renamed.
@client.event
async def on_ready():
    print("Logged in as",client.user.name)



@client.event
async def on_message(message):
    global timer
    global timer_state

    #reddit
    if message.content.startswith('!r'):
        message_vars=[]
        for x in message.content.split():
            message_vars.append(x)
        sub=reddit.subreddit(message_vars[1])
        await client.send_message(message.channel,'http://www.reddit.com%s' % sub.url)

    if message.content.startswith('!reddit random'):
        sub=reddit.random_subreddit()
        neat=0

        for post in sub.new(limit=1):
            neat=post.url
        await client.send_message(message.channel, neat)

    if message.content.startswith('!red'):
        message_vars=[]
        for x in message.content.split():
            message_vars.append(x)

        sub=reddit.subreddit(message_vars[2])

        if message_vars[1]=='new':
            for post in sub.new(limit=1):
                sub_url=post.url
            await client.send_message(message.channel,sub_url)
        if message_vars[1]=='hot':
            for post in sub.hot(limit=2):
                if post != sub.sticky():
                    sub_url=post.url
            await client.send_message(message.channel,sub_url)
        if message_vars[1]=='top':
            for post in sub.top(limit=1):
                sub_url=post.url
            await client.send_message(message.channel,sub_url)
        if message_vars[1]=='rising':
            for post in sub.rising(limit=1):
                sub_url=post.url
            await client.send_message(message.channel,sub_url)
        if message_vars[1]=='controversial':
            for post in sub.controversial(limit=1):
                sub_url=post.url
            await client.send_message(message.channel,sub_url)

#tyler stopwatch/timer for when he leaves ocmputer
    if message.content.startswith("!start"):
        await client.send_message(message.channel,"Timer Started")
        timer=0
        timer_state=True
        while timer_state:
            timer += 1
            await asyncio.sleep(1)
            print(timer)

    if message.content.startswith("!stop"):
        timer_state = False
        await client.send_message(message.channel, "It took tyler " + str(timer) + " seconds")


#tempature for my new boston
    if message.content.startswith("!temp"):
        r=requests.get("http://samples.openweathermap.org/data/2.5/weather?zip="+zipcode+",us&appid="+key)
        temp_temp=float((9/5*(r.json()['main']['temp']-273)+32))
        await client.send_message(message.channel,"The temperature is %.2f"%temp_temp)

# bunch of math functions

    if message.content.startswith("!add"):
        user_input=message.content[5:].split()
        await client.send_message(message.channel,(float(user_input[0])+float(user_input[1])))

    if message.content.startswith("!sub"):
        user_input=message.content[5:].split()
        await client.send_message(message.channel,(float(user_input[0])-float(user_input[1])))

    if message.content.startswith("!times"):
        user_input=message.content[7:].split()
        await client.send_message(message.channel,(float(user_input[0])*float(user_input[1])))

    if message.content.startswith("!divide"):
        user_input=message.content[8:].split()
        await client.send_message(message.channel,"%.2f"%(float(user_input[0])/float(user_input[1])))

#links opgg accounts
    if message.content.startswith("!opgg"):
        user_input=message.content[6:]
        await client.send_message(message.channel,
                                  "http://na.op.gg/summoner/userName=%s"%user_input)
# league of legends api stuff
    if message.content.startswith("!runes"):
        user_input=message.content[7:]
        rune_list=league_requests.runes(user_input,key)
        await client.send_message(message.channel,"{0}, {1}, {2}, {3}, {4}, {5}".format(rune_list[0],rune_list[1],rune_list[2],rune_list[3],rune_list[4],rune_list[5]))

    if message.content.startswith("!wrchamp"):
        message_vars=[]
        for x in message.content.split():
            message_vars.append(x)
        print(message_vars)
        ratio=league_wr.main(message_vars[1],message_vars[2],key)
        await client.send_message(message.channel,str(ratio))

    if message.content.startswith("!wr"):
        message_wr_vars=[]
        for x in message.content.split():
            message_wr_vars.append(x)
        await client.send_message(message.channel,str(league_summoner_wr.summoner_wr(message_wr_vars[1],key).win_rate))

    if message.content.startswith("!counter"):
        message_champ_vars=[]
        for x in message.content.split():
            message_champ_vars.append(x)
        champ=champ_counter.countering_champ(message_champ_vars[1])
        await client.send_message(message.channel, "\n".join("{}: {}".format(index, value) for index, value in enumerate(champ.champ_list, 1)))


# json pretty upload file
    if message.content.startswith("!json"):

        message_json = []

        for x in message.content.split():
            message_json.append(x)

        ree = python_json_write_to_file.json_write(message_json[1])

        ree.file_write()


        await client.send_file(message.channel,'json_bot.json')
        ree.file_delete()

# play
    if message.content.startswith('!playing'):
        await client.send_message(message.channel, '<@165698419820724224> ''<@125029977404997632> ' '<@166315074821029888>')

#help command for servers
    if message.content.startswith("!help"):
        await client.send_message(message.channel,"Few commands such as: !start, !stop, !temp, !add, !sub, !times, !divide !opgg !runes !wr !wrchamp !red !reddit random !r (subreddt)*links subreddit* !json !play")



# discord client run key

discord_token=api_list[2]


client.run(discord_token)