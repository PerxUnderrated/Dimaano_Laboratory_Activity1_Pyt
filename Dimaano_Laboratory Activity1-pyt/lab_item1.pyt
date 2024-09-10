def main():

    print("Enter the year: ", end="")
    year = int(input().strip())

    print("Enter the genre: ", end="")
    genre = input().strip()

    print("Enter the album: ", end="")
    album = input().strip()

    print("Enter the song title: ", end="")
    title = input().strip()

    print("Enter the artist: ", end="")
    artist = input().strip()

    print("---------------------------")
    print("SONG DETAILS")
    print("---------------------------")
    print(f"Year Released: {year}")
    print(f"Genre: {genre}")
    print(f"Album: {album}")
    print(f"Title: \"{title}\"")
    print(f"Artist: {artist}")

if __name__ == "__main__":
    main()