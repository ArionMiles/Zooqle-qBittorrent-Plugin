# Zooqle qBittorrent Plugin
Zooqle search plugin for qBittorrent
Uses `xml.mini.dom` to parse [Zooqle.com's](https://zooqle.com/) OpenSearch XML feeds and display the results. Draws inspiration from the [Extratorrent's](https://github.com/qbittorrent/qBittorrent/blob/master/src/searchengine/nova/engines/extratorrent.py) search plugin.
Follows the [search plugin guidlines](https://github.com/qbittorrent/qBittorrent/wiki/How-to-write-a-search-plugin) for writing qBittorrent Search Plugins.

Supports Python2 & Python3.

# Installation
Install the plugin by:
<kbd>Search tab</kbd> 🡪 <kbd>Search Plugins</kbd> 🡪 <kbd>Install a new one</kbd> 🡪 Selecting the `zooqle.py` file.

Or by manually copying the `zooqle.py` to the following location:
  * Linux: `~/.local/share/data/qBittorrent/nova/engines/`
  * Mac: `~/Library/Application Support/qBittorrent/nova/engines/`
  * Windows: `C:\Users\%USERPROFILE%\AppData\Local\qBittorrent\nova\engines\`

# Contributors
* [v1k45](https://github.com/v1k45)
* [dwilbanks](https://github.com/dwilbanks)
* [affaff](https://github.com/affaff)
* [Pireo](https://github.com/Pireo)

# License
MIT License. See LICENSE file.
