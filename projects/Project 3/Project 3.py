class Song:
    def __init__(self, title, album, artist, genre, year, rating):
        self.title = title
        self.album = album
        self.artist = artist
        self.genre = genre
        self.liked = False #Sets the default liked status to unliked(False) when the song is first created#
        self.year = year
        self.rating = rating

class Library: #Contains methods to add a song, like a song, change the rating of a song, and search for a song#
    def __init__(self):
        self.library_list = [] #List that contains all the Song objects#
    
    def add_song(self, song): #Adds the song object that is passed into the function to the list of all song objects library_list#
        self.library_list.append(song)
        return f"'{song.title}' added to library."
    
    def like_song(self, title_name):
        for song in self.library_list: #Iterates through all the songs in the library#
            if song.title == title_name and song.liked == False: #Likes the song if it exists in the library and hasn't been liked yet#
                song.liked = True
                return f"'{song.title}' has been liked."
            elif song.title == title_name and song.liked == True: #Notifies the user if the song has already been liked#
                return f"'{song.title}' has already been liked!"
        return f"'{title_name}' is not currently in the library." #Notifies the user if the song doesn't exist in their library#

    def change_rating(self, title_name, rating):
        for song in self.library_list: #Iterates through all the songs in the library#
            if song.title == title_name and song.rating != rating: #Updates the song rating to the new rating that the user chose if the song's current rating is different than the new rating#
                song.rating = rating
                return f"Rating for '{song.title}' has been updated to {song.rating}."
            elif song.title == title_name and song.rating == rating: #Notifies the user if the song's current rating is the same as the rating they want to change it to#
                return f"'{song.title}' already has the rating {rating}!"
        return f"'{title_name}' is not currently in the library." #Notifies the user if the song doesn't exist in their library#


    def title_search(self, user_choice):
        search_list = []
        [search_list.append(f"'{song.title}' by {song.artist}") for song in self.library_list if song.title == user_choice] #Adds songs to the list of songs if they match the user's search criteria#
        if len(search_list) > 0: #Returns the list of all the songs that match the user's search criteria#
            return ', '.join(search_list) #', '.join is used here to format the list into a string with commas between element in the list#
        else: #Notifies the user if there were no matches to their search criteria#
            return f"No songs with the title {user_choice} were found!"
        
    def album_search(self, user_choice):
        search_list = []
        [search_list.append(f"'{song.title}' by {song.artist}") for song in self.library_list if song.album == user_choice] #Adds songs to the list of songs if they match the user's search criteria#
        if len(search_list) > 0: #Returns the list of all the songs that match the user's search criteria#
            return ', '.join(search_list) #', '.join is used here to format the list into a string with commas between element in the list#
        else: #Notifies the user if there were no matches to their search criteria#
            return f"No songs from the album {user_choice} were found!"
    
    def artist_search(self, user_choice):
        search_list = []
        [search_list.append(f"'{song.title}' by {song.artist}") for song in self.library_list if song.artist == user_choice] #Adds songs to the list of songs if they match the user's search criteria#
        if len(search_list) > 0: #Returns the list of all the songs that match the user's search criteria#
            return ', '.join(search_list) #', '.join is used here to format the list into a string with commas between element in the list#
        else: #Notifies the user if there were no matches to their search criteria#
            return f"No songs by the artist {user_choice} were found!"
    
    def genre_search(self, user_choice):
        search_list = []
        [search_list.append(f"'{song.title}' by {song.artist}") for song in self.library_list if song.genre == user_choice] #Adds songs to the list of songs if they match the user's search criteria#
        if len(search_list) > 0: #Returns the list of all the songs that match the user's search criteria#
            return ', '.join(search_list) #', '.join is used here to format the list into a string with commas between element in the list#
        else: #Notifies the user if there were no matches to their search criteria#
            return f"No songs of the genre {user_choice} were found!"
    
    def year_search(self, user_choice):
        search_list = []
        [search_list.append(f"'{song.title}' by {song.artist}") for song in self.library_list if song.year == user_choice] #Adds songs to the list of songs if they match the user's search criteria#
        if len(search_list) > 0: #Returns the list of all the songs that match the user's search criteria#
            return ', '.join(search_list) #', '.join is used here to format the list into a string with commas between element in the list#
        else: #Notifies the user if there were no matches to their search criteria#
            return f"No songs from the year {user_choice} were found!"
    
    def rating_search(self, user_choice):
        search_list = []
        [search_list.append(f"'{song.title}' by {song.artist}") for song in self.library_list if song.rating == user_choice] #Adds songs to the list of songs if they match the user's search criteria#
        if len(search_list) > 0: #Returns the list of all the songs that match the user's search criteria#
            return ', '.join(search_list) #', '.join is used here to format the list into a string with commas between element in the list#
        else: #Notifies the user if there were no matches to their search criteria#
            return f"No songs with the rating {user_choice} were found!"


