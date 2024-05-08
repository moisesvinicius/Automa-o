# Passo a passo projeto automação
# 1 - Abrir o sistema da empresa
import pyautogui as pa
import time
pa.PAUSE = 0.9
pa.press('win')
pa.write('Microsoft Edga')
pa.press('enter')
time.sleep(10)
pa.click(x=398, y=55)
pa.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pa.press('enter')

time.sleep(6)

# 2 - fazer login
# Pega posição do mause:
pa.click(x=491, y=350)
pa.write('moisesvinicius156@gmail.com')
pa.press('tab')
pa.write('minhasenha234')
pa.press('tab')
pa.press('enter')


# 3 - abrir/importa a base de dados de produtos para cadastra
import pandas as pd

tabela = pd.read_csv('produtos.csv')

time.sleep(3)

# 4 - cadastra um produto
for linha in tabela.index: # 5 - repetir isso tudo até acabar a lista de produtos.

    pa.click(x=1083, y=79) # presiona X para tira notificação
    pa.click(x=471, y=244)
    pa.write(str(tabela.loc[linha, 'codigo']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'marca']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'tipo']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'categoria']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'preco_unitario']))
    pa.press('tab')
    pa.write(str(tabela.loc[linha, 'custo']))
    pa.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pa.write('obs')
    pa.press('tab')
    pa.press('enter')
    pa.scroll(5000)

