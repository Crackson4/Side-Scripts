import sys

from pytube import YouTube


def main():
    yt = YouTube(sys.argv[1]).streams
    video = yt.filter(progressive=True).get_highest_resolution()

    video.download()


if __name__ == "__main__":
    main()
