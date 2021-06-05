from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("Rental Mobil")
root.geometry("450x570")

bg = PhotoImage(file="D:\SD card\Background.png")
label1 = Label(root, image=bg)
label1.pack()

def harga():
    try:
        int(e2.get())
        int(e3.get())

        mbl = listmobil.get()
        nama = e1.get()
        hri = int(e3.get())
        pembayaran = listpembayaran.get()

        avanza = 300000
        fortuner = 550000
        xenia = 300000
        hiace = 1100000
        alphard  = 1200000

        if mbl == "Toyota Avanza":
            total = hri*avanza
        elif mbl == "Toyota Fortuner":
            total = hri*fortuner
        elif mbl == "Daihatsu Xenia":
            total = hri*xenia
        elif mbl == "Toyota Hi-Ace":
            total = hri*hiace
        elif mbl == "Toyota Alphard":
            total = hri*alphard

        global label17, label18, label19, label20, label21, label22

        label17 = Label(root, text="Nama :  " + nama, bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10)) 
        label17.place(x=5, y=420)
        label18 = Label(root, text="Jenis Mobil : " + mbl, bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
        label18.place(x=5, y=440)
        label19 = Label(root, text="Lama Meminjam : " + str(hri) + " hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
        label19.place(x=5, y=460)
        label20 = Label(root, text="Total Pembayaran : " + "Rp" + str(total), bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
        label20.place(x=5, y=480)
        label21 = Label(root, text="Metode Pembayaran : ", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
        label21.place(x=5, y=500)

        global label22, label23, label24, label25, label26, label27, label28, label29, label30, label31

        if pembayaran == "Bank BCA":
            label22 = Label(root, text="No.Rek 7000561985, An.Fachrurazi", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label22.place(x=5, y=520)
            label23 = Label(root, text="Bank BCA", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label23.place(x=140, y=500)
        elif pembayaran == "Bank Mandiri":
            label24 = Label(root, text="No.Rek 3119866513230, An.Fachrurazi", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label24.place(x=5, y=520)
            label25 = Label(root, text="Bank Mandiri", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label25.place(x=140, y=500)
        elif pembayaran == "Bank BNI":
            label26 = Label(root, text="No.Rek 1000348841, An.Fachrurazi", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label26.place(x=5, y=520)
            label27 = Label(root, text="Bank BNI", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label27.place(x=140, y=500)
        elif pembayaran == "Shopee Pay":
            label28 = Label(root, text="No.Tlp 085716362188", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label28.place(x=5, y=520)
            label29 = Label(root, text="Shopee Pay", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label29.place(x=140, y=500)
        elif pembayaran == "Dana":
            label30 = Label(root, text="No.Tlp 085716362188", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label30.place(x=5, y=520)
            label31 = Label(root, text="Dana", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
            label31.place(x=140, y=500)
    except:
        messagebox.showerror("Error", "Data Input Salah/Belum Mengisi Semua Data")

def clear():

    pembayaran = listpembayaran.get()

    listmobil.set(" ")
    listpembayaran.set(" ")
    label17.destroy()
    label18.destroy()
    label19.destroy()
    label20.destroy()
    label21.destroy()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    
    if pembayaran == "Bank BCA":
        label23.destroy()
        label22.destroy()
    elif pembayaran == "Bank Mandiri":
        label25.destroy()
        label24.destroy()
    elif pembayaran == "Bank BNI":
        label27.destroy()
        label26.destroy()
    elif pembayaran == "Shopee Pay":
        label29.destroy()
        label28.destroy()
    elif pembayaran == "Dana":
        label31.destroy()
        label30.destroy()


label2 = Label(root, text="Masukkan Nama Lengkap Anda", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label2.place(x=10, y=70)
label3 = Label(root, text="Masukkan No.Tlp", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label3.place(x=10, y=130)
label4 = Label(root, text="Pilih Jenis Mobil", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label4.place(x=10, y=190)
label5 = Label(root, text="Masukkan Jumlah hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label5.place(x=10, y=250)
label6 = Label(root, text="Metode Pembayaran", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label6.place(x=10, y=310)
label7 = Label(root, text="Toyota Avanza", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label7.place(x=230, y=70)
label8 = Label(root, text="Toyota Fortuner", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label8.place(x=230, y=160)
label9 = Label(root, text="Daihatsu Xenia", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label9.place(x=230, y=260)
label10 = Label(root, text="Toyota Hi-Ace", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label10.place(x=230, y=359)
label11 = Label(root, text="Toyota Alphard", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",10))
label11.place(x=230, y=455)
label12 = Label(root, text="Rp350.000/Hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",8))
label12.place(x=360, y=100)
label13 = Label(root, text="Rp.550.000/Hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",8))
label13.place(x=360, y=200)
label14 = Label(root, text="Rp300.000/Hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",8))
label14.place(x=360, y=300)
label15 = Label(root, text="Rp1.100.000/Hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",8))
label15.place(x=360, y=400)
label16 = Label(root, text="Rp1.200.000/Hari", bg="#f0f0d8", fg="#60a8c0", font=("helvetica",8))
label16.place(x=360, y=500)


e1 = Entry(root, width=32)
e1.place(x=10, y=90)
e2 = Entry(root, width=32)
e2.place(x=10, y=150)
e3 = Entry(root, width=32)
e3.place(x=10, y=270)

list1 = ["Toyota Avanza", "Toyota Fortuner", "Daihatsu Xenia", "Toyota Hi-Ace", "Toyota Alphard"]
listmobil = StringVar(root)
listmobil.set(" ")
list2 = ["Bank BCA","Bank BNI", "Bank Mandiri", "Shopee Pay", "Dana"]
listpembayaran = StringVar(root)
listpembayaran.set(" ")

drop1 = OptionMenu(root, listmobil, *list1)
drop1.place(x=10, y=210, width=200)
drop2 = OptionMenu(root, listpembayaran, *list2)
drop2.place(x=10, y=330, width=200)

pesan = Button(root, text="Pesan", command=harga, width=10)
pesan.place(x=10, y=370)
clear = Button(root, text="Clear", command=clear, width=10)
clear.place(x=120, y=370)

root.mainloop()
