#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python 学习笔记 之 常用内建模块(4)
# struct

# 快速打印
from util import p
import struct

PATH_BMP = '../assets/struct.bmp'

sp1 = struct.pack('>I', 10242048)  # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
p(sp1)
# 后面的参数个数要和处理指令一致
sp2 = struct.unpack('>I', b'\x00\x9cH\x00')
p(sp2)
# bytes依次变为I：4字节无符号整数 和 H：2字节无符号整数
sp3 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
p(sp3)

with open(PATH_BMP, 'rb') as bmp:  # 打开一张bmp图
    bt = bmp.read(30)  # 读取前30字节
    # 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；c c
    # 一个4字节整数：表示位图大小；
    # 一个4字节整数：保留位，始终为0；
    # 一个4字节整数：实际图像的偏移量；
    # 一个4字节整数：Header的字节数；
    # 一个4字节整数：图像宽度；
    # 一个4字节整数：图像高度；
    # 一个2字节整数：始终为1；
    # 一个2字节整数：颜色数。
    sbmp = struct.unpack('<ccIIIIIIHH', bt)
    p(sbmp)

# ----------------------------------struct字符处理集------------------------------------
# Format    	C Type 	            Python type 	    Standard size 	    Notes
#   x 	        pad                 byte 	            no                  value
#   c 	        char 	            bytes of length     1 	                 1
#   b 	        signed char 	    integer 	        1 	                (1),(3)
#   B 	        unsigned char 	    integer 	        1 	                (3)
#   ? 	        _Bool 	            bool 	            1 	                (1)
#   h 	        short 	            integer 	        2 	                (3)
#   H 	        unsigned short 	    integer 	        2 	                (3)
#   i 	        int 	            integer 	        4 	                (3)
#   I 	        unsigned int 	    integer 	        4 	                (3)
#   l 	        long 	            integer 	        4 	                (3)
#   L 	        unsigned long 	    integer 	        4 	                (3)
#   q 	        long long 	        integer 	        8 	                (2), (3)
#   Q 	        unsigned long-long 	integer 	        8 	                (2), (3)
#   n 	        ssize_t 	        integer 	  	                        (4)
#   N 	        size_t 	            integer 	  	                        (4)
#   e 	        (7) 	            float 	            2 	                (5)
#   f 	        float 	            float 	            4 	                (5)
#   d 	        double 	            float 	            8 	                (5)
#   s 	        char[]          	bytes
#   p 	        char[] 	            bytes
#   P  	        void * 	            integer 	  	                        (6)
