HELP_1 = """<b><u>Admin Commands :</b></u>

Just add <b>c</b> in the starting of the commands to use them for channel.


/pause : Pause the current playing stream.

/resume : Resume the paused stream.

/skip : Skip the current playing stream and start streaming the next track in queue.

/end or /stop : Clears the queue and end the current playing stream.

/player : Get an interactive player panel.

/queue : Shows the queued tracks list.
"""

HELP_2 = """
<b><u>Auth Users :</b></u>

Auth users can use admin rights in the bot without admin rights in the chat.

/auth [username/user_id] : Add a user to auth list of the bot.
/unauth [username/user_id] : Remove an auth user from the auth users list.
/authusers : Shows the list of auth users of the group.
"""

HELP_3 = """
<u><b>Broadcast Feature</b></u> [Only for Sudoers] :

/broadcast [message or reply to a message] : Broadcast a message to served chats of the bot.

<u>Broadcasting Modes :</u>
<b>-pin</b> : Pins your broadcasted messages in served chats.
<b>-pinloud</b> : Pins your broadcasted message in served chats and send notification to the members.
<b>-user</b> : Broadcasts the message to the users who have started your bot.
<b>-assistant</b> : Broadcast your message from the assistant account of the bot.
<b>-nobot</b> : Forces the bot to not broadcast the message.

<b>Example:</b> <code>/broadcast -user -assistant -pin Testing broadcast</code>
"""

HELP_4 = """<u><b>Chat Blacklist Feature :</b></u> [Only for Sudoers]

Restrict undesired chats from using our bot.

/blacklistchat [chat id] : Blacklist a chat from using the bot.
/whitelistchat [chat id] : Whitelist the blacklisted chat.
/blacklistedchat : Shows the list of blacklisted chats.
"""

HELP_5 = """
<u><b>Block Users:</b></u> [Only for Sudoers]

Starts ignoring the blacklisted user, so that they can't use bot commands.

/block [username or reply to a user] : Block the user from our bot.
/unblock [username or reply to a user] : Unblocks the blocked user.
/blockedusers : Shows the list of blocked users.
"""

HELP_6 = """
<u><b>Channel Play Commands:</b></u>

You can stream audio/video in channel.

/cplay : Starts streaming the requested audio track on channel's videochat.
/cvplay : Starts streaming the requested video track on channel's videochat.
/cplayforce or /cvplayforce : Stops the ongoing stream and starts streaming the requested track.

/channelplay [chat username or id] or [disable] : Connect channel to a group and starts streaming tracks by the help of commands sent in group.
"""

HELP_7 = """
<u><b>Global Ban Feature</b></u> [Only for Sudoers] :

/gban [username or reply to a user] : Globally bans the user from all the served chats and blacklist them from using the bot.
/ungban [username or reply to a user] : Globally unbans the globally banned user.
/gbannedusers : Shows the list of globally banned users.
"""

HELP_8 = """
<b><u>Loop Stream :</b></u>

<b>Starts streaming the ongoing stream in loop</b>

/loop [enable/disable] : Enables/disables loop for the ongoing stream
/loop [1, 2, 3, ...] : Enables the loop for the given value.
"""

HELP_9 = """
<u><b>Maintenance Mode</b></u> [Only for Sudoers] :

/logs : Get logs of the bot.

/logger [enable/disable] : Bot will start logging the activities happen on bot.

/maintenance [enable/disable] : Enable or disable the maintenance mode of your bot.
"""

HELP_10 = """
<b><u>Ping & Stats :</b></u>

/start : Starts the music bot.
/help : Get help menu with explanation of commands.

/ping : Shows the ping and system stats of the bot.

/stats : Shows the overall stats of the bot.
"""

HELP_11 = """
<u><b>Play Commands :</b></u>

<b>v :</b> Stands for video play.
<b>force :</b> Stands for force play.

/play or /vplay : Starts streaming the requested track on videochat.

/playforce or /vplayforce : Stops the ongoing stream and starts streaming the requested track.
"""

HELP_12 = """
<b><u>Shuffle Queue :</b></u>

/shuffle : Shuffle's the queue.
/queue : Shows the shuffled queue.
"""

HELP_13 = """
<b><u>Seek Stream :</b></u>

/seek [duration in seconds] : Seek the stream to the given duration.
/seekback [duration in seconds] : Backward seek the stream to the given duration.
"""

HELP_14 = """
<b><u>Song Download</b></u>

/song [song name/YT url] : Download any track from YouTube in MP3 or MP4 formats.
"""

HELP_15 = """
<b><u>Speed Commands :</b></u>

You can control the playback speed of the ongoing stream. [Admins Only]

/speed or /playback : For adjusting the audio playback speed in group.
/cspeed or /cplayback : For adjusting the audio playback speed in channel.
"""

HELP_16 = """
<b><u>Mass Action Commands :</b></u>

Note : Mass action can only be used by group owner.

/banall : Ban all group members. (Only group owner execute cmd)
/unbanall : Unban all banned group members. (Only group owner execute cmd)
/muteall : Mute all group members. (Only group owner execute cmd)
/unmuteall : Unmute all muted group members. (Only group owner execute cmd)
/kickall : Kick all group members. (Only group owner execute cmd)
/unpinall : Unpin all pinned messages in group. (Only group owner execute cmd)
"""

HELP_17 = """
<b><u>Owners :</b></u>

/leaveall1 - for assis 1
/leaveall2 - for assis 2
/leaveall3 - for assis 3
/leaveall4 - for assis 4
/leaveall5 - for assis 5
"""
