from app_modules import *
from app_define import *

def getLogger(loggerName, is_verbose=True, is_save_file=True):
    # 建立 logger
    rootLogger = logging.getLogger("my_logger")
    target_level = logging.DEBUG
    rootLogger.setLevel(target_level)

    now = datetime.now()

    # Define format
    formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d [%(levelname)5s] [%(threadName)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 建立控制台 handler
    if is_verbose:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(target_level)
        console_handler.setFormatter(formatter)

    # 建立檔案 handler
    if is_save_file:
        now_str = now.strftime('%Y%m%d_%H%M%S')
        log_url = os.path.join(os.path.join(LOG_DIR, '{loggerName}_{now_str}.log'))
        file_handler = logging.handlers.TimedRotatingFileHandler(log_url, when="H", interval=1)
        file_handler.setLevel(target_level)        
        file_handler.setFormatter(formatter)

    # 將 handler 加入 logger 中
    rootLogger.addHandler(console_handler)
    rootLogger.addHandler(file_handler)
    
    return rootLogger

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
        rootLogger.info(yt.channel_url)     # 影片作者頻道網址
        rootLogger.info(yt.thumbnail_url)   # 影片縮圖網址
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
    rootLogger = getLogger('getYTmedia')
    rootLogger.info('test')
    # Input target URL
    target_url = "https://youtube.com/shorts/iyvCkf2YtwM"

    yt = YouTube(target_url)
    downloadVideo(rootLogger, yt)

    downloadAudio(rootLogger, yt)