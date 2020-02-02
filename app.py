import logging
from logging import handlers
import os

host = "http://182.92.81.159"
header = {"Content-Type": "application/json"}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def init_logging():
    # 1.初始化日志器
    logger = logging.getLogger()
    # 2.设置日志等级
    logger.setLevel(logging.INFO)
    # 3.创建控制处理器
    sh = logging.StreamHandler()
    # 4.创建文件处理器
    log_path = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(
        filename=log_path, when="D", interval=1, backupCount=7, encoding="utf-8")
    # 5.创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] - [%(message)s]"
    formatter = logging.Formatter(fmt)
    # 6.讲格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 7.将处理器添加到日志
    logger.addHandler(sh)
    logger.addHandler(fh)

