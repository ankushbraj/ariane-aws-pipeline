from setuptools import setup, find_packages

setup(
    name='awscoreml',
    version='0.0.1rc0',

    # Package data
    packages=find_packages(),
    include_package_data=True,

    # Insert dependencies list here
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'nltk',
        'Keras',
        'tensorflow',
        'matplotlib',
        'flask',
        'gevent',
        'gunicorn',
        'boto3'
    ],

    entry_points={
       "awscoreml.training": [
           "train=awscoreml.train:entry_point",
       ],
        "awscoreml.hosting": [
           "serve=awscoreml.server:start_server",
       ]
    }
)


'''
Traceback (most recent call last):
File "/opt/run.py", line 1, in <module>
from awscoreml.train import entry_point
File "/usr/local/lib/python3.6/site-packages/awscoreml/train.py", line 14, in <module>
from resolve import paths

ModuleNotFoundError: No module named 'resolve'
'''