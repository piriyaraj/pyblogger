from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Autopost:
    def __init__(self):
        self.driver=None
        self.errorHandling=True
        pass

    def openWindow(self,chromeDriver):
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(chromeDriver, options=chr_options)
        driver.get("https://stackoverflow.com/users/login?ssrc=head")
        driver.maximize_window()
        self.driver=driver
        pass

    def loginAccount(self,mail,password,blogUrl):
        driver=self.driver
        driver.find_element_by_xpath("//*[@id='openid-buttons']/button[1]").click()
        email = driver.find_element_by_xpath("//*[@id='identifierId']")
        email.send_keys(mail)
        email.send_keys(Keys.RETURN)
        time.sleep(10)
        passw = driver.find_elements_by_xpath("//input[@type='password']")[0]
        passw.send_keys(password)
        passw.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.get(blogUrl)

        pass

    def newPost(self,newpostcount=1):
            # global newpostcount
        driver=self.driver
        if(newpostcount > 2):
            print("Exit!")
            return(1)
        try:
            WebDriverWait(driver, 30).until(
                lambda d: d.find_element_by_class_name("MIJMVe"))
            time.sleep(1)
            driver.find_element_by_class_name("MIJMVe").click()
            driver.find_element_by_class_name("MIJMVe").click()

            Wait = WebDriverWait(driver, 30)
            Wait.until(EC.presence_of_element_located(
                (By.XPATH, "//*/span/c-wiz/div/div[2]/div[5]/div/span/div/div")))

            driver.refresh()
            return("hello")  # dont delete

        except Exception:
            # print(traceback.format_exc())
            if(self.errorHandling):
                print(newpostcount, end="/")
                driver.refresh()
                newpostcount += 1
                self.newPost(driver, newpostcount=newpostcount)
            pass

    def putTitle():
        pass

    def putTag():
        pass

    def putDescription():
        pass

    def putSchdule():
        pass

    def postImg():
        pass

    def postContent():
        pass