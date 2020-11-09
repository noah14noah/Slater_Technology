# Slater_Technology_Lead_Generator

Selenium-based webscraping tool to return relevant investors and LinkedIN profile data for primary contacts at investment firms. Takes Pitchbook Excel data. 

Dependencies: 

    numpy==1.19.2
    pandas==1.1.2
    pandasgui==0.2.3.5
    selenium==3.141.0
    parsel==1.6.0
    regex==2020.7.14
    
Instructions for Slater Tech: 

1. Make sure Python3 is downloaded on computer
2. Import Deals and Investors list for relevant comparables list (ie. HappyNest) 
3. Delete ALL Cells in Excel spreadsheet besides rows, column titles 
4. Download Chrome and chromedriver. 
5. Clone repo
    1. “Code” 
    2. Copy to Clipboard 
    3. git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    4. “Enter”
6. Make sure that all files are (including excel spreadsheets) are in the same directory. 
7. Open “Terminal” on computer 
8. Navigate to correct directory (cd <directory> = enter that directory, cd .. = go back, ls = list files/subdirectories in current directory)
9. Pip install packages
10. Run selenium_webdriver_load_page.py first
    1. In Terminal, “python3 selenium_web_driver.py”
    2. This will produce “step_1.csv” in Slater_Technoplogy directory 
11. Next, run happynest_comparables.py
    1. In Terminal, “python3 happynest_comparables.py”
    2. Should return "Ranked_LinkedIn_Output.xlsx” to directory 


Troubleshooting: 

Probably you will run into most problems with LinkedIn web-scraping. As a good first step, I would login LinkedIn before attempting this process. This will ensure that we don’t run into any verification issues. 
