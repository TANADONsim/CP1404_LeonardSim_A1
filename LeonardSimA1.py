"""
Replace the contents of this module docstring with your own details.
"""
import csv


def main():
    # menu to be displayed
    menu = """
L - List songs
A - Add new song
C - Complete a song
Q - Quit
>>> """

    # Preparing the .csv for use
    import csv
    songs_file = open('songs.csv', 'r')
    song_reader = csv.reader(songs_file, delimiter=',', quotechar='|')
    song_list = list(song_reader)
    song_count = len(song_list)
    songs_file.close()

    # Welcome message and menu display
    print("Songs To Learn 1.0 - by Leonard Sim")
    while True:
        user_input = str(input(menu))

        # Option 1, List songs
        user_input = listing_songs(song_count, song_list, user_input)

        # Option 2, Add new songs
        user_input = adding_songs(song_list, user_input)

        # Option 3, Completing songs
        user_input = completing_songs(song_list, user_input)

        # Option 4, Quit program
        if user_input.upper() == "Q" or user_input.upper() == "4":
            print("{0} songs saved to songs.csv".format(song_count))
            print("Have a nice day :)")
            break

        # Invalid option, return to menu
        else:
            if user_input != "1":
                print("Invalid menu choice.")
            print("Returning to menu.")


def completing_songs(song_list, user_input):
    if user_input.upper() == "C" or user_input == "3":
        while True:
            try:
                user_input = int(input("Enter the number of a song to mark as learned "))
                song = song_list[user_input]
                break
            except (ValueError, IndexError):
                print("Invalid input; enter a valid number")
                continue

        # Check if song cleared
        if song[3] == "n":
            print("This song has already been cleared")

        # If song not yet cleared
        elif song[3] == "y":
            # clear song in a local list
            song[3] = "n"
            print("{0} by {1} learned".format(song[1], song[2]))
            # clear song in the .csv
            with open("songs.csv", "w", newline="") as songs_file:
                song_writer = csv.writer(songs_file)
                song_writer.writerows(song_list)
        user_input = "1"
    return user_input


def adding_songs(song_list, user_input):
    if user_input.upper() == "A" or user_input == "2":
        new_additions = []
        for song in song_list:
            new_additions.append(song[0])
        while True:
            new_title = str(input("Title: "))
            if len(new_title) < 1:
                print("Input cannot be blank")
                continue
            else:
                new_additions.append(new_title)
                break
        while True:
            new_artist = str(input("Artist: "))
            if len(new_artist) < 1:
                print("Input cannot be blank")
                continue
            else:
                new_additions.append(new_artist)
                break
        while True:
            try:
                new_year = int(input("Year: "))
            except ValueError:
                print("Invalid input; enter a valid number")
                continue
            if new_year < 0:
                print("Number must be >= 0")
                continue
            else:
                new_additions.append(new_year)
                break
        new_additions.append(new_artist)
        new_additions.append(new_year)
        new_additions.append("y")
        song_list.append(new_additions)
        with open("songs.csv", "w", newline="") as songs_file:
            song_writer = csv.writer(songs_file)
            song_writer.writerows(song_list)
        print("{0} by {1} ({2}) added to song list".format(new_title, new_artist, new_year))
        user_input = "1"
    return user_input


def listing_songs(song_count, song_list, user_input):
    if user_input.upper() == "L" or user_input == "1":
        song_num = 0
        songs_cleared = 0
        for song in song_list:
            status = "*"
            if song[3] == "n":
                status = " "
                songs_cleared += 1
            print("{0}. {1} {2:<30} - {3:<25} ({4})".format(song_num, status, song[0], song[1], song[2]))
            song_num += 1
        print("{0} songs learned, {1} songs still to learn".format(songs_cleared, song_count - songs_cleared))
        user_input = "1"
    return user_input


main()
