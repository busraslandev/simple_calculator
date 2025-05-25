import tkinter as tk 

def butona_tikla(karakter):
    mevcut = giris.get()
    giris.delete(0, tk.END)
    giris.insert(tk.END, mevcut + karakter)

 

def hesapla():
    try:
        mevcut = giris.get()
        sonuc = eval(mevcut)
        giris.delete(0, tk.END)
        giris.insert(tk.END, float(sonuc))
    except:
        giris.delete(0, tk.END)
        giris.insert(tk.END, "hata")
def sil():
    mevcut = giris.get()
    mevcut = mevcut[:-1]

root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("390x485")
root.configure(bg="#375838")


giris = tk.Entry(root, width=40, borderwidth=8,bg="#C8E4C9",fg="#000000")
giris.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

butonlar = [
    ('7',1,0), ('8',1,1), ('9',1,2),('sil',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('- ',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('+',3,3),
    ('0',4,0), ('*',4,1), ('/',4,2), ('=',4,3),
]

for (text, row, col) in butonlar:
    if text=="=":
        komut = hesapla
    elif text=="sil":
        komut = sil
    else:
        komut =lambda x=text: butona_tikla(x)

    tk.Button(root, text=text, padx=40, pady=40,bg="#144D43",fg="#FAFAFA", command=komut).grid(row=row, column=col)


root.mainloop()
