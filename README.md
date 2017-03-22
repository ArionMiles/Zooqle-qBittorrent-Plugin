# Zooqle qBittorrent Plugin
Zooqle search plugin for qBittorrent
Uses `xml.mini.dom` to parse [Zooqle.com's](https://zooqle.com/) OpenSearch XML feeds and display the results. Draws inspiration from the [Extratorrent's](https://github.com/qbittorrent/qBittorrent/blob/master/src/searchengine/nova/engines/extratorrent.py) search plugin.
Follows the [search plugin guidlines](https://github.com/qbittorrent/qBittorrent/wiki/How-to-write-a-search-plugin) for writing qBittorrent Search Plugins.

# Installation
Install the plugin by:
<kbd>Search tab</kbd> 🡪 <kbd>Search Plugins</kbd> 🡪 <kbd>Install a new one</kbd> 🡪 Selecting the `zooqle.py` file.

Or by manually copying the `zooqle.py` to the following location:
  * Linux: `~/.local/share/data/qBittorrent/nova/engines/zooqle.py`
  * Mac: `~/Library/Application Support/qBittorrent/nova/engines/zooqle.py`
  * Windows: `C:\Documents and Settings\%USERPROFILE%\Local Settings\Application Data\qBittorrent\nova\engines\zooqle.py`

# License
MIT License. See LICENSE file.
