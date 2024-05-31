from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuração inicial do Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Carrega a página
    driver.get('https://www.natura.com.br/c/especial-primeira-compra?price_filter=100..149&sort=top-sellers')
    # Dá um tempo para o JavaScript carregar
    driver.implicitly_wait(10)

    # Usa BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Encontrar especificamente a div com classe 'natds4'
    target_div = soup.find('div', class_='natds4')
    if target_div:
        print("Div 'natds4' encontrada.")
        # Imprimir uma versão mais detalhada do conteúdo interno
        for child in target_div.find_all(recursive=True):  # Procura por todos os elementos internos
            tag_name = child.name
            class_list = ' '.join(child.get('class', []))
            content_preview = child.get_text(strip=True, separator=' ')[0:100]  # Primeiros 100 caracteres
            print(f"Elemento: {tag_name}, Classe: {class_list}, Conteúdo: {content_preview}")
    else:
        print("Div 'natds4' não encontrada.")

finally:
    # Fecha o navegador
    driver.quit()



