#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns

def merkezi_egilim_ve_dagilim_hesapla(dizi):
    # Ortalama hesapla
    ortalama = sum(dizi) / len(dizi)
    
    # Medyan hesapla
    sirali_dizi = sorted(dizi)
    n = len(dizi)
    if n % 2 == 0:
        medyan = (sirali_dizi[n // 2 - 1] + sirali_dizi[n // 2]) / 2
    else:
        medyan = sirali_dizi[n // 2]
    
    # Standart sapma hesapla
    toplam_kare_fark = sum((x - ortalama) ** 2 for x in dizi)
    standart_sapma = (toplam_kare_fark / len(dizi)) ** 0.5
    
    # Histogram, Kutu Grafiği ve Scatter Plot'u Çiz
    plt.figure(figsize=(15, 5))

    # Histogram
    plt.subplot(1, 3, 1)
    plt.hist(dizi, bins=20, color='blue', edgecolor='black')
    plt.title('Histogram')

    # Kutu Grafiği
    plt.subplot(1, 3, 2)
    plt.boxplot(dizi)
    plt.title('Kutu Grafiği')

    # Scatter Plot
    plt.subplot(1, 3, 3)
    sns.scatterplot(x=range(len(dizi)), y=dizi, color='green')
    plt.title('Scatter Plot')

    # Ortalama ve Medyanı göster
    plt.axhline(ortalama, color='red', linestyle='dashed', linewidth=2, label='Ortalama')
    plt.axhline(medyan, color='orange', linestyle='dashed', linewidth=2, label='Medyan')

    # Grafiği göster
    plt.legend()
    plt.show()

    # Sonuçları ekrana yazdır
    print("Ortalama:", ortalama)
    print("Medyan:", medyan)
    print("Standart Sapma:", standart_sapma)

# Kullanıcıdan dizi girişi al
try:
    dizi = [float(x) for x in input("Diziyi girin (sayıları boşlukla ayırın): ").split()]
    
    # Fonksiyonu çağır
    merkezi_egilim_ve_dagilim_hesapla(dizi)
except ValueError:
    print("Lütfen geçerli sayılar girin.")


# In[ ]:





# In[ ]:





# In[ ]:




