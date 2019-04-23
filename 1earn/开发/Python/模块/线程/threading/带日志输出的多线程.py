import logging
import threading


#get_logger 函数。这段代码将创建一个被设置为调试级别的日志记录器。
#它将日志保存在当前目录（即脚本运行所在的目录）下，然后设置每行日志的格式。格式包括时间戳、线程名、日志记录级别以及日志信息。
def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("threading1.log")
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


def doubler(number, logger1):
    """
    可以被线程使用的一个函数
    """

    #调用get_logger，传入message
    logger1.debug('doubler function executing')
    result = number * 2

    # 调用get_logger，传入message
    logger1.debug('doubler function ended with: {}'.format(
        result))


if __name__ == '__main__':
    logger2 = get_logger()

    # 线程名称
    thread_names = ['Mike', 'George', 'Wanda', 'Dingbat', 'Nina']

    for i in range(5):
        my_thread = threading.Thread(target=doubler, name=thread_names[i], args=(i,logger2))
        my_thread.start()