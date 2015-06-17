StaatsbladScraper
=====
Scrapy example with complex navigation.

Gets addresses from http://www.ejustice.just.fgov.be/tsv/tsvn.htm for new companies. This is a demonstration of the use of scrapy, not to use the scraped data as this could be a violation of the privacy laws.
Every company that is not a sole proprietorship is published in the "Belgian Law Gazette" (Staatsblad). Because of the way the website is constructed it was a challenge to see if I could do it. This is the result.

Setup
=====

Install the Python package 'virtualenv':

    sudo pip install virtualenv

Create a virtual environment for Python libraries:

    virtualenv venv

Activate the virtual environment:

    source ./venv/bin/activate

Install the Python library dependencies of this repo:

    pip install -r requirements.txt

Run the script:

    python staatsblad_scaper.py -f 2015-06-01 -t 2015-06-17 testset_postcodes.csv



