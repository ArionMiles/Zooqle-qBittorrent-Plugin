#VERSION: 1.10
#AUTHOR: Arion_Miles (https://github.com/ArionMiles/)
#LICENSE: MIT License
from xml.dom import minidom
from novaprinter import prettyPrinter
from helpers import download_file 
from io import StringIO
import gzip

try:
    from urllib2 import urlopen, Request, URLError
except ImportError:
    from urllib.request import urlopen, Request, URLError
    
def retrieve_url_gzip(url):
    """ Return the content of the url page as a string """
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:38.0) Gecko/20100101 Firefox/38.0'}
    req = Request(url, headers = headers)
    try:
        response = urlopen(req)
    except URLError as errno:
        print(" ".join(("Connection error:", str(errno.reason))))
        print(" ".join(("URL:", url)))
        return ""
    dat = response.read()
    # Check if it is gzipped
    if dat[:2] == '\037\213':
        # Data is gzip encoded, decode it
        compressedstream = StringIO(dat)
        gzipper = gzip.GzipFile(fileobj=compressedstream)
        extracted_data = gzipper.read()
        dat = extracted_data
        return dat
    return dat #new line

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
        """ Performs search """
        page = 1
        while page < 11:
            query = "".join((self.url, "/search?q=", what, "+category%3A", self.supported_categories[cat], "&fmt=rss"))
            if( page>1 ):
                query = query + "&pg=" + str (page)
            response = retrieve_url_gzip(query)
            xmldoc = minidom.parseString(response)
            itemlist = xmldoc.getElementsByTagName('item')
            if( len(itemlist ) ==0):
                return
            for item in itemlist:
                zooqle_dict = zooqle_dict = {"engine_url" : self.url}
                size = item.getElementsByTagName('enclosure')[0].attributes['length'].childNodes[0].data
                zooqle_dict['name'] = item.getElementsByTagName('title')[0].childNodes[0].data
                if(size=="0"):
                    zooqle_dict["link"] = item.getElementsByTagName('torrent:magnetURI')[0].childNodes[0].data
                else:
                    zooqle_dict["link"] = item.getElementsByTagName('enclosure')[0].attributes['url'].value  
                
                
                zooqle_dict["desc_link"] = item.getElementsByTagName('link')[0].childNodes[0].data
                zooqle_dict["size"] = size
                
                zooqle_dict["leech"] = item.getElementsByTagName('torrent:peers')[0].childNodes[0].data
                if not zooqle_dict["leech"].isdigit():
                    zooqle_dict["leech"] = ''
                zooqle_dict["seeds"] = item.getElementsByTagName('torrent:seeds')[0].childNodes[0].data
                if not zooqle_dict["seeds"].isdigit():
                    zooqle_dict["seeds"] = ''
                prettyPrinter(zooqle_dict)
            totalResultVal  = xmldoc.getElementsByTagName('opensearch:totalResults')[0].childNodes[0].nodeValue
            startIndex  = xmldoc.getElementsByTagName('opensearch:startIndex')[0].childNodes[0].nodeValue
            itemsPerPage = xmldoc.getElementsByTagName('opensearch:itemsPerPage')[0].childNodes[0].nodeValue
            if( ( int(startIndex)  + int(itemsPerPage) > int( totalResultVal ))):
                return
            page += 1
        return
