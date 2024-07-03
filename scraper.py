# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import re

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def extract_image_url(style):
    match = re.search(r'url\("([^"]+\.jpg)"\)', style)
    if match:
        return match.group(1)
    return None

try:
    driver.get('https://www.natura.com.br/c/presentes-faixa-de-preco-agradecer?pageSize=48&price_filter=20..50&sort=top-sellers')
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    ).click()
    print("Clicou no botão")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "natds127")))
    product_cards = driver.find_elements(By.CLASS_NAME, "natds127")
    print(f"Encontrados {len(product_cards)} cartões de produtos.")

    for card in product_cards:
        image_div = card.find_element(By.CSS_SELECTOR, 'div[style*="background-image"]')
        style = image_div.get_attribute('style')
        image_url = extract_image_url(style)
        print("URL da Imagem:", image_url)

        #title_element = card.find_element(By.XPATH, ".//p[contains(@class, 'MuiBox-root natds676 natds95 natds675 natds665')]")
        #print("Título do Produto:", title_element.text)

        #price_element = card.find_element(By.XPATH, ".//h6[contains(@class, 'MuiTypography-root natds667 MuiTypography-subtitle2')]")
        #print("Preço do Produto:", price_element.text)

except Exception as e:
    print(f"Erro encontrado: {str(e)}")

finally:
    driver.quit()
