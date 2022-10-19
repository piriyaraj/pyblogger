from lib2to3.pgen2 import driver
import os
from autopost.autopost import Autopost


driver=os.path.abspath("./chromedriver")
Autopost.openWindow(driver)