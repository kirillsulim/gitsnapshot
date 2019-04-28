from setuptools import setup
from os import path
from encodings import utf_8


project_directory = path.abspath(path.dirname(__file__))


def load_from(file_name):
    with open(path.join(project_directory, file_name), encoding=utf_8.getregentry().name) as f:
        return f.read()

setup(
    name='gitsnapshot',
    version='0.1.1post1',
    description='Python module to simplify loading of snapshot of git repository',
    long_description=load_from('README.md'),
    long_description_content_type='text/markdown',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    license='MIT',
    url='https://github.com/kirillsulim/gitsnapshot',
    py_modules=['gitsnapshot'],
    test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Version Control :: Git',
    ],
    keywords='git snapshot load download delivery config',
)
