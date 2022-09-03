from selenium import webdriver
from multiprocessing import Pool

# I remove global driver because you cannot use shared driver in multiprocess.
def browser():  
    driver = webdriver.Chrome()
    return driver
 
def test_func(link):
    driver = browser()  # Each browser use different driver.
    driver.get(link)

def multip():
    links = ["https://stackoverflow.com/", "https://signup.microsoft.com/"]
    pool = Pool(processes=3)
    for i in range(0, len(links)):  
        pool.apply_async(test_func, args={links[i]})

    pool.close()
    pool.join()
    
# if name == ' main ': multip()