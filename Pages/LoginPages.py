from Pages.Webgeneric import Webgeneric

class Login(Webgeneric):
    def __init__(self,driver):
        Webgeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="email"
        self.pwd_name="pass"
        self.login_btn_xpath="//input[@type='submit']"


    def Login1(self,un,pwd):
        wg=Webgeneric(self.driver)
        wg.enter(self.un_id,un)
        wg.enter(self.pwd_name,pwd)
        wg.submit(self.login_btn_xpath)