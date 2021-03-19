from tkinter import *
root=Tk()
root.geometry("400x500")
label_name=Label(root,text="Name : ")
label_name.place(relx=0.3,rely=0.1,anchor=CENTER)
entry_name=Entry()
entry_name.place(relx=0.6,rely=0.1,anchor=CENTER)
label_pass=Label(root,text="Password : ")
label_pass.place(relx=0.3,rely=0.2,anchor=CENTER)
entry_pass=Entry()
entry_pass.place(relx=0.6,rely=0.2,anchor=CENTER)
label_cap=Label(root,text="Captcha : ")
label_cap.place(relx=0.3,rely=0.3,anchor=CENTER)
entry_cap=Entry()
entry_cap.place(relx=0.6,rely=0.3,anchor=CENTER)
label_na=Label(root)
label_na.place(relx=0.5,rely=0.5,anchor=CENTER)
label_ca=Label(root)
label_ca.place(relx=0.5,rely=0.6,anchor=CENTER)
label_pa=Label(root)
label_pa.place(relx=0.5,rely=0.7,anchor=CENTER)
na=""
ca=""
pa=""
class Database():
    def __init__(self):
        self.__name="RK"
        self.__pass="abcd"
        self.__cap="royce"
    def se(self):
        global na
        global ca
        global pa
        na=entry_name.get()
        pa=entry_pass.get()
        ca=entry_cap.get()
        self.__name=na
        self.__pass=pa
        self.__cap=ca
    def GetUser(self):
        label_na["text"]=self.__name
        label_pa["text"]=self.__pass
        label_ca["text"]=self.__cap
def do():
    obj=Database()
    obj.se()
btn=Button(root,text="Update Login Details",command=do)
btn.place(relx=0.3,rely=0.4,anchor=CENTER)
btn1=Button(root,text="Show Profile",command=Database().GetUser)
btn1.place(relx=0.7,rely=0.4,anchor=CENTER)
root.mainloop()
