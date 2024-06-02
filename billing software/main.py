from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime
import tkinter as tk
import openpyxl,xlrd
from openpyxl import workbook
import pathlib






class bill_app:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1920x1080+0+0")
        self.root.title("billing software")


        # file=pathlib.path("backened_data.xlsx")
        # if file.exists():
        #     pass
        # else:
        #     file=workbook()
        #     sheet=file.active
        #     sheet['A1']="c_name"
        #     sheet['B1']="c_phone"
        #     sheet['C1']="bill_no"
        #     sheet['D1']="c_email"
        #     sheet['E1']="search_bill"
        #     sheet['F1']="product"
        #     sheet['G1']="prices"
        #     sheet['H1']="qty"
        #     sheet['I1']="sub_total"
        #     sheet['J1']="tax_input"
        #     sheet['K1']="total"


        #     file.save("backened_data.xlsx")


        # =================variables============
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_Total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()



        
        #product category list
        self.category=["Select Option","Oil","dry fruit","others"]

        #sub oil
        self.subOil=["soyabean","sarso"]
        self.soyabean=["sunflower","fortune"]
        self.price_sunflower=420
        self.price_fortune=143

        self.sarso=["dabur","fortune1"]
        self.price_dabur=105
        self.price_fortune1=120

        #dry fruit
        self.subdryfruit=["kismis","badam","kaaju"]
        self.kismis=["tatasampan","tulsi"]
        self.price_tatasampan=93
        self.price_tulsi=40
        
        self.badam=["nutraj","kashmiri"]
        self.price_nutraj=899
        self.price_kashmiri=1600

        self.kaaju=["kaajucutting","safed","american"]
        self.price_kaajucutting=408
        self.price_safed=299
        self.price_american=300

        #others
        self.subothers=["kalawa","teen ekka daal","hing"]
        self.kalawa=["pack of 12","rakshasutra"]
        self.price_packof12=180
        self.price_rakshasutra=126

        self.teenekkadaal=["5kg","1kg"]
        self.price_5kg=600
        self.price_1kg=120

        self.hing=["pusp","vandevi"]
        self.price_pusp=1700
        self.price_vandevi=1620





        


        img=Image.open("image/m&b1.jpg")
        img=img.resize((300,130),Image.ANTIALIAS)##antialias gives best quality image it is an parameter
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=300,height=130)
        
        img_1=Image.open("image/pujari.jpg")
        img_1=img_1.resize((500,130),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=300,y=0,width=500,height=130)
        
        img_2=Image.open("image/jain.jpg")
        img_2=img_2.resize((470,130),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=800,y=0,width=470,height=130)

        lbl_title=Label(self.root,text=" M&B BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=130,width=1400,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=('times new roman',16,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=120,height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)


        Cust_Frame=LabelFrame(Main_Frame,text="customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=325,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile_NO",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=4,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=4,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,stick=W,padx=4,pady=2)

        self.lblEmail=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=4,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,stick=W,padx=4,pady=2)
        
        #Product label frame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=335,y=5,width=600,height=140)
        
        #category
        self.lblcategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="select categories",bd=4)
        self.lblcategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_category=ttk.Combobox(Product_Frame,value=self.category,font=("arial",10,"bold"),width=20,state="readonly")
        self.Combo_category.current(0)
        self.Combo_category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        self.Combo_category.bind("<<ComboboxSelected>>",self.categories)

        #subcategory
        self.lblsubcategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="select sub categories",bd=4)
        self.lblsubcategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.Combosubcategory=ttk.Combobox(Product_Frame,value=[""],font=("arial",10,"bold"),width=20,state="readonly")
        self.Combosubcategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        self.Combosubcategory.bind("<<ComboboxSelected>>",self.product_Add)

        #product Name
        self.lblproductcategory=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Product Name",bd=4)
        self.lblproductcategory.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Comboproduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial",10,"bold"),width=20,state="readonly")
        self.Comboproduct.grid(row=2,column=1,stick=W,padx=5,pady=2)
        self.Comboproduct.bind("<<ComboboxSelected>>",self.price)

        #price
        self.lblprice=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="price",bd=4)
        self.lblprice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.Comboprice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=20,state="readonly")
        self.Comboprice.grid(row=0,column=3,stick=W,padx=5,pady=2)


        #Qty
        self.lblQty=Label(Product_Frame,font=("arial",12,"bold"),bg="white",text="Qty",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10,"bold"),width=20)
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)

        #middle frame
        middle_Frame=Frame(Main_Frame,bd=10)
        middle_Frame.place(x=10,y=150,width=930,height=340)

        #image
        img12=Image.open("image/mix.jpg")
        img12=img12.resize((465,340),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        lbl_img12=Label(middle_Frame,image=self.photoimg12)
        lbl_img12.place(x=0,y=0,width=465,height=200)


        #image 1
        img_13=Image.open("image/bill.jpg")
        img_13=img_13.resize((465,340),Image.ANTIALIAS)
        self.photoimg_13=ImageTk.PhotoImage(img_13)
        
        lbl_img_13=Label(middle_Frame,image=self.photoimg_13)
        lbl_img_13.place(x=465,y=0,width=465,height=200)


        #search
        search_Frame=Frame(Main_Frame,bd=2,bg="white")
        search_Frame.place(x=950,y=10,width=500,height=40)

        self.lblbill=Label(search_Frame,font=("arial",12,"bold"),fg="white",bg="red",text="Bill Number")
        self.lblbill.grid(row=0,column=0,stick=W,padx=1)

        self.txt_Entry_search=ttk.Entry(search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=12)
        self.txt_Entry_search.grid(row=0,column=1,stick=W,padx=2)

        self.Btnsearch=Button(search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=10,cursor="hand2")
        self.Btnsearch.grid(row=0,column=2)







        #rightframe bill area

        RightLabelFrame=LabelFrame(Main_Frame,text="BILL Area ",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=950,y=40,width=325,height=290)

        Scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=Scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #bill counter label frame
        bottom_Frame=LabelFrame(Main_Frame,text="bill counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        bottom_Frame.place(x=0,y=330,width=1300,height=120)

        self.lblsubTotal=Label(bottom_Frame ,font=("arial",12,"bold"),bg="white",text="SubTotal",bd=4)
        self.lblsubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntysubTotal=ttk.Entry(bottom_Frame,font=("arial",10,"bold"),width=24)
        self.EntysubTotal.grid(row=0,column=1,stick=W,padx=5,pady=2)

        self.lbl_tax=Label(bottom_Frame,font=("arial",12,"bold"),bg="white",text="Gov Tax",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(bottom_Frame,font=("arial",10,"bold"),width=24)
        self.txt_tax.grid(row=1,column=1,stick=W,padx=5,pady=2)

        self.lblAmountTotal=Label(bottom_Frame,font=("arial",12,"bold"),bg="white",text="Total",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(bottom_Frame,font=("arial",10,"bold"),width=24)
        self.txtAmountTotal.grid(row=2,column=1,stick=W,padx=5,pady=2)

        #botton frame

        Btn_Frame=Frame(bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddtoCart=Button(Btn_Frame,command=self.Additem,text="Add to cart",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnAddtoCart.grid(row=0,column=0)

        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,text="generate bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,command=self.save_bill,text="Save bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
        #====================function declarartion ==================================

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END," Welcome to Mukesh & Brothers")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Number:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email Number:{self.c_email.get()}")

        self.textarea.insert(END,f"\n ================================\n")
        self.textarea.insert(END,f"\n products\t\tQTY\t\tprice")
        self.textarea.insert(END,f"\n ================================")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_Total.set("")
        self.tax_input.set('')
        self.total.set("")
        self.welcome()












    def Additem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","please select the product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t{self.m}")
            self.sub_Total.set(str("Rs%.2f" %(sum(self.l))))
            self.tax_input.set(str(" Rs%.2f " %((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str(" Rs%.2f " %(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))



    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please add to cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END," =========================")
            self.textarea.insert(END,f" \nSub Amount:\t{self.sub_Total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t{self.total.get()}")
            self.textarea.insert(END,"\n =========================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    



    def categories(self,event=""):
        if self.Combo_category.get()=="Oil":
            self.Combosubcategory.config(values=self.subOil)
            self.Combosubcategory.current(0)

        if self.Combo_category.get()=="dry fruit":
            self.Combosubcategory.config(values=self.subdryfruit)
            self.Combosubcategory.current(0)

        if self.Combo_category.get()=="others":
            self.Combosubcategory.config(values=self.subothers)
            self.Combosubcategory.current(0)

    def product_Add(self,event=""):
        if self.Combosubcategory.get()=="soyabean":
            self.Comboproduct.config(value=self.soyabean) 
            self.Comboproduct.current(0)  

        if self.Combosubcategory.get()=="sarso":
            self.Comboproduct.config(value=self.sarso) 
            self.Comboproduct.current(0)  

        #dryfruit

        if self.Combosubcategory.get()=="kismis":
            self.Comboproduct.config(values=self.kismis)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="badam":
            self.Comboproduct.config(values=self.badam)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="kaaju":
            self.Comboproduct.config(values=self.kaaju)
            self.Comboproduct.current(0)

        #others

        if self.Combosubcategory.get()=="kalawa":
            self.Comboproduct.config(values=self.kalawa)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="teen ekka daal":
            self.Comboproduct.config(values=self.teenekkadaal)
            self.Comboproduct.current(0)

        if self.Combosubcategory.get()=="hing":
            self.Comboproduct.config(values=self.hing)
            self.Comboproduct.current(0)

    def price(self,event=""):
        #oil
        if self.Comboproduct.get()=="sunflower":
            self.Comboprice.config(value=self.price_sunflower)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="fortune":
            self.Comboprice.config(value=self.price_fortune)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="dabur":
            self.Comboprice.config(value=self.price_dabur)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="fortune1":
            self.Comboprice.config(value=self.price_fortune1)
            self.Comboprice.current(0)
            self.qty.set(1)
#dry fruit
        if self.Comboproduct.get()=="tatasampan":
            self.Comboprice.config(value=self.price_tatasampan)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="tulsi":
            self.Comboprice.config(value=self.price_tulsi)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="nutraj":
            self.Comboprice.config(value=self.price_nutraj)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="kashmiri":
            self.Comboprice.config(value=self.price_kashmiri)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="kaajucutting":
            self.Comboprice.config(value=self.price_kaajucutting)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="safed":
            self.Comboprice.config(value=self.price_safed)
            self.Comboprice.current(0)
            self.qty.set(1)
        if self.Comboproduct.get()=="american":
            self.Comboprice.config(value=self.price_american)
            self.Comboprice.current(0)
            self.qty.set(1)
#others
        if self.Comboproduct.get()=="pack of 12":
            self.Comboprice.config(value=self.price_packof12)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="rakshasutra":
            self.Comboprice.config(value=self.price_rakshasutra)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="5kg":
            self.Comboprice.config(value=self.price_5kg)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="1kg":
            self.Comboprice.config(value=self.price_1kg)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="pusp":
            self.Comboprice.config(value=self.price_pusp)
            self.Comboprice.current(0)
            self.qty.set(1)

        if self.Comboproduct.get()=="vandevi":
            self.Comboprice.config(value=self.price_vandevi)
            self.Comboprice.current(0)
            self.qty.set(1)





       


        

       





        
        
        
        
        

    
if __name__ == '__main__':
    root=Tk()
    obj=bill_app(root)
    root.mainloop()




