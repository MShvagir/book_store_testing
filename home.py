from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
#  добавление комментария
driver.execute_script("window.scrollBy(0,600);")
slr_one = "#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > img"
book_one = driver.find_element_by_css_selector(slr_one).click()
reviews_btn = driver.find_element_by_css_selector("li.reviews_tab > a").click()
rating_before = driver.find_element_by_css_selector(".stars")
rating_fife_star = driver.find_element_by_css_selector("a.star-5").click()
review_area = driver.find_element_by_id("comment")
review_area.send_keys("Nice book!")
name_area = driver.find_element_by_id("author")
name_area.send_keys("Marta Smith")
email_area = driver.find_element_by_id("email")
email_area.send_keys("blabla@gmail.com")
submit_btn = driver.find_element_by_id("submit").click()
driver.quit()


