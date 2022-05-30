#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from  tkinter import BOTH
from tkinter import ttk
import numpy as np
import numpy.linalg as la
import tkinter.messagebox




class Example(tk.Frame):
  
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="gray80")
  
        
        self.frame = tk.Frame(self.canvas, background="gray80")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        
        
       
        
        
        self.canvas.pack(side="left", fill="both", expand=True)
        
        
      
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        
        self.canvas.create_line(200,25,200,25,fill='black')

        
        self.frame.bind("<Configure>", self.onFrameConfigure)
       
        self.populate()
        

    def populate(self):
        
        global v
        v=tk.IntVar()
        v.set(10)
        
        global o
        o=tk.IntVar()
        o.set(12)
        global entry
        
        global A
        global B
        global C
        global D
        global E
        global F
        global G
        global H
        
        
        #fi
        def closer():
            ans=tkinter.messagebox.askquestion('Exit Pane','Are you sure you want to exit the Program?')
            if ans=='yes':
                root.destroy()
        
        
        e0=tk.Label(self.frame,text='')
        e5=tk.Label(self.frame,text='')
        l18=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80")
        l18.place(x=340,y=330)  
        l19=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80")
        l19.place(x=80,y=410)
        
       
        heading=tk.Label(self.frame,text="BASIC OPERATIONS ON MATRICES",width="63",height="1",bg="gray99",font="Segoe 25 underline bold",fg='gray99').grid(row=0,column=0,columnspan=24,rowspan=1,sticky='N',pady=1)
        heading_2=tk.Label(self.frame,text="BASIC OPERATIONS ON MATRICES",height="1",bg="gray99",font="Segoe 25 underline bold").place(x=250,y=1)#grid(row=0,column=0,columnspan=24,rowspan=1,sticky='N',pady=1)
        l1=tk.Label(self.frame,text=' Prepared By: Krishang Gupta',font=("Arial",8),bg="gray80",fg="gray80").grid(row=3,column=20,columnspan=3,sticky='W')
        l2=tk.Label(self.frame,text='                   2K20/A9/49',font=("Arial",8),bg="gray80",fg="gray80").grid(row=4,column=21,sticky='W')
        l3=tk.Label(self.frame,text='                   Mechanical Engineering(I SEM)',font=("Arial",8),bg="gray80",fg="gray80").grid(row=5,column=21,sticky='w')
        l4=tk.Label(self.frame,text='Guided  By  :  Dr.Nilam and Ankit Sharma Sir',font=("Arial",8),bg="gray80",fg="gray80").grid(row=6,column=20,columnspan=4,sticky='W')
        
        l1_2=tk.Label(self.frame,text=' Prepared By: Krishang Gupta',font=("Arial",8),bg="gray80").place(x=800,y=50)#grid(row=3,column=20,columnspan=3,sticky='W')
        l2_2=tk.Label(self.frame,text='                   2K20/A9/49',font=("Arial",8),bg="gray80").place(x=812,y=70)#grid(row=4,column=21,sticky='W')
        l3_2=tk.Label(self.frame,text='                   Mechanical Engineering(I SEM)',font=("Arial",8),bg="gray80").place(x=812,y=90)#grid(row=5,column=21,sticky='w')
        l4_2=tk.Label(self.frame,text='Guided  By  :  Dr.Nilam  and Ankit Sharma Sir',font=("Arial",8),bg="gray80").place(x=800,y=110)#grid(row=6,column=20,columnspan=4,sticky='W')
        
        endtitle=tk.Label(self.frame,text='Dedicated To  : Bhagat Singh Sir (Principal and HOD Mathematics,Hope Hall Foundation School,R.K.Puram,New-Delhi & Ankit Mittal Sir(FIITJEE, South Delhi) )',font=("Arial",6),bg="gray80")
        endtitle.place(x=300,y=1160)
    
        
        l5=tk.Label(self.frame,text='Select the Order of the Square Matrices\t:',fg="blue",bg="gray80",font="Times 18").grid(row=13,column=0,columnspan=3,sticky='w')
        
        r1=tk.Radiobutton(self.frame,text=" 2x2",fg="black",bg="gray80",font="Times 15",variable=v,value=0,command=lambda:changer()).grid(row=13,column=6,sticky='w')
        r2=tk.Radiobutton(self.frame,text=" 3x3",fg="black",bg="gray80",font="Times 15",variable=v,value=1,command=lambda:changer()).grid(row=13,column=8,sticky='w')
                 
            
        waste1=tk.Label(self.frame,text=" ",fg="red",bg="gray80",font="Times 15").grid(row=13,column=10,sticky='w')
        waste2=tk.Label(self.frame,text="hihieiieh ",fg="gray80",bg="gray80",font="Times 15").grid(row=13,column=12,sticky='w')
                    
            
            
        blank=tk.Label(self.frame,text='\n\n\n',bg="gray80").grid(row=15,column=0) 
        
        l6=tk.Label(self.frame,text='Select the Operation on Matrices\t:',fg="blue",bg="gray80",font="Times 18").grid(row=25,column=0,columnspan=4,sticky='w')
        r5=tk.Radiobutton(self.frame,text="Add",fg="black",bg="gray80",font="Times 15",variable=o,value=0,command=lambda:changer()).grid(row=25,column=6,sticky='w')
        r6=tk.Radiobutton(self.frame,text="Subtract",fg="black",bg="gray80",font="Times 15",variable=o,value=1,command=lambda:changer()).grid(row=27,column=6,sticky='w')
        r7=tk.Radiobutton(self.frame,text="Multiply",fg="black",bg="gray80",font="Times 15",variable=o,value=2,command=lambda:changer()).grid(row=29,column=6,sticky='w')
        r8=tk.Radiobutton(self.frame,text="Inverse",fg="black",bg="gray80",font="Times 15",variable=o,value=3,command=lambda:changer()).grid(row=25,column=8,sticky='w')
        r9=tk.Radiobutton(self.frame,text="Adjoint",fg="black",bg="gray80",font="Times 15",variable=o,value=4,command=lambda:changer()).grid(row=27,column=8,sticky='w')
        r10=tk.Radiobutton(self.frame,text="Determinant",fg="black",bg="gray80",font="Times 15",variable=o,value=5,command=lambda:changer()).grid(row=29,column=8,sticky='w')
        r11=tk.Radiobutton(self.frame,text="Transpose",fg="black",bg="gray80",font="Times 15",variable=o,value=6,command=lambda:changer())
        r11.grid(row=25,column=10,sticky='w')
    
        l7=tk.Label(self.frame,text='2X2',bg="gray80",font=("Arial",25),fg="red").grid(row=40,column=0)
        
        
       
        l8=tk.Label(self.frame,text='[',font=("Script",100),bg="gray80").grid(row=46,column=1,rowspan=3,sticky='w')
        
        
        
        
        
        
        
        e1=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e1.grid(row=46,column=1)#a11
        e2=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e2.grid(row=46,column=2,sticky='w')#a12
        e3=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e3.grid(row=47,column=1,sticky='s')#a21
        e4=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e4.grid(row=47,column=2,sticky='sw')#a22   
    
        l9=tk.Label(self.frame,text=']',font=("Script",100),bg="gray80",fg="black").grid(row=46,column=2,rowspan=3)
        
        
        
        l20=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80")
        l20.place(x=357,y=422)
        
        
        
        
      
    
        l10=tk.Label(self.frame,text='[',font=("Script",100),bg="gray80").place(x=380,y=370)
        
        e6=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e6.grid(row=46,column=6)#a11
        e7=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e7.grid(row=46,column=7,sticky='e')#a12
        e8=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e8.grid(row=47,column=6,sticky='s')#a21
        e9=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e9.grid(row=47,column=7,sticky='se')#a22
    
        l11=tk.Label(self.frame,text=']',font=("Script",100),bg="gray80").grid(row=46,column=8,rowspan=3,sticky='w')
        
        
        
        
    
        
        
        l12=tk.Label(self.frame,text='[',font=("Script",100),bg="gray80").place(x=730,y=370)
        
        e10=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e10.grid(row=46,column=11,sticky='e',padx='3')#a11
        e11=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e11.grid(row=46,column=12,sticky='e')#a12
        e12=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e12.grid(row=47,column=11,sticky='se',padx='3')#a21
        e13=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e13.grid(row=47,column=12,sticky='se')#a22
    
        l13=tk.Label(self.frame,text=']',font=("Script",100),bg="gray80").grid(row=46,column=15,rowspan=3,sticky='w')
        
        
        #determinant
        
        l14=tk.Label(self.frame,text='|',font=("Script",100),bg="gray80").grid(row=50,column=1,rowspan=3,sticky='w')
        e14=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e14.grid(row=50,column=1)#a11
        e15=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e15.grid(row=50,column=2,sticky='w')#a12
        e16=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e16.grid(row=51,column=1,sticky='s')#a21
        e17=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e17.grid(row=51,column=2,sticky='sw')#a22
        l15=tk.Label(self.frame,text='|',font=("Script",100),bg="gray80").grid(row=50,column=2,rowspan=3)
        
        
        
        
        e18=tk.Entry(self.frame,bd=7,width='15',state="disabled",disabledbackground="gray65")
        e18.place(x=810,y=583)
        
        
        
        
       
        l21=tk.Label(self.frame,text='3X3',bg="gray80",font=("Arial",25),fg="red").grid(row=55,column=0,ipady='30')
        l22=tk.Label(self.frame,text='[',font=("Script",120),bg="gray80").grid(row=56,column=1,rowspan=3,sticky='w')
        tk.Label(self.frame,text="hi",bg="gray80").grid(row=56,column=1)
        tk.Label(self.frame,text="hi",bg="gray80").grid(row=57,column=1)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=58,column=1)
        
        e19=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e19.place(x=180,y=800)
        e20=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e20.place(x=180,y=855)
        e21=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e21.place(x=180,y=905)
        
        
        
        
        l23=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80").grid(row=56,column=2,rowspan=3)
        
        
        
        e22=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e22.place(x=230,y=800)
        e23=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e23.place(x=230,y=855)
        e24=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e24.place(x=230,y=905)
        
        e25=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e25.place(x=280,y=800)
        e26=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e26.place(x=280,y=855)
        e27=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e27.place(x=280,y=905)
        
        
        
        
        
        
        
        l24=tk.Label(self.frame,text='[',font=("Script",120),bg="gray80").place(x=390,y=785)#grid(row=56,column=3,rowspan=3,sticky='w')
        l25=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80",fg='gray80').grid(row=56,column=8,rowspan=3,sticky='w')
        l25_2=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80").place(x=550,y=785)#grid(row=56,column=8,rowspan=3,sticky='w')
        e28=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e28.place(x=425,y=800)
        e29=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e29.place(x=425,y=855)
        e30=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e30.place(x=425,y=905)
        
        e31=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e31.place(x=475,y=800)
        e32=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e32.place(x=475,y=855)
        e33=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e33.place(x=475,y=905)
        
        e34=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e34.place(x=525,y=800)
        e35=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e35.place(x=525,y=855)
        e36=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e36.place(x=525,y=905)
        
        
        
        l26=tk.Label(self.frame,text='[',font=("Script",120),bg="gray80").place(x=720,y=785)#grid(row=56,column=3,rowspan=3,sticky='w')
        l27=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80",fg='gray80').grid(row=56,column=16,rowspan=4,sticky='w')
        l27_2=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80").place(x=960,y=785)#grid(row=56,column=16,rowspan=4,sticky='w')
        
        e37=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e37.place(x=765,y=800)
        e38=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e38.place(x=765,y=855)
        e39=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e39.place(x=765,y=905)
        
        e40=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e40.place(x=835,y=800)
        e41=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e41.place(x=835,y=855)
        e42=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e42.place(x=835,y=905)
        
        e43=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e43.place(x=905,y=800)
        e44=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e44.place(x=905,y=855)
        e45=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e45.place(x=905,y=905)
       
    
    
    
    
        l28=tk.Label(self.frame,text='|',font=("Script",120),bg="gray80").grid(row=60,column=1,rowspan=3,sticky='nw')
        l29=tk.Label(self.frame,text='|',font=("Script",120),bg="gray80").grid(row=60,column=2,rowspan=2)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=60,column=1)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=61,column=1)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=62,column=1)
        
        
 
        
        e46=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e46.place(x=180,y=985)
        e47=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e47.place(x=180,y=1040)
        e48=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e48.place(x=180,y=1095)
        
        e49=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e49.place(x=230,y=985)
        e50=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e50.place(x=230,y=1040)
        e51=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e51.place(x=230,y=1095)
        
        e52=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e52.place(x=280,y=985)
        e53=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e53.place(x=280,y=1040)
        e54=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e54.place(x=280,y=1095)
        
        
         
        e55=tk.Entry(self.frame,bd=7,width='15',state="disabled",disabledbackground="gray65")
        e55.place(x=815,y=1040)
        
        
        
        
        
        
        l5=tk.Label(self.frame,text='Select the Order of the Square Matrices\t:',fg="blue",bg="gray80",font="Times 18").grid(row=13,column=0,columnspan=3,sticky='w')
        
        r1=tk.Radiobutton(self.frame,text=" 2x2",fg="black",bg="gray80",font="Times 15",variable=v,value=0,command=lambda:changer()).grid(row=13,column=6,sticky='w')
        r2=tk.Radiobutton(self.frame,text=" 3x3",fg="black",bg="gray80",font="Times 15",variable=v,value=1,command=lambda:changer()).grid(row=13,column=8,sticky='w')
                 
            
        waste1=tk.Label(self.frame,text=" ",fg="red",bg="gray80",font="Times 15").grid(row=13,column=10,sticky='w')
        waste2=tk.Label(self.frame,text="hihieiieh ",fg="gray80",bg="gray80",font="Times 15").grid(row=13,column=12,sticky='w')
                    
            
            
        blank=tk.Label(self.frame,text='\n\n\n',bg="gray80").grid(row=15,column=0) 
        
        
        b0=tk.Button(state="disabled")#waste
        
        
        
        entry=[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,
              e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55]
        
        
        
        
        
        l30=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80",fg='black')
        l30.place(x=340,y=745)
        
        
        l31=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80",fg='black')
        l31.place(x=80,y=845)
        
        l32=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80",fg='black')
        l32.place(x=362,y=850)
        #######################################################################################################
        exitter=tk.Button(self.frame,text="Exit",command=closer,fg='white',bg='red',activebackground='red',height='1',bd='7',width='9',font=(" Arial 10 bold"))
        exitter.place(x=616,y=1100)
        
        
        
        
        for i in range(0,56):
            entry[i].configure(state="disabled")
            entry[i].update()
        
            
      
    
        b1=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b1.place(x=620,y=422)
        
        b2=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b2.place(x=620,y=580)
        
        b3=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b3.place(x=620,y=850)
                     
        b4=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b4.place(x=620,y=1040)

        button=[b0,b1,b2,b3,b4]   
        
            
            
        for i in range(0,5):
            button[i].configure(state="disabled")
            button[i].update()
    
    
        
        
        
        
                
        def compulsary():
            if o.get()!=0 and o.get()!=1 and o.get()!=2 and o.get()!=3 and o.get()!=4 and o.get()!=5 and o.get()!=6:
                tkinter.messagebox.showerror('Error','Select the Operation on the Matrix!')
                
                
                if v.get()==0:
                    for i in range(10,14):
                        entry[i].configure(state="disabled")
                        entry[i].update()
                     
                   
                elif v.get()==1:
                    for i in range(37,46):
                        entry[i].configure(state="disabled")
                        entry[i].update()

                
            
        
        def changer():
            
            l18.configure(text="")
            l18.update()

            l19.configure(text="")
            l19.update()

            l20.configure(text="")
            l20.update()

            
            
            if v.get()==0:#If user selected 2x2 matrix
                   
               
                
                    l30.configure(text="")
                    l30.update()
                    l31.configure(text="")
                    l31.update()
                    l32.configure(text="")
                    l32.update()
              
                    
                    for i in range(19,56):#close entry in 3x3
                        entry[i].configure(state="disabled")
                        entry[i].update()
                    for i in range(0,19):#open all in 2x2
                        entry[i].configure(state="normal")
                        entry[i].update()
                        
                        
                    for i in range(3,5):#close button in 3x3
                        button[i].configure(state="disabled")
                        button[i].update()
                        
                        
                        
                        
                        
                        
                    
                    if o.get()==6:#if user selected by tranpose 
                        l18.configure(text="T")
                        l18.update()
                        
                        
                        

                    elif o.get()==3:#if user selected by inverse
                        l18.configure(text="-1")
                        l18.update()
                        
                        

                    else:
                        l18.configure(text="")
                        l18.update()

                    if o.get()==4:#if user selected by adjoint
                        l19.configure(text="Adj",fg="black")
                        l19.update()
                        
                        
                        
                        
                    else:

                        l19.configure(text="")
                        l19.update()


                    if o.get()==0:#add selected by user
                        l20.configure(text="+")
                        l20.update()

                    elif o.get()==1:#sub selected by user
                        l20.configure(text="-")
                        l20.update()

                    elif o.get()==2:#multiply selected by user
                        l20.configure(text="*")
                        l20.update()
                    else:
                        l20.configure(text="")
                        l20.update()


                    if o.get()==5: #if  determinant selected by user
                        
                       
                        
                        for i in range(14,19):
                            entry[i].configure(state="normal")
                            entry[i].update()
                        for i in range(1,14):
                            entry[i].configure(state="disabled")
                            entry[i].update()
                        
                        
                        b2.configure(state="normal")
                        b1.configure(state="disabled")
                        b2.update()
                        b1.update()



                    else: #instead of determinant 
                        for i in range(14,19):
                            entry[i].configure(state="disabled")
                            entry[i].update()
                            
                        for i in range(1,14):
                            entry[i].configure(state="normal")
                            entry[i].update()
                        
                        b2.configure(state="disabled")
                        b2.update()
                        b1.configure(state="normal")
                        b1.update()
                        
                     
                    if o.get()==3 or o.get()==4 or o.get()==6:#if user selected any of inverse,adjoint,transpose
                        e6.configure(state="disabled")
                        e7.configure(state="disabled")
                        e8.configure(state="disabled")
                        e9.configure(state="disabled")

                        e6.update()
                        e7.update()
                        e8.update()
                        e9.update()

                    elif o.get()!=5:#instead of determinant option 
                        e6.configure(state="normal")
                        e7.configure(state="normal")
                        e8.configure(state="normal")
                        e9.configure(state="normal")
                        e6.update()
                        e7.update()
                        e8.update()
                        e9.update()
                        
                        
                        
                     
                    
                    
           
            elif v.get()==1:#If user selected 3x3 matrix
                
                


                

                    for i in range(1,19):#close the entry boxes in 2x2 columns and close the buttons in 2x2
                            entry[i].configure(state="disabled")
                            entry[i].update()
                            
                    for i in range(1,3):#close the buttons in 2x2
                            button[i].configure(state="disabled")
                            button[i].update()
                            
                            
                    for i in range(19,46):#open the entry boxes of 3x3 first row
                            entry[i].configure(state="normal")
                            entry[i].update()
                            
                        
                            
                            
                    if o.get()==6:#if transpose selected by user
                            l30.configure(text="T")
                            l30.update()

                    elif o.get()==3:#if inverse selected by user
                            l30.configure(text="-1")
                            l30.update()


                    else:
                            l30.configure(text="")
                            l30.update()


                    if o.get()==4:#if adjoint  selected 
                            l31.configure(text="Adj",fg="black")
                            l31.update()
                            
                            

                    else:

                            l31.configure(text="")
                            l31.update()
                            
                            
                    if o.get()==3 or o.get()==4 or o.get()==6: #if selected any of inverse,adjoint,transpose
                            for i in range(19,28):
                                    entry[i].configure(state="normal")
                                    entry[i].update() 
                            for i in range(37,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update() 
                                    
                        
                            for i in range(28,37):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()
                            
                            

                    if o.get()==0:#if add selected by user
                            l32.configure(text="+")
                            l32.update()
                            
                            
                            
                            for i in range(19,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update()
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()        

                    elif o.get()==1:#if sub selected by user
                            l32.configure(text="-")
                            l32.update()
                           
                            
                            for i in range(19,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update()
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()

                    elif o.get()==2:#if multiply by user
                            l32.configure(text="*")
                            l32.update()
                            
                           
                            
                            for i in range(19,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update()
                                    
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()
                                    
                    else:
                            l32.configure(text="")
                            l32.update()

                            




                    if o.get()==5: #if user selected determinant option
                        

                            for i in range(19,46):
                                entry[i].configure(state="disabled")
                                entry[i].update()
                            for i in range(46,56):
                                entry[i].configure(state="normal")
                                entry[i].update()
                                
                            b4.configure(state="normal")
                            b4.update()
                            
                            b3.configure(state="disabled")
                            b3.update()
                     
                    elif o.get()!=5: #instead of determinant 

                            b4.configure(state="disabled")
                            b4.update()

                            b3.configure(state="normal")
                            b3.update()  
            
            
            
            
            def op1():#all operations  2x2
                            for i in range(10,14):
                                        entry[i].configure(state="normal")
                            
                            c=np.matrix([[0,0],[0,0]])
                            if o.get()==0:#add
                                
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                B=np.matrix([   [float(entry[6].get()),float(entry[7].get())]  ,   [float(entry[8].get()),float(entry[9].get())]   ])
                                c=A+B
                              
                            elif o.get()==1:#sub
                            
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                B=np.matrix([   [float(entry[6].get()),float(entry[7].get())]  ,   [float(entry[8].get()),float(entry[9].get())]   ])                                                                                       
                                c=A-B
                                    
                            elif o.get()==2:#mult
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                B=np.matrix([   [float(entry[6].get()),float(entry[7].get())]  ,   [float(entry[8].get()),float(entry[9].get())]   ])                                                                                       
                                c=A*B
                                    
                            elif o.get()==3:#inverse
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                
                                
                                if round(la.det(A),2)==0 or round(la.det(A),2)==float(0) or round(la.det(A),2)==float('-0'):
                                    aa=tkinter.messagebox.showerror('Error!','You  have  entered  a  Singular  Matrix. A  matrix  whose  determinant  is  0  is  known  as  a  Singular  Matrix. Since  the determinant  of  a  Singular  Matrix  is  0, its  Inverse  is  not  defined')
                                    
                                    for i in range(10,14):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                    
                                    
                                else:
                                    c=la.inv(A)
                  
                            elif o.get()==4:#adjoint
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                
                                if la.det(A)!=0:#calculate using formula
                                    c=(la.det(A))*(la.inv(A))
                                else:#calculate using general method for 2x2 adjofloat
#NOT FOR DECIMALS                                     
                                    A[0,0],A[1,1]=A[1,1],A[0,0]
                                    A[0,1]= -1*A[0,1]
                                    A[1,0]= -1*A[1,0]
                                    
                                    c=A
                                    
                                    
                            elif o.get()==5:#determinant
                                
                                for i in range(10,14):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                D=np.matrix([[float(entry[14].get()),float(entry[15].get())],[float(entry[16].get()),float(entry[17].get())]] )
                                if round(la.det(D),2)==0 or round(la.det(D),2)==float(0) or round(la.det(D),2)==float('-0'):
                                    ans=0
                                else:                                    
                                    ans=(la.det(D))    
                                entry[18].delete(0,'end')
                                entry[18].insert(0,round(ans,2))
                                   
                                              
                            

                            elif o.get()==6:#transpose
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])                                                                                        
                                c=np.transpose(A)
                                
                            
                            for i in range(10,14):
                                entry[i].delete(0,'end')
                                
                            entry[10].insert(0,round(c[0,0],2))
                            entry[11].insert(0,round(c[0,1],2))
                            entry[12].insert(0,round(c[1,0],2))
                            entry[13].insert(0,round(c[1,1],2))
                            
             
                  
            def op2():#all operations 3x3
                            for i in range(37,46):
                                        entry[i].configure(state="normal")
                            c=np.matrix([[0,0,0],[0,0,0],[0,0,0]])
                            if o.get()==0:#add
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])



                                F=np.matrix([ [float(entry[28].get()),float(entry[29].get()),float(entry[30].get())],[float(entry[31].get()),float(entry[32].get()),float(entry[33].get())],
                                [float(entry[34].get()),float(entry[35].get()),float(entry[36].get())]  ])

                                c=E+F
                                
                            elif o.get()==1:#sub
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])



                                F=np.matrix([ [float(entry[28].get()),float(entry[29].get()),float(entry[30].get())],[float(entry[31].get()),float(entry[32].get()),float(entry[33].get())],
                                [float(entry[34].get()),float(entry[35].get()),float(entry[36].get())]  ])

                                c=E-F
                                
                            elif o.get()==2:#multiply
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])



                                F=np.matrix([ [float(entry[28].get()),float(entry[29].get()),float(entry[30].get())],[float(entry[31].get()),float(entry[32].get()),float(entry[33].get())],
                                [float(entry[34].get()),float(entry[35].get()),float(entry[36].get())]  ])

                                c=E*F
                                
                            elif o.get()==3:#inverse
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])
                                
                                if round(la.det(E),2)==0 or round(la.det(E),2)==float(0) or round(la.det(E),2)==float('-0'):
                                    tkinter.messagebox.showerror('Error!','You  have  entered  a  Singular  Matrix. A  matrix  whose  determinant  is  0  is  known  as  a  Singular  Matrix. Since  the determinant  of  a  Singular  Matrix  is  0, its  Inverse  is  not  defined')
                                    for i in range(37,46):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                else:
                                    c=la.inv(E)
                                
                                    
                               
                                
                            elif o.get()==4:#adjoint
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])

                                if la.det(E)!=0:
                                    c=(la.inv(E))*(la.det(E))
                                    
                                    
                                else:
                                    m11=np.matrix([[float(entry[23].get()),float(entry[24].get())],[float(entry[26].get()),float(entry[27].get())]])
                                    m12=np.matrix([[float(entry[22].get()),float(entry[24].get())],[float(entry[25].get()),float(entry[27].get())]])
                                    m13=np.matrix([[float(entry[22].get()),float(entry[23].get())],[float(entry[25].get()),float(entry[26].get())]])
                                    m21=np.matrix([[float(entry[20].get()),float(entry[21].get())],[float(entry[26].get()),float(entry[27].get())]])
                                    m22=np.matrix([[float(entry[19].get()),float(entry[21].get())],[float(entry[25].get()),float(entry[27].get())]])
                                    m23=np.matrix([[float(entry[19].get()),float(entry[20].get())],[float(entry[25].get()),float(entry[26].get())]])
                                    m31=np.matrix([[float(entry[20].get()),float(entry[21].get())],[float(entry[23].get()),float(entry[24].get())]])
                                    m32=np.matrix([[float(entry[19].get()),float(entry[21].get())],[float(entry[22].get()),float(entry[24].get())]])
                                    m33=np.matrix([[float(entry[19].get()),float(entry[20].get())],[float(entry[22].get()),float(entry[23].get())]])
                                    
                                    m12=-1*float((la.det(m12)))
                                    m21=-1*float((la.det(m21)))
                                    m23=-1*float((la.det(m23)))
                                    m32=-1*float((la.det(m32)))
                                    
                                    m11=float(la.det(m11))
                                    m13=float(la.det(m13))
                                    m22=float(la.det(m22))
                                    m31=float(la.det(m31))
                                    m33=float(la.det(m33))
                                    
                                    
                                    matrix=np.matrix([[m11,m21,m31],[m12,m22,m32],[m13,m23,m33]])
                                    
                                    c=matrix
                                    
                                    
                                    
                                    
                                
                            elif o.get()==5:#determinant
                                
                                
                                for i in range(37,46):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                H=np.matrix([ [float(entry[46].get()),float(entry[47].get()),float(entry[48].get())],[float(entry[49].get()),float(entry[50].get()),float(entry[51].get())],
                                [float(entry[52].get()),float(entry[53].get()),float(entry[54].get())] ])

                                
                                if round(la.det(H),2)==0 or round(la.det(H),2)==float(0) or round(la.det(H),2)==float('-0'):
                                    det=0
                                else:                                    
                                    det=(la.det(H))
                              
                                entry[55].delete(0,'end')
                                entry[55].insert(0,round(det,2))
                                
                                
                                    
                                
                                
                                
                                
                            elif o.get()==6:#transpose
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])
                                c=np.transpose(E)
                        
                                
                                
                            for i in range(37,46):
                                entry[i].delete(0,'end')
                                
                                
                            entry[37].insert(0,round(c[0,0],2))
                            entry[38].insert(0,round(c[0,1],2))
                            entry[39].insert(0,round(c[0,2],2))
                            entry[40].insert(0,round(c[1,0],2))
                            entry[41].insert(0,round(c[1,1],2))
                            entry[42].insert(0,round(c[1,2],2))
                            entry[43].insert(0,round(c[2,0],2))
                            entry[44].insert(0,round(c[2,1],2))
                            entry[45].insert(0,round(c[2,2],2))
                                
              
           
            b1.configure(command=lambda: (op1(),compulsary()))
            b1.update()
            b2.configure(command=lambda: op1())
            b2.update()
            b3.configure(command=lambda: (op2(),compulsary()))
            b3.update()
            b4.configure(command=lambda: op2())
            b4.update()
            
            
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Maths Innovative Project By Krishang Gupta")
    root.resizable(width=False, height=False)
    example = Example(root)
    example.pack(side="top", fill="both", expand=True)
    root.geometry("1100x730")
    root.mainloop()
    
    


