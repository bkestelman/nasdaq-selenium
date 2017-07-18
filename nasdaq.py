import os
import time
from selenium import webdriver

# short example
# stocks = ["ewem", "schd"] 
# full list (all etrade commission-free ETF's)
stocks = ["acsi", "krma", "actx", "cath", "sciu", "rsp", "jhml", "jpus", "esgl", "eps", "ext", "dgrw", "guru", "rwl", "rdiv", "dtn", "dhs", "dln", "ezy", "dtd", "ewmc", "jhmm", "jpme", "ezm", "div", "rwk", "don", "ewsc", "jpse", "rwj", "ees", "dgrs", "des", "cxse", "sdem", "emfm", "ewem", "jpem", "emcg", "xsoe", "dem", "dgre", "dgs", "scid", "hfxe", "jpeh", "jpeu", "hedj", "eusc", "eudg", "dfe", "guri", "hfxi", "jpih", "jpin", "dnl", "ihdg", "ddwm", "doo", "dwm", "dth", "epi", "scij", "hfxj", "ause", "dxge", "scix", "axjl", "sgqi", "jpge", "esgf", "dew", "sdiv", "rcd", "jhmc", "rhs", "jhms", "mlpj", "mlpx", "mlpa", "rye", "jhme", "ryf", "jhmf", "drw", "ryh", "jhmh", "rgi", "jhmi", "ghii", "rtm", "gres", "jhma", "sret", "ewre", "roof", "ryt", "jhmt", "ryu", "jhmu", "spxh", "bzf"]

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.alwaysAsk.force', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')
#profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream, application/csv, application/x-csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values, text/plain, text/x-csv, application/force-download, application/vnd.ms-excel, application/xls, text/csv')

driver = webdriver.Firefox(firefox_profile=profile)

for stock in stocks:
    print("stock: " + stock)
    try:
        driver.get("http://www.nasdaq.com/symbol/" + stock + "/historical")
    except:
        print("Error at driver.get(\"http://www.nasdaq.com/symbol/" + stock + "/historical\")")
        continue
    time_select = driver.find_element_by_id("ddlTimeFrame")
    options = time_select.find_elements_by_tag_name("option")
    #for option in options:
        #print("Value is: %s" % option.get_attribute("value"))
    options[4].click()
    driver.find_element_by_id("lnkDownLoad").click()
    timeout = 10
    while not os.path.exists("HistoricalQuote.csv"):
        timeout -= 1
        if timeout == 0:
            break
        time.sleep(1)
    try: 
        os.rename("HistoricalQuotes.csv", stock + ".csv")
    except:
        print("Error: file HistoricalQuotes.csv was not downloaded for " + stock)
driver.close()
