#  Task 1: Parsing and printing song lengths
def seconds_to_string(seconds):
    """
    Converts seconds to a string in the format mm:ss where mm is the number of minutes and ss is the number of seconds.
    """
    return f"{seconds // 60}:{seconds % 60:02d}"


def string_to_seconds(string):
    """
    Converts a string in the format mm:ss to seconds as an integer. Returns None if the string is not in the
    correct format.
    """
    try:  # Try to convert the string to seconds and return the result.
        minutes, seconds = string.split(":")
        minutes = int(minutes)
        seconds = int(seconds)
        # If the minutes or seconds are negative or the seconds are greater than 59, raise a ValueError.
        if minutes < 0 or seconds < 0 or seconds >= 60:
            raise ValueError
        return minutes * 60 + seconds
    except ValueError:  # Exception handling for the ValueError raised above.
        raise ValueError(f"Invalid time format: {string}")


# Task 2: Loading a library from a file
def read_library(filename):
    """
    Reads a library from a file and returns it as a dictionary.
    """
    library = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")
                if len(parts) != 3:
                    raise ValueError
                artist, song, length = parts
                string_to_seconds(length)
                if artist not in library:
                    library[artist] = {}
                library[artist][song] = length
        return library
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
    except ValueError:
        raise ValueError("The input file is malformed")


def print_library(library):
    """
    Prints a library in a nice format.
    """
    total_songs = 0
    total_length = 0
    for artist, songs in library.items():
        num_songs = len(songs)
        total_songs += num_songs
        artist_length = 0
        for song_name, length in songs.items():
            artist_length += string_to_seconds(length)
        total_length += artist_length
        print(f"{artist} ({num_songs} songs, {seconds_to_string(artist_length)})")
        for song_name, length in songs.items():
            minutes, seconds = length.split(":")
            print(f"- {song_name} ({minutes}:{seconds})")
    print(f"Total: ({total_songs} songs, {seconds_to_string(total_length)})")


# Task 3: Creating playlists
def make_playlist(library, theme):
    """
    Creates a playlist of songs from the library with the given theme.
    """
    playlist = []
    for artist, songs in library.items():
        for song_name, length in songs.items():
            if theme in song_name:
                playlist.append((artist, song_name, length))
    if not playlist:
        raise ValueError(f"No songs with the theme {theme}")
    return playlist


def write_playlist(playlist, filename):
    """
    Writes a playlist to a file.
    """
    if not filename:
        raise ValueError("The playlist name cannot be empty")
    with open(filename, "w") as file:
        for artist, song_name, length in playlist:
            file.write(f"{artist},{song_name},{length}\n")



library = read_library("80s_library.txt")

house = make_playlist(library, "House")
write_playlist(house, "house_playlist.txt")


# Task 4: Putting it all together
def main():
    """
    The main function of the program.
    """
    while True:
        try:
            filename = input("Which music library do you want to load: ")
            library = read_library(filename)
            print_library(library)
            break
        except FileNotFoundError:
            print("File not found")
        except ValueError:
            print("The file is malformed")
    while True:
        theme = input("Enter a playlist theme: ")
        try:
            playlist = make_playlist(library, theme)
            break
        except ValueError:
            print("No songs match this theme")
    while True:
        filename = input("Enter the playlist name: ")
        try:
            write_playlist(playlist, filename)
            break
        except ValueError:
            print("The playlist name cannot be empty")
    print("Playlist created successfully")
