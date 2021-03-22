# Peanut Butter documentation

The main goal of the project is to make a bot that is fun to play around with.

#### Commands

* checks if a member is cool
  * use `#cool "discord_username"` (not server nickname)
* run Wikipedia searches
  * use `#wiki "keyword/topic"`
* clear to clean the discord chat of unwanted chats
  * use `#clear value` where `value` is number of chats to clear. Default is 10

#### Use of Commands with Examples

Use the `#` character before calling a command phrase to signify to the bot a command is being called.

* `#cool` will call the cool command where `cool` will not.

When using a string (word/phrase) argument, if the string contains a space in between, surrond the string with `""` characters to include the entire string.

* `#cool "Peanut Butter"` will check `Peanut Butter` where `#cool Peanut Butter` will check `Peanut`

Single string arguments do not need to be surrounded in quotes

* `#cool phrase` is acceptable.
