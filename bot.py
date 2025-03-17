# Copyright (c) 2025 V H#5111
# THE BOT WAS CODED BY V H#5111. CREATED FOR DEVELOPERS CAFE.
# USING WITHOUT CREDITS PROHIBITED.

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import discord
import os
import shutil
import aiohttp
import zipfile
import asyncio
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN_HERE_LOL_BOT_MADE_BY_VH5111"  # Replace with your bot token
PASSWORD = "vhop5111lol"

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
intents.dm_messages = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"V H GITUNZIPER BOT LOGIN AS {bot.user}")

@bot.command()
async def gitunzip(ctx):
    """Handles the GitHub unzip process"""
    await ctx.send("**Welcome To V H GITUNZIPER BOT!**\nPlease enter the password to continue")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        # Wait for password input
        msg = await bot.wait_for("message", check=check, timeout=30)
        await msg.delete()  # Delete password message immediately

        if msg.content != PASSWORD:
            await ctx.send("<:wrong_dcafe_lol:943390694360358932> **Wrong password! Try again**")
            return

        # Request GitHub link
        await ctx.send("<a:DCAFE_TICK:926098787397697616> **Acess Granted!** Now send a valid GitHub repository link (e.g., `https://github.com/VH5111/VTD-V-H-TEXTDRAW-CREATOR-DISCORD-BOT-`)")

        # Wait for GitHub link input
        msg = await bot.wait_for("message", check=check, timeout=60)
        github_url = msg.content.strip()
        await msg.delete()  # Delete GitHub link message immediately

        # Validate GitHub URL
        if not github_url.startswith("https://github.com/") or "/archive/" in github_url:
            await ctx.send("<:wrong_dcafe_lol:943390694360358932> **Invalid GitHub link!** Please provide a proper repository link.")
            return

        # Convert to ZIP download link
        repo_name = github_url.rstrip("/").split("/")[-1]
        zip_url = f"{github_url}/archive/refs/heads/main.zip"

        await ctx.send("<a:LOADING_3:926098041637863484> **Downloading & Unzipping... Please wait**\n ```AFTER SAVING FILES THE BOT SENDS THE EXTRACTED FILES SAFELY TO YOUR DMS!```             <:VH_OP:935801670368129075>\n __BOT MADE BY V H#5111__ | <a:FUNNY_MEME_DCAFE:926098260945412136> [JOIN DCAFE FOR SUPPORT](https://dsc.gg/dcafe)<a:FUNNY_MEME_DCAFE:926098260945412136> ")

        # Download the ZIP file
        zip_path = f"{repo_name}.zip"
        extract_folder = f"temp_{ctx.author.id}"

        async with aiohttp.ClientSession() as session:
            async with session.get(zip_url) as response:
                if response.status != 200:
                    await ctx.send("<:wrong_dcafe_lol:943390694360358932> **Failed to download the repository!** Make sure the repo exists and is public.")
                    return

                with open(zip_path, "wb") as f:
                    f.write(await response.read())

        # Extract ZIP file
        if os.path.exists(extract_folder):
            shutil.rmtree(extract_folder)  # Remove old temp files

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_folder)

        # Send files to user's DM
        user = ctx.author
        try:
            await user.send("<a:DCAFE_TICK:926098787397697616> **Repository Unzipped! Sending files...**")

            for root, _, files in os.walk(extract_folder):
                for file in files:
                    file_path = os.path.join(root, file)

                    if os.path.getsize(file_path) > 8 * 1024 * 1024:  # Discord max file size per message
                        await user.send(f"<a:dcafe_caution:1351268304102232196> **Skipping large file:** __{file}__\n NOTE :- DISCORD BOTS CAN'T SEND LARGE FILES THAT'S WHY **V H GITUNZIPER SKIPPED** __{file}__")
                        continue

                    with open(file_path, "rb") as f:
                        await user.send(file=discord.File(f))

            await user.send("<a:DCAFE_TICK:926098787397697616> **Thank you for using V H GITUNZIPER!**\n<:lock_dcafe:943440007740416020> **Connection Closed**")

        except discord.Forbidden:
            await ctx.send("<:wrong_dcafe_lol:943390694360358932> **I couldn't send you a DM! Please enable DMs and try again**")

        # Cleanup
        os.remove(zip_path)
        shutil.rmtree(extract_folder)

    except asyncio.TimeoutError:
        await ctx.send("<:wrong_dcafe_lol:943390694360358932> **Time expired! Please restart the process using `$gitunzip`**")

bot.run(TOKEN)

# Copyright (c) 2025 V H#5111
# THE BOT WAS CODED BY V H#5111. CREATED FOR DEVELOPERS CAFE.
# USING WITHOUT CREDITS PROHIBITED.

# MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
