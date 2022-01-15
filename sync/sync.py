import boto3
import json
import urllib3
import concurrent.futures

# Insert API key here
API_KEY = None

channels = [
    "UCIeSUTOTkF9Hs7q3SGcO-Ow",  # Elira
    "UCP4nMSTdwU1KqYWu3UH5DHQ",  # Pomu
    "UCu-J8uIXuLZh16gG-cT1naw",  # Finana

    "UC4WvIIAo89_AzGUh1AZ6Dkg",  # Rosemi
    "UCgA2jKRkqpY_8eysPUs8sjw",  # Petra
    "UCV1xUwfM2v2oBtT3JNvic3w",  # Selen

    "UC47rNmkDcNgbOcM-2BwzJTQ",  # Millie
    "UCBURM8S4LH7cRZ0Clea9RDA",  # Reimu
    "UCkieJGn3pgJikVW8gmMXE2w",  # Nina
    "UCR6qhsLpn62WVxCBK1dkLow",  # Enna

    "UC4yNIKGvy-YUrwYupVdLDXA",  # Ike
    "UC7Gb7Uawe20QyFibhLl1lzA",  # Luca
    "UCckdfYDGrjojJM28n5SHYrA",  # Vox
    "UCG0rzBZV_QMP4MtWg6IjhEA",  # Shu
    "UCIM92Ok_spNKLVB5TsgwseQ",  # Mysta

    "UC-JSeFfovhNsEhftt1WHMvg",  # Official En
]


def get_videos(channel):
    print(f'Fetching {channel}')
    http = urllib3.PoolManager()
    resp = http.request(
        'GET',
        'https://holodex.net/api/v2/videos',
        headers={'x-apikey': API_KEY},
        fields={'channel_id': channel, 'limit': '7', 'include': 'live_info,sources'},
    )
    return json.loads(resp.data)

def upload_api_response(data):
    print(f'Uploading data')
    s3 = boto3.client('s3')
    s3.put_object(
        ACL='public-read',
        Bucket='pomuhub.com',
        Key='api/data',
        Body=data
    )

def lambda_handler(*args, **kwargs):
    videos = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for channel_vids in executor.map(get_videos, channels):
            videos.extend(channel_vids)
    data = json.dumps(videos)
    upload_api_response(data)

if __name__ == '__main__':
    print(lambda_handler())
