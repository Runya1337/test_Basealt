from setuptools import setup, find_packages

setup(
    name='package_comparator',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'packaging',
        'rpm'

    ],
    entry_points='''
        [console_scripts]
        compare-packages=package_app.cli:main
    ''',
    author='Ainur',
    author_email='ainurnurtdinov1337@gmail.com',
    description='Сравнивает пакета двух предложенных бранчей',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Runya1337/test_Basealt',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)