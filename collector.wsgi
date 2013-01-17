import os
import site
import sys

def get_application():
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    PYTHON_LIB_PATH = os.path.join(BASE_PATH, 'env', 'lib', 'python%d.%d' % sys.version_info[:2])
    PYTHON_SRC_PATH = os.path.join(BASE_PATH, 'src')
    SITE_PACKAGES_PATH = os.path.join(PYTHON_LIB_PATH, 'site-packages')

    sys.path.insert(0, BASE_PATH)
    sys.path.insert(1, SITE_PACKAGES_PATH)
    sys.path.insert(2, PYTHON_SRC_PATH)

    site.addsitedir(SITE_PACKAGES_PATH)

    from config import resources
    from mdb import initdb
    initdb(resources)

    from server import app as application
    return application

application = get_application()
