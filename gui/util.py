__author__ = 'Anuj'
import os
import errno


def create_dir_path(folderpath):
    try:
        if not folderpath:
            return
        path = os.path.normpath(folderpath)
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise OSError(exception)
    except Exception, e:
        raise Exception(e)


