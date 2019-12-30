# beautifulsoupWithPython
__Date of Project:__ April 2019

This is a project on XML parsing using Beautifulsoup 4 in Python. I have written a script that extracts media attributes (Bitrate, Type, Height, Width, Link etc.) from a VAST 3.0 _XML_ file and makes a dataframe using Pandas package which is then extracted to both _csv_ and _xlsx_ formats. This script scans the current directory and walks the directory as a tree with current as the root to find all available XML files. There are also two formats of Bitrates which are handled via _try/catch_ blocks.

# Instructions for environment setup:
* Install __Python 3.x.x__ using [Python downloads page](https://www.python.org/downloads/) and selecting your operating system and latest stable release
* Install __Pandas__ in Python using `[sudo] pip install pandas`
* Install __BeautifulSoup4__ in Python using `[sudo] pip install beautifulsoup4`

# Execution instructions:
`python XML_Parser.py`
