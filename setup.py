import os
from setuptools import setup, find_packages


PACKAGES = find_packages()


opts = dict(name='groupby',
            version='0.1',
            description='Social media and calendar data analysis',
            long_description='Tools to visualize personal use of '
                                'social media platforms (Facebook, Twitter, '
                                'and LinkedIn) both individually and collectively '
                                'in relation to personal calendar data.',
            license=open('LICENSE').read(),
            url='https://github.com/UWSEDS-aut17/groupby',
            author='avantichande, agarwalpranay, jtkovacs, shibashish, shrawansher',
            packages=PACKAGES,
            # package_data={'savvy': ['sample_data_files/*.*',
            #        'sample_data_files/without_second_order_indices/*.*']},
            #include_package_data=True
            #install_requires=REQUIRES,
            #requires=REQUIRES
            test_suite='nose.collector',
            tests_require=['nose']
            )


if __name__ == '__main__':
    setup(**opts)