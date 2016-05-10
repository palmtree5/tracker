BlockedServers/tracker
----------------------

Mojang recently [introduced](https://www.reddit.com/r/Minecraft/comments/4h3c6u/mojang_is_blocking_certain_servers_as_of_193_r2) a [blacklisting mechanism](https://www.reddit.com/r/admincraft/comments/4h3d99/incoming_session_server_blacklist_193/) which allowed Mojang to block servers that violate the [Minecraft End User License Agreement](https://account.mojang.com/documents/minecraft_eula)

And then shortly after in 1.9.3 Pre-Release 3 [it went missing again](https://www.reddit.com/r/Minecraft/comments/4hmlcb/minecraft_193_prerelease_3/d2qux1d)

Only to be brought back later [inside a modified Netty dependency](https://gist.github.com/Chnkr/7f1503f5f4a05a6b432f4044ab3855ea#file-bootstrap-java)


How does it work?
-------------------------

See: [this decompiled version of their netty bootstrap.java](https://gist.github.com/Chnkr/7f1503f5f4a05a6b432f4044ab3855ea#file-bootstrap-java)

More information
----------------
This repository is being updated every five minutes, and it attempts to utilize the dictionary in `support/dictionary` to determine which server(s) have been blocked by Mojang.

**IF YOU HAPPEN TO RUN, OR KNOW PEOPLE THAT MANAGE TOPSITES PLEASE ASK THEM VERY POLITELY TO SHARE THEIR HOSTNAMES WITH ME SO I CAN ADD THEM TO OUR DICTIONARY!**
