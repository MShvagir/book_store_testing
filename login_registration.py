from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#  регистрация аккаунта
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_css_selector("#menu-item-50 > a").click()
email_area = driver.find_element_by_id("reg_email")
email_area.send_keys("alira_m@mail.ru")
pswrd_area = driver.find_element_by_id("reg_password")
pswrd_area.send_keys("Dt6G4F@s2@6KPQ@")
register_btn = driver.find_element_by_css_selector("p.woocomerce-FormRow.form-row > input.woocommerce-Button.button").click()
driver.quit()

#  логин в систему
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_css_selector("#menu-item-50 > a").click()
login_area = driver.find_element_by_id("username")
login_area.send_keys("alira_m@mail.ru")
pswd_area = driver.find_element_by_id("password")
pswd_area.send_keys("Dt6G4F@s2@6KPQ@")
login_btn = driver.find_element_by_css_selector("form > p:nth-child(3) > input.woocommerce-Button.button").click()
logout_elmnt = driver.find_element_by_css_selector("div.woocommerce > div > p:nth-child(1) > a")
logout_elmnt_text = logout_elmnt.text
assert logout_elmnt_text == "Sign out"
driver.quit()