# In[ ]:


import tkinter as tk
from  tkinter import BOTH
from tkinter import ttk
import numpy as np
import numpy.linalg as la
import tkinter.messagebox




class Example(tk.Frame):
  
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="gray80")
  
        
        self.frame = tk.Frame(self.canvas, background="gray80")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        
        
       
        
        
        self.canvas.pack(side="left", fill="both", expand=True)
        
        
      
        self.canvas.create_window((4,4), window=self.frame, anchor="nw",
                                  tags="self.frame")
        
        self.canvas.create_line(200,25,200,25,fill='black')

        
        self.frame.bind("<Configure>", self.onFrameConfigure)
       
        self.populate()
        

    def populate(self):
        
        global v
        v=tk.IntVar()
        v.set(10)
        
        global o
        o=tk.IntVar()
        o.set(12)
        global entry
        
        global A
        global B
        global C
        global D
        global E
        global F
        global G
        global H
        
        
        #fi
        def closer():
            ans=tkinter.messagebox.askquestion('Exit Pane','Are you sure you want to exit the Program?')
            if ans=='yes':
                root.destroy()
        
        
        e0=tk.Label(self.frame,text='')
        e5=tk.Label(self.frame,text='')
        l18=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80")
        l18.place(x=340,y=330)  
        l19=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80")
        l19.place(x=80,y=410)
        
       
        heading=tk.Label(self.frame,text="BASIC OPERATIONS ON MATRICES",width="63",height="1",bg="gray99",font="Segoe 25 underline bold",fg='gray99').grid(row=0,column=0,columnspan=24,rowspan=1,sticky='N',pady=1)
        heading_2=tk.Label(self.frame,text="BASIC OPERATIONS ON MATRICES",height="1",bg="gray99",font="Segoe 25 underline bold").place(x=250,y=1)#grid(row=0,column=0,columnspan=24,rowspan=1,sticky='N',pady=1)
        l1=tk.Label(self.frame,text=' Prepared By: Krishang Gupta',font=("Arial",8),bg="gray80",fg="gray80").grid(row=3,column=20,columnspan=3,sticky='W')
        l2=tk.Label(self.frame,text='                   2K20/A9/49',font=("Arial",8),bg="gray80",fg="gray80").grid(row=4,column=21,sticky='W')
        l3=tk.Label(self.frame,text='                   Mechanical Engineering(I SEM)',font=("Arial",8),bg="gray80",fg="gray80").grid(row=5,column=21,sticky='w')
        l4=tk.Label(self.frame,text='Guided  By  :  Dr.Nilam Rathi and Ankit Sharma Sir',font=("Arial",8),bg="gray80",fg="gray80").grid(row=6,column=20,columnspan=4,sticky='W')
        
        l1_2=tk.Label(self.frame,text=' Prepared By: Krishang Gupta',font=("Arial",8),bg="gray80").place(x=800,y=50)#grid(row=3,column=20,columnspan=3,sticky='W')
        l2_2=tk.Label(self.frame,text='                   2K20/A9/49',font=("Arial",8),bg="gray80").place(x=812,y=70)#grid(row=4,column=21,sticky='W')
        l3_2=tk.Label(self.frame,text='                   Mechanical Engineering(I SEM)',font=("Arial",8),bg="gray80").place(x=812,y=90)#grid(row=5,column=21,sticky='w')
        l4_2=tk.Label(self.frame,text='Guided  By  :  Dr.Nilam Rathi and Ankit Sharma Sir',font=("Arial",8),bg="gray80").place(x=800,y=110)#grid(row=6,column=20,columnspan=4,sticky='W')
        
        endtitle=tk.Label(self.frame,text='Dedicated To  : Bhagat Singh Sir (Principal and HOD Mathematics,Hope Hall Foundation School,R.K.Puram,New-Delhi & Ankit Mittal Sir(FIITJEE, South Delhi) )',font=("Arial",6),bg="gray80")
        endtitle.place(x=300,y=1160)
    
        
        l5=tk.Label(self.frame,text='Select the Order of the Square Matrices\t:',fg="blue",bg="gray80",font="Times 18").grid(row=13,column=0,columnspan=3,sticky='w')
        
        r1=tk.Radiobutton(self.frame,text=" 2x2",fg="black",bg="gray80",font="Times 15",variable=v,value=0,command=lambda:changer()).grid(row=13,column=6,sticky='w')
        r2=tk.Radiobutton(self.frame,text=" 3x3",fg="black",bg="gray80",font="Times 15",variable=v,value=1,command=lambda:changer()).grid(row=13,column=8,sticky='w')
                 
            
        waste1=tk.Label(self.frame,text=" ",fg="red",bg="gray80",font="Times 15").grid(row=13,column=10,sticky='w')
        waste2=tk.Label(self.frame,text="hihieiieh ",fg="gray80",bg="gray80",font="Times 15").grid(row=13,column=12,sticky='w')
                    
            
            
        blank=tk.Label(self.frame,text='\n\n\n',bg="gray80").grid(row=15,column=0) 
        
        l6=tk.Label(self.frame,text='Select the Operation on Matrices\t:',fg="blue",bg="gray80",font="Times 18").grid(row=25,column=0,columnspan=4,sticky='w')
        r5=tk.Radiobutton(self.frame,text="Add",fg="black",bg="gray80",font="Times 15",variable=o,value=0,command=lambda:changer()).grid(row=25,column=6,sticky='w')
        r6=tk.Radiobutton(self.frame,text="Subtract",fg="black",bg="gray80",font="Times 15",variable=o,value=1,command=lambda:changer()).grid(row=27,column=6,sticky='w')
        r7=tk.Radiobutton(self.frame,text="Multiply",fg="black",bg="gray80",font="Times 15",variable=o,value=2,command=lambda:changer()).grid(row=29,column=6,sticky='w')
        r8=tk.Radiobutton(self.frame,text="Inverse",fg="black",bg="gray80",font="Times 15",variable=o,value=3,command=lambda:changer()).grid(row=25,column=8,sticky='w')
        r9=tk.Radiobutton(self.frame,text="Adjoint",fg="black",bg="gray80",font="Times 15",variable=o,value=4,command=lambda:changer()).grid(row=27,column=8,sticky='w')
        r10=tk.Radiobutton(self.frame,text="Determinant",fg="black",bg="gray80",font="Times 15",variable=o,value=5,command=lambda:changer()).grid(row=29,column=8,sticky='w')
        r11=tk.Radiobutton(self.frame,text="Transpose",fg="black",bg="gray80",font="Times 15",variable=o,value=6,command=lambda:changer())
        r11.grid(row=25,column=10,sticky='w')
    
        l7=tk.Label(self.frame,text='2X2',bg="gray80",font=("Arial",25),fg="red").grid(row=40,column=0)
        
        
       
        l8=tk.Label(self.frame,text='[',font=("Script",100),bg="gray80").grid(row=46,column=1,rowspan=3,sticky='w')
        
        
        
        
        
        
        
        e1=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e1.grid(row=46,column=1)#a11
        e2=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e2.grid(row=46,column=2,sticky='w')#a12
        e3=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e3.grid(row=47,column=1,sticky='s')#a21
        e4=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e4.grid(row=47,column=2,sticky='sw')#a22   
    
        l9=tk.Label(self.frame,text=']',font=("Script",100),bg="gray80",fg="black").grid(row=46,column=2,rowspan=3)
        
        
        
        l20=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80")
        l20.place(x=357,y=422)
        
        
        
        
      
    
        l10=tk.Label(self.frame,text='[',font=("Script",100),bg="gray80").place(x=380,y=370)
        
        e6=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e6.grid(row=46,column=6)#a11
        e7=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e7.grid(row=46,column=7,sticky='e')#a12
        e8=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e8.grid(row=47,column=6,sticky='s')#a21
        e9=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e9.grid(row=47,column=7,sticky='se')#a22
    
        l11=tk.Label(self.frame,text=']',font=("Script",100),bg="gray80").grid(row=46,column=8,rowspan=3,sticky='w')
        
        
        
        
    
        
        
        l12=tk.Label(self.frame,text='[',font=("Script",100),bg="gray80").place(x=730,y=370)
        
        e10=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e10.grid(row=46,column=11,sticky='e',padx='3')#a11
        e11=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e11.grid(row=46,column=12,sticky='e')#a12
        e12=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e12.grid(row=47,column=11,sticky='se',padx='3')#a21
        e13=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e13.grid(row=47,column=12,sticky='se')#a22
    
        l13=tk.Label(self.frame,text=']',font=("Script",100),bg="gray80").grid(row=46,column=15,rowspan=3,sticky='w')
        
        
        #determinant
        
        l14=tk.Label(self.frame,text='|',font=("Script",100),bg="gray80").grid(row=50,column=1,rowspan=3,sticky='w')
        e14=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e14.grid(row=50,column=1)#a11
        e15=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e15.grid(row=50,column=2,sticky='w')#a12
        e16=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e16.grid(row=51,column=1,sticky='s')#a21
        e17=tk.Entry(self.frame,bd=7,width='4',state="disabled",disabledbackground="gray65")
        e17.grid(row=51,column=2,sticky='sw')#a22
        l15=tk.Label(self.frame,text='|',font=("Script",100),bg="gray80").grid(row=50,column=2,rowspan=3)
        
        
        
        
        e18=tk.Entry(self.frame,bd=7,width='15',state="disabled",disabledbackground="gray65")
        e18.place(x=810,y=583)
        
        
        
        
       
        l21=tk.Label(self.frame,text='3X3',bg="gray80",font=("Arial",25),fg="red").grid(row=55,column=0,ipady='30')
        l22=tk.Label(self.frame,text='[',font=("Script",120),bg="gray80").grid(row=56,column=1,rowspan=3,sticky='w')
        tk.Label(self.frame,text="hi",bg="gray80").grid(row=56,column=1)
        tk.Label(self.frame,text="hi",bg="gray80").grid(row=57,column=1)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=58,column=1)
        
        e19=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e19.place(x=180,y=800)
        e20=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e20.place(x=180,y=855)
        e21=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e21.place(x=180,y=905)
        
        
        
        
        l23=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80").grid(row=56,column=2,rowspan=3)
        
        
        
        e22=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e22.place(x=230,y=800)
        e23=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e23.place(x=230,y=855)
        e24=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e24.place(x=230,y=905)
        
        e25=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e25.place(x=280,y=800)
        e26=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e26.place(x=280,y=855)
        e27=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e27.place(x=280,y=905)
        
        
        
        
        
        
        
        l24=tk.Label(self.frame,text='[',font=("Script",120),bg="gray80").place(x=390,y=785)#grid(row=56,column=3,rowspan=3,sticky='w')
        l25=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80",fg='gray80').grid(row=56,column=8,rowspan=3,sticky='w')
        l25_2=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80").place(x=550,y=785)#grid(row=56,column=8,rowspan=3,sticky='w')
        e28=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e28.place(x=425,y=800)
        e29=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e29.place(x=425,y=855)
        e30=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e30.place(x=425,y=905)
        
        e31=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e31.place(x=475,y=800)
        e32=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e32.place(x=475,y=855)
        e33=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e33.place(x=475,y=905)
        
        e34=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e34.place(x=525,y=800)
        e35=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e35.place(x=525,y=855)
        e36=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e36.place(x=525,y=905)
        
        
        
        l26=tk.Label(self.frame,text='[',font=("Script",120),bg="gray80").place(x=720,y=785)#grid(row=56,column=3,rowspan=3,sticky='w')
        l27=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80",fg='gray80').grid(row=56,column=16,rowspan=4,sticky='w')
        l27_2=tk.Label(self.frame,text=']',font=("Script",120),bg="gray80").place(x=960,y=785)#grid(row=56,column=16,rowspan=4,sticky='w')
        
        e37=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e37.place(x=765,y=800)
        e38=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e38.place(x=765,y=855)
        e39=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e39.place(x=765,y=905)
        
        e40=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e40.place(x=835,y=800)
        e41=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e41.place(x=835,y=855)
        e42=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e42.place(x=835,y=905)
        
        e43=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e43.place(x=905,y=800)
        e44=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e44.place(x=905,y=855)
        e45=tk.Entry(self.frame,bd=7,width='7',state="normal",disabledbackground="gray65")
        e45.place(x=905,y=905)
       
    
    
    
    
        l28=tk.Label(self.frame,text='|',font=("Script",120),bg="gray80").grid(row=60,column=1,rowspan=3,sticky='nw')
        l29=tk.Label(self.frame,text='|',font=("Script",120),bg="gray80").grid(row=60,column=2,rowspan=2)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=60,column=1)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=61,column=1)
        tk.Label(self.frame,text="hi",bg="gray80",fg="gray80").grid(row=62,column=1)
        
        
 
        
        e46=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e46.place(x=180,y=985)
        e47=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e47.place(x=180,y=1040)
        e48=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e48.place(x=180,y=1095)
        
        e49=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e49.place(x=230,y=985)
        e50=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e50.place(x=230,y=1040)
        e51=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e51.place(x=230,y=1095)
        
        e52=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e52.place(x=280,y=985)
        e53=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e53.place(x=280,y=1040)
        e54=tk.Entry(self.frame,bd=7,width='4',state="normal",disabledbackground="gray65")
        e54.place(x=280,y=1095)
        
        
         
        e55=tk.Entry(self.frame,bd=7,width='15',state="disabled",disabledbackground="gray65")
        e55.place(x=815,y=1040)
        
        
        
        
        
        
        l5=tk.Label(self.frame,text='Select the Order of the Square Matrices\t:',fg="blue",bg="gray80",font="Times 18").grid(row=13,column=0,columnspan=3,sticky='w')
        
        r1=tk.Radiobutton(self.frame,text=" 2x2",fg="black",bg="gray80",font="Times 15",variable=v,value=0,command=lambda:changer()).grid(row=13,column=6,sticky='w')
        r2=tk.Radiobutton(self.frame,text=" 3x3",fg="black",bg="gray80",font="Times 15",variable=v,value=1,command=lambda:changer()).grid(row=13,column=8,sticky='w')
                 
            
        waste1=tk.Label(self.frame,text=" ",fg="red",bg="gray80",font="Times 15").grid(row=13,column=10,sticky='w')
        waste2=tk.Label(self.frame,text="hihieiieh ",fg="gray80",bg="gray80",font="Times 15").grid(row=13,column=12,sticky='w')
                    
            
            
        blank=tk.Label(self.frame,text='\n\n\n',bg="gray80").grid(row=15,column=0) 
        
        
        b0=tk.Button(state="disabled")#waste
        
        
        
        entry=[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26,e27,e28,e29,e30,e31,e32,e33,e34,e35,e36,e37,e38,
              e39,e40,e41,e42,e43,e44,e45,e46,e47,e48,e49,e50,e51,e52,e53,e54,e55]
        
        
        
        
        
        l30=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80",fg='black')
        l30.place(x=340,y=745)
        
        
        l31=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80",fg='black')
        l31.place(x=80,y=845)
        
        l32=tk.Label(self.frame,text="",font="Arial 25 bold",bg="gray80",fg='black')
        l32.place(x=362,y=850)
        #######################################################################################################
        exitter=tk.Button(self.frame,text="Exit",command=closer,fg='white',bg='red',activebackground='red',height='1',bd='7',width='9',font=(" Arial 10 bold"))
        exitter.place(x=616,y=1100)
        
        
        
        
        for i in range(0,56):
            entry[i].configure(state="disabled")
            entry[i].update()
        
            
      
    
        b1=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b1.place(x=620,y=422)
        
        b2=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b2.place(x=620,y=580)
        
        b3=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b3.place(x=620,y=850)
                     
        b4=tk.Button(self.frame,bd=7,text="CALCULATE",bg="green",fg="white")
        b4.place(x=620,y=1040)

        button=[b0,b1,b2,b3,b4]   
        
            
            
        for i in range(0,5):
            button[i].configure(state="disabled")
            button[i].update()
    
    
        
        
        
        
                
        def compulsary():
            if o.get()!=0 and o.get()!=1 and o.get()!=2 and o.get()!=3 and o.get()!=4 and o.get()!=5 and o.get()!=6:
                tkinter.messagebox.showerror('Error','Select the Operation on the Matrix!')
                
                
                if v.get()==0:
                    for i in range(10,14):
                        entry[i].configure(state="disabled")
                        entry[i].update()
                     
                   
                elif v.get()==1:
                    for i in range(37,46):
                        entry[i].configure(state="disabled")
                        entry[i].update()

                
            
        
        def changer():
            
            l18.configure(text="")
            l18.update()

            l19.configure(text="")
            l19.update()

            l20.configure(text="")
            l20.update()

            
            
            if v.get()==0:#If user selected 2x2 matrix
                   
               
                
                    l30.configure(text="")
                    l30.update()
                    l31.configure(text="")
                    l31.update()
                    l32.configure(text="")
                    l32.update()
              
                    
                    for i in range(19,56):#close entry in 3x3
                        entry[i].configure(state="disabled")
                        entry[i].update()
                    for i in range(0,19):#open all in 2x2
                        entry[i].configure(state="normal")
                        entry[i].update()
                        
                        
                    for i in range(3,5):#close button in 3x3
                        button[i].configure(state="disabled")
                        button[i].update()
                        
                        
                        
                        
                        
                        
                    
                    if o.get()==6:#if user selected by tranpose 
                        l18.configure(text="T")
                        l18.update()
                        
                        
                        

                    elif o.get()==3:#if user selected by inverse
                        l18.configure(text="-1")
                        l18.update()
                        
                        

                    else:
                        l18.configure(text="")
                        l18.update()

                    if o.get()==4:#if user selected by adjoint
                        l19.configure(text="Adj",fg="black")
                        l19.update()
                        
                        
                        
                        
                    else:

                        l19.configure(text="")
                        l19.update()


                    if o.get()==0:#add selected by user
                        l20.configure(text="+")
                        l20.update()

                    elif o.get()==1:#sub selected by user
                        l20.configure(text="-")
                        l20.update()

                    elif o.get()==2:#multiply selected by user
                        l20.configure(text="*")
                        l20.update()
                    else:
                        l20.configure(text="")
                        l20.update()


                    if o.get()==5: #if  determinant selected by user
                        
                       
                        
                        for i in range(14,19):
                            entry[i].configure(state="normal")
                            entry[i].update()
                        for i in range(1,14):
                            entry[i].configure(state="disabled")
                            entry[i].update()
                        
                        
                        b2.configure(state="normal")
                        b1.configure(state="disabled")
                        b2.update()
                        b1.update()



                    else: #instead of determinant 
                        for i in range(14,19):
                            entry[i].configure(state="disabled")
                            entry[i].update()
                            
                        for i in range(1,14):
                            entry[i].configure(state="normal")
                            entry[i].update()
                        
                        b2.configure(state="disabled")
                        b2.update()
                        b1.configure(state="normal")
                        b1.update()
                        
                     
                    if o.get()==3 or o.get()==4 or o.get()==6:#if user selected any of inverse,adjoint,transpose
                        e6.configure(state="disabled")
                        e7.configure(state="disabled")
                        e8.configure(state="disabled")
                        e9.configure(state="disabled")

                        e6.update()
                        e7.update()
                        e8.update()
                        e9.update()

                    elif o.get()!=5:#instead of determinant option 
                        e6.configure(state="normal")
                        e7.configure(state="normal")
                        e8.configure(state="normal")
                        e9.configure(state="normal")
                        e6.update()
                        e7.update()
                        e8.update()
                        e9.update()
                        
                        
                        
                     
                    
                    
           
            elif v.get()==1:#If user selected 3x3 matrix
                
                


                

                    for i in range(1,19):#close the entry boxes in 2x2 columns and close the buttons in 2x2
                            entry[i].configure(state="disabled")
                            entry[i].update()
                            
                    for i in range(1,3):#close the buttons in 2x2
                            button[i].configure(state="disabled")
                            button[i].update()
                            
                            
                    for i in range(19,46):#open the entry boxes of 3x3 first row
                            entry[i].configure(state="normal")
                            entry[i].update()
                            
                        
                            
                            
                    if o.get()==6:#if transpose selected by user
                            l30.configure(text="T")
                            l30.update()

                    elif o.get()==3:#if inverse selected by user
                            l30.configure(text="-1")
                            l30.update()


                    else:
                            l30.configure(text="")
                            l30.update()


                    if o.get()==4:#if adjoint  selected 
                            l31.configure(text="Adj",fg="black")
                            l31.update()
                            
                            

                    else:

                            l31.configure(text="")
                            l31.update()
                            
                            
                    if o.get()==3 or o.get()==4 or o.get()==6: #if selected any of inverse,adjoint,transpose
                            for i in range(19,28):
                                    entry[i].configure(state="normal")
                                    entry[i].update() 
                            for i in range(37,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update() 
                                    
                        
                            for i in range(28,37):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()
                            
                            

                    if o.get()==0:#if add selected by user
                            l32.configure(text="+")
                            l32.update()
                            
                            
                            
                            for i in range(19,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update()
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()        

                    elif o.get()==1:#if sub selected by user
                            l32.configure(text="-")
                            l32.update()
                           
                            
                            for i in range(19,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update()
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()

                    elif o.get()==2:#if multiply by user
                            l32.configure(text="*")
                            l32.update()
                            
                           
                            
                            for i in range(19,46):
                                    entry[i].configure(state="normal")
                                    entry[i].update()
                                    
                            for i in range(46,56):
                                    entry[i].configure(state="disabled")
                                    entry[i].update()
                                    
                    else:
                            l32.configure(text="")
                            l32.update()

                            




                    if o.get()==5: #if user selected determinant option
                        

                            for i in range(19,46):
                                entry[i].configure(state="disabled")
                                entry[i].update()
                            for i in range(46,56):
                                entry[i].configure(state="normal")
                                entry[i].update()
                                
                            b4.configure(state="normal")
                            b4.update()
                            
                            b3.configure(state="disabled")
                            b3.update()
                     
                    elif o.get()!=5: #instead of determinant 

                            b4.configure(state="disabled")
                            b4.update()

                            b3.configure(state="normal")
                            b3.update()  
            
            
            
            
            def op1():#all operations
                            for i in range(10,14):
                                        entry[i].configure(state="normal")
                            
                            c=np.matrix([[0,0],[0,0]])
                            if o.get()==0:#add
                                
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                B=np.matrix([   [float(entry[6].get()),float(entry[7].get())]  ,   [float(entry[8].get()),float(entry[9].get())]   ])
                                c=A+B
                              
                            elif o.get()==1:#sub
                            
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                B=np.matrix([   [float(entry[6].get()),float(entry[7].get())]  ,   [float(entry[8].get()),float(entry[9].get())]   ])                                                                                       
                                c=A-B
                                    
                            elif o.get()==2:#mult
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                B=np.matrix([   [float(entry[6].get()),float(entry[7].get())]  ,   [float(entry[8].get()),float(entry[9].get())]   ])                                                                                       
                                c=A*B
                                    
                            elif o.get()==3:#inverse
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                
                                
                                if la.det(A)==0:
                                    aa=tkinter.messagebox.showerror('Error!','You  have  entered  a  Singular  Matrix. A  matrix  whose  determinant  is  0  is  known  as  a  Singular  Matrix. Since  the determinant  of  a  Singular  Matrix  is  0, its  Inverse  is  not  defined')
                                    
                                    for i in range(10,14):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                    
                                    
                                else:
                                    c=la.inv(A)
                  
                            elif o.get()==4:#adjoint
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])
                                
                                if la.det(A)!=0:#calculate using formula
                                    c=(la.det(A))*(la.inv(A))
                                else:#calculate using general method for 2x2 adjofloat
#NOT FOR DECIMALS                                     
                                    A[0,0],A[1,1]=A[1,1],A[0,0]
                                    A[0,1]= -1*A[0,1]
                                    A[1,0]= -1*A[1,0]
                                    
                                    c=A
                                    
                                    
                            elif o.get()==5:#determinant
                                
                                for i in range(10,14):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                D=np.matrix([[float(entry[14].get()),float(entry[15].get())],[float(entry[16].get()),float(entry[17].get())]] )
                                ans=(la.det(D))
                                entry[18].delete(0,'end')
                                entry[18].insert(0,round(ans,2))
                                   
                                              
                            

                            elif o.get()==6:#transpose
                                A=np.matrix([   [float(entry[1].get()),float(entry[2].get())]  ,   [float(entry[3].get()),float(entry[4].get())]   ])                                                                                        
                                c=np.transpose(A)
                                
                            
                            for i in range(10,14):
                                entry[i].delete(0,'end')
                                
                            entry[10].insert(0,round(c[0,0],2))
                            entry[11].insert(0,round(c[0,1],2))
                            entry[12].insert(0,round(c[1,0],2))
                            entry[13].insert(0,round(c[1,1],2))
                            
             
                  
            def op2():#all operations
                            for i in range(37,46):
                                        entry[i].configure(state="normal")
                            c=np.matrix([[0,0,0],[0,0,0],[0,0,0]])
                            if o.get()==0:#add
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])



                                F=np.matrix([ [float(entry[28].get()),float(entry[29].get()),float(entry[30].get())],[float(entry[31].get()),float(entry[32].get()),float(entry[33].get())],
                                [float(entry[34].get()),float(entry[35].get()),float(entry[36].get())]  ])

                                c=E+F
                                
                            elif o.get()==1:#sub
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])



                                F=np.matrix([ [float(entry[28].get()),float(entry[29].get()),float(entry[30].get())],[float(entry[31].get()),float(entry[32].get()),float(entry[33].get())],
                                [float(entry[34].get()),float(entry[35].get()),float(entry[36].get())]  ])

                                c=E-F
                                
                            elif o.get()==2:#multiply
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])



                                F=np.matrix([ [float(entry[28].get()),float(entry[29].get()),float(entry[30].get())],[float(entry[31].get()),float(entry[32].get()),float(entry[33].get())],
                                [float(entry[34].get()),float(entry[35].get()),float(entry[36].get())]  ])

                                c=E*F
                                
                            elif o.get()==3:#inverse
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])
                                
                                if la.det(E)==0:
                                    tkinter.messagebox.showerror('Error!','You  have  entered  a  Singular  Matrix. A  matrix  whose  determinant  is  0  is  known  as  a  Singular  Matrix. Since  the determinant  of  a  Singular  Matrix  is  0, its  Inverse  is  not  defined')
                                    for i in range(37,46):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                else:
                                    c=la.inv(E)
                                
                                    
                               
                                
                            elif o.get()==4:#adjoint
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])

                                if la.det(E)!=0:
                                    c=(la.inv(E))*(la.det(E))
                                    
                                    
                                else:
                                    m11=np.matrix([[float(entry[23].get()),float(entry[24].get())],[float(entry[26].get()),float(entry[27].get())]])
                                    m12=np.matrix([[float(entry[22].get()),float(entry[24].get())],[float(entry[25].get()),float(entry[27].get())]])
                                    m13=np.matrix([[float(entry[22].get()),float(entry[23].get())],[float(entry[25].get()),float(entry[26].get())]])
                                    m21=np.matrix([[float(entry[20].get()),float(entry[21].get())],[float(entry[26].get()),float(entry[27].get())]])
                                    m22=np.matrix([[float(entry[19].get()),float(entry[21].get())],[float(entry[25].get()),float(entry[27].get())]])
                                    m23=np.matrix([[float(entry[19].get()),float(entry[20].get())],[float(entry[25].get()),float(entry[26].get())]])
                                    m31=np.matrix([[float(entry[20].get()),float(entry[21].get())],[float(entry[23].get()),float(entry[24].get())]])
                                    m32=np.matrix([[float(entry[19].get()),float(entry[21].get())],[float(entry[22].get()),float(entry[24].get())]])
                                    m33=np.matrix([[float(entry[19].get()),float(entry[20].get())],[float(entry[22].get()),float(entry[23].get())]])
                                    
                                    m12=-1*float((la.det(m12)))
                                    m21=-1*float((la.det(m21)))
                                    m23=-1*float((la.det(m23)))
                                    m32=-1*float((la.det(m32)))
                                    
                                    m11=float(la.det(m11))
                                    m13=float(la.det(m13))
                                    m22=float(la.det(m22))
                                    m31=float(la.det(m31))
                                    m33=float(la.det(m33))
                                    
                                    
                                    matrix=np.matrix([[m11,m21,m31],[m12,m22,m32],[m13,m23,m33]])
                                    
                                    c=matrix
                                    
                                    
                                    
                                    
                                
                            elif o.get()==5:#determinant
                                
                                
                                for i in range(37,46):
                                        entry[i].configure(state="disabled",disabledbackground='gray65')
                                H=np.matrix([ [float(entry[46].get()),float(entry[47].get()),float(entry[48].get())],[float(entry[49].get()),float(entry[50].get()),float(entry[51].get())],
                                [float(entry[52].get()),float(entry[53].get()),float(entry[54].get())] ])

                                det=la.det(H)
                                entry[55].delete(0,'end')
                                entry[55].insert(0,round(det,2))
                                
                                
                                
                                
                            elif o.get()==6:#transpose
                                E=np.matrix([ [float(entry[19].get()),float(entry[20].get()),float(entry[21].get())] , [float(entry[22].get()),float(entry[23].get()),float(entry[24].get())],
                                [float(entry[25].get()),float(entry[26].get()),float(entry[27].get())]])
                                c=np.transpose(E)
                        
                                
                                
                            for i in range(37,46):
                                entry[i].delete(0,'end')
                                
                                
                            entry[37].insert(0,round(c[0,0],2))
                            entry[38].insert(0,round(c[0,1],2))
                            entry[39].insert(0,round(c[0,2],2))
                            entry[40].insert(0,round(c[1,0],2))
                            entry[41].insert(0,round(c[1,1],2))
                            entry[42].insert(0,round(c[1,2],2))
                            entry[43].insert(0,round(c[2,0],2))
                            entry[44].insert(0,round(c[2,1],2))
                            entry[45].insert(0,round(c[2,2],2))
                                
              
           
            b1.configure(command=lambda: (op1(),compulsary()))
            b1.update()
            b2.configure(command=lambda: op1())
            b2.update()
            b3.configure(command=lambda: (op2(),compulsary()))
            b3.update()
            b4.configure(command=lambda: op2())
            b4.update()
            
            
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        

if __name__ == "__main__":
    root=tk.Tk()
    root.title("Maths Innovative Project By Krishang Gupta")
    root.resizable(width=False, height=False)
    example = Example(root)
    example.pack(side="top", fill="both", expand=True)
    root.geometry("1100x730")
    root.mainloop()
    
    


# In[ ]:





# In[ ]:




