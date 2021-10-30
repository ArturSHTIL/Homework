# Parser for RSS pages
This project is designed to parse RSS feeds and convert them in a more concise view (simple text or json). 
It offers command-line interface to run RSS parsing

## Requirements
To run the rss parser you need the following:
* Python 3.9+
* Internet Access


## Features
RSS parser has the following features:
* RSS version 2.0 support
* simple text representation of RSS feed in the console
* export RSS news as a JSON String (`--json` parameter)
* limit to a number of items to view (`--limit` parameter)

## Setup instructions
To install RSS parser you need to install a package from `dist` directory using `pip`:
* `pip install .\dist\rss_reader-1.0.2-py3-none-any.whl`


## Usage
Please follow setup instructions above before using RSS parser.

To run RSS Reader please use `rss_reader`:
```
Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      show program's version number and exit
  --json         Print result as JSON in stdout
  --to-html      Print result as HTML in stdout
  --to-pdf       Save RSS as pdf in current directory
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided
  --date DATE    
```
Command line parameters:
* `source` (required) - URL link to RSS feed
* `--limit` - limit a number of articles shown if specified option. All articles are shown by default
* `--json` - format RSS feed as JSON string if specified. Simple text representation is used by default 
* `--version` - print the version and exits the program
* `--verbose` - show all logs in the console while the application is running
* `--date` - show the articles by date from local storage
* `--to-pdf` - export RSS feed to PDF
* `--to-html` - format RSS feed as HTML

Example:
```
rss_reader https://www.theguardian.com/uk/rss --limit 2

Rss feed title: The Guardian
Rss feed link: https://www.theguardian.com/uk
Rss feed description: Latest news, sport, business, comment, analysis and reviews from the Guardian, the world's leading liberal voice
Rss feed date: Mon, 25 Oct 2021 09:19:49 GMT

title: Sajid Javid ‘leaning towards’ mandatory Covid jab for NHS staff
link: https://www.theguardian.com/world/2021/oct/25/sajid-javid-leaning-towards-mandatory-covid-jab-nhs-staff
date: Mon, 25 Oct 2021 08:15:27 GMT
description: Health secretary yet to make final decision on whether to bring NHS in line with care home sector in EnglandCoronavirus – latest updatesSee all ou
r coronavirus coverageNHS staff have been warned they could face a mandatory requirement to be vaccinated against Covid, with the health secretary saying he is
 “leaning towards” making the jabs compulsory for staff in England.Sajid Javid said he had not made a final decision, but the move would put NHS staff in Engla
nd broadly in line with the requirement for care home workers. Continue reading...

title: Children’s obesity linked to England’s health disparities, study finds
link: https://www.theguardian.com/society/2021/oct/25/childrens-obesity-linked-to-englands-health-disparities-study-finds
date: Mon, 25 Oct 2021 08:41:18 GMT
description: Exclusive: one in 12 cases could be avoided if health outcomes in worst parts were improved to match bestHundreds of thousands of children in Engl
and are growing up overweight or obese because of widening health disparities across the country, analysis suggests.Child obesity has proliferated in recent ye
ars for a variety of reasons. Children live increasingly sedentary lifestyles, where physical activity has fallen and activities such as watching TV, playing v
ideo games and spending time on phones have increased. Continue reading...

```
### RSS format details
The following information from RSS is shown to the user:
* title - title of an RSS feed or an RSS article
* link - link to an RSS feed or an RSS article
* date - date and time of publication for an RSS feed or an RSS article
* description - more detailed description of an RSS feed or an RSS article

## Development setup
### Development setup instructions
To install dependencies and start working on RSS reader please follow these steps:
1. Create a virtual environment - `python -m venv my_venv`
2. Activate the virtual environment from step 2:
  - Windows - `.\my_venv\Scripts\activate.bat` or `.\my_venv\Scripts\activate.ps1` depending on the console you are using
  - Linux - `source my_venv/Scripts/activate`
3. Install dependencies - `pip install -r requirements.txt`
4. Now you can run the RSS parser using the dedicated virtual environment created on step 1 (make sure it was activated) - `python .\rss_reader.py https://www.theguardian.com/uk/rss --limit 2`

### How to run tests
To run tests please use the following command in the terminal in root directory of the project:
```
python -m unittest discover tests
```

### Building package
To build the package please use the following commands:
1. Create a virtual environment (if not exists) and activate it
2. Build the package - `py -m build`
3. Now `dist` directory contains your package

### Dependencies
The following libraries are used during development (please see [requirements.txt](requirements.txt) for more details):
* `beautifulsoup4>=4.10.0`
* `lxml>=4.6.3`
* `requests>=2.26.0`
* `setuptools>=56.0.0`
* `build>=0.7.0`
