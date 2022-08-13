# README
**author**: Stephen Stark

## Intro
This webscraper project is my take John Watson Rooney's webscraping tutorial **"Web Scraping with Python: 
Ecommerce Product Pages. In Depth including troubleshooting"** 
found here: [Link to YouTube](https://www.youtube.com/watch?v=nCuPv3tf2Hg&ab_channel=JohnWatsonRooney)

## Overview
Scraper.py the Whiskeys of the World found on The Whisky Exchange website \
found here: https://www.thewhiskyexchange.com/

<div align="center">
    <img src="/screenshots/whiskyexchange.jpg" title="Whiskyexchange.com" alt="Source site Whiskyexchange.com"></img> 
</div>

The whiskeys are scraped into a pandas DataFrame that is stored as a CSV in the 'output' directory. Two versions are 
saved, one for the latest run, and one in a folder with the current timestamp. I included this functionality so that 
historical scrapes are always preserved.

<div align="center">
    <img src="/screenshots/screen1.jpg" title="Sample Output" alt="Screenshot of the CSV output opened in excel to show 
the sample format."></img> 
</div>

