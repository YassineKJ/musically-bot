import discord
from discord.ext import commands
import music
import youtube_dl
import urllib.request
import urllib.parse
import re

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())


class music(commands.Cog):
  wait_list = []
  query = ""

  def __init__(self, client):
    self.client = client

  @commands.command(name="join")
  async def join(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("You're not in the voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      ctx.voice_client.move_to(voice_channel)

  @commands.command()
  async def disconnect(self, ctx):
    await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self, ctx, *request):
    for i in range(len(request)):
      self.query = self.query + request[i] + " "
    self.wait_list.append(self.query)
    print(self.wait_list)
    self.query = ""
    try:
      self.play_next(ctx)
    except:
      pass

  def play_next(self, ctx):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                      'options': '-vn'}
    YDL_OPTIONS = {'format': "bestaudio"}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      try:
        data = urllib.parse.urlencode({'search_query': self.wait_list[0]})
        with urllib.request.urlopen("http://www.youtube.com/results?" + data) as f:
          search_results = re.findall(r'/watch\?v=(.{11})', f.read().decode())
          url = 'http://www.youtube.com/watch?v=' + search_results[0]
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
        vc.play(source, after=lambda e: self.play_next(ctx))
        if len(self.wait_list) > 0:
          self.wait_list.pop(0)
          print(self.wait_list)
      except:
        pass

  @commands.command()
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused")

  @commands.command()
  async def resume(self, ctx):
    await ctx.voice_client.resume()
    await ctx.send("Resumed")

  @commands.command()
  async def skip(self, ctx):
    try:
      ctx.voice_client.stop()
      if len(self.wait_list) > 0:
        self.play_next(ctx)

    except:
      pass


#def setup(client):
  #client.add_cog(music(client))

#cogs = [music]
#for i in range(len(cogs)):
  #cogs[i].setup(client)


client.add_cog(music(client))

client.run("OTkyNDkxNDkxMTY1NDg3MTY0.GiJESI._rK-JpOSW4uCQM-7tM9u2c5-v7e-_wmtsdFo7c")