from urllib2 import urlopen
import json
import os


class Movie:
    def __init__(self, title):
        self.title = title
        Movie.download_data(self)

    def download_data(self):
        url = "http://www.omdbapi.com/?t="+self.title
        response = urlopen(url)
        data = json.loads(response.read().decode("utf-8"))
        self.storyline = data['Plot']
        self.box_art = data['Poster']       
        image_path = self.title+".jpg"        
        if not(os.path.isfile(image_path)):
            box_art_response = urlopen(self.box_art)
            image_file = open(image_path, 'w')
            image_file.write(box_art_response.read())
            image_file.close()
