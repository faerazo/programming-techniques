#  Task 1: Parsing and printing song lengths
def seconds_to_string(seconds):
    """
    Converts seconds to a string in the format mm:ss where mm is the number of minutes and ss is the number of seconds.
    """
    return f"{seconds // 60}:{seconds % 60:02d}"


def string_to_seconds(string):
    """
    Converts a string in the format mm:ss to seconds as an integer.
    """
    try:  # Try to convert the string to seconds and return the result
        minutes, seconds = string.split(":")  # Split the string based by colon punctuation mark
        minutes = int(minutes)
        seconds = int(seconds)
        # If the minutes or seconds are negative or the seconds are greater than 59, raise a ValueError
        if minutes < 0 or seconds < 0 or seconds >= 60:
            raise ValueError
        return minutes * 60 + seconds  # Return the number of seconds
    except ValueError:  # Exception handling for the ValueError raised above
        raise ValueError(f"Invalid time format: {string}")


# Task 2: Loading a library from a file
def read_library(filename):
    """
    Reads a library from a file and returns it as a dictionary.
    """
    library = {}  # Create an empty dictionary
    try:  # Try to read the library from the file
        with open(filename, "r") as file:  # Open the file in read mode
            for line in file:
                line = line.strip()  # Remove whitespaces
                parts = line.split(",")  # Split the line based by comma punctuation mark
                if len(parts) != 3:  # Every line should have three parts, if not, raise a ValueError
                    raise ValueError
                artist, song, length = parts
                string_to_seconds(length)  # Check if the length is valid by using string_to_seconds function
                if artist not in library:  # If the artist is not in the library, add it
                    library[artist] = {}
                library[artist][song] = length  # Add the song to the artist
        return library
    except FileNotFoundError:  # Exception handling for the FileNotFoundError raised by open function above
        raise FileNotFoundError(f"File {filename} not found")
    except ValueError:  # Exception handling for the ValueError raised by string_to_seconds function above
        raise ValueError("The input file is malformed")


def print_library(library):
    """
    Prints a library in a structured format.
    """
    total_songs = 0
    total_length = 0
    for artist, songs in library.items():  # Loop through the library
        num_songs = len(songs)  # Get the number of songs for the artist
        total_songs += num_songs  # Add the number of songs to the total number of songs
        artist_length = 0
        for song_name, length in songs.items():  # Loop through the songs of the artist
            artist_length += string_to_seconds(length)  # Add the length of the song to the artist length
        total_length += artist_length  # Add the artist length to the total length
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
            if theme in song_name:  # If the theme is in the song name, add the song to the playlist
                playlist.append((artist, song_name, length))  # Add the song to the playlist
    if not playlist:  # If the playlist is empty, raise a ValueError
        raise ValueError(f"No songs with the theme {theme}")
    return playlist


def write_playlist(playlist, filename):
    """
    Writes a playlist to a file.
    """
    if not filename:  # If the filename is empty, raise a ValueError
        raise ValueError("The playlist name cannot be empty")
    with open(filename, "w") as file:  # Open the file in write mode
        for artist, song_name, length in playlist:  # Loop through the playlist
            file.write(f"{artist},{song_name},{length}\n")  # Write the song to the file


# Task 4: Putting it all together
def main():
    """
    The main function of the program.
    """
    while True:  # Loop until the user enters a valid filename
        try:
            filename = input("Which music library do you want to load: ")
            library = read_library(filename)
            print_library(library)
            break  # Break the loop if the library is read successfully
        except FileNotFoundError:  # Exception handling for the FileNotFoundError raised by read_library function
            print("File not found")
        except ValueError:  # Exception handling for the ValueError raised by read_library function
            print("The file is malformed")
    while True:  # Loop until the user enters a valid theme
        theme = input("Enter a playlist theme: ")
        try:
            playlist = make_playlist(library, theme)
            break  # Break the loop if the playlist is created successfully
        except ValueError:  # Exception handling for the ValueError raised by make_playlist function
            print("No songs match this theme")
    while True:  # Loop until the user enters a valid filename
        filename = input("Enter the playlist name: ")
        try:
            write_playlist(playlist, filename)
            break  # Break the loop if the playlist is written successfully
        except ValueError:  # Exception handling for the ValueError raised by write_playlist function
            print("The playlist name cannot be empty")
    print("Playlist created successfully")


main()  # Test the program

