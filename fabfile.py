from fabric.api import local

def test():
    local("./manage.py test --settings=lima_backoffice.settings.tests ./tests")