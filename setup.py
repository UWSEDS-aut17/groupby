from os import path

try:
    from setuptools import setup, find_packages
except:
    from distutils.core import setup


PACKAGES = find_packages(exclude=['docs', 'tests'])


# Get long description from README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


opts = dict(name='groupby',
            version='0.1',
            description='Social media and calendar data analysis',
            long_description=long_description,
            license=open('LICENSE').read(),
            url='https://github.com/UWSEDS-aut17/groupby',
            author='avantichande, agarwalpranay, jtkovacs, shibashish, shrawansher',
            keywords='social_media personal_analytics',

            packages=PACKAGES,
            
            install_requires=['argparse', 
                              'arrow',
                              'bs4',
                              #'calendar',
                              #'collections', 
                              #'codecs',
                              'datetime',
                              'fpdf',
                              'icalendar',
                              #'io',
                              #'itertools',
                              'matplotlib',
                              'numpy',
                              'pandas',
                              'pyparsing',
                              #'ptyz',
                              #'re',
                              'seaborn',
                              #'subprocess',
                              'wordcloud'
                              ],
            package_data={'groupby':['data/*']},
            include_package_data=True,
            test_suite='nose.collector',
            tests_require=['nose'],
            scripts=['bin/groupby']
            )


if __name__ == '__main__':
    setup(**opts)