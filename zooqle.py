# VERSION: 1.00
# AUTHOR: Arion_Miles (https://github.com/ArionMiles/)
# LICENSE: MIT License
from xml.dom import minidom
from novaprinter import prettyPrinter
from helpers import download_file
user_agent = 'Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0'
headers    = {'User-Agent': user_agent}

import urllib2, StringIO, gzip
def retrieve_url(url):
    """ Return the content of the url page as a string """
    req = urllib2.Request(url, headers = headers)
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError as errno:
        print(" ".join(("Connection error:", str(errno.reason))))
        return ""
    dat = response.read()
    # Check if it is gzipped
    if dat[:2] == '\037\213':
        # Data is gzip encoded, decode it
        compressedstream = StringIO.StringIO(dat)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        extracted_data = gzipper.read()
        dat = extracted_data
    info = response.info()
    return dat

class zooqle(object):
    """ Search engine class """
    url = 'https://zooqle.com'
    name = 'Zooqle'
    supported_categories = {'all'       : 'all',
                            'movies'    : 'Movies',
                            'tv'        : 'TV',
                            'music'     : 'Music',
                            'games'     : 'Games',
                            'anime'     : 'Anime',
                            'software'  : 'Apps',
                            'books'     : 'Books',
                            'others'  : 'Other'}

    def download_torrent(self, info):
        """ Downloader """
        print(download_file(info))

    def search(self, what, cat="all"):
        """ Performs search"""
        query = "".join((self.url, "/search?q=", what, "+category%3A", self.supported_categories[cat], "&fmt=rss"))
        response = retrieve_url(query)

        xmldoc = minidom.parseString(response)
        itemlist = xmldoc.getElementsByTagName('item')
        for item in itemlist:
            zooqle_dict = zooqle_dict = {"engine_url" : self.url}
            zooqle_dict['name'] = item.getElementsByTagName('title')[0].childNodes[0].data
            zooqle_dict["link"] = item.getElementsByTagName('enclosure')[0].attributes['url'].value
            zooqle_dict["desc_link"] = item.getElementsByTagName('link')[0].childNodes[0].data
            zooqle_dict["size"] = item.getElementsByTagName('enclosure')[0].attributes['length'].childNodes[0].data
            zooqle_dict["leech"] = item.getElementsByTagName('torrent:peers')[0].childNodes[0].data
            if not zooqle_dict["leech"].isdigit():
                zooqle_dict["leech"] = ''
            zooqle_dict["seeds"] = item.getElementsByTagName('torrent:seeds')[0].childNodes[0].data
            if not zooqle_dict["seeds"].isdigit():
                zooqle_dict["seeds"] = ''

            prettyPrinter(zooqle_dict)

        return