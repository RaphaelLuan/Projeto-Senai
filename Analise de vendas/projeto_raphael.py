import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_data():
    data = pd.read_csv('./Analise de vendas/dados.csv', delimiter=';', encoding='latin-1') # ler arquivo CSV 

    # Extrair dados da planilha
    total = data['TOTAL'] # Extrai dados da primeira coluna
    produto = data['PRODUTO'] # Extrai dados da segunda coluna

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.plot(produto, total, marker='o', 
    linestyle='-', color='b')
    grafico.grid(True)

    # add as labels - etiquetas
    grafico.set_xlabel('')
    grafico.set_ylabel('TOTAL')
    grafico.set_title('Vendas Gerais')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela) # fig é oq vem do matplot e janela será o Tkinter
    canvas.draw() # desenha a figura criada na variavel canvas
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # layout do botão que vai ativar tudo que ta dentro do "canvas"

def pizza_data():
    data = pd.read_csv('./Analise de vendas/dados.csv', delimiter=';') # ler arquivo CSV 

    # Extrair dados da planilha
    vendas = data['TOTAL'] # Extrai dados da primeira coluna
    vendedor = data['PRODUTO'] # Extrai dados da segunda coluna:
    
    total_vendas = np.sum(vendas)
    porcentagem_vendas = (vendas / total_vendas) * 100

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.pie(porcentagem_vendas, labels=vendedor,autopct='%1.1f%%', startangle=140)

    # add as labels - etiquetas
    grafico.set_title('Distribuição de Vendas por Produto')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela) # fig é oq vem do matplot e janela será o Tkinter
    canvas.draw() # desenha a figura criada na variavel canvas
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True) # layout do botão que vai ativar tudo que ta dentro do "canvas"


# janela tkinter - Cria uma janela principal com o nome que está em title
janela = tk.Tk()
janela.title('Gráfico de Vendas')

frame_botoes = tk.Frame(janela)
frame_botoes.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NE)

texto = "Após análise dos gráficos, é possível identificar que os aparelhos eletronicos são as vendas mais significativas, a análise mostra, que a empresa deve focar nesse nicho de vendas."
label = tk.Label(janela, text=texto)
label.pack(side=tk.TOP, pady=10) 

# button
botao = tk.Button(frame_botoes, text='Exibir Gráfico Padrão', command=plot_data)
botao.pack(side=tk.LEFT, padx=10, pady=10)

botao = tk.Button(frame_botoes, text='Exibir Gráfico de Pizza', command=pizza_data)
botao.pack(side=tk.LEFT, padx=10, pady=10)

# loop tkinter
janela.mainloop()
