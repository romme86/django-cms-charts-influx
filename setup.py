import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms_influx_charts',
    version='1.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='DjangoCMS Plugin to add and edit ChartJs charts extended with live data update from influxDB',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/romme86/djangocms_influx_charts',
    author='Francesco Romeo based on the work of Michael Carder Ltd',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'six',
        'django>=1.11',
        'django-cms>=3.4',
    ],
    package_data={
        'readme': ['README.rst'],
        'license': ['LICENSE']
    },
)