class Playlist: #Contains methods to add and remove songs from playlists#
    playlists = [] #Class variable list containing all created Playlist objects#

    def __init__(self, library, name): #Creates a new Playlist object w/ access to the library, and w/ variables for the playlist's name and the list of songs it contains#
        self.library = library
        self.name = name
        self.songs = []
        Playlist.playlists.append(self) #Adds playlist to the list of all playlists#

    def add_song_playlist(self, song_title):
        for s in self.library.library_list: #Goes through the library list to find the correct song from the library list#
            if s.title == song_title:
                self.songs.append(s) #Appends the correct song to the playlist's list of songs if it exists in the user's library#
                return f"Song '{s.title}' added to playlist '{self.name}'"
        return f"Song '{song_title}' is not in your library!" #Notifies the user if the song doesn't exist in their library#

    def remove_song_playlist(self, song_title):
        for s in self.library.library_list: #Goes through the library list to find the correct song from the library list#
            if s.title == song_title and s in self.songs:
                self.songs.remove(s) #Removes the correct song from the playlist's list of songs if it exists in the user's library and exists in the playlist#
                return f"Song '{s.title}' removed from playlist '{self.name}'"
            elif s.title == song_title and s not in self.songs: #Notifies the user if the song exists in their library, but hasn't been added to the playlist they are trying to remove it from#
                return f"Song '{song_title}' is not in the playlist '{self.name}'!"
        return f"Song '{song_title}' is not in your library!" #Notifies the user if the song doesn't exist in their library#
    
    def show_playlists():
        return ', '.join([p.name for p in Playlist.playlists]) #Returns a list of all the playlists the user has created, using ', '.join to format the list into a string with commas between element in the list##


class Queue: #Maintains a list of songs to be played. Allows songs to be queued and dequeued. Provides a method to play songs, printing them out in order until the queue is empty#
    queue = [] #Class list variable to keep a running list of all the Song objects that are in the queue#

    def add_song_queue(library, song_title):
        for s in library.library_list: #Goes through the library list to find the correct song from the library list#
            if s.title == song_title:
                Queue.queue.append(s) #Appends the correct song to the queue list#
                return f"'{song_title}' has been added to the queue."
        return f"Song '{song_title}' is not in your library!" #Notifies the user if the song doesn't exist in their library#

    def remove_song_queue(library, song_title):
        for s in library.library_list: #Goes through the library list to find the correct song from the library list#
            if s.title == song_title and s in Queue.queue: 
                Queue.queue.remove(s) #Removes the correct song from the queue's list of songs if it exists in the user's library and exists in the queue#
                return f"'{song_title}' has been removed from the queue."
            elif s.title == song_title and s not in Queue.queue: #Notifies the user if the song exists in their library, but hasn't been added to the queue#
                return f"Song '{song_title}' is not in the queue!"
        return f"Song '{song_title}' is not in your library!" #Notifies the user if the song doesn't exist in their library#

    def play_queue():
        return '\n'.join([f"Now playing '{song.title}' by {song.artist}" for song in Queue.queue]) #Returns a list of all the songs and their respective artists in the queue, using '\n'.join to print out each element in the list on a new line#
        

