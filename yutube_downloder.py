from pytube import YouTube

try:
    yt_vedio = YouTube("Enter The Link You want To Download" )
    stream = yt_vedio.streams.get_highest_resolution()
    stream.download()
    
    print("Download completed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")