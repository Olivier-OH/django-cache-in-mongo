from setuptools import setup, find_packages

setup(
    name='django-cache-in-mongo',
    version='1.0',
    packages=['django_cache_in_mongo'],
    package_dir={'django_cache_in_mongo': 'django_cache_in_mongo'},
    provides=['django_cache_in_mongo'],
    include_package_data=True,
    url='https://github.com/Olivier-OH/django_cache_in_mongo',
    license=open('LICENSE').read(),
    author='Olivier Hoareau',
    author_email='olivier.p.hoareau@gmail.com',
    maintainer='Olivier Hoareau',
    maintainer_email='olivier.p.hoareau@gmail.com',
    description='Provides caching ability through MongoDB. Forked from django_mongodb_cash_backend.',
    long_description=open('README.md').read(),
    install_requires=[
        'Django~=1.11.13',
        'pymongo~=3.6.1'
    ],
    keywords=[
        'django',
        'web',
        'cache',
        'mongodb'
    ],
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development'
    ],
)
