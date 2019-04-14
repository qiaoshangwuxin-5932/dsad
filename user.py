# -*- coding: utf-8 -*-

from flask import Flask,request,session,flash,jsonify,make_response,flash
from sqlalchemy import Column,String,Integer
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import *
app = Flask(__name__)
CORS(app,supports_credentials=True)
CORS(app, resources=r'/*')
def res():
    result_text = {"status": 200,}
    response = make_response(jsonify(result_text))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
    response.hearder['Access-Control-Allow-Origin'] ="*"
    return response
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SECRET_KEY'] = 'hackwekk'
# app.secret_key = 'hackweek'
# app.config.update(SECRET_KEY = 'hackweek')
#数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:keyu0102@47.101.204.202/TheSecondhack?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# 5 个数据库　分五个储存
class User_xingzheng(db.Model):
    __tablename__ = "xingzheng_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数
class User_sheji(db.Model):
    __tablename__ = "sheji_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数
class User_yanfa(db.Model):
    __tablename__ = "yanfa_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(500),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数
class User_chanpin(db.Model):
    __tablename__ = "chanpin_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数
class User_yunying(db.Model):
    __tablename__ = "yunying_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数


# @app.before_request  # 钩子
# def before_request():
#     print("HTTP {} {}".format(request.method, request.url))  # 符合 HTTP 的才可接受
@app.route('/ada',methods=['POST'])
def ada():
    return "hello world"
# 账户提交
@app.route('/api/game_user',methods=['POST'])
def login(*args,**kwargs):
    username = request.form.get("username")
    print(username)
    check_username = User_yanfa.query.filter_by(username=username).first()
    if check_username:

        return jsonify({
            "success":'1'
        })
    else:
        check_username = User_sheji.query.filter_by(username=username).first()
        if check_username:
            return jsonify({
                'success':'False'
            })
        else:
            check_username = User_xingzheng.query.filter_by(username=username).first()
            if check_username:
                return jsonify({
                    'success':'1'
                })
            else:
                check_username = User_yunying.query.filter_by(username=username).first()
                if check_username:
                    return jsonify({
                        'success': '1'
                    })
                else:
                    check_username = User_chanpin.query.filter_by(username=username).first()
                    if check_username:
                        return jsonify({
                            'success': '1',
                        })
                    else:
                        return jsonify({
                            'success':'0'
                        }),200



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    # username = request.form.get('username')
    # #研发提交
    # if group == "研发":
    #     #check_username = User_yanfa.query.filter_by(username=username).first()
    #     # if check_username:          #判断是否　
    #     #     return 'your username have been logined'  # 返回小错误
    #     # else:
    #
    #  设计提交
    # elif group == "设计":
    #     check_username = User_sheji.query.filter_by(username=username).first()
    #     if check_username:          #判断是否　
    #          return 'your username have been logined'  # 返回小错误
    #     else:
    #
    #      行政　提交
    #
    # elif group == "行政":
    #     check_username = User_xingzheng.query.filter_by(username=username).first()
    #     if check_username:           #判断是否　
    #         return 'your username have been logined'  # 返回小错误
    #     else:
    #
    #
    # # 产品提交
    # elif group == "产品":
    #      check_username = User_chanpin.query.filter_by(username=username).first()
    #      if check_username:           #判断是否　
    #          return 'your username have been logined'  # 返回小错误
    #      else:
    #
    #
    # # 运营提交
    # elif group == "运营":
    #     check_username = User_yunying.query.filter_by(username=username).first()
    #     if check_username:  # 判断是否　
    #         return 'your username have been logined'  # 返回小错误
    #     else:
    #
    # return 'xxx'
# 比分提交
# @app.route('/api/score',methods=['POST'])
# def score():
#
#     username = request.form.get('username')
#     group = request.form.get('group')
#     score = request.form.get('score')
#     if group == '研发':
#
#         user = User_yanfa(username=username,score=score)
#         db.session.add(user)
#         db.session.commit()
#         return jsonify({
#             'success':'True',
#             'message':'Your username and score(yanfa) have been submited'
#         })

        # user = User_yanfa.query.filter_by(username=username).first()
        # user.score = score
        # db.session.commit()
    # else:
    #     if group == '设计':
    #         user = User_sheji(username=username,score=score)
    #         db.session.add(user)
    #         db.session.commit()
    #         return jsonify({
    #             'success': 'True',
    #             'message': 'Your score and username(sheji) have been submited'
    #         })
    #     else:
    #         if group == '运营':
    #             user = User_yunying(username=username,score=score)
    #             db.session.add(user)
    #             db.session.commit()
    #             return jsonify({
    #                 'success': 'True',
    #                 'message': 'Your username and score(yunying）have been submited'
    #             })
    #         else:
    #             if group == '行政':
    #                 user = User_xingzheng(username=username,score=score)
    #                 db.session.add(user)
    #                 db.session.commit()
    #                 return jsonify({
    #                     'success': 'True',
    #                     'message': 'Your username and score(xingzheng) have been submited'
    #                 })
    #
    #             else:       #产品分数的提交
    #                 user = User_chanpin(username=username,score=score)
    #                 db.session.add(user)
    #                 db.session.commit()
    #                 return jsonify({
    #                     'success': 'True',
    #                     'message': 'Your username and score(chanpin) have been submited'
    #                 })
    #


