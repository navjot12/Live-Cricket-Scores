#Live Cricket Scores Terminal App

###### A python script that brings cricket scores right into your terminal in real time!

Since there is no proper API available for cricket scores, this python script scrapes www.espncricinfo.com to get scores of live cricket matches and presents them in a well formatted manner in the terminal!

Version 2.0 brings bowling scorecards and a better UX.

The script has been carefully crafted to handle improper inputs for flawless user experience.

The code might seem crazy to look at as there has been a lot of scraping, cleaning and formatting of data. Further more, bowling scorecards have been directly extracted from the html code without the use of beautiful-soup. This has been done since the tables containing bowling scorecards were not extractable from beautiful-soup.
