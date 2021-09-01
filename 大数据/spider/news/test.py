import sys,traceback,time

class Spider():
    def __init__(self):
        pass

    def start(self):
        print('aaa')

    def main(self):
        try:
            intervals = sys.argv[1]  # 获取前面传递过来的 更新间隔时间
        except Exception as err:
            intervals = 1800
        while True:
            self.start()
            time.sleep(int(intervals))
if __name__ == '__main__':
    spider = Spider()
    spider.main()