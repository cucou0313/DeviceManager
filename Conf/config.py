# -*- coding: utf-8 -*- 
"""
Project: DeviceManager
Author: guokaikuo
Create time: 2022-07-11 13:17
IDE: PyCharm
"""

import os

"""
logger配置
"""
# 日志级别
LogLevel = 'DEBUG'
# 日志目录
LogPath = os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) + os.sep + "logs"

"""
DataBase配置
"""
# sqlite3
SQLITE_SETTING = 'sqlite:///{path}{db}'.format(path=os.path.dirname(os.path.dirname((os.path.abspath(__file__))))+ os.sep,
                                                db='DeviceManager.db')  # 相对路径


if __name__ == '__main__':
    print(SQLITE_SETTING)