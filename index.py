from pytubefix import YouTube
from pytubefix.cli import on_progress
import csv


def download(url):
    print(url)
    yt = YouTube(url, on_progress_callback=on_progress)

    ys = yt.streams.filter(file_extension='mp4',
                           type='video').get_highest_resolution(False)

    if ys:
        ys.download()


def main():
    with open('links.csv', mode='r') as target:
        file = csv.reader(target)
        for index, line in enumerate(file):
            if index == 0:
                continue
            link = line[0]
            download(link)


if __name__ == '__main__':
    main()
