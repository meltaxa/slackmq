from os.path import join, dirname
from setuptools import setup

__version__ = open(join(dirname(__file__), 'VERSION')).read().strip()

install_requires = (
    'slacker>=0.9.50'
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='slackmq',
    py_modules=['slackmq'],
    version=__version__,
    description='A Slack Message Queue system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Dennis Mellican',
    author_email='dennis@mellican.com',
    url='https://github.com/meltaxa/slackmq',
    license='MIT',
    include_package_data=True,
    install_requires=install_requires,
    classifiers=['Development Status :: 4 - Beta',
                  'License :: OSI Approved :: MIT License',
                  'Operating System :: OS Independent',
                  'Programming Language :: Python',
                  'Programming Language :: Python :: 2',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3',
                  'Programming Language :: Python :: 3.4',
                  'Programming Language :: Python :: 3.5',
                  'Programming Language :: Python :: 3.6'])
