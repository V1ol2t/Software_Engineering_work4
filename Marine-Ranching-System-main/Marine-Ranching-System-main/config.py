import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'gsolvit'

    @staticmethod
    def init_app(app):
        pass

config={
    'default':Config,
    'MYSQL_PASSWORD':'1234',
    'DATABASE_NAME':'marineranching_system'
}