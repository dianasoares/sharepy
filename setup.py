import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from codecs import open

with open('shareplum/version.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name='Sharepy',
    version=version,
    description='Python SharePoint Library',
    long_description=open('README.rst').read(),
    url='https://github.com/dianasoares/sharepy',
    author='Jason Rollins | Diana Soares',
    author_email='soaresd32@hotmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Office/Business',
    ],
    keywords=['SharePoint'],
    packages=['sharepy'],
    install_requires=['lxml', 'requests', 'requests-ntlm', 'requests-toolbelt'],
)
