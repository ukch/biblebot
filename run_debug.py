import os
import subprocess

heroku = 'heroku'

# Yuck! Nasty local import. But what choice do I have?
from app import app

# Preserve data integrity on the host
BLACKLISTED = frozenset(['REDISTOGO_URL'])


if __name__ == '__main__':
    data = subprocess.check_output([heroku, 'config'])
    for line in data.strip().split(os.linesep)[1:]:
        try:
            key, value = line.split(':', 1)
        except ValueError:
            print line
            raise
        if key in BLACKLISTED:
            print 'Ignoring blacklisted variable {}'.format(key)
            continue
        os.environ[key] = value.strip()
    app.debug = True
    app.run()
