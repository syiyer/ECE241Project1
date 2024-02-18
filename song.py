class Song:
    def __init__(self, artist_name: str, song_title: str, song_id: str, duration: float, year: int):
        self.artist_name = str(artist_name)
        self.song_title = str(song_title)
        self.song_id = str(song_id)
        self.duration = float(duration)
        self.year = int(year)
        pass

    def __str__(self):
        return "%s by %s (ID: %s) released in %s" % (self.song_title, self.artist_name, self.song_id, self.year)
        # return string of song with info

    def play(self):
        print("%s is playing, with a duration of %s second(s)" % (self.song_title, ("%.6f" % self.duration)))
        # print out title and duration of song which is playing
        pass