def user_input(library): #With the library object that was created at the start as the parameter, user_input asks the user what they want to do, then calls the appropriate function according to the user's choice of action, then recalls the function if they choose numbers 1-11 or input a number outside the range 1-12#
    print(f"\nPlease select an action:\n1. Add song to library\n2. Like a song\n3. Change a song rating\n4. Search for a song\n5. Create a Playlist\n6. Add a song to a playlist\n7. Remove a song from a playlist\n8. View all playlists\n9. Add a song to queue\n10. Remove song from queue\n11. Play queue\n12. Exit")
    action = int(input()) #Holds the user's choice of action#
    if action == 1: #Creates a new Song object and calls Library.add_song to store the new song in the user's library#
        print("Enter song title:")
        title = input()
        print("Enter song album:")
        album = input()
        print("Enter song artist:")
        artist = input()
        print("Enter song genre:")
        genre = input()
        print("Enter song year:")
        year = input()
        print("Enter song rating (1-5):")
        rating = input()
        print(library.add_song(Song(title, album, artist, genre, year, rating)))

        user_input(library)
    elif action == 2: #Calls Library.like_song w/ title of the song the user wants to like#
        print("Enter song title to like:")
        title_to_like = input()
        print(library.like_song(title_to_like)) #Calls like_song() function w/ title of the song the user wants to like#

        user_input(library)
    elif action == 3: #Calls Library.change_rating w/ title of the song the user wants to change the rating of and the new rating#
        print("Enter song title:")
        title_change_rating = input()
        print("Enter new rating (1-5):")
        new_rating = input()
        print(library.change_rating(title_change_rating, new_rating))

        user_input(library)
    elif action == 4: #Asks user what kind of search they want to conduct, then calls the correct search function with their chosen search querry as the argument#
        print("Search by (title/album/artist/genre/year/rating):")
        search_type = input()
        print(f"Enter {search_type}:")
        search_input = input()

        if search_type == "title":
            print(library.title_search(search_input))
        elif search_type == "album":
            print(library.album_search(search_input))
        elif search_type == "artist":
            print(library.artist_search(search_input))
        elif search_type == "genre":
            print(library.genre_search(search_input))
        elif search_type == "year":
            print(library.year_search(search_input))
        elif search_type == "rating":
            print(library.rating_search(search_input))
        else:
            print("Please enter a valid search criteria.") #notifies user if they don't choose one of the 6 available 'search by' options#

        user_input(library)
    elif action == 5: #Creates a new Playlist object with the name the user chooses#
        print("Enter name for the new playlist:")
        new_playlist = input()
        Playlist(library, new_playlist)
        print(f"Playlist '{new_playlist}' has been created.")

        user_input(library)
    elif action == 6: #Adds the song that the user chooses to the playlist that the user chooses#
        print("Enter song title:")
        title = input()
        print("Enter playlist name:")
        playlist = input()
        for p in Playlist.playlists: #Finds the correct playlist, makes sure it exists#
            if p.name == playlist:
                print(f"{p.add_song_playlist(title)}") #calls the add_song_playlist function w/ the correct Playlist object#
        
        user_input(library)
    elif action == 7: #Removes the song that the user chooses from the playlist that the user chooses#
        print("Enter song title:")
        title = input()
        print("Enter playlist name:")
        playlist = input()
        for p in Playlist.playlists: #Finds the correct playlist, makes sure it exists#
            if p.name == playlist:
                print(f"{p.remove_song_playlist(title)}") #calls the remove_song_playlist function w/ the correct Playlist object#

        user_input(library)
    elif action == 8: #Calls show_playlist to print the list of all the user-created playlists#
        print("Available playlists:")
        print(Playlist.show_playlists())

        user_input(library)
    elif action == 9: #Calls add_song_queue w/ the song the user wants to add to the queue#
        print("Enter song title:")
        title = input()
        print(Queue.add_song_queue(library, title))

        user_input(library)
    elif action == 10: #Calls remove_song_queue w/ the song the user wants to remove from the queue#
        print("Enter song title:")
        title = input()
        print(Queue.remove_song_queue(library, title))

        user_input(library)
    elif action == 11: #Calls play_queue to print the list of all songs in the queue#
        print(Queue.play_queue())

        user_input(library)
    elif action == 12:
        print("Thank you for using the music library. Goodbye!") #Exits the user out of the music library#
    else:
        print("Please select a number 1-10.") #Notifies the user with the correct way to select an action, recalls the user_input method#
        user_input(library)

