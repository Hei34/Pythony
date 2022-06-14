import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

datax=[1,2,3,4,5,6,7]
datay=[30,22,31,34,15,16,17]
datay2=[10,32,11,24,35,26,27]
datay3=[36,12,11,14,15,36,67]
szer=0.3
indexy=np.arange(len(datax))

fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1)
ax1.bar(indexy-szer, datay,width=szer, label="wykres1")
ax1.bar(indexy, datay2,width=szer, label="wykres2")
ax1.bar(indexy+szer, datay3,width=szer, label="wykres3")

x=np.linspace(0,10)
ax2.plot(x,x**2)
# plt.show()

tabelkaexelka = pd.read_excel('ceny2.xlsx')
tabelkaexelka.columns=['towar','wartosc','jednostka','rok']
produkt1 = tabelkaexelka.query('towar == "ryż - za 1kg"')
produkt2 = tabelkaexelka.query('towar == "mąka pszenna - za 1kg"')
print(produkt2['wartosc'].mean())

tabelkaexelka.plot()
plt.show()