# -*- coding: utf-8 -*-
from flask import Flask,request,session,jsonify,redirect,url_for,make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer
import os
from wsgiref.simple_server import make_server
from flask_cors import CORS


app = Flask(__name__)
#数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:keyu0102@47.101.204.202/TheSecondhack?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
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


#研发数据表类
class User_yanfa(db.Model):
    __tablename__ = "yanfa_user" # 数据表的名字
    __table_args__ = {
        "mysql_collate":"utf8_general_ci"
    }
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=False)   #玩家分数

    # 定义一个类属性__mapper_args__，为order_by 的倒序排列
    __mapper_args__ = {
        "order_by":score.desc()
    }
    #定义后文的输出方式
    def __repr__(self):
        return ";username:%s;score:%s" %(self.username,self.score)
    # def to_json(self):
    #     dict = self.__dict__
    #     if "_sa_instance_state" in dict:
    #         del dict["_sa_instance_state"]
    #     return dict
    # def to_dict(self):
    #     return {c.name:getattr(self,c.name,None) for c in  self.__tablename__.Columns}
class User_xingzheng(db.Model):
    __tablename__ = "xingzheng_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数
    # 定义一个类属性__mapper_args__，为order_by 的倒序排列
    __mapper_args__ = {
        "order_by": score.desc()
    }
    # 定义后文的输出方式
    def __repr__(self):
        return "%s,%s" % (self.username, self.score)
#设计数据库类
class User_sheji(db.Model):
    __tablename__ = "sheji_user" # 数据表的名字
    id = db.Column(db.Integer, primary_key=True,nullable=False)# 玩家ID （无用）
    username = db.Column(db.String(100),nullable=False) #玩家名字
    score = db.Column(db.String(100),nullable=True)   #玩家分数
    # 定义一个类属性__mapper_args__，为order_by 的倒序排列
    __mapper_args__ = {
        "order_by": score.desc()
    }
    # 定义后文的输出方式
    def __repr__(self):
        return "%s,%s" % (self.username, self.score)
#产品数据库类
class User_chanpin(db.Model):
    __tablename__ = "chanpin_user"  # 数据表的名字
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 玩家ID （无用）
    username = db.Column(db.String(100), nullable=False)  # 玩家名字
    score = db.Column(db.String(100), nullable=True)  # 玩家分数
    # 定义一个类属性__mapper_args__，为order_by 的倒序排列
    __mapper_args__ = {
        "order_by": score.desc()
    }
    # 定义后文的输出方式
    def __repr__(self):
        return "%s,%s" % (self.username, self.score)
#运营数据库类
class User_yunying(db.Model):
    __tablename__ = "yunying_user"  # 数据表的名字
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 玩家ID （无用）
    username = db.Column(db.String(100), nullable=False)  # 玩家名字
    score = db.Column(db.String(100), nullable=True)  # 玩家分数
    # 定义一个类属性__mapper_args__，为order_by 的倒序排列
    __mapper_args__ = {
        "order_by": score.desc()
    }
    # 定义后文的输出方式
    def __repr__(self):
        return "%s,%s" % (self.username, self.score)
# @app.before_request  # 钩子
# def before_request():
#     print("HTTP {} {}".format(request.method, request.url))  # 符合 HTTP 的才可接受


