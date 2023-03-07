from app_modules import *
from app_define import *
from app_functions import *

def printYTInfo(rootLogger, yt):
    if rootLogger is None:
        print(yt.title)           # 影片標題
        print(yt.length)          # 影片長度 ( 秒 )
        print(yt.author)          # 影片作者
        print(yt.channel_url)     # 影片作者頻道網址
        print(yt.thumbnail_url)   # 影片縮圖網址
        print(yt.views)           # 影片觀看數
    else:
        rootLogger.info(yt.title)           # 影片標題
        rootLogger.info(yt.length)          # 影片長度 ( 秒 )
        rootLogger.info(yt.author)          # 影片作者
        rootLogger.info(str(yt.channel_url))     # 影片作者頻道網址
        rootLogger.info(str(yt.thumbnail_url))   # 影片縮圖網址
        rootLogger.info(yt.views)           # 影片觀看數

def downloadVideo(rootLogger, yt, filename=None, output_dir=OUTPUT_DIR):
    # Check output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Check filename
    if filename is None:
        rstr = r"[\/\\\:\*\?\"\<\>\|]"
        filename = re.sub(rstr, '_', str(yt.title))
        filename = f"{filename}.mp4"
    save_url = os.path.join(output_dir, filename)

    # Download video
    yt.streams.filter().get_highest_resolution().download(filename=save_url)

    if rootLogger is not None:
        rootLogger.info(f'Video Downloaded, filename: {save_url}')
    else:
        print(f'Video Downloaded, filename: {save_url}')


def downloadAudio(rootLogger, yt, filename=None, output_dir=OUTPUT_DIR):
    # Check output directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Check filename
    if filename is None:
        rstr = r"[\/\\\:\*\?\"\<\>\|]"
        filename = re.sub(rstr, '_', str(yt.title))
        filename = f"{filename}.mp3"
    save_url = os.path.join(output_dir, filename)

    # Download video
    yt.streams.filter().get_audio_only().download(filename=save_url)

    if rootLogger is not None:
        rootLogger.info(f'Video Downloaded, filename: {save_url}')
    else:
        print(f'Video Downloaded, filename: {save_url}')


if __name__ == "__main__":
    # Get Logger
    rootLogger = getLogger('getYTmedia')

    # Input target URL
    target_url = "https://youtube.com/shorts/iyvCkf2YtwM"
    yt = YouTube(target_url)
    rootLogger.info(f'Target Youtube URL: {target_url}')

    printYTInfo(rootLogger, yt)

    # Video
    downloadVideo(rootLogger, yt)

    # Music / Audio
    downloadAudio(rootLogger, yt)