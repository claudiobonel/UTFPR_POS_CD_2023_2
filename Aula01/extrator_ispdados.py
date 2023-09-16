import pandas as pd

#definir coleta de dados
df_ocorrencias = pd.read_csv("http://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv",encoding='ISO-8859-1',sep=';')

#Coluna para linha e filtro de tipos de ocorrência desnecessárias
df_ocorrencias = df_ocorrencias.melt(id_vars=['cisp', 'mes', 'ano', 'mes_ano', 'aisp', 'risp', 'munic', 'mcirc','regiao'],
                                     var_name='TipoOcorrencias',
                                     value_name='Qtde').query("ano >= 2023 and TipoOcorrencias not in ('outros_roubos', 'total_roubos', 'outros_furtos', 'total_furtos', 'apf', 'aaapai','cmp', 'cmba','registro_ocorrencias', 'fase')")

df_ocorrencias.to_excel('Ocorrencias_2023.xlsx', index=False, sheet_name='ocorrencias')