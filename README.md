# Video Downloader based on yt-dlp

This Python script provides a convenient wrapper around the powerful `yt-dlp` library to download videos from YouTube and other video sites. It allows for more control over the download process, including quality selection, subtitle downloads, and progress reporting.

## Features

- Download single videos from various platforms supported by `yt-dlp`.
- Specify the desired video quality (e.g., 'best', '1080p', '720p').
- Automatically download available subtitles for the video.
- Provides a progress callback mechanism to track download status in real-time.
- Flexible output path: save to a specific directory or define the exact output filename.

## Requirements

- Python 3.6+
- `yt-dlp`

You can install the required Python library using pip:

```bash
pip install yt-dlp
```

## Usage

The primary component is the `download_video_advanced` function located in `download_imp.py`. You can import and use this function in your own Python projects.

### Function Signature

```python
def download_video_advanced(
    url: str,
    save_path: str,
    quality: str = 'best',
    subtitle: bool = False,
    progress_callback: Optional[callable] = None
) -> Optional[str]:
```

### Parameters

- `url` (str): The URL of the video you want to download.
- `save_path` (str): The path where the video should be saved.
    - If it's a directory (e.g., `/path/to/downloads`), the video will be saved inside with its original title.
    - If it's a full file path (e.g., `/path/to/my_video.mp4`), the video will be saved with that specific name.
- `quality` (str, optional): The desired video quality. This corresponds to the `format` option in `yt-dlp`. Defaults to `'best'`.
- `subtitle` (bool, optional): Set to `True` to download subtitles along with the video. Defaults to `False`.
- `progress_callback` (callable, optional): A function that will be called during the download with progress information. The function should accept a single argument (a float representing the percentage).

### Returns

- `(Optional[str])`: The full path to the downloaded video file if the download is successful, otherwise `None`.

## Example

Here is a basic example of how to use the `download_video_advanced` function.

```python
from download_imp import download_video_advanced
from typing import Optional

def my_progress_hook(percent: float):
    # A simple progress bar
    bar_length = 20
    filled_length = int(bar_length * percent // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rDownloading: |{bar}| {percent:.2f}%', end='')
    if percent == 100:
        print()

# URL of the video to download
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Path to save the video
# This will save the video in the 'my_videos' directory
save_directory = "./my_videos"

print(f"Starting download for: {video_url}")

# Call the download function
final_path: Optional[str] = download_video_advanced(
    url=video_url,
    save_path=save_directory,
    quality='best',
    subtitle=True,
    progress_callback=my_progress_hook
)

if final_path:
    print(f"Download complete! Video saved at: {final_path}")
else:
    print("Download failed.")

```
