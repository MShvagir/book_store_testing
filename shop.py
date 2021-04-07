from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#  отображение страницы товара
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_css_selector("#menu-item-50 > a").click()
login_area = driver.find_element_by_id("username")
login_area.send_keys("alira_m@mail.ru")
pswd_area = driver.find_element_by_id("password")
pswd_area.send_keys("Dt6G4F@s2@6KPQ@")
login_btn = driver.find_element_by_css_selector("form > p:nth-child(3) > input.woocommerce-Button.button").click()
shop_menu = driver.find_element_by_id("menu-item-40").click()
book_one = driver.find_element_by_xpath("//*[@id='content']/ul/li[3]/a[1]/img").click()
book_title = driver.find_element_by_css_selector(".summary.entry-summary > h1")
book_title_text = book_title.text
assert book_title_text == "HTML5 Forms"
driver.quit()

#  количество товара в категории
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_css_selector("#menu-item-50 > a").click()
login_area = driver.find_element_by_id("username")
login_area.send_keys("alira_m@mail.ru")
pswd_area = driver.find_element_by_id("password")
pswd_area.send_keys("Dt6G4F@s2@6KPQ@")
login_btn = driver.find_element_by_css_selector("form > p:nth-child(3) > input.woocommerce-Button.button").click()
shop_menu = driver.find_element_by_id("menu-item-40").click()
ctgr_html = driver.find_element_by_css_selector(".cat-item.cat-item-19 > a").click()
books_list = driver.find_elements_by_xpath("//*[@id='content']/ul/li")
if len(books_list) == 3:
    print("the number of books is", len(books_list))
else:
    print("the number of books isn't 3")
driver.quit()

#  сортировка товара
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_css_selector("#menu-item-50 > a").click()
login_area = driver.find_element_by_id("username")
login_area.send_keys("alira_m@mail.ru")
pswd_area = driver.find_element_by_id("password")
pswd_area.send_keys("Dt6G4F@s2@6KPQ@")
login_btn = driver.find_element_by_css_selector("form > p:nth-child(3) > input.woocommerce-Button.button").click()
shop_menu = driver.find_element_by_id("menu-item-40").click()
sorted_list = driver.find_element_by_css_selector(".orderby")
sorted_list_default = sorted_list.get_attribute("value")
assert sorted_list_default == "menu_order"
select = Select(sorted_list)
select.select_by_value("price-desc")
sorted_list = driver.find_element_by_css_selector(".orderby")
sorted_list_hight_low = sorted_list.get_attribute("value")
assert sorted_list_hight_low == "price-desc"
driver.quit()

#  отображение, скидка товара
driver.get("http://practice.automationtesting.in/")
account_menu = driver.find_element_by_css_selector("#menu-item-50 > a").click()
login_area = driver.find_element_by_id("username")
login_area.send_keys("alira_m@mail.ru")
pswd_area = driver.find_element_by_id("password")
pswd_area.send_keys("Dt6G4F@s2@6KPQ@")
login_btn = driver.find_element_by_css_selector("form > p:nth-child(3) > input.woocommerce-Button.button").click()
shop_menu = driver.find_element_by_id("menu-item-40").click()
book_first = driver.find_element_by_xpath("//*[@id='content']/ul/li[1]/a[1]/img").click()
old_price = driver.find_element_by_css_selector("div:nth-child(2) > p > del > span")
old_price_text = old_price.text
assert old_price_text == "₹600.00"
new_price = driver.find_element_by_css_selector("ins > .woocommerce-Price-amount.amount")
new_price_text = new_price.text
assert new_price_text == "₹450.00"
waiting = WebDriverWait(driver, 10)
book_pic = waiting.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='product-169']/div[1]/a/img")))
book_pic.click()
book_pic_small = waiting.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
driver.quit()

#  проверка цены в корзине
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_id("menu-item-40").click()
book_first = driver.find_element_by_xpath("//*[@id='content']/ul/li[6]/a[1]/img").click()
to_basket_btn = driver.find_element_by_css_selector(".single_add_to_cart_button.button.alt").click()
cart_count = driver.find_element_by_css_selector(".cartcontents")
cart_count_text = cart_count.text
assert cart_count_text == "1 Item"
price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
price_text = price.text
assert price_text == "₹350.00"
basket = driver.find_element_by_css_selector(".button.wc-forward").click()
waiting = WebDriverWait(driver, 10)
subtotal = waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "₹350.00"))
total = waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"), "₹367.50"))
driver.quit()

#  работа в корзине
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0,300);")
book_first = driver.find_element_by_css_selector(".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
time.sleep(3)
to_basket_btn = driver.find_element_by_css_selector(".added_to_cart.wc-forward").click()
time.sleep(2)
remove = driver.find_element_by_css_selector(".product-remove .remove").click()
undo = driver.find_element_by_css_selector("div.woocommerce-message > a").click()
qnt_area = driver.find_element_by_css_selector(".input-text.qty.text").clear()
qnt_area_new = driver.find_element_by_css_selector(".input-text.qty.text")
qnt_area_new.send_keys("3")
update_cart = driver.find_element_by_name("update_cart").click()
time.sleep(2)
cart_count = driver.find_element_by_css_selector(".input-text.qty.text")
cart_count_value = cart_count.get_attribute("value")
assert cart_count_value == "3"
time.sleep(3)
coupon = driver.find_element_by_name("apply_coupon").click()
coupon_error = driver.find_element_by_css_selector("div.woocommerce > ul > li")
coupon_error_text = coupon_error.text
assert coupon_error_text == "Please enter a coupon code."
driver.quit()

# покупка товара
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0,300);")
book_first = driver.find_element_by_css_selector(".button.product_type_simple.add_to_cart_button.ajax_add_to_cart").click()
time.sleep(3)
to_basket_btn = driver.find_element_by_css_selector(".added_to_cart.wc-forward").click()
time.sleep(2)
waiting = WebDriverWait(driver, 10)
checkout_btn = waiting.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward")))
checkout_btn.click()
first_name = waiting.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Greta")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Garbo")
email_area = driver.find_element_by_id("billing_email")
email_area.send_keys("alira_m@mail.ru")
phone_area = driver.find_element_by_id("billing_phone")
phone_area.send_keys("79227641899")
country = driver.find_element_by_css_selector("span.select2-arrow > b").click()
country_search = driver.find_element_by_id("s2id_autogen1_search")
country_search.send_keys("France")
country_choice = driver.find_element_by_xpath("//*[@id='select2-result-label-278']").click()
street_area = driver.find_element_by_xpath("//*[@id='billing_address_1']")
street_area.send_keys("Monami")
postcode_area = driver.find_element_by_xpath("//*[@id='billing_postcode']")
postcode_area.send_keys("123456")
town_area = driver.find_element_by_xpath("//*[@id='billing_city']")
town_area.send_keys("Paris")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
payments = driver.find_element_by_id("payment_method_cheque").click()
place_order = driver.find_element_by_id("place_order").click()
thank_msg = waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
paymethod = waiting.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce > ul > li.method > strong"), "Check Payments"))
driver.quit()