import os
import argparse
from youtube_utils import fetch_video_ids, fetch_and_save_all_videos

def fetch_and_process_videos(channel_id, lang, api_key):
    video_ids = fetch_video_ids(channel_id, api_key)
    if video_ids:
        fetch_and_save_all_videos(video_ids, lang, api_key)
    else:
        print(f'No videos found for channel ID {channel_id}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Fetch and process YouTube videos.")
    parser.add_argument('--channel_id', type=str, required=True, help='YouTube channel ID')
    parser.add_argument('--lang', type=str, required=True, help='Language code for subtitles')
    parser.add_argument('--api_key', type=str, required=True, help='YouTube Data API key')
    args = parser.parse_args()

    fetch_and_process_videos(args.channel_id, args.lang, args.api_key)
