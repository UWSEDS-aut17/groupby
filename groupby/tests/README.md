This directory contains tests to ensure that code is performing as expected.

Run these tests from the command line: 

```Bash
nosetests --with-coverage --cover-package=utils groupby/tests/test_groupby.py
nosetests --with-coverage --cover-package=utils groupby/tests/test_facebook.py
nosetests --with-coverage --cover-package=utils groupby/tests/test_linkedin.py
nosetests --with-coverage --cover-package=utils groupby/tests/test_twitter.py
nosetests --with-coverage --cover-package=utils groupby/tests/test_gcal.py
```
