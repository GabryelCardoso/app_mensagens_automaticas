from tkinter import *
from tkinter import filedialog

from app import enviar_mensagens
#variaveis
permissao = True

#dicionarios
contatos_enviados = {}
contatos_naoEnviados = {}
#listas
Enviados = []
naoEnviados = []
numEnviados = []
numNaoEnviados = []

# Funções
def LocPlanilha():
    caminho = filedialog.askopenfilename()
    if caminho: 
        nome_arquivo = caminho
    else:
        nome_arquivo = "Nenhum arquivo selecionado"
    planilha_escolhida["text"] = nome_arquivo
    
def zerar_estruturas():
    Enviados.clear()
    naoEnviados.clear()
    numEnviados.clear()
    numNaoEnviados.clear()
    contatos_enviados.clear()
    contatos_naoEnviados.clear()



def IniciarAuto():
    zerar_estruturas()
    planilha_caminho = planilha_escolhida["text"]
    if planilha_caminho == "Nenhum arquivo selecionado":
        mensagem_retorno["text"] = "Selecione uma planilha."
    else:
        mensagem_retorno["text"] = "Enviando mensagens..."
        texto_inserido = entrada.get("1.0", "end-1c")
        print(planilha_escolhida["text"])
        enviar_mensagens(planilha_caminho, texto_inserido, Enviados, naoEnviados, numEnviados, numNaoEnviados)
        tamanhoE = len(Enviados) 
        tamanhoNE = len(naoEnviados)
        mensagem_retorno["text"] = f'{tamanhoE} mensagens enviadas.\n {tamanhoNE} mensagens não enviadas.'
        #botao_detalhes.config(state="normal")
            
        
   
#loop para adicionar elementos da interface
def adicionar_elementos():
    for i in range(len(Enviados)):
        contatos_enviados[Enviados[i]] = numEnviados[i]
    for i in range(len(naoEnviados)):
        contatos_naoEnviados[naoEnviados[i]] = numNaoEnviados[i]


    
#Janela que vai conter os detalhes da operação
def janela_detalhes():
    #configurações da janela
    janela_det = Tk()
    janela_det.title("Detalhes")
    janela_det.maxsize(width=475, height=750)
    janela_det.minsize(width=475, height=600)
    
    #Textos1
    label_ct1 = Label(janela_det, text="Mensagem:")
    label_ct1.grid(column=0, row=0, pady=10)
    #caixa de texto 1
    caixa_texto = Text(janela_det, width=40, height=7)
    caixa_texto.grid(column=0, row=1, padx=15)
    #textos2
    label_ct2 = Label(janela_det, text="Mensagens enviadas:")
    label_ct2.grid(column=0, row=2, pady=10)
    #caixa de texto 2
    caixa_texto2 = Text(janela_det, width=40, height=7)
    caixa_texto2.grid(column=0, row=3, padx=15)
    #textos3
    label_ct2 = Label(janela_det, text="Mensagens não enviadas:")
    label_ct2.grid(column=0, row=4, pady=10)
    #caixa de texto 3
    caixa_texto3 = Text(janela_det, width=40, height=7)
    caixa_texto3.grid(column=0, row=5, padx=15)
    
    adicionar_elementos()
    print(contatos_enviados)
    #Primeira Caixa
    texto_inserido = entrada.get("1.0", "end-1c")
    caixa_texto.insert('1.0', f'{texto_inserido}')
    caixa_texto.configure(state="disabled")
    #Segunda Caixa
    for chave, valor in contatos_enviados.items():
        caixa_texto2.insert( '1.0' ,f'Nome: {chave} | Número: {valor}\n')
    caixa_texto2.configure(state="disabled")
    #Terceira Caixa
    for chave, valor in contatos_naoEnviados.items():
        caixa_texto3.insert( '1.0' ,f'Nome: {chave} | Número: {valor}\n\n')
    caixa_texto3.configure(state="disabled")
    janela_det.mainloop()  



janela = Tk()                   #Cria a Janela

janela.title("AutoZap")         #título
#janela.maxsize(width=450, height=450)
janela.minsize(width=400, height=500)
nova_fonte = ("Arial", 10)
janela.option_add("*Font",nova_fonte)
#Selecionar planilha
#texto
selecionar_planilha = Label(janela, text="Selecione a planilha a ser utilizada: ")
selecionar_planilha.grid(column=0, row=1, pady=5)
#Botão
botao_plans = Button(janela, text="Selecionar",command=LocPlanilha)
botao_plans.grid(column=0, row=3, pady=5)
#Retorno
planilha_escolhida = Label(janela, text="Nenhum arquivo selecionado")
planilha_escolhida.grid(column=0, row=2,pady=5)

#Enviando mensagem
#texto
escrever_texto = Label(janela, text="Digite sua mensagem:")
escrever_texto.grid(column=0, row=4, pady=5)
#espaço para inserção de dados
entrada = Text(janela, width=40, height=7) #Cria um widget de entrada de texto
entrada.grid(column=0, row=5, padx=15, pady=5)


#mensagem de retorno
mensagem_retorno = Label(janela,text="Aguardando mensagem")
mensagem_retorno.grid(column=0, row=7, pady=10)
#botão para enviad os dados
botao_entrada = Button(janela, text="Enviar mensagem", command=IniciarAuto)
botao_entrada.grid(column=0, row=8,)

#botão para mostrar os detalhes
botao_detalhes = Button(janela, text="Exibir detalhes",command=janela_detalhes)
botao_detalhes.grid(column=0, row=9,pady=10)
#botão para cancelar a automação
janela.mainloop()               #Mantém a janela aberta


