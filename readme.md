
BlockedServers/tracker
----------------------

Minecraft 1.9.3 Pre-Release 2 [introduced](https://www.reddit.com/r/Minecraft/comments/4h3c6u/mojang_is_blocking_certain_servers_as_of_193_r2) a [blacklisting mechanism](https://www.reddit.com/r/admincraft/comments/4h3d99/incoming_session_server_blacklist_193/) which allowed Mojang to block servers that violate the [Minecraft End User License Agreement](https://account.mojang.com/documents/minecraft_eula)

This mechanism [seems to be missing](https://www.reddit.com/r/Minecraft/comments/4hmlcb/minecraft_193_prerelease_3/d2qux1d) in Minecraft 1.9.3 Pre-Release 3

How does it work?
-------------------------

The Minecraft 1.9.3 Pre-Release 2 client would compare the sha1 of the current hostname, and the current hostname without subdomains to a [list](https://sessionserver.mojang.com/blockedservers) containing blocked servers.

More information
----------------

This repository is being updated every five minutes, and it attempts to utilize the dictionary in `support/dictionary` to determine which server(s) have been blocked by Mojang.

