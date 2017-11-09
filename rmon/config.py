""" rmon.config

rmon 配置文件
"""
import os

class DevConfig:
    """开发环境配置
       """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_DATABASE_URL = 'sqlite://'  #用于连接数据的数据库
    TEMPLATES_AUTO_RELOAD = True

class ProductConfig(DevConfig):
    """生产环境配置
       """
    DEBUG = False
    path = os.path.join(os.getcwd(),'rmon.db').replace('\\','/')
    SQLALCHEMY_DATABASE_URL = 'sqlite:///%s' %path
