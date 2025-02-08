#Importei o pyautogui, time(necessario pra criar um tempo entre um linha de codigo e outra) e o pandas(pra conseguir gerenciar minha tabela de produtos)
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

#Entrando no site fornecido pelo curso
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#adicionando o login necessario
pyautogui.click(x=733, y=521)
pyautogui.write("joaozinhojose58@gmail.com")
pyautogui.press("tab")

time.sleep(2)

pyautogui.write("12345678")
pyautogui.press("tab")
pyautogui.press("enter")

#Gerenciando a tabela usando o pandas
tabela = pd.read_csv("./automação avançada/produtos.csv")

print(tabela)

#Usando um laço de repetição(for) para ir adiciando os produtos
for linha in tabela.index:
    pyautogui.click(x=660, y=352)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    observacao = str(tabela.loc[linha, "obs"])
    if observacao != "nan":
        pyautogui.write(observacao)

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(15555555)



