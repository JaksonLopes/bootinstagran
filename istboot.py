from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time
import random
from random import randint


class InstragranBot:
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.driver =  webdriver.Firefox(executable_path= "./geckodriver.exe")
    #fazendo login    
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        #varendo os capos usuario e senha 
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        time.sleep(2)
        campo_senha.send_keys(Keys.RETURN) #simular botao enter 
        
    # digitar letra por letra  
    @staticmethod
    def digitar_como_uma_pessoa(frase,onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(2,9)/10)

 
    def comenta_sorteio(self):
        url_sorteio = 'https://www.instagram.com/p/CUtHQx0rBOs/' #aui tem que autera para a url do sorteio em andamento 
        time.sleep(6)
        driver = self.driver
        driver.get(url_sorteio)
        
        for multcomentarios in range(1,20000):
          
            try:
                aleatorio = str(randint(0,844544))
                comentarios = ["Eu quero","Já é meu","Otimos premios","Parabens pelos otimos premios",
                "Faça sempre o seu melhor","E acredite que o melhor possa ser feito!",
                "Não espere,ponha em prática!","Mesmo que pareça difícil, não pare!",
                "Só trabalhando é possível trilhar o caminho!","Tenha coragem!",
                "Descubra quem você realmente é…","E se aceite","A causa da derrota, não está nos obstáculos, ou no rigor das circunstâncias, está na falta de determinação e desistência da própria pessoa.",
                "Mudar é difícil mas é possível.","Se não houver felicidade, negócio vira uma tortura.",
                "Não tenha receio de desistir do bom para correr atrás do ótimo",
                "Sucesso? Eu não sei o que exatamente isso significa. Eu sou feliz. A definição de sucesso varia de pessoa para pessoa. Para mim, o sucesso é ter paz interior",
                "Seja muito bom, que eles não vão ter como ignorar você",
                "Não sei qual é o segredo do sucesso, mas o segredo do fracasso é tentar agradar a todo mundo",
                "Para ser bem sucedido, o desejo pelo sucesso deve ser maior que o medo de falhar.",
                "O sucesso não consiste em não errar, mas em não cometer os mesmos equívocos mais de uma vez",
                "Inspiração vem dos outros. Motivação vem de dentro de nós.","A maior glória não é ficar de pé, mas levantar-se cada vez que se cai.",
                "A esperança morre no primeiro insucesso; a ambição sobrevive à última derrota",
                "Identifique seus problemas, mas dê seu poder e energia a soluções.",
                "Andar para trás só se for para pegar impulso.",
                "Diga ‘obrigado’ a todos que você encontrar e para tudo o que eles fazem por você."]

                lista_numerica = []
                lista_numerica.append(str(multcomentarios))
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")

                self.digitar_como_uma_pessoa(random.choice(comentarios)+(str(aleatorio)),campo_comentario)
                time.sleep(random.randint(30,50))
                #campo_comentario.send_keys(Keys.RETURN)

                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                print(multcomentarios)
                time.sleep(random.randint(30,50))
                if multcomentarios == 20:
                    driver.get('https://www.instagram.com/p/CF5jlwrhxem/')
                    time.sleep(60)
                    driver.get(url_sorteio)
                    time.sleep(5)

                elif multcomentarios ==40:
                    time.sleep(220)
                    driver.get('https://www.instagram.com/p/CRR3ke0BHSD/')
                    time.sleep(58)
                    driver.get(url_sorteio)

                elif multcomentarios == 80:
                    time.sleep(60)
                    driver.get('https://www.instagram.com/p/CNV16uKjhjX6ww54DFe9m9WwiPuhawImT94Xxo0/')
                    time.sleep(48)
                    driver.get(url_sorteio)
                    
                elif multcomentarios == 120:
                    driver.get('https://www.instagram.com/p/CQMo1yKlrVN/')
                    time.sleep(37)
                    driver.get(url_sorteio)
                elif multcomentarios == 160:
                    driver.get('https://www.instagram.com/p/CQMo1yKlrVN/')
                    time.sleep(120)
                    driver.get(url_sorteio)
               
            except Exception as E:
                print(E)
                time.sleep(2000)

        

jaksonbot = InstragranBot('USUARIO','SENHA') #PASSA OS PAREMETROS USUARIO E SENHA 
jaksonbot.login()
jaksonbot.comenta_sorteio()





