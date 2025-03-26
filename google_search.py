# Importige vajalikud moodulid Seleniumi ja veebilehitseja teenuse jaoks
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# Looge Firefoxi valikud, et määrata veebilehitseja asukoht
options = Options()
# Määrame Snap installatsiooni kaudu Firefoxi asukoha
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"  # Täpsustage õige tee

# Määrake geckodriver asukoht, mis on vajalik Firefoxi käivitamiseks Seleniumi kaudu
geckodriver_path = '/usr/local/bin/geckodriver'

# Kasutame Service klassi, et määrata geckodriver asukoht
service = Service(geckodriver_path)

# Käivitage Firefoxi veebilehitseja ja seadistage Selenium WebDriver
driver = webdriver.Firefox(service=service, options=options)

# Avage Google'i veebileht
driver.get("https://www.google.com")

# Otsingukasti leidmine ja otsingupäringu sisestamine
search_box = driver.find_element("name", "q")
search_box.send_keys("Tere maailm Seleniumiga")  # Sisestame otsingupäringu
search_box.submit()  # Esitame otsingu

# Ootame 3 sekundit, et tulemused laeksid
time.sleep(3)

# Lõpetame sessiooni ja sulgeme brauseri
driver.quit()
