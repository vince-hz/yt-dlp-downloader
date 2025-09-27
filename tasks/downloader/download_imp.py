import yt_dlp
from pathlib import Path
from typing import Optional, Any


def download_video_advanced(
    url: str,
    save_path: str,
    *,
    post_process_to_mp4: bool = True,
    cookie_path: str = "",
    quality: Any = (
        "best[vcodec^=avc1][ext=mp4][height<=720]/"  # Explicitly require mp4 format
        "best[vcodec^=avc1][ext!=ts][height<=720]/"  # Exclude .ts files
        "best[ext=mp4][height<=720]/"  # Any codec mp4
        "best[ext!=ts]"  # Exclude all ts formats
    ),
    subtitle: bool = False,
    progress_callback: Optional[callable] = None,
) -> Optional[str]:
    """
    Download video using yt-dlp (enhanced version)

    Args:
        url (str): Video URL
        save_path (str): Save path, can be directory or specific filename
        post_process_to_mp4 (bool): Whether to convert downloaded video to mp4 format
        quality (str): Video quality, default is 'best'
        subtitle (bool): Whether to download subtitles
        progress_callback (callable): Progress callback function

    Returns:
        str: Final saved file path, returns None if download fails
    """
    try:
        save_path = Path(save_path)

        # Determine if it's a directory or file
        if save_path.suffix == "" or save_path.is_dir():
            output_dir = save_path
            output_template = str(output_dir / "%(title)s.%(ext)s")
        else:
            output_dir = save_path.parent
            filename_without_ext = save_path.stem
            output_template = str(output_dir / f"{filename_without_ext}.%(ext)s")

        # Ensure output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)

        # Configuration options
        ydl_opts = {
            "outtmpl": output_template,
            "noplaylist": True,
        }

        if post_process_to_mp4:
            ydl_opts["postprocessors"] = [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",
                }
            ]
            # Ensure FFmpeg is used
            ydl_opts["prefer_ffmpeg"] = True
            # Force re-encoding instead of copying
            ydl_opts["postprocessor_args"] = {
                "ffmpeg_o": [
                    "-c:v",
                    "libx264",
                    "-profile:v",
                    "main",
                    "-level:v",
                    "3.1",
                    "-c:a",
                    "aac",
                    "-f",
                    "mp4",
                    "-movflags",
                    "+faststart",
                ]
            },


        ydl_opts["format"] = quality

        if cookie_path:
            print("cookiefile path", cookie_path)
            with open(cookie_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content:
                    print("Cookie content is not empty")
                else:
                    print("Cookie content is empty")

        if cookie_path:
            ydl_opts["cookiefile"] = cookie_path

        # Subtitle options
        if subtitle:
            ydl_opts["writesubtitles"] = True
            ydl_opts["writeautomaticsub"] = True

        downloaded_file = None

        def download_hook(d):
            nonlocal downloaded_file
            status = d["status"]

            if status == "finished":
                downloaded_file = d["filename"]
                print("update file with", downloaded_file)

            if status == "downloading":
                downloaded_bytes = d.get("downloaded_bytes", 0)
                total_bytes = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
                if total_bytes > 0:
                    percent = (downloaded_bytes / total_bytes) * 100
                    if progress_callback:
                        progress_callback(percent)

        ydl_opts["progress_hooks"] = [download_hook]

        # Execute download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return downloaded_file

    except Exception as e:
        print(f"Download failed: {str(e)}")
        return None


# Usage example
if __name__ == "__main__":

    def progress_hook(d):
        if d["status"] == "downloading":
            percent = d.get("_percent_str", "N/A")
            speed = d.get("_speed_str", "N/A")
            print(f"\rDownload progress: {percent} Speed: {speed}", end="", flush=True)
        elif d["status"] == "finished":
            print(f"\nDownload completed: {d['filename']}")

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Download video
    result = download_video_advanced(
        url, "/oomol-driver/oomol-storage", progress_callback=progress_hook
    )
    print(f"Final save path: {result}")
