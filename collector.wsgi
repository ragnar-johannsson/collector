import os
import site
import sys

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

def get_application():
    PYTHON_ENV_PATH = os.path.join(BASE_PATH, 'env')
    PYTHON_LIB_PATH = os.path.join(PYTHON_ENV_PATH, 'lib', 'python%d.%d' % sys.version_info[:2])
    PYTHON_SRC_PATH = os.path.join(PYTHON_ENV_PATH, 'src')
    SITE_PACKAGES_PATH = os.path.join(PYTHON_LIB_PATH, 'site-packages')

    sys.path.insert(0, BASE_PATH)
    sys.path.insert(1, SITE_PACKAGES_PATH)

    try:
        sys.path.extend((os.path.join(PYTHON_SRC_PATH, a) 
            for a in os.listdir(PYTHON_SRC_PATH)
            if os.path.isdir(os.path.join(PYTHON_SRC_PATH, a))))
    except OSError:
        pass

    site.addsitedir(SITE_PACKAGES_PATH)

    from server import app as application 
    return application

application = get_application()
