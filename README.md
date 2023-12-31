# clicord
<br>

<h1>WARNING</h1><br>
CLICORD IS TO BE USED AT YOUR OWN RISK. USING CLICORD BREAKS DISCORD'S TOS. IT IS PURELY FOR EXPERIMENTAL USE, NOT MALICIOUS USE!<br>
Clicord is made for use on linux systems, and will most probably not work on windows systems without the use of WSL. <br>

<h1>Requirements</h1> <br>

Clicord requires `aioconsole` and  `discord.py`<br>
Install these via `pip3 install aioconsole discord` <br>

<h1>Usage</h1>

Paste your discord bot token into the `token.txt` file. Then just run `main.py` and follow the instructions.<br>
You can send and receive messages through clicord, as well as using the builtin commands for other purposes. <br>

<h1>Commands</h1>

Clicord has commands that can be used by beginning a normal message with the defined prefix. The default prefix is `..` and can be changed in the `main.py` file. Just change the `PREFIX` variable to any other string. <br>
Commands will not be sent to the channel you are in.<br>
You can easily change between guilds and channels with the use of `..cc`. This command will bring up a prompt to select your guild, by number and then the channel, by number.
![image](https://github.com/Polarzz/clicord/assets/57324714/28114780-bc43-42be-95fd-606f9653b416)


<br>

<h1>Notes</h1>

`Util().cin()`, which is used to evaluate user input, always needs to return a list in the format `[bool, [guildObject, channelObject]` where `guildObject` and `channelObject` are both inputs to `Util().cin()`  or different guild/channel objects, and the `bool` represents whether or not the user is in a valid channel, if `False` they will be prompted to join a different channel, if `True` nothing will happen.
