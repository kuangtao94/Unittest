import logging,os,time

#日志保存的路径
# log_path = "D:\\Test\\TestCase\\Log"
# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Log():
    def __init__(self):
        #日志文件的命名
        self.logname = os.path.join(log_path,"%s.log"%time.strftime("%y_%m_%d"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG) #log的等级

    def __console(self, level, message):
        #日志输出格式
        self.formatter = logging.Formatter(fmt=
            "[%(asctime)s]-%(filename)s-%(levelname)s-%(module)s:%(message)s")
        #创建一个FileHandler,用于写入本地
        fh = logging.FileHandler(self.logname,"a",encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建一个StreamHandler,用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == "info":
            self.logger.info(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "waring":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeFilter(fh)
        self.logger.removeHandler(ch)
        #关闭打开的文件
        fh.close()

    def info(self,message):
        self.__console("info",message)
    def debug(self,message):
        self.__console("debug",message)
    def waring(self,message):
        self.__console("waring",message)
    def error(self,message):
        self.__console("error",message)

if __name__ == '__main__':
    log = Log()
    log.info("测试开始")
    log.info("输入信息")
    log.waring("测试结束")