@app.route('/api/ranking',methods=['POST'])
def if_or():
    group = request.form.get('group')
    score = request.form.get('score')
    username = request.form.get('userName')
    if group == '研发':
        #start_responce('200 OK',[('Contenttype-Type','text/html')])
        user = User_yanfa(username=username, score=score)
        db.session.add(user)
        db.session.commit()
        # 限制数量为 3
        rank = User_yanfa.query.limit(3).all()  # 利用order_by 查询倒叙排名前１０的username
        a = rank[0]
        onename = a.username
        onescore = a.score
        result1 = []
        b = rank[1]
        twoname =b.username
        twoscore =b.score
        #化为列表
        result1.append(b.__repr__())
        result_for = [str(i) for i in result1]
        result_for_str1 = ''.join(result_for)
        result2 = [3  ]
        c = rank[2]
        thirdname =c.username
        thirdscore=c.score
        my_rank = User_yanfa.query.filter_by(username=username).first_or_404()
        myName = my_rank.username
        myScore = my_rank.score
        return jsonify(
            {"0":
                 {'username':onename,
                  'rank':'1',
                  'score':onescore},
             "1":{'username':twoname,
                  'rank':'2',
                  'score':twoscore},
             "2":{'username':thirdname,
                  'rank':'3',
                  'score':thirdscore},
             "3":{'username':myName,
                  'rank':'?',
                  'score':myScore}
             }), 200


    elif group == '设计':
        user = User_sheji(username=username, score=score)
        db.session.add(user)
        db.session.commit()
        rank = User_sheji.query.limit(3).all()
        print(rank)
        a = rank[0]
        onename = a.username
        onescore = a.score
        b = rank[1]
        twoname = b.username
        twoscore = b.score
        c = rank[2]
        thirdname = a.username
        thirdscore = a.score
        my_rank = User_sheji.query.filter_by(username=username).first_or_404()
        myName = my_rank.username
        myScore = my_rank.score
        return jsonify(
            {"0":
                 {'username': onename,
                  'rank': '1',
                  'score': onescore},
             "1": {'username': twoname,
                   'rank': '2',
                   'score': twoscore},
             "2": {'username': thirdname,
                   'rank': '3',
                   'score': thirdscore},
             "3": {'username': myName,
                   'rank': '?',
                   'score': myScore}
             }), 200


    elif group == '行政':
        user = User_xingzheng(username=username, score=score)
        db.session.add(user)
        db.session.commit()
        rank = User_xingzheng.query.limit(3).all()
        print(rank)
        a = rank[0]
        onename = a.username
        onescore = a.score
        b = rank[1]
        twoname = b.username
        twoscore = b.score
        c = rank[2]
        thirdname = c.username
        thirdscore = c.score
        my_rank = User_xingzheng.query.filter_by(username=username).first_or_404()
        myName = my_rank.username
        myScore = my_rank.score
        return jsonify(
            {"0":
                 {'username': onename,
                  'rank': '1',
                  'score': onescore},
             "1": {'username': twoname,
                   'rank': '2',
                   'score': twoscore},
             "2": {'username': thirdname,
                   'rank': '3',
                   'score': thirdscore},
             "3": {'username': myName,
                   'rank': '?',
                   'score': myScore}
             }), 200

    elif group == '运营':

        user = User_yunying(username=username, score=score)
        db.session.add(user)
        db.session.commit()
        rank = User_yunying.query.limit(3).all()
        print(rank)
        a = rank[0]
        onename = a.username
        onescore = a.score
        b = rank[1]
        twoname = b.username
        twoscore = b.score
        c = rank[2]
        thirdname = c.username
        thirdscore = c.score
        my_rank = User_yunying.query.filter_by(username=username).first_or_404()
        myName = my_rank.username
        myScore = my_rank.score
        return jsonify(
            {"0":
                 {'username': onename,
                  'rank': '1',
                  'score': onescore},
             "1": {'username': twoname,
                   'rank': '2',
                   'score': twoscore},
             "2": {'username': thirdname,
                   'rank': '3',
                   'score': thirdscore},
             "3": {'username': myName,
                   'rank': '?',
                   'score': myScore}
             }), 200

    elif group == '产品':
        rank = User_chanpin.query.limit(3).all()
        user = User_chanpin(username=username, score=score)
        db.session.add(user)
        db.session.commit()
        print(rank)
        # 把 rank内的数据已类User_chapin内的形式作为返回值
        a = rank[0]
        onename = a.username
        onescore = a.score
        b = rank[1]
        twoname = b.username
        twoscore = b.score
        c = rank[2]
        thirdname = c.username
        thirdscore = c.score
        my_rank = User_chanpin.query.filter_by(username=username).first_or_404()
        myName = my_rank.username
        myScore = my_rank.score
        return jsonify(
            {"0":
                 {'username': onename,
                  'rank': '1',
                  'score': onescore},
             "1": {'username': twoname,
                   'rank': '2',
                   'score': twoscore},
             "2": {'username': thirdname,
                   'rank': '3',
                   'score': thirdscore},
             "3": {'username': myName,
                   'rank': '?',
                   'score': myScore}
             }), 200
# @app.route('/MyRank')
# def my_rank(mine):
#     return 'Your rank is %s'%(mine)
#@app.route('/yanfa',methods=['GET'])


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=8000)
    # #创建一个服务器，IP地址为空，端口为8000 处理函数就是databases
    # httpd = make_server('', 8000, if_or)
    # print("Serving HTTP on port 6000")
    # # 开始监听端口80000
    # httpd.serve_forever()