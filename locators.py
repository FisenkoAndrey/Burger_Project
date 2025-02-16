from selenium.webdriver.common.by import By


class AuthPageLocators:
     REGISTRATIONLINK = By.XPATH, '//*[@id="root"]/div/form/div[4]/p[1]/a/button'
     INPUTEMAIL = By.XPATH, '//*[@id="root"]/div/form/div[1]/div/input'
     INPUTPASSWORD = By.XPATH, '//*[@id="root"]/div/form/div[2]/div/input'
     PRESSBUTTON = By.XPATH, '/html/body/div[1]/div/form/div[3]/button'


class NavigationLocators:
    PROFILE = By.XPATH, "//p[text()='Личный кабинет']"


class RegistrationLocators:

    NAME = By.XPATH,'//*[@id="root"]/div/form/div[1]/div/input'
    EMAIL = By.XPATH, '//*[@id="root"]/div/form/div[2]/div/input'
    PASSWORD = By.XPATH, '//*[@id="root"]/div/form/div[3]/div/input'
    BUTTON = By.XPATH, '//*[@id="root"]/div/form/div[4]/button'
    SHOWPASSWORD = By.XPATH, '//*[@id="root"]/div/form/div[4]/button'
    AUTHLINK = By.XPATH,'//*[@id="root"]/div/form/div[5]/p/a/button'


class ProfileLocators:
    PRPOFILENAME = By.XPATH, "//*[@id='root']/div/div/form/div[1]/div/input"
    PROFILEEMAIL = By.XPATH, "//*[@id='root']/div/div/form/div[2]/div/input"

    
class ConstructorLocators:
    BUN = By.XPATH, "//*[@id='root']/div/main/div[1]/section/div[2]/div[1]/div/a[1]"
    WINDOWCLOSEBUTTON = By.XPATH, "//*[@id='react-modals']/section[2]/div[1]/button"
    MODALWINDOWNAME = By.XPATH, "//*[@id='react-modals']/section[2]/div[1]/h2"
    OOTSIDEPOINT = By.XPATH, "//*[contains(@class, 'ModalOverlay')]"
    DROP = By.XPATH, "//*[@id='root']/div/main/div[2]/section/div[1]/div[1]"








