import os

# Cấu hình DJANGO_SETTINGS_MODULE cho Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')

# Xử lý việc import MySQLdb, nếu không có thì sử dụng pymysql
try:
    import MySQLdb  # noqa: F401, imported for side effect
except ImportError:
    import pymysql

    pymysql.install_as_MySQLdb()

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Lấy ứng dụng WSGI
application = get_wsgi_application()
