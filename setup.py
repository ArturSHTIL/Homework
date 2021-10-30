from setuptools import setup, find_packages

REQUIRED = ['beautifulsoup4>=4.10.0',
            'lxml>=4.6.3',
            'requests>=2.26.0',
            'setuptools>=56.0.0',
            'build>=0.7.0',
            'python-dateutil']

setup(
    name='rss_reader',
    version='1.0.3',
    packages=find_packages(include=['rss_reader', 'rss_reader.*']),
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
            "rss_reader=rss_reader.rss_reader_base:main"
        ]
    },
)
