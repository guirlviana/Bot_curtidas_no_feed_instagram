from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
import getpass
import time
import random
from selenium.webdriver.common import keys

class botcurtir:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException]
        )
        self.nome = str(input("Qual o usuario do instagram? @"))
        self.senha =  getpass.getpass(prompt="Qual a senha do perfil no instagram? ", stream=None)
        self.fotos = int(input("Quantas fotos devo curtir para você? "))
    
    def iniciar(self):
        self.driver.get("https://www.instagram.com/")
        self.FazerLogin(self.nome, self.senha)
        self.Avisos()
        self.curtir(self.fotos)
        

    def FazerLogin(self, username, senha):
        try:
            campo_username =  self.wait.until(CondicaoExperada.element_to_be_clickable(
                        (By.XPATH, f'//input[@name ="username"]')))

            campo_username.click()
            for letra in username:
                campo_username.send_keys(letra)
                time.sleep(random.randint(1,5) / 30)

        
            campo_senha = self.wait.until(CondicaoExperada.element_to_be_clickable(
                        (By.XPATH, f'//input[@name ="password"]')))
            for letra in senha:
                campo_senha.send_keys(letra)
                time.sleep(random.randint(1,5) / 30)

            campo_senha.send_keys(keys.Keys.ENTER)
            time.sleep(2)          

            passar_login =  self.wait.until(CondicaoExperada.element_to_be_clickable(
                        (By.XPATH, f'//button[@class="sqdOP yWX7d    y3zKF     "]'))) 
        
            if passar_login is not None:
                passar_login.click()
            if passar_login is None:
                pass 
            time.sleep(2)
        except Exception as erro :
            print("Dados de login incorreto, feche e abra o bot novamente")

    def Avisos(self):
        print("Acabei de fazer o login")
        print(f"Em 10 segundos começarei a curtir")
        print("NAO MEXA NA TELA")
        for i in range(1,11):
            time.sleep(1)
            print(f"iniciando em {i}/10")

    def curtir(self, curtidas):
        try:
            self.cont = 0
            for i in range(1, curtidas+1):
                
                btn_curtir = self.wait.until(CondicaoExperada.element_to_be_clickable(
                        (By.XPATH, f'//span[@class="fr66n"]')))
                self.driver.execute_script('window.scrollBy(0, 100)')
                   
                if btn_curtir.is_selected() == False:
                    btn_curtir.click()
                    print("Estou curtindo ;)")                        
                    time.sleep(3) 
                        
                elif btn_curtir.is_selected() == True:
                    pass
                self.cont += 1
        except Exception as erro :
            print("Algo deu errado, feche o bot e abra novamente")   
        self.feedback()    
    
    def feedback(self):
        print(f"Eu curti {self.cont} fotos")
        continuar = str(input("Quer curtir mais? [S/N] ")).upper().strip()[0]
        if continuar == "S":
            self.qnt = int(input("Mais quantas fotos? ")) 
            self.curtir(self.qnt)
        else:
            print(f"Obrigado por utilizar {self.nome} :)")
            time.sleep(2)
            self.driver.quit() 

            

root = botcurtir()
root.iniciar()