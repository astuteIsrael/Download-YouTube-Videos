from pytube import YouTube

video_url = "https://youtu.be/9OeznAkyQz4?si=z1o2Wf_N_C1vH723"


yt = YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download()