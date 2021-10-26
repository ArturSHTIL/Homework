from setuptools import setup

REQUIRED = ['beautifulsoup4>=4.10.0',
            'lxml>=4.6.3',
            'requests>=2.26.0',
            'setuptools>=56.0.0',
            'build>=0.7.0']

setup(
    name='rss_reader',
    version='1.0.2',
    py_modules=['rss_reader'],
    url='https://github.com/ArturSHTIL/Homework',
    description='Web Rss Parser',
    license='',
    author='Kalenik Arthur',
    author_email='arturshtill@gmail.com',
    test_suite='tests',
    include_package_data=True,
    install_requires=REQUIRED,
    entry_points={
        "console_scripts": [
            "rss_reader=rss_reader:main"
        ]
    },
)
