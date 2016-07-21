
##Installation

This project was coded using Python 2.7 on a Mac.

Make sure you have the following installed

- Python 2.7
- pip
- MongoDB
- wget
 

Please follow the following prereqs to setup everything

- `pip install -r requirements.txt`
- `chmod u+x *.sh`
- `./download.sh`
- `python sample.py`
- `python data.py`




##Files
- `data/`: All datasets fils
- `audit.py`: audits streets and zipcodes, also provides cleaning methods
- `data.py`: Cleans the osn data, shapes it for import into MongoDB
- `count_tag.py`: counts occurence of each tag
- `db.conf`: MongoDB config file
- `requirements.txt`: contains list of Python packages used for the project
- `README.md`: this file
- `run.sh`: Bash script to boot MongoDB
- `final.pdf`: PDF format Report.ipynb
- `sample.py`: Samples a part of the OSM Data
- `scrape.py`: Scrapes street suffixes from the web for cleaning data later
- `tags.py`: script for exploring data