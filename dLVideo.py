import requests
import os

def download_video(url, output_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(output_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        print(f"Video downloaded to: {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = "https://ev-h-ph.rdtcdn.com/hls/videos/202306/12/433417091/,1080P_4000K,720P_4000K,480P_2000K,240P_1000K,_433417091.mp4.urlset/seg-15-f1-v1-a1.ts?validfrom=1693781909&validto=1693789109&hdl=-1&hash=bb%2Bx4EY9OXtuMRdDOAwxUx9WLyU%3D&&&"
    output_file = input("Enter the path to save the video: ")


    download_video(video_url, output_file)
