class Config():
    SECRET_KEY = "abc1"
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/kimis" #usuario yy contraseña, local + bdname
    SQLALCHEMY_TRACK_MODIFICATIONS = False