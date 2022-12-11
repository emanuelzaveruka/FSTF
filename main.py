import pandas as pd;
import os
import urllib.request

root_path = os.getcwd()
dataframe = pd.read_excel('index.xlsx')
folders = dataframe['NOME'].tolist()
images = dataframe['IMAGEM'].tolist()
i = 0
erroCont = 0

coluns = ['NOME', 'IMAGEM']
dataframeWithError = pd.DataFrame(columns=coluns)

for folder in folders:
    path = os.path.join(root_path, folder)
    os.mkdir(path)
    try:
        urllib.request.urlretrieve(images[i], os.path.join(path, folders[i] + '.png'))
        image = urllib.request.urlretrieve(images[i])
    except:
        dataframeWithError = dataframeWithError.append({'NOME': folders[i], 'IMAGEM': images[i]}, ignore_index=True)
        erroCont = erroCont + 1     
    i = i + 1

if dataframeWithError.empty == False:
    dataframeWithError.to_excel('erros.xlsx')

print('Total de erros: ' + str(erroCont))