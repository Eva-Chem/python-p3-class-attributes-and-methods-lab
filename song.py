
class Song:
    # Class attributes shared by all Song instances
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every time a song is created:
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        """Add unique artists to the artists list"""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        """Add unique genres to the genres list"""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Count how many songs belong to each genre"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Count how many songs each artist has"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
