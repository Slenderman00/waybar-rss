#!/usr/bin/env python3

import feedparser
import argparse
import json
import subprocess

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--feed")
    parser.add_argument("-g", "--goto", action="store_true")

    args = parser.parse_args()

    if not args.feed:
        exit()

    feed = feedparser.parse(args.feed)

    title = feed['entries'][0]['title']
    summary = feed['entries'][0]['summary']
    url = feed['entries'][0]['link']

    if args.goto:
        subprocess.run(["firefox", url])
        exit()


    print(json.dumps({'text': title, 'tooltip': summary, 'url': url}))

if __name__ == "__main__":
    main()