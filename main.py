## Oraculo do Programador 
import random
import tkinter as tk
from tkinter import messagebox

## Lista de frases do oráculo para o Soteio

elogios_dev = [
    "Você é um programador incrível!",
    "Seu código é elegante e eficiente!",
    "Você tem um talento natural para programação!",
    "Seu trabalho é admirável!",
    "Você é um mestre da lógica!",
    "Seu código é uma obra de arte!",
    "Você é um solucionador de problemas excepcional!",
    "Seu conhecimento em programação é impressionante!",
    "Você é um verdadeiro gênio da programação!",]              

frases_motivacionais = [
    "Continue se esforçando, você está no caminho certo!",
    "Acredite em si mesmo e no seu potencial!",
    "Cada desafio é uma oportunidade de crescimento!",
    "Não desista, grandes conquistas levam tempo!",
    "Mantenha o foco e a determinação, você vai conseguir!",
    "Aprender com os erros é parte do processo de evolução!",
    "A prática leva à perfeição, continue praticando!",
    "Acredite no seu talento e siga em frente!",
    "O sucesso é construído com dedicação e perseverança!",]    

def gerar_frase(nome, opcao):
    if not nome.strip():
        messagebox.showwarning("Atenção", "Digite seu nome antes de gerar uma frase.")
        return

    frases = elogios_dev if opcao == 1 else frases_motivacionais
    frase_label.config(text=f"{nome}, {random.choice(frases)}")

## Criando a interface gráfica
janela = tk.Tk()
janela.title("Gerador de Frases Motivacionais e Elogios para Programadores")
janela.geometry("350x450")
janela.config(bg="#f0f0f0")

## Titulo do aplicativo
titulo = tk.Label(janela, text="Oráculo do Programador", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)    

## Campo de entrada para o nome do usuário
nome_label = tk.Label(janela, text="Digite seu nome:", font=("Helvetica", 12), bg="#f0f0f0")
nome_label.pack(pady=5)

nome_entry = tk.Entry(janela, width=30)
nome_entry.pack(pady=5)

## Variável para armazenar a frase gerada
opcao_selecionada = tk.IntVar(value=1)

## Botoes de escolha unica (radio buttons) para selecionar o tipo de frase
frames_opcoes = tk.Frame(janela, bg="#f0f0f0")
frames_opcoes.pack(pady=10) 

rb1 = tk.Radiobutton(frames_opcoes, text="Elogio", variable=opcao_selecionada, value=1, font=("Helvetica", 12), bg="#f0f0f0")
rb1.pack(anchor="w", padx=20)
rb2 = tk.Radiobutton(frames_opcoes, text="Frase Motivacional", variable=opcao_selecionada, value=2, font=("Helvetica", 12), bg="#f0f0f0")
rb2.pack(anchor="w", padx=20)   
## Botao de acao para gerar a frase
botao_gerar = tk.Button(janela, text="Gerar Frase", font=("Helvetica", 12), command=lambda: gerar_frase(nome_entry.get(), opcao_selecionada.get()))
botao_gerar.pack(pady=20)
## Area onde a frase gerada sera exibida
frase_label = tk.Label(janela, text="", font=("Helvetica", 12), wraplength=300, justify="center", bg="#f0f0f0")
frase_label.pack(pady=10)

## inciar o do loop principal da interface grafica
janela.mainloop()   