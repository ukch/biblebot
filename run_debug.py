import os
import subprocess

heroku = 'heroku'

# Yuck! Nasty local import. But what choice do I have?
from app import app

if __name__ == '__main__':
    data = subprocess.check_output([heroku, 'config'])
    for line in data.strip().split(os.linesep)[1:]:
        try:
            key, value = line.split(': ')
        except ValueError:
            print line
            raise
        os.environ[key] = value
    app.debug = True
    app.run()
