# -*- coding: utf-8 -*- 
"""
Project: DeviceManager
Author: guokaikuo
Create time: 2022-07-11 12:39
IDE: PyCharm
"""
import traceback

from flask import Flask, request
from Model.my_model import *
from utils.mylogger import get_logger

logger = get_logger("views")
app = Flask(__name__)
session = DBSession()


@app.route('/')
def index():
    return "Hello DeviceManager！"


# 查询
@app.route('/user', methods=["GET", "POST", "PUT", "DELETE"])
def user():
    try:
        # 127.0.0.1:12306/user?name=1&order=id asc
        if request.method == "GET":
            name = request.args.get("name",None)
            if name:
                res = session.query(User).filter(User.name == name).all()
            else:
                res = session.query(User).all()
            return {
                "msg": "get user success.",
                "errCode": 0,
                "data": [x.to_dict() for x in res]
            }
    except Exception as e:
        traceback.print_exc()
        logger.error(traceback.format_exc())
        return {"errMsg": str(e), "errCode": 1}


# 运行
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=12306)
