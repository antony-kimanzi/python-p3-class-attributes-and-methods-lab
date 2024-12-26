class Song:

    count = 0
    genres= []
    artists =  []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1                                 

all_of_the_lights = Song("All of The Lights", "Kanye West", "HipHop")
print(f"\nSong: {all_of_the_lights.name}\n Artist: {all_of_the_lights.artist}\n Genre:  {all_of_the_lights.genre}\n")

over_my_dead_body = Song("Over My Dead Body", "Drake", "HipHop")
print(f"Song: {over_my_dead_body.name}\n Artist: {over_my_dead_body.artist}\n Genre:  {over_my_dead_body.genre}\n")

baby_its_you = Song("Baby Its You", "Jojo", "Pop")
print(f"Song: {baby_its_you.name}\n Artist: {baby_its_you.artist}\n Genre:  {baby_its_you.genre}\n")

print(f"Genres: {Song.genres}")
print(f"Artists: {Song.artists}")
print(f"Genre Count: {Song.genre_count}")
print(f"Artist Count: {Song.artist_count}")