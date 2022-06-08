from application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='主键')
    nickname = db.Column(db.String(30, 'utf8mb4_0900_ai_ci'), nullable=False, info='昵称')
    login_name = db.Column(db.String(20, 'utf8mb4_0900_ai_ci'), nullable=False, unique=True, info='登陆用户名')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='插入时间')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='最后一次更新时间')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='状态 0: 无效  1: 有效')
    login_salt = db.Column(db.String(32), nullable=False, info='登陆密码随机字符串')
    login_pwd = db.Column(db.String(32), nullable=False, info='登陆密码')
