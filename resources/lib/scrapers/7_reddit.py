import time
import urllib2
import simplejson as json 
import xbmc
import re
from scraper import ScraperPlugin


class Scraper(ScraperPlugin):

    _title = 'Reddit'

    def _get_albums(self):
        self.albums = []
        self.albums.append({'title': "hot",
                            'album_id': 1,
                            'pic': "http://blogs-images.forbes.com/gregvoakes/files/2012/06/reddit-logo.jpeg",
                            'description': "HOT",
                            'album_url': "http://www.reddit.com/.json?feed=b37a5c83510ebd741dd3b290939af9a2a7aa45cc&user=Vrokolos"})
        self.albums.append({'title': "week",
                            'album_id': 1,
                            'pic': "http://blogs-images.forbes.com/gregvoakes/files/2012/06/reddit-logo.jpeg",
                            'description': "HOT",
                            'album_url': "http://www.reddit.com/top/.json?sort=top&t=week&feed=b37a5c83510ebd741dd3b290939af9a2a7aa45cc&user=Vrokolos"})
        self.albums.append({'title': "month",
                            'album_id': 1,
                            'pic': "http://blogs-images.forbes.com/gregvoakes/files/2012/06/reddit-logo.jpeg",
                            'description': "HOT",
                            'album_url': "http://www.reddit.com/top/.json?sort=top&t=month&feed=b37a5c83510ebd741dd3b290939af9a2a7aa45cc&user=Vrokolos"})
        self.albums.append({'title': "year",
                            'album_id': 1,
                            'pic': "http://blogs-images.forbes.com/gregvoakes/files/2012/06/reddit-logo.jpeg",
                            'description': "HOT",
                            'album_url': "http://www.reddit.com/top/.json?sort=top&t=year&feed=b37a5c83510ebd741dd3b290939af9a2a7aa45cc&user=Vrokolos"})
        self.albums.append({'title': "all",
                            'album_id': 1,
                            'pic': "http://blogs-images.forbes.com/gregvoakes/files/2012/06/reddit-logo.jpeg",
                            'description': "HOT",
                            'album_url': "http://www.reddit.com/top/.json?sort=top&t=all&feed=b37a5c83510ebd741dd3b290939af9a2a7aa45cc&user=Vrokolos"})
        return self.albums

    def _get_photos(self, album_url):
        self.photos = []
        realalbumurl = album_url
        for x in range(0, 3):
            try:
                photos2, album_url = self.__get_photo_page(album_url, realalbumurl)
                self.photos.extend(photos2)
                time.sleep(1)
            except: 
                photos2, album_url = self.__get_photo_page(album_url, realalbumurl)
                self.photos.extend(photos2)
                time.sleep(1)
        return self.photos 

    def __get_photo_page(self, album_url, realalbumurl):
        page_photos = []
        next_page_url = None
        response = urllib2.urlopen(album_url).read()
        album_title = album_url
        photos1 = json.loads(response)
        for photo in photos1['data']['children']:
            link = photo['data']['url']
            if link.endswith('.jpg') or link.endswith('.png'):
                description = ''
                d = photo['data']['title']
                title = d.encode('ascii', 'ignore')
                page_photos.append({'title': title,
                                    'album_title': album_title,
                                    'photo_id': link,
                                    'pic': link,
                                    'description': description,
                                    'album_url': album_url})
        if 'after' in photos1['data']:
            s = photos1['data']['after']
            next_page_url = realalbumurl + '&after=' + s
        return page_photos, next_page_url 

def register(id):
    return Scraper(id)
