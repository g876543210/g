from tkinter import *
from tkinter import messagebox

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    

def btn_clear():
    global expression
    expression = ''
    input_text.set(expression)
    pass

def btn_backclear():
    global expression
    expression = expression[0:len(expression)-1]
    input_text.set(expression)
    
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=''
 
    


win=Tk()
win.title("welcome to calc pro ")
win.geometry("400x500+300+100")
win.resizable()
root = Frame(win, width=400, height=500, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
root.pack(side=TOP)

expression=""
input_text=StringVar()

keyEntry=Entry(root,textvariable=input_text,width=35,fg='black', bd=5,font=('arial',20, 'bold'))
keyEntry.place(x=2,y=55)

btn1=Button(root,text="1",font=50,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(1))
btn1.place(x=5,y=105)
btn2=Button(root,text="2",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(2))
btn2.place(x=135,y=105)
btn3=Button(root,text="3",font=20,width=11,height=2,fg="black",bg="#ed3833",command=lambda:btn_click(3))
btn3.place(x=265,y=105)
btn4=Button(root,text="4",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(4))
btn4.place(x=5,y=165)
btn5=Button(root,text="5",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(5))
btn5.place(x=135,y=165)
btn6=Button(root,text="6",font=20,width=11,height=2,fg="black",bg="#ed3833",command=lambda:btn_click(6))
btn6.place(x=265,y=165)
btn7=Button(root,text="7",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(7))
btn7.place(x=5,y=225)
btn8=Button(root,text="8",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(8))
btn8.place(x=135,y=225)
btn9=Button(root,text="9",font=20,width=11,height=2,fg="black",bg="#ed3833",command=lambda:btn_click(9))
btn9.place(x=265,y=225)

btnclear=Button(root,text="C",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_clear())
btnclear.place(x=5,y=285)
btn0=Button(root,text="0",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click(0))
btn0.place(x=135,y=285)
btnper=Button(root,text="del",font=20,width=5,height=1,fg="black",bg="#fff",command=lambda:btn_backclear())
btnper.place(x=342,y=15)
btnadd=Button(root,text="+",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click('+'))
btnadd.place(x=5,y=351)
btnmul=Button(root,text="X",font=20,width=11,height=3,fg="black",bg="#ed3833",command=lambda:btn_click('*'))
btnmul.place(x=135,y=351)
btneql=Button(root,text="=",font=20,width=11,height=5,fg="black",bg="#ed3833",command=lambda:btn_equal())
btneql.place(x=265,y=285)
btnsub=Button(root,text="-",font=20,width=11,height=2,fg="black",bg="#ed3833",command=lambda:btn_click('-'))
btnsub.place(x=5,y=420)
btndiv=Button(root,text="÷",font=20,width=11,height=2,fg="black",bg="#ed3833",command=lambda:btn_click('/'))
btndiv.place(x=135,y=420)
#Button(text="÷",font=20,width=11,height=2,fg="white",bg="#ed3833").place(x=140,y=400)


win.mainloop()
 