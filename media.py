from urllib2 import urlopen
import json
import os
'''
Defines Movie object
Given a title and youtube url for its trailer,
downloads box art and summary using OMDB API
'''


class Movie:
    def __init__(self, title, trailer_youtube_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url
        Movie.download_data(self)

    def download_data(self):
        url = "http://www.omdbapi.com/?t="+self.title
        url = url.replace(" ", "%20")
        response = urlopen(url)
        data = json.loads(response.read().decode("utf-8"))
        self.storyline = data['Plot']
        self.box_art = data['Poster']
        image_path = self.title+".jpg"
        # Check if the image file has already been downloaded; if not, download
        if not(os.path.isfile(image_path)):
            box_art_response = urlopen(self.box_art)
            image_file = open(image_path, 'w')
            image_file.write(box_art_response.read())
            image_file.close()
        self.poster_image_url = image_path
