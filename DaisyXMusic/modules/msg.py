# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**I  I am advance music play bot in telegram voice chat 🎃                                             I can play music in voice chats of Telegeam Groups & Channels.                                                            I have a lot of cool feature that will amaze you!                                                                       To add in your group contact me at @sl_bot_zone .                                                   Hit  /help  list of available commands.."
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

⭕️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⭕️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Setting up**

1️⃣ Make bot admin (Group and in channel if use cplay)
2️⃣ Start a voice chat
3️⃣ Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1️⃣ Make me admin of your channel 
2️⃣ Send /userbotjoinchannel in linked group
3️⃣ Now send commands in linked group

**Commands**

**📛 Common Commands ♻️**

🏷 /play: Play the requestd song
🏷 /play [yt url] : Play the given yt url
🏷 /play [reply yo audio]: Play replied audio
🏷 /dplay: Play song via deezer
🏷 /splay: Play song via jio saavn
🏷 /ytplay: Directly play song via Youtube Music
🏷 /current - Show now playing
🏷 /song  - download songs you want quickly
🏷 /search  - search videos on youtube with details
🏷 /deezer  - download songs you want quickly via deezer
🏷 /saavn  - download songs you want quickly via saavn
🏷 /video  - download videos you want quickly


**📛 Group Admin Commands 🔰**

🏷 /player: Open Settings menu of player
🏷/skip: Skips the current track
🏷 /pause: Pause track
🏷 /resume: Resumes the paused track
🏷 /end: Stops media playback
🏷 /current: Shows the current Playing track
🏷 /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**=>> Channel Music Play 🛠**

⭕️  For linked group admins only:

- /cplay [song name] - play song you requested
- /cdplay [song name] - play song you requested via deezer
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⭕️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
