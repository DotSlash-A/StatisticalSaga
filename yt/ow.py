# Install the required library
# Run this command in your terminal if you don't have pytube installed: pip install pytube

from pytube import YouTube

def download_unlisted_video(video_url, save_path="."):
    try:
        # Create YouTube object
        yt = YouTube(video_url)
        
        # Display video details
        print("Title:", yt.title)
        print("Author:", yt.author)
        print("Length (seconds):", yt.length)

        # Choose the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        print(f"Downloading '{yt.title}'...")
        stream.download(output_path=save_path)
        print(f"Download completed! Saved to {save_path}")
    except Exception as e:
        print("An error occurred:", e)

# Replace this URL with your unlisted video URL
video_url = "https://www.youtube.com/watch?v=Ym_7xEeDaco"
download_unlisted_video(video_url)
