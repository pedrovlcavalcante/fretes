import pandas as pd
import os

dfs = []

def agrega_bomfim(dfs:list):
    for file in os.listdir("fretes_bomfim"):
        df = pd.read_csv(f"fretes_bomfim\\{file}", sep=";")
        print(df.size)
        dfs.append(df)    
    bomfim = pd.concat(dfs, ignore_index=True)
    bomfim.to_csv("bomfim_jan_jul.csv")
    bomfim.to_excel("bomfim_jan_jul.xlsx")
    dfs.clear()

def agrega_braspress(dfs:list):
    for file in os.listdir("fretes_braspress"):
        df = pd.read_excel(f"fretes_braspress\\{file}", header=6)
        print(df.size)
        dfs.append(df)    
    braspress = pd.concat(dfs, ignore_index=True)
    braspress.to_csv("braspress_jan_jul.csv")
    braspress.to_excel("braspress_jan_jul.xlsx")
    dfs.clear()

def agrega_transceara(dfs:list):
    import chardet

    
    for file in os.listdir("fretes_transceara"):
        # with open(f"fretes_transceara\\{file}", 'rb') as f:
        #     raw_data = f.read(10000)  # Read first 10k bytes to guess
        #     result = chardet.detect(raw_data)
        #     file_encoding = result['encoding']
        #     print(f"Detected encoding: {file_encoding}")
        df = pd.read_excel(f"fretes_transceara\\{file}")
        # print("erro, ", file)
        print(df.size)
        dfs.append(df)    
    transceara = pd.concat(dfs, ignore_index=True)
    transceara.to_csv("transceara_jan_jul.csv")
    transceara.to_excel("transceara_jan_jul.xlsx")
    dfs.clear()

# agrega_bomfim(dfs)
# agrega_braspress(dfs)
agrega_transceara(dfs)