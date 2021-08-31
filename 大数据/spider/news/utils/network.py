# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:23:19 2021

@author: RN01945
"""
import time

try:
    import psutil
except ImportError:
    print('Error: psutil module not found!')
    exit()


class GetNetSpeed():

    def get_key(self):
        """
        获取所有的网卡的 下载和下载的 字节数(历史统计的所有的)
        """

        key_info = psutil.net_io_counters(pernic=True).keys()

        recv = {}
        sent = {}

        for key in key_info:
            recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
            sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

        return key_info, recv, sent

    def get_rate(self):
        """
        获取下载
        """

        delay_time = 1
        key_info, old_recv, old_sent = self.get_key()  # 当前时刻的上传下载的字节数
        time.sleep(delay_time)
        key_info, now_recv, now_sent = self.get_key()  # 1秒后的上传下载的字节数

        net_in = {}
        net_out = {}

        for key in key_info:
            net_in.setdefault(key, float('%.2f' % ((now_recv.get(key) - old_recv.get(key)) / 1024)))  # 计算的是 间隔时间的下载的网速
            net_out.setdefault(key, float('%.2f' % ((now_sent.get(key) - old_sent.get(key)) / 1024)))

        return key_info, net_in, net_out

    def get_netspeed(self):
        try:
            key_info, net_in, net_out = self.get_rate()  # 获取 间隔时间的 所有网卡的下载上传的 网速
            for key in key_info:
                # lo 是linux的本机回环网卡，以太网是我win10系统的网卡名
                # if key != 'lo' or key == 'em1':
                if key == '以太网':
                    # print('%s: \t 下载:\t %-5sKB/s \t 上传:\t %-5sKB/s' % (key, net_in.get(key), net_out.get(key)),
                    #       end='\r', flush=True)
                    return net_in.get(key), net_out.get(key)
        except KeyboardInterrupt:
            exit()


if __name__ == '__main__':
    netspeed = GetNetSpeed()
    while True:
        down,up = netspeed.get_netspeed()
        print('下载:\t %-5sKB/s \t 上传:\t %-5sKB/s' % (down, up),
              end='\n', flush=True)

