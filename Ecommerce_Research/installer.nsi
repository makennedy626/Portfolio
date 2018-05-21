[Application]
name=twitter_scraper
version=1.0
# How to launch the app - this calls the 'main' function from the 'myapp' package:
entry_point=twitter_scraper:main
icon=twitter_scraper.ico

[Python]
version=3.6.3

[Include]
# Packages from PyPI that your application requires, one per line
# These must have wheels on PyPI:
pypi_wheels = requests==2.18.4
     beautifulsoup4==4.6.0
     html5lib==0.999999999

# To bundle packages which don't publish wheels, see the docs on the
# config file.

# Other files and folders that should be installed
files = LICENSE
    data_files/