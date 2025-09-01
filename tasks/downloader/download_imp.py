from ctypes import Union
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
        "best[vcodec^=avc1][ext=mp4][height<=720]/"  # 明确要求 mp4 格式
        "best[vcodec^=avc1][ext!=ts][height<=720]/"  # 排除 .ts 文件
        "best[ext=mp4][height<=720]/"  # 任何编码的 mp4
        "best[ext!=ts]"  # 排除所有 ts 格式
    ),
    subtitle: bool = False,
    progress_callback: Optional[callable] = None,
) -> Optional[str]:
    """
    使用 yt-dlp 下载视频（增强版）

    Args:
        url (str): 视频URL
        save_path (str): 保存路径，可以是目录或具体文件名
        post_process_to_mp4 (bool): 是否将下载的视频转换为mp4格式
        quality (str): 视频质量，默认为 'best'
        subtitle (bool): 是否下载字幕
        progress_callback (callable): 进度回调函数

    Returns:
        str: 最终保存的文件路径，如果下载失败返回 None
    """
    try:
        save_path = Path(save_path)

        # 判断是目录还是文件
        if save_path.suffix == "" or save_path.is_dir():
            output_dir = save_path
            output_template = str(output_dir / "%(title)s.%(ext)s")
        else:
            output_dir = save_path.parent
            filename_without_ext = save_path.stem
            output_template = str(output_dir / f"{filename_without_ext}.%(ext)s")

        # 确保输出目录存在
        output_dir.mkdir(parents=True, exist_ok=True)

        # 配置选项
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
            # 确保使用 FFmpeg
            ydl_opts["prefer_ffmpeg"] = True
            # 强制重新编码而不是复制
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

        print("cookiefile path", cookie_path)
        with open(cookie_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

        if len(cookie_path) > 0:
            ydl_opts["cookiefile"] = cookie_path

        # 字幕选项
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

        # 执行下载
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return downloaded_file

    except Exception as e:
        print(f"下载失败: {str(e)}")
        return None


# 使用示例
if __name__ == "__main__":

    def progress_hook(d):
        if d["status"] == "downloading":
            percent = d.get("_percent_str", "N/A")
            speed = d.get("_speed_str", "N/A")
            print(f"\r下载进度: {percent} 速度: {speed}", end="", flush=True)
        elif d["status"] == "finished":
            print(f"\n下载完成: {d['filename']}")

    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # 下载视频
    result = download_video_advanced(
        url, "/oomol-driver/oomol-storage", progress_callback=progress_hook
    )
    print(f"最终保存路径: {result}")
