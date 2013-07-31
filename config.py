import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app3.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#CSRF_ENABLED = False
#SECRET_KEY = 'al;#(Lkjv089a)@L#($nmlaasd#$(@*&VL;ksdf;alksjd)*(UVsdf'
