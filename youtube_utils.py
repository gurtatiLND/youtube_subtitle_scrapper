import os
import json
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from nltk.tokenize import sent_tokenize
from cache_utils import cached_api_request, save_cache

VIDEOS_FOLDER = './videos'

def fetch_video_ids(channel_id, api_key):
    try:
        video_ids = []
        next_page_token = ''
        while True:
            url = f'https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=50&pageToken={next_page_token}'
            response = requests.get(url)  # No caching for this request
            data = response.json()
            ids = [item['id']['videoId'] for item in data['items'] if 'videoId' in item['id']]
            video_ids.extend(ids)
            next_page_token = data.get('nextPageToken', '')
            if not next_page_token:
                break
        return video_ids
    except Exception as error:
        print(f'Error fetching video IDs: {error}')
        return []

def fetch_subtitles(video_id, lang):
    try:
        subtitles = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        return [{'text': subtitle['text']} for subtitle in subtitles]
    except Exception as error:
        if 'Could not find a transcript' in str(error):
            print(f'No subtitles found for video ID {video_id}')
            return []
        else:
            print(f'Error fetching subtitles for video ID {video_id}: {error}')
            return []

def process_subtitles(subtitles):
    subtitle_text = ' '.join([sub['text'] for sub in subtitles])
    sentences = sent_tokenize(subtitle_text)
    return ' '.join(sentences)

def fetch_video_metadata(video_id, api_key):
    try:
        url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails'
        data = cached_api_request(url)
        video = data['items'][0]

        if not video:
            print(f'No video found with the provided ID {video_id}.')
            return None

        metadata = {
            'title': video['snippet']['title'],
            'description': video['snippet']['description'],
            'publishedAt': video['snippet']['publishedAt'],
            'duration': video['contentDetails']['duration'],
            'tags': video['snippet'].get('tags', [])
        }

        return metadata
    except Exception as error:
        print(f'Error fetching video metadata for video ID {video_id}: {error}')
        return None

def fetch_and_save_all_data(video_id, lang, api_key, output_path):
    try:
        if not os.path.exists(VIDEOS_FOLDER):
            os.makedirs(VIDEOS_FOLDER)

        if os.path.exists(output_path):
            print(f'File {output_path} already exists. Skipping fetching data.')
            return

        subtitles = fetch_subtitles(video_id, lang)
        if not subtitles:
            print(f'No subtitles available for video ID {video_id}. Skipping.')
            return

        metadata = fetch_video_metadata(video_id, api_key)
        if not metadata:
            print(f'Failed to fetch metadata for video ID {video_id}. Skipping.')
            return

        processed_subtitles = process_subtitles(subtitles)
        data = {
            'metadata': metadata,
            'subtitles': processed_subtitles
        }

        with open(output_path, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f'All data saved to {output_path}')
    except Exception as error:
        print(f'Error fetching and saving data for video ID {video_id}: {error}')

def fetch_and_save_all_videos(video_ids, lang, api_key):
    for video_id in video_ids:
        output_path = os.path.join(VIDEOS_FOLDER, f'{video_id}_{lang}.json')
        fetch_and_save_all_data(video_id, lang, api_key, output_path)
