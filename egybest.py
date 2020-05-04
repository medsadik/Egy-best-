from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


#################################BACH YKHDM HAD L3JB 5ASK 3 L7WAYJ:#################################################
###############1-KHAS TDIR HADI F SHELL 'pip install selenium' W HADI 'pip install pyautogui'#######################
###############################2-KHAS YKOUN 3NDK CHROME ALFA9IR ####################################################
###############3- KHAS TINSTALLI CHROMEDRIVER W T7AT DOSSIER F DESKTOP DARORI ######################################
################################4- KHAS MATKHT2CH F SMIYT LFILM ####################################################
####################################################################################################################
####################################################################################################################
####################################################################################################################


def CheckAds(driver): #katraj3k l page dyal egybest ila khrjo l Ads
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[0])


def CheckTitle(titles,film): #tat3tik ga3 les film li khrjo f recherche
    for elt in titles:
        if elt.lower() == film.lower() or elt[:-7].lower() == film.lower():
            return titles.index(elt)


def location(element): # tatlocalisé play button (lil2asaf it's not perfect)
    location = element.location
    size = element.size
    x = location['x']
    y = location['y']
    return (x,y)


def Mouse(x,y,driver):
    pyautogui.moveTo(x+200,y-950,duration = 1)
    pyautogui.click()
    CheckAds(driver)
    time.sleep(6)
    pyautogui.click()
    CheckAds(driver)

def egybest(film =input('Tap the correct film name: ')): #main function
    l_movie = []
    driver = webdriver.Chrome('C:\\Users\moham\Desktop\Quarantine projects\chromedriver.exe') #path dyal webdriver
    driver.maximize_window()
    driver.get("https://rain.egybest.me")
    search = driver.find_element_by_name("q")
    search.send_keys(film)
    search.send_keys(Keys.RETURN)
    CheckAds(driver)
    search.send_keys(Keys.RETURN)
    try: #tsna tatloada lpage
        movies = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "movies"))
    )
    except:
        driver.quit()
    titles = movies.find_elements_by_class_name('title')
    for span in titles: #tatlisti ga3 les resultats li 3tathom recherche
        l_movie.append(span.text)
    position = CheckTitle(l_movie,film)
    driver.implicitly_wait(10) #tsnaw chwiya bima banou les elements Html
    link = driver.find_element(By.XPATH, '//*[@id="movies"]/a['+str(position+1)+']/span[2]')
    link.click()
    time.sleep(5)
    CheckAds(driver)
    driver.implicitly_wait(10)
    watch = driver.find_element(By.XPATH,'//*[@id="mainLoad"]/div[1]/div[2]/div[1]/a')
    watch.click()
    CheckAds(driver)
    driver.implicitly_wait(10)
    frame = driver.find_element_by_class_name("auto-size")
    x,y = location(frame)
    frame.click()
    CheckAds(driver)
    Mouse(x,y,driver)
    CheckAds(driver)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    print("ENJOY ALFA9IR xD ")


egybest()






