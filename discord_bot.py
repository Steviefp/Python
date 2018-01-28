import discord
import asyncio
import requests
import league_requests
import league_wr
import praw
# zipcode and key are for requests for the weather api website
zipcode,key='48164','05dc89dd3fd81bfcc393477e92a0e8d7'

#start discord
client=discord.Client()

#timing vars
timer=0
timer_state=True

#reddit bot
reddit = praw.Reddit(client_id='6wT1IggpXMSgEw',
                     client_secret='f90jNXEuumY9UfrrIWKD7X64j24',
                     user_agent='description i believe')


#Someone reason on_ready and on_message have to be called like that and can't be renamed.
@client.event
async def on_ready():
    print("Logged in as",client.user.name)



@client.event
async def on_message(message):
    global timer
    global timer_state


    if message.content.startswith('!reddit'):
        sub=reddit.random_subreddit()
        neat=0

        for post in sub.new(limit=1):
            neat=post.url
        await client.send_message(message.channel, neat)


    if message.content.startswith('!play'):
        await client.send_message(message.channel, '<@165698419820724224> ''<@125029977404997632> ' '<@166315074821029888>')
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

    if message.content.startswith("!runes"):
        user_input=message.content[7:]
        rune_list=league_requests.nice(user_input)
        await client.send_message(message.channel,"{0}, {1}, {2}, {3}, {4}, {5}".format(rune_list[0],rune_list[1],rune_list[2],rune_list[3],rune_list[4],rune_list[5]))

    if message.content.startswith("!wr"):
        message_vars=[]
        for x in message.content.split():
            message_vars.append(x)
        print(message_vars)
        ratio=league_wr.main(message_vars[1],message_vars[2])
        await client.send_message(message.channel,str(ratio))

#help command for servers
    if message.content.startswith("!help"):
        await client.send_message(message.channel,"Few commands such as: !start, !stop, !temp, !add, !sub, !times, !divide !opgg !runes !wr !reddit !play")



# discord client run key
client.run('MzQ5MTg2MDMzMTkzMDU4MzA3.DH2RnA.6MWBaIx7TzO21vJRzFeYwsxgEE0')