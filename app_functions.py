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
        log_url = os.path.join(os.path.join(LOG_DIR, f'{loggerName}_{now_str}.log'))
        file_handler = logging.handlers.TimedRotatingFileHandler(log_url, when="H", interval=1, encoding="utf-8")
        file_handler.setLevel(target_level)        
        file_handler.setFormatter(formatter)

    # 將 handler 加入 logger 中
    rootLogger.addHandler(console_handler)
    rootLogger.addHandler(file_handler)
    
    return rootLogger