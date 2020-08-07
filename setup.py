from setuptools import setup, find_packages

classifiers = [
        'Developoment Status :: 5 - Production / Stable',
        'Intended Audiance :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
]

setup(
    name='Calculator',
    version='0.0.1',
    description='Short Description, A very basic calulator',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Open Source Contribution',
    author_email='bibhurox@gmail.com',
    License='MIT License',
    classifiers=classifiers,
    keywords='calculator',
    packages=find_packages(),
    install_requires=['']

)