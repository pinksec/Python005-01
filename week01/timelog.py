# 编写一个函数, 当函数被调用时，将调用的时间记录在日志中
# 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log

import time
import logging

def logtime():
    logging.basicConfig(filename='python-{}.log'.format(time.asctime()),
        datefmt='%Y-%m-%d %h-%m-%s',
        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
    )

    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.critical('critical message')

    exit()

logtime()




