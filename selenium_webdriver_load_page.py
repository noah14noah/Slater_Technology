from time import sleep
from selenium import webdriver
from parsel import Selector
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd

# class
class LinkedInProfile:
    def __init__(self, user_name, highlightset, job_title, company, school):
        self.user_name = user_name
        self.highlightset = highlightset
        self.job_title = job_title
        self.company = company
        self.school = school

    def to_dict(self):
        output_dict = {'user_name': self.user_name, "highlightset": self.highlightset, "job_title": self.job_title,
                       "company": self.company, "school": self.school}
        return output_dict


# functions
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


# Generate input contact list from dataframe
input_investors = input(
    "Enter filename (including extension) of investors downlaodable: ")  # "Happynest_Comparables_Investors.xlsx"
investors = pd.read_excel(input_investors)
contact_list = investors["Primary Contact"]
contact_list.dropna(inplace=True)

# TODO: populate this file
file_name = 'results_file.csv'

# Inputs from user:
email_input = input("Pleae enter your LinkedIn login email: ")
password_input = input("Please enter LinkIn login password: ")

DRIVER_PATH = input("Enter Driver Path: ") #/Users/njjones14/PycharmProjects/Slater_Technology/chromedriver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

Output_path = input("Enter Output Path: ")  #/Users/njjones14/PycharmProjects/Slater_Technology/step_1.csv

# TODO: make sure that empty primary contacts are removed, and that there is no downstream consequences dor happynest_comparables.py
# Generate URLs
contact_dict = {}  # dictionary where keys = contact_list, value = url
contact_dict_output = {}
for contact in contact_list:
    if contact != "":
        driver.get('https:www.google.com')
        sleep(0.5)
        search_query = driver.find_element_by_name("q")
        print(contact)
        print(type(contact))
        search_query.send_keys("Linkedin " + str(contact) + " VC")  # TODO: do I add "VC" / "Capital"
        sleep(0.5)
        search_query.send_keys(Keys.RETURN)
        sleep(3)
        linkedin_urls = driver.find_elements_by_class_name('iUh30')  # class name for url of seach result
        # TODO: how do I only get the top valid search result?
        linkedin_urls = [url.text for url in linkedin_urls]
        top_result = linkedin_urls[0]
        print(top_result)

        count = 0
        for i in top_result[19:]:
            if (i.isspace()):
                count = count + 1
        if count == 0 and top_result[0:3] == "www":
            contact_dict[contact] = "https://www.linkedin.com/in/" + top_result[19:]
            print(contact_dict[contact])

        contact_dict_output[contact] = []
        sleep(0.5)

print(contact_dict)

# At this point we have a dictionary with names as keys and urls as values
driver.get('https://www.linkedin.com')

# Username
username = driver.find_element_by_name("session_key")
username.send_keys(email_input)
sleep(0.5)
# Password
password = driver.find_element_by_id('session_password')
password.send_keys(password_input)
sleep(0.5)
# Login button
login_in_button = driver.find_element_by_class_name("sign-in-form__submit-button")
login_in_button.click()
sleep(30)

for contact, linkedin_url in contact_dict.items():
    driver.get(linkedin_url)
    # add a 10 second pause loading each URL
    sleep(10)
    # assigning the source code for the webpage to variable sel
    sel = Selector(text=driver.page_source)
    name = sel.xpath("//li[contains(@class, 'inline')]").extract_first()
    print(name)
    print(type(name))
    if name is not None:
        name = cleanhtml(name)
        name = name.strip()
    print(name)
    sleep(1)
    # Hightlight
    highlightsSet = sel.xpath("//p[contains(@class, 'pv-highlight-entity__secondary-text')]").getall()
    print(highlightsSet)
    print(type(highlightsSet))
    h_list = []
    for h in highlightsSet:
        highlight = cleanhtml(h)
        h_list.append(highlight.strip())
        print(highlight.strip())
    sleep(1)
    job = sel.xpath("//h2[contains(@class, 'mt1')]").get()
    print(job)
    print(type(job))
    if job is not None:
        job = cleanhtml(job)
    if job:
        job = job.strip()
    print(job)
    sleep(1)
    company = sel.xpath("//span[contains(@class,'ml2')]").getall()
    if company:
        print(company)
        print(type(company))
        company_name = cleanhtml(company[0])
        company_name = company_name.strip()
    if len(company) == 2:
        school = cleanhtml(company[1])
    if school:
        school = school.strip()
    sleep(2)

    profile = [name, h_list, job, company_name, school]
    contact_dict_output[contact] = profile

print(contact_dict_output)
# AT this point I will have all the LInkedIn information for the investors, now I need to match to investor list from happynest_comparables.py
# output_df = pd.DataFrame(columns=["Name", "Profile"])

output_df = pd.concat(
    [pd.DataFrame([[name, profile]], columns=["Name", "Profile"]) for name, profile in contact_dict_output.items()],
    ignore_index=True)

print(output_df)

# compression_opts = dict(method='zip', archive_name='step_1.csv')
output_df.to_csv(path_or_buf=Output_path)
