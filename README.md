# README
**author**: Stephen Stark

## Intro
"Scraper.py" scrapes "Whiskeys of the World" found on The Whisky Exchange website \
[www.thewhiskyexchange.com](https://www.thewhiskyexchange.com/) into a CSV filed stored in the "output" directory


## Overview
This webscraper project is my take John Watson Rooney's webscraping tutorial **"Web Scraping with Python:
Ecommerce Product Pages. In Depth including troubleshooting"**
found here: [Link to YouTube](https://www.youtube.com/watch?v=nCuPv3tf2Hg&ab_channel=JohnWatsonRooney)

## Source Website
<div align="center">
    <img src="/screenshots/whiskyexchange.jpg" title="Whiskyexchange.com" alt="Source site Whiskyexchange.com"> 
</div>


<div align="center">
    <img src="/screenshots/whiskyexchange.jpg" title="Whiskyexchange.com" alt="Source site Whiskyexchange.com">
[Sample Breadcrumb](/screenshots/breadcrumb.jpg)
</div>

<div align="center">
    <img src="/screenshots/breadcrumb.jpg" title="Whiskyexchange.com" alt="Source site Whiskyexchange.com"> 
</div>

The whiskeys are scraped into a pandas DataFrame that is stored as a CSV in the 'output' directory. Two versions are 
saved, one for the latest run, and one in a folder with the current timestamp. I included this functionality so that 
historical scrapes are always preserved.

<div align="center">
    <img src="/screenshots/screen1.jpg" title="Sample Output" alt="Screenshot of the CSV output opened in excel to show 
the sample format.">
</div>

