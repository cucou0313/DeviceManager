# -*- coding: utf-8 -*- 
"""
Project: DeviceManager
Author: guokaikuo
Create time: 2022-07-11 13:22
IDE: PyCharm
"""

from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Integer, String, TIMESTAMP, Text, ForeignKey
from sqlalchemy.pool import SingletonThreadPool

from Conf import config
from utils.mylogger import get_logger

logger = get_logger("model")

BaseModel = declarative_base()

# sqlalchemy 的sqlite多线程设置
engine = create_engine(config.SQLITE_SETTING,
                       poolclass=SingletonThreadPool,
                       connect_args={'check_same_thread': False})
DBSession = sessionmaker(bind=engine)  # 创建DBSession类型:类似数据库连接
session = DBSession()


# 用户
class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    email = Column(String(32))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):  # 将读取的数据和转化成字典
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


def init_db():
    """生成数据表"""
    BaseModel.metadata.create_all(engine)


def drop_db():
    """删除数据表"""
    BaseModel.metadata.drop_all(engine)


if __name__ == '__main__':
    init_db()

    admin = User('admin', 'admin@example.com')
    session.add(admin)
    guestes = [User('guest1', 'guest1@example.com'),
               User('guest2', 'guest2@example.com'),
               User('guest3', 'guest3@example.com'),
               User('guest4', 'guest4@example.com')]
    session.add_all(guestes)
    session.commit()
