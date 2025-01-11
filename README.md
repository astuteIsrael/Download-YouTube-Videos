# YouTube Video Downloader with Pytube

This project provides a simple and easy-to-use Python script to download YouTube videos in their highest resolution using the `pytube` library.

## Features

- Download YouTube videos by providing the video URL.
- Downloads the video in the highest available resolution.
- Simple and minimalistic script.

## Requirements

- Python 3.x
- `pytube` library

You can install the required library using pip:

```bash
pip install pytube
```

## How to Use

1. Clone or download the repository.
2. Install the dependencies using pip (as mentioned above).
3. Update the `video_url` variable in the `download.py` script with the YouTube video URL.
4. Run the script:

```bash
python download.py
```

The video will be downloaded in the highest available resolution to the current working directory.

## Example

```python
from pytube import YouTube

video_url = "https://youtu.be/9OeznAkyQz4?si=z1o2Wf_N_C1vH723"  # Replace with the URL of the video you want to download

yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download()
```

The script will download the video and save it to the current directory.

## Troubleshooting

- **Error: Pytube Not Installed**  
  Ensure you have installed `pytube` using:

  ```bash
  pip install pytube
  ```

- **Video Not Found**  
  Make sure the video URL is correct and accessible

Feel free to customize this according to your preferences or project specifics
