from os import access, path, X_OK
import urlparse

def is_executable(path):
    return access(path, X_OK)

def uri_to_path(uri):
    p = urlparse.urlparse(uri)
    return path.abspath(path.join(p.netloc, p.path))
