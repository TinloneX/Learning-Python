#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用第三方模块(4)
# psutil (pip install psutil)

# 快速打印
from util import p
import psutil

p(psutil.cpu_count())  # CPU核心数
p(psutil.cpu_count(logical=False))  # CPU物理核心数
p(psutil.cpu_times())  # CPU用户，系统，空闲时间，中断 ...

for x in range(3):  # top命令
    """p(psutil.cpu_percent(interval=1, percpu=True))"""

p(psutil.virtual_memory())  # 获取(物理)内存信息
p(psutil.swap_memory())  # 获取交换内存信息

p(psutil.disk_partitions())  # 磁盘分区信息
p(psutil.disk_usage('/'))  # 磁盘使用情况
p(psutil.disk_io_counters())  # 磁盘IO信息

p(psutil.net_io_counters())  # 获取网络读取字节/包的个数
p(psutil.net_if_addrs())  # 获取网络接口信息
p(psutil.net_if_stats())  # 获取网络接口状态

p(psutil.net_connections())  # 获取网络连接信息

p(psutil.pids())  # 所有进程id
pcs = psutil.Process(3236)  # 根据pid获取进程（在资源管理器中任意找一个进程号尝试）
p(pcs.name())  # 进程名称
p(pcs.exe())  # 进程exe路径
p(pcs.cwd())    # 进程工作目录
p(pcs.cmdline())    # 进程启动命令行
p(pcs.ppid)     # 父进程pid
p(pcs.parent())     # 父进程
p(pcs.children())  # 子进程列表
p(pcs.status())     # 进程状态
p(pcs.username())   # 进程用户名
p(pcs.create_time())    # 进程创建时间
# p(pcs.terminal())   # 进程终端 (报错...)
p(pcs.cpu_times())  # 进程使用的CPU时间
p(pcs.memory_info())    # 进程使用的内存
p(pcs.open_files())     # 进程打开的文件
p(pcs.connections())    # 进程相关网络连接
p(pcs.num_threads())    # 进程的线程数
p(pcs.threads())    # 进程所有线程信息
p(pcs.environ())    # 进程环境变量
# p(pcs.terminate())  # 结束进程

psutil.test()
