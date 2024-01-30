import tkinter as tk
from random import randint
import threading

class ZarAtmaUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Zar Atma Deneyi")
        self.root.geometry("800x600")
        
        self.sonuc_label = tk.Label(root, text="Sonuç: ")
        self.sonuc_label.pack(pady=10)

        self.zar_at_button = tk.Button(root, text="Zar At", command=self.zar_at)
        self.zar_at_button.pack(pady=20)

        self.zar_at_100_button = tk.Button(root, text="100 Zar At", command=lambda: self.zar_at_n(100))
        self.zar_at_100_button.pack(pady=10)

        self.zar_at_1000_button = tk.Button(root, text="1000 Zar At", command=lambda: self.zar_at_n(1000))
        self.zar_at_1000_button.pack(pady=10)

        self.zar_at_100000_button = tk.Button(root, text="100.000 Zar At", command=lambda: self.zar_at_n(100000))
        self.zar_at_100000_button.pack(pady=10)

        self.sonuclar_listbox = tk.Listbox(root, width=30, height=10)
        self.sonuclar_listbox.pack()

        self.gelme_oranlari_label = tk.Label(root, text="Gelme Oranları:")
        self.gelme_oranlari_label.pack()

        self.gelme_oranlari_listbox = tk.Listbox(root, width=30, height=10)
        self.gelme_oranlari_listbox.pack()

        self.zar_sayisi = 0
        self.zar_gelme_sayisi = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def zar_at(self):
        zar_sonucu = randint(1, 6)
        self.sonuc_label.config(text=f"Sonuç: {zar_sonucu}")

        self.sonuclar_listbox.insert(0, f"Atış: {zar_sonucu}")
        self.zar_sayisi += 1
        self.zar_gelme_sayisi[zar_sonucu] += 1

        self.guncelle_gelme_oranlari()

    def zar_at_n(self, n):
        for _ in range(n):
            zar_sonucu = randint(1, 6)
            self.sonuclar_listbox.insert(0, f"Atış: {zar_sonucu}")
            self.zar_sayisi += 1
            self.zar_gelme_sayisi[zar_sonucu] += 1

        self.guncelle_gelme_oranlari()

    def guncelle_gelme_oranlari(self):
        self.gelme_oranlari_listbox.delete(0, tk.END)
        for i in range(1, 7):
            gelme_orani = (self.zar_gelme_sayisi[i] / self.zar_sayisi) * 100 if self.zar_sayisi > 0 else 0
            self.gelme_oranlari_listbox.insert(0, f"{i}: %{gelme_orani:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = ZarAtmaUygulamasi(root)
    root.mainloop()