import unittest
class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        #Creates 7 Song objects#
        self.song1 = Song("Around the World", "Homework", "Daft Punk", "electronic", "1997", "4")
        self.song2 = Song("One More Time", "Discovery", "Daft Punk", "electronic", "2001", "5")
        self.song3 = Song("Africa", "Toto IV", "TOTO", "soft rock", "1982", "5")
        self.song4 = Song("Eye of the Tiger", "Eye Of The Tiger", "Survivor", "rock", "1982", "3")
        self.song5 = Song("Clay", "U Want The Scoop?", "The Garden", "alternative", "2017", "4")
        self.song6 = Song("Have A Good Day Sir", "U Want The Scoop?", "The Garden", "alternative", "2017", "5")
        self.song7 = Song("Birdhouse in Your Soul", "Flood", "They Might Be Giants", "indie", "1990", "4")
        #Adds the 7 new Song objects to the library list#
        self.library.add_song(self.song1)
        self.library.add_song(self.song2)
        self.library.add_song(self.song3)
        self.library.add_song(self.song4)
        self.library.add_song(self.song5)
        self.library.add_song(self.song6)
        self.library.add_song(self.song7)

    def test_add_song(self):
        #Checks that the songs have been appended to the library list#
        self.assertIn(self.song1, self.library.library_list)
        self.assertIn(self.song2, self.library.library_list)
        self.assertIn(self.song3, self.library.library_list)
        self.assertIn(self.song4, self.library.library_list)
        self.assertIn(self.song5, self.library.library_list)
        self.assertIn(self.song6, self.library.library_list)
        self.assertIn(self.song7, self.library.library_list)

    def test_like_song(self):
        #Checks that the song is unliked by default#
        self.assertFalse(self.song1.liked)
        self.assertFalse(self.song2.liked)
        #Checks the like_song function, making sure that is sets liked equal to True#
        self.library.like_song("Around the World")
        self.assertTrue(self.song1.liked)
        self.library.like_song("One More Time")
        self.assertTrue(self.song2.liked)
        #Checks that like_song notifies the user if the song has already been liked#
        self.assertEqual(self.library.like_song("Around the World"), "'Around the World' has already been liked!")
        #Checks that like_song notifies the user if the song they are trying to like does not exist in their library#
        self.assertEqual(self.library.like_song("Crocodile Rock"), "'Crocodile Rock' is not currently in the library.")

    def test_change_rating(self):
        #Checks that the change_rating notifies the user that the rating has been changed#
        self.assertEqual(self.library.change_rating("Africa","4"),"Rating for 'Africa' has been updated to 4.")
        self.assertEqual(self.library.change_rating("Eye of the Tiger","2"),"Rating for 'Eye of the Tiger' has been updated to 2.")
        #Checks that the song's rating variable gets updated to the new rating#
        self.assertEqual(self.song3.rating, "4")
        self.assertEqual(self.song4.rating, "2")
        #Checks that change_rating notifies the user if they try to change the rating to the same exact rating it was before#
        self.assertEqual(self.library.change_rating("Eye of the Tiger","2"), "'Eye of the Tiger' already has the rating 2!")
        #Checks that change_rating notifies the user if they are trying to change the rating of a song that does not exist in their library#
        self.assertEqual(self.library.change_rating("Crocodile Rock","5"), "'Crocodile Rock' is not currently in the library.")
        
    def test_search_methods(self):
        #Title#
        #Checks that title_search returns a list of songs with the same title as the user's choice#
        self.assertEqual(self.library.title_search("Clay"), "'Clay' by The Garden")
        #Checks that title_search notifies the user if there are no results for the user's search#
        self.assertEqual(self.library.title_search("Crocodile Rock"), "No songs with the title Crocodile Rock were found!")

        #Album#
        #Checks that album_search returns a list of songs with the same album as the user's choice#
        self.assertEqual(self.library.album_search("U Want The Scoop?"), "'Clay' by The Garden, 'Have A Good Day Sir' by The Garden")
        #Checks that album_search notifies the user if there are no results for the user's search#
        self.assertEqual(self.library.album_search("IGOR"), "No songs from the album IGOR were found!")

        #Artist#
        #Checks that artist_search returns a list of songs with the same artist as the user's choice#
        self.assertEqual(self.library.artist_search("Daft Punk"), "'Around the World' by Daft Punk, 'One More Time' by Daft Punk")
        #Checks that artist_search notifies the user if there are no results for the user's search#
        self.assertEqual(self.library.artist_search("Elton John"), "No songs by the artist Elton John were found!")

        #Genre#
        #Checks that genre_search returns a list of songs with the same genre as the user's choice#
        self.assertEqual(self.library.genre_search("alternative"), "'Clay' by The Garden, 'Have A Good Day Sir' by The Garden")
        #Checks that genre_search notifies the user if there are no results for the user's search#
        self.assertEqual(self.library.genre_search("goth"), "No songs of the genre goth were found!")

        #Year#
        #Checks that year_search returns a list of songs with the same year as the user's choice#
        self.assertEqual(self.library.year_search("1982"), "'Africa' by TOTO, 'Eye of the Tiger' by Survivor")
        #Checks that year_search notifies the user if there are no results for the user's search#
        self.assertEqual(self.library.year_search("2002"), "No songs from the year 2002 were found!")

        #Rating#
        #Checks that rating_search returns a list of songs with the same rating as the user's choice#
        self.assertEqual(self.library.rating_search("4"), "'Around the World' by Daft Punk, 'Clay' by The Garden, 'Birdhouse in Your Soul' by They Might Be Giants")
        #Checks that rating_search notifies the user if there are no results for the user's search#
        self.assertEqual(self.library.rating_search("1"), "No songs with the rating 1 were found!")

    def test_playlist_methods(self):
        #Adds 2 new playlists to the list of playlists#
        self.playlist1 = Playlist(self.library, "Awesome")
        self.playlist2 = Playlist(self.library, "Cool")
        #Checks that the playlists have been added to the list playlists#
        self.assertIn(self.playlist1, Playlist.playlists)
        self.assertIn(self.playlist2, Playlist.playlists)
        #Checks that add_song_playlist returns a notification for the user that the correct song was added to the correct playlist#
        self.assertEqual(self.playlist1.add_song_playlist("Around the World"), "Song 'Around the World' added to playlist 'Awesome'")
        self.assertEqual(self.playlist1.add_song_playlist("Africa"), "Song 'Africa' added to playlist 'Awesome'")
        self.assertEqual(self.playlist1.add_song_playlist("Have A Good Day Sir"), "Song 'Have A Good Day Sir' added to playlist 'Awesome'")
        #Checks that add_song_playlist notifies the user when the song they are trying to add is not in their library#
        self.assertEqual(self.playlist1.add_song_playlist("Crocodile Rock"), "Song 'Crocodile Rock' is not in your library!")
        #Checks that the add_song_playlist method adds a user's chosen song to the playlist's list of songs#
        self.assertIn(self.song1, self.playlist1.songs)
        self.assertIn(self.song3, self.playlist1.songs)
        self.assertIn(self.song6, self.playlist1.songs)

        #Checks that remove_song_playlist returns a notification for the user that the correct song was removed from the correct playlist#
        self.assertEqual(self.playlist1.remove_song_playlist("Around the World"), "Song 'Around the World' removed from playlist 'Awesome'")
        self.assertEqual(self.playlist1.remove_song_playlist("Africa"), "Song 'Africa' removed from playlist 'Awesome'")
        self.assertEqual(self.playlist1.remove_song_playlist("Have A Good Day Sir"), "Song 'Have A Good Day Sir' removed from playlist 'Awesome'")
        #Checks that remove_song_playlist notifies the user when the song they are trying to remove is not in the playlist#
        self.assertEqual(self.playlist1.remove_song_playlist("Have A Good Day Sir"), "Song 'Have A Good Day Sir' is not in the playlist 'Awesome'!")
        self.assertEqual(self.playlist2.remove_song_playlist("Eye of the Tiger"), "Song 'Eye of the Tiger' is not in the playlist 'Cool'!")       
        #Checks that remove_song_playlist notifies the user when the song they are trying to remove is not in their library#
        self.assertEqual(self.playlist1.remove_song_playlist("Crocodile Rock"), "Song 'Crocodile Rock' is not in your library!")
        #Checks that the remove_song_playlist method adds a user's chosen song to the playlist's list of songs#
        self.assertNotIn(self.song1, self.playlist1.songs)
        self.assertNotIn(self.song3, self.playlist1.songs)
        self.assertNotIn(self.song6, self.playlist1.songs)

        #Checks that the Playlist show_playlist method returns a list of all created Playlist objects#
        self.assertEqual(Playlist.show_playlists(), "Awesome, Cool")

    def test_queue_methods(self):
        #Adds songs to the queue, checks that add_song_queue returns a notification for the user that the correct song was added to the queue#
        self.assertEqual(Queue.add_song_queue(self.library, "Eye of the Tiger"), "'Eye of the Tiger' has been added to the queue.")
        self.assertEqual(Queue.add_song_queue(self.library, "Clay"), "'Clay' has been added to the queue.")
        self.assertEqual(Queue.add_song_queue(self.library, "Birdhouse in Your Soul"), "'Birdhouse in Your Soul' has been added to the queue.")
        #Checks that add_song_queue notifies the user when the song they are trying to add is not in their library#
        self.assertEqual(Queue.add_song_queue(self.library, "Crocodile Rock"), "Song 'Crocodile Rock' is not in your library!")
        #Checks that the songs have been added to the queue list#
        self.assertIn(self.song4, Queue.queue)
        self.assertIn(self.song5, Queue.queue)
        self.assertIn(self.song7, Queue.queue)
        
        #Checks that the Queue play_queue method returns a list of all created Playlist objects#
        self.assertEqual(Queue.play_queue(), f"Now playing 'Eye of the Tiger' by Survivor\nNow playing 'Clay' by The Garden\nNow playing 'Birdhouse in Your Soul' by They Might Be Giants")

        #Removes songs from the queue, checks that remove_song_queue returns a notification for the user that the correct song was removed from the queue#
        self.assertEqual(Queue.remove_song_queue(self.library, "Eye of the Tiger"), "'Eye of the Tiger' has been removed from the queue.")
        self.assertEqual(Queue.remove_song_queue(self.library, "Clay"), "'Clay' has been removed from the queue.")
        self.assertEqual(Queue.remove_song_queue(self.library, "Birdhouse in Your Soul"), "'Birdhouse in Your Soul' has been removed from the queue.")
        #Checks that remove_song_queue notifies the user when the song they are trying to remove is not in the queue#
        self.assertEqual(Queue.remove_song_queue(self.library, "Have A Good Day Sir"), "Song 'Have A Good Day Sir' is not in the queue!")
        self.assertEqual(Queue.remove_song_queue(self.library, "Eye of the Tiger"), "Song 'Eye of the Tiger' is not in the queue!")       
        #Checks that remove_song_queue notifies the user when the song they are trying to remove is not in their library#
        self.assertEqual(Queue.remove_song_queue(self.library, "Crocodile Rock"), "Song 'Crocodile Rock' is not in your library!")
        #Checks that the songs have been removed from the queue list#
        self.assertNotIn(self.song4, Queue.queue)
        self.assertNotIn(self.song5, Queue.queue)
        self.assertNotIn(self.song7, Queue.queue)

if __name__ == '__main__':
    unittest.main()

library = Library()
user_input(library)