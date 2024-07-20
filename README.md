# YouTube Fetcher

This project fetches video data from a YouTube channel, including subtitles and metadata, and saves the processed information to JSON files. It uses caching to minimize redundant API requests and improve performance.

## Prerequisites

- Python 3.6+
- A YouTube Data API v3 key

## Setup Instructions

### 1. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 2. Install Dependencies

Ensure you have requests, youtube-transcript-api, and nltk installed:

```bash
pip install -r requirements.txt
```

### 3. Download NLTK Tokenizer Models

Open a Python interpreter and run:

```python
import nltk
nltk.download('punkt')
```

### 4. Getting a YouTube Data API v3 Key

To run this project, you need a YouTube Data API v3 key. Follow these steps to get one:

1. **Go to the Google Cloud Console**:
   - Navigate to the [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project**:
   - Click on the project dropdown at the top of the page.
   - Select `New Project`.
   - Enter a name for your project and click `Create`.

3. **Enable the YouTube Data API v3**:
   - In the Google Cloud Console, navigate to the `API & Services` dashboard.
   - Click on `Enable APIs and Services`.
   - Search for `YouTube Data API v3` and click on it.
   - Click `Enable`.

4. **Create Credentials**:
   - After enabling the API, you will be prompted to create credentials.
   - Click `Create Credentials`, then select `API key`.
   - Your new API key will be displayed. Copy this key as you will need it to run the script.

5. **Restrict Your API Key** (Optional but recommended):
   - For security purposes, it's a good practice to restrict your API key.
   - Click on `Restrict Key`.
   - Under `Application restrictions`, you can specify the websites, IP addresses, or apps that can use this key.
   - Under `API restrictions`, select `YouTube Data API v3`.
   - Click `Save` to apply the restrictions.

6. **Usage Quotas**:
   - Be aware of the usage quotas for the YouTube Data API. By default, you have a quota of 10,000 units per day.
   - Different API requests consume different amounts of quota. For more details, refer to the [YouTube Data API Quota Usage](https://developers.google.com/youtube/v3/getting-started#quota).

Now you have a YouTube Data API v3 key that you can use to run the project.

### 5. Finding Your YouTube Channel ID

To fetch video data from a YouTube channel, you need the channel's unique ID. Follow these steps to find your YouTube Channel ID:

1. **Go to the YouTube Website**:
   - Open your web browser and go to [YouTube](https://www.youtube.com/).

2. **Navigate to the Channel**:
   - Use the search bar to find the channel you're interested in or click on your profile icon and select "Your channel" if you're looking for your own channel.

3. **Get the Channel ID from the URL**:
   - Click on the channel description to open the about popup
   - Click "Share channel" button
   - Click "Copy channel ID"

### 6. Run the Script

Use the following command to run the script, replacing `YOUR_CHANNEL_ID`, `YOUR_LANGUAGE_CODE`, and `YOUR_API_KEY` with appropriate values:

```bash
python main.py --channel_id YOUR_CHANNEL_ID --lang YOUR_LANGUAGE_CODE --api_key YOUR_API_KEY
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact
If you have any questions or issues, please open an issue on this repository.

