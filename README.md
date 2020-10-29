# Slater_Technology
Webscraping

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

1. Make sure Python3 is downloaded on compute
2. Import packages
    1. “pip install <package>”
3. Import Deals and Investors list for relevant comparables list (ie. HappyNest) 
4. Delete ALL Cells in Excel spreadsheet besides rows, column titles 
5. Download Chrome and chromedriver. 
6. Make sure that all files are (including excel spreadsheets) are in the same directory. 
7. Open “Terminal” on computer 
8. Navigate to correct directory (cd <directory> = enter that directory, cd .. = go back, ls = list files/subdirectories in current directory)
9. Pip install packages
10. Run selenium_webdriver_load_page.py first
    1. In Terminal, “python3 selenium_web_driver.py”
    2. This will produce “step_1.csv” in Slater_Technoplogy directory 
    3. If you run into any problems
11. Next, run happynest_comparables.py
    1. In Terminal, “python3 happynest_comparables.py”
    2. Should return “data frame.csv” to directory
12. Finally, run relevancy_score.py
    1. In Terminal, “python3 relevancy_score.py”
    2. Should return "Ranked_LinkedIn_Output.xlsx” to directory 
13. Open “Ranked_LinkedIn_Output.xlsx” to see results and LinkedIn profile information

