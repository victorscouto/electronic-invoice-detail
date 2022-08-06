from xml.dom import minidom
import pandas as pd


lst_cprod  = []
lst_cean   = []
lst_xprod  = []
lst_vuncom = []
lst_ucom   = []
lst_qcom   = []
lst_vprod  = []
lst_data_proc = []
lst_dt_emissao = []

with open("../assets/raw/to-do/26220602193012000105550010002389511065963317.xml", 'r', encoding='utf-8') as file:
  xml = minidom.parse(file)
  cprod  = xml.getElementsByTagName("cProd")
  cean   = xml.getElementsByTagName("cEAN")
  xprod  = xml.getElementsByTagName("xProd")
  vuncom = xml.getElementsByTagName("vUnCom")
  ucom   = xml.getElementsByTagName("uCom")
  qcom   = xml.getElementsByTagName("qCom")
  vprod  = xml.getElementsByTagName("vProd")
  data_proc = xml.getElementsByTagName("dhEmi")

  for tag in data_proc:
      lst_data_proc.append(tag.firstChild.data)

  data_emissao_nfe = '{}{}{}'.format(lst_data_proc[0][0:4],
                                     lst_data_proc[0][5:7],
                                     lst_data_proc[0][8:10])

  for tag in cprod:
    lst_cprod.append(tag.firstChild.data)

  for tag in cean:
    lst_cean.append(tag.firstChild.data)

  for tag in xprod:
    lst_xprod.append(tag.firstChild.data)

  for tag in vuncom:
    f_vuncom = round(float(tag.firstChild.data), 2)
    lst_vuncom.append(str(f_vuncom).replace('.',','))

  for tag in ucom:
    lst_ucom.append(tag.firstChild.data)

  for tag in qcom:
    lst_qcom.append(tag.firstChild.data)

  for tag in vprod:
    f_vprod = round(float(tag.firstChild.data), 2)
    lst_vprod.append(str(f_vprod).replace('.',','))
    lst_dt_emissao.append(data_emissao_nfe)

df = pd.DataFrame(list(zip(lst_cprod, lst_cean, lst_xprod,
                           lst_vuncom, lst_ucom, lst_qcom,
                           lst_vprod, lst_dt_emissao)),
                  columns=['cprod', 'ean', 'nome_prod',
                           'valor_unit', 'unit_com',
                           'qtde', 'valor_total', 'dt_emissao_nfe'])

df.set_index('cprod', inplace=True)

df.to_csv(path_or_buf='../assets/stg/nfe-venosan-price.csv', sep=';', encoding='utf-8')
