# Slater_Technology
Webscraping tool to return relevant investors and LinkedIN profile data for primary contacts at investment firms. Takes Pitchbook Excel data. 

Dependencies: 

selenium_webdriver_load_page.py: 

    from time import sleep
    from selenium import webdriver
    from parsel import Selector
    from selenium.webdriver.common.keys import Keys
    import re
    import pandas as pd

happynest_comparables.py: 

    import pandas as pd  
    import numpy as np  
    import pickle


Installation Instructions: 
1. Make sure Python3 is downloaded on computer
2. Import Deals and Investors list for relevant comparables list (ie. HappyNest) 
3. Delete ALL Cells in Excel spreadsheet besides rows, column titles 
4. Download Chrome and chromedriver. 
5. Make sure that all files are (including excel spreadsheets) are in the same directory. 
6. Open “Terminal” on computer 
7. Navigate to correct directory (cd <directory> = enter that directory, cd .. = go back, ls = list files/subdirectories in current directory)
8. Pip install packages
9. Run selenium_webdriver_load_page.py first
    1. In Terminal, “python3 selenium_web_driver.py”
    2. This will produce “step_1.csv” in Slater_Technoplogy directory 
    3. If you run into any problems
10. Next, run happynest_comparables.py
    1. In Terminal, “python3 happynest_comparables.py”
    2. Should return "Ranked_LinkedIn_Output.xlsx” to directory 
11. Open “Ranked_LinkedIn_Output.xlsx” to see results and LinkedIn profile information

