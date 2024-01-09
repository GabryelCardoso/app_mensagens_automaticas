#importando biblioteca para manusear planilhas
import openpyxl

#importando uma biblioteca para codificar a mensagem para funcionar no link do whatsapp
from urllib.parse import quote

#importando o modulo que permite abrir o navegador
import webbrowser

#importando biblioteca para conseguir dar pausas no código
from time import sleep

#importando biblioteca para dar clique na tela e teclado
import pyautogui

#importando função para utilizar o tempo
import time



#Função de cronômetro
def cronometro(segundos):
    for i in range(segundos, 0,-1):
        print(f'{i} s')
        time.sleep(1)

def enviar_mensagens(planilha, texto, listaV, listaF, listanumV, listanumF):
    
    # variáveis
    contadorS = 0
    contadorF = 0
    #webbrowser.open('https://web.whatsapp.com/')
   
    
    #lendo a planilha desejada e guardando ela na variável workbook
    
    workbook = openpyxl.load_workbook(planilha)

    #especificando qual página da planilha deve ser lida e guardando na variável
    pagina_clientes = workbook['Página1']

   

        #Criando um laço que passa em cada linha da página começando a partir da segunda
    for linha in pagina_clientes.iter_rows(min_row=2):
        #nome, telefone
        nome = linha[0].value
        telefone = linha[1].value
        #mensagem a ser enviada
        mensagem = f'Olá {nome}, {texto}'
        # link base: https://web.whatsapp.com/send?phone=&text=
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
            
        #abrindo whatsapp
            
        #Abrindo link da conversa
        webbrowser.open(link_mensagem_whatsapp)
        sleep(12)
            
        try:
            #localizando a imagem e o centro dela
            seta1 = pyautogui.locateCenterOnScreen('seta1.png')
            #clicka na imagem
            pyautogui.click(seta1[0], seta1[1])
            sleep(5)
            #Fechando página
            pyautogui.hotkey('ctrl','w')
            print(f'Mensagem enviada para {nome}')
            contadorS = contadorS + 1
            #adiciona o nome na lista de nomes
            listaV.append(nome)
            #adiciona o número na lista de números
            listanumV.append(telefone)
            print(listaV)
            sleep(5)
                    
                
                #se não conseguir executar
        except:
                try:
                    seta2 = pyautogui.locateCenterOnScreen('seta2.png')
                    pyautogui.click(seta2[0], seta2[1])
                    sleep(5)
                    pyautogui.hotkey('ctrl','w')
                    print(f'Mensagem enviada para {nome}')
                    contadorS = contadorS + 1
                    #adiciona o nome a lista de nomes
                    listaV.append(nome)
                    print(listaV)
                    #adiciona o número na lista de números
                    listanumV.append(telefone)
                    sleep(5)
                except:

                    #Devolve esta mensagem
                    print(f'Não foi possível enviar mensagem para {nome}')                
                    #contador para saber quantas mensagens não foram enviadas
                    contadorF = contadorF + 1
                    listaF.append(nome)
                    #adiciona o número a lista de telefones
                    listanumF.append(telefone)
                    print(listaF)
                    #Fechando página
                    pyautogui.hotkey('ctrl','w')
                    sleep(5)
        
    
    me = f'{contadorS} mensagens enviadas com sucesso'
    print(me)
    mf = f'{contadorF} mensagens não enviadas'
    print(mf)
 

    
    
    


  


   
        
        



        



