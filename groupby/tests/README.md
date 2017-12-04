#### Unit tests

This directory contains unit tests to ensure that code is performing as expected. Run these tests from the command line or with `run.sh` as specified in the [project README:](https://github.com/UWSEDS-aut17/groupby/blob/master/README.md)

```Bash
nosetests --with-coverage --cover-package=groupby/groupby.py groupby/tests/test_groupby.py
nosetests --with-coverage --cover-package=groupby/facebook.py groupby/tests/test_facebook.py
nosetests --with-coverage --cover-package=groupby/linkedin.py groupby/tests/test_linkedin.py
nosetests --with-coverage --cover-package=groupby/twitter.py groupby/tests/test_twitter.py
nosetests --with-coverage --cover-package=groupby/gcal.py groupby/tests/test_gcal.py
```
