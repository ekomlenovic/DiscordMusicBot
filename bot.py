import discord
from discord.ext import commands
import yt_dlp
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

# Options yt-dlp
YTDLP_OPTIONS = {'format': 'bestaudio/best', 'noplaylist': True, 'quiet': True}
FFMPEG_OPTIONS = {'options': '-vn'}

song_queue = []

def search_youtube(query):
    """Search YouTube and get stream URL and title."""
    with yt_dlp.YoutubeDL(YTDLP_OPTIONS) as ytdl:
        results = ytdl.extract_info(f"ytsearch:{query}", download=False)
        if results and results['entries']:
            info = results['entries'][0]
            return info['url'], info['title']
        return None, None

async def play_next(ctx):
    """Play next song in queue."""
    if song_queue:
        url, title = song_queue.pop(0)
        source = discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS)
        source = discord.PCMVolumeTransformer(source, volume=0.5) 
        ctx.voice_client.play(source, after=lambda e: bot.loop.create_task(play_next(ctx)))

@bot.slash_command(description="Play a song from YouTube")
async def play(ctx, query: str):
    voice = ctx.author.voice
    if not voice:
        await ctx.respond("You must be in a voice channel to use this command.")
        return

    await ctx.defer()

    if not ctx.voice_client:
        await voice.channel.connect()

    url, title = search_youtube(query)
    if not url:
        await ctx.followup.send("No results found on YouTube.")
        return

    song_queue.append((url, title))

    if not ctx.voice_client.is_playing():
        await play_next(ctx)
        await ctx.followup.send(f"🎵 **Now playing:** {title}")
    else:
        await ctx.followup.send(f"✅ **Queued:** {title}")

@bot.slash_command(description="Shows the current queue")
async def queue(ctx):
    if song_queue:
        qlist = "\n".join(f"{idx+1}. {song[1]}" for idx, song in enumerate(song_queue))
        await ctx.respond(f"🎼 **Queue:**\n{qlist}")
    else:
        await ctx.respond("The queue is empty.")

@bot.slash_command(description="Adjust playback volume (0-100)")
async def volume(ctx, volume: int):
    if ctx.voice_client and ctx.voice_client.source:
        if isinstance(ctx.voice_client.source, discord.PCMVolumeTransformer):
            ctx.voice_client.source.volume = volume / 100
            await ctx.respond(f"🔊 Volume set to {volume}%")
        else:
            await ctx.respond("Unable to adjust volume (not a PCMVolumeTransformer).")
    else:
        await ctx.respond("Nothing is playing currently.")

@bot.slash_command(description="Disconnect the bot")
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.respond("Disconnected.")
    else:
        await ctx.respond("I'm not connected to any voice channel.")

@bot.slash_command(description="Show available commands")
async def h(ctx):
    await ctx.respond("""
🎵 **Music Bot Commands**
- `/play [song]`: Play a song from YouTube.
- `/queue`: View song queue.
- `/volume [0-100]`: Adjust volume.
- `/leave`: Disconnect bot.
""")

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

bot.run(TOKEN)
