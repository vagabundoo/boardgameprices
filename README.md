# Boardgameprices

![Scrabble](./input/scrabble.jpeg)

This project was an exercise in getting data from two different sources, a CSV and an API, and then combining the data and making a set of functions that could be called from the command line. The workflow was as follows:

1. Import and some cleaning of the dataset (see **source/1-treatdata2019**)
2. Fetching additional data for the dataset from an API (see **source/2-fetch-data-with-api**)
3. Combining the data from both datasets (see **source/3-combineDFs-and-get-statistics**)
4. Storing these operations in a **functions.py** file to call from other files.

=> Using this dataset to create a python file with a series of functions that can be used to get information and listings on boardgames, and create a PDF with the top board games **main.py**

Type **$ python3 main.py -h**  
in the terminal (once the repo is cloned) to get started.

In addition, I have experimented with sending myself emails from python, with plain text (**source/send_email.py**) and with plots embedded in html (not working yet, **send_emailhtml**)
