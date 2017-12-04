import os
from setuptools import setup, find_packages
PACKAGES = find_packages()


opts = dict(name='groupby',
            description='social media and calendar data analysis',
            long_description=LONG_DESCRIPTION,
            license=open('LICENSE').read(),
            author='jtkovacs, avantichande, shibashish, agarwalpranay, shrawansher',
            packages=['groupby', 'groupby/tests'],
            # package_data={'savvy': ['sample_data_files/*.*',
            #        'sample_data_files/without_second_order_indices/*.*']},
            #include_package_data=True
            #install_requires=REQUIRES,
            #requires=REQUIRES
            )


if __name__ == '__main__':
setup(**opts)