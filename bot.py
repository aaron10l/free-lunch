from dotenv import load_dotenv
import discord
import asyncio
import praw
import os

load_dotenv()

# REDDIT CONNECTION
reddit = praw.Reddit(
	client_id = os.getenv('REDDIT_CLIENT_ID'),
	client_secret = os.getenv('REDDIT_CLIENT_SECRET'),
	user_agent = os.getenv('REDDIT_USER_AGENT'),
    check_for_async=False
)

# DISCORD CONNECTION
discord_key = os.getenv('DISCORD_TOKEN')
channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
client = discord.Client(intents=discord.Intents.default())

# subreddit to search
subreddit = reddit.subreddit('chipotle')


@client.event
async def find_free_food():
    channel = client.get_channel(channel_id)
    last_checked_post_time = None
    while True:
        print("Checking for free food")
        new_posts = list(subreddit.new(limit=10))
        
        if last_checked_post_time == None:
            last_checked_post_time = new_posts[len(new_posts) - 1].created_utc
        for post in new_posts:
            if post.created_utc > last_checked_post_time:
                for word in post.title.split(" "):
                    if word.lower() == "free":
                        await channel.send(f"Found free post: {post.title} \n {post.url}")
                        print(f"Found free post: {post.title}")
                        break
            else:
                break
        last_checked_post_time = new_posts[0].created_utc
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print(f'user {client.user} is online')
    await find_free_food()

client.run(discord_key)
