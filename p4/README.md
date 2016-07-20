
##Installation

This project was coded using Python 2.7 on a Mac.

Make sure you have the following installed

- Python 2.7
- pip
- MongoDB
- wget
 

Please follow the following prereqs to setup everything

- `chmod u+x *.sh`
- `./download.sh`
- `python sample.py`
- `python data.py`




##Files
- `data/`: data files and output from scripts (`austin.osm` and `austin.osm.json` excluded)
- `audit.py`: audits streets and zipcodes, also provides cleaning methods
- `data.py`: Cleans the osn data, shapes it for import into MongoDB
- `mapparser.py`: parses the OSM file and provides insight on tag data
- `db.conf`: MongoDB config file
- `requirements.txt`: contains list of Python packages used for the project
- `README.md`: this file
- `run.sh`: Bash script to boot MongoDB
- `submission.pdf`: PDF format of this document
- `sample.py`: Samples a part of the OSM Data
- `scrape.py`: Scrapes street suffixes from the web for cleaning data later
- `tags.py`: script for conducting exploratory data analysis on tag data