from setuptools import setup

def readme():
    with open('readme.rst') as f:
        return f.read()

setup(name='sequentialOSM',
    version='0.1',
    description='',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3.2',
    ],
    keywords='osm sequential generator',
    url='https://github.com/scubbx/sequential-osm',
    author='Markus Mayr',
    author_email='markusmayr@gmx.net',
    license='MIT',
    packages=['sequentialOSM'],
    zip_safe=False)
