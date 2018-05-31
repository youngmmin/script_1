import urllib.request
from xml.dom.minidom import *
from tkinter import *
from tkinter import font, PhotoImage
import tkinter.simpledialog
import tkinter.messagebox
import smtplib
from email.mime.text import MIMEText


g_Tk = Tk()
g_Tk.geometry("400x600+500+130")
g_Tk.title("미세먼지 및 대기오염 정보조회")
DataList = []
#사진

photo = PhotoImage(file="미세먼지.png")
imageLabel = Label(g_Tk, image = photo)
imageLabel.pack()



#메인부분
def m_yebo():
    
    InitTopText()
    mail_button()
    InitSearchButton1()
    InitSearchButton2()
    InitSearchButton3()
    InitSearchButton4()
    InitRenderText()


#first page


def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font=TempFont,bg ="blue",fg = "white", text="미세먼지 예보 App")
    MainText.pack()
    MainText.place(x=70, y = 20)

def InitSearchButton1():#측정소별 실시간 조회
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="측정소 별 \n　 실시간 조회 　　", command=click_InitSearchButton1)
    SearchButton.pack()
    SearchButton.place(x=30,y=90)

def InitSearchButton2():#시도 별 측정소 위치 조회
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text=" 시도 별 측정소 \n  위치 조회   ", command=click_InitSearchButton2)
    SearchButton.pack()
    SearchButton.place(x=200, y=90)


def InitSearchButton3():  # 전국 미세먼지 평균 수치
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="  전국주간 미세먼지\n 평균 수치 조회", command=click_InitSearchButton3)
    SearchButton.pack()
    SearchButton.place(x=30,y=160)

def InitSearchButton4():  # 통합 대기 환경지수 나쁨 이상 조회
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="통합대기 환경지수 \n나쁨 이상 조회", command=click_InitSearchButton4)
    SearchButton.pack()
    SearchButton.place(x=200,y=160)

def mail_button():#메일버튼
    TempFont = font.Font(g_Tk, size=8, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk,font = TempFont, text=" 메일보내기 ",  command='mailmain')
    SearchButton.pack()
    SearchButton.place(x=305,y=550)

def InitRenderText():# 스크롤
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375,y=200)
    TempFont = font.Font(g_Tk, size=10,family='Consolas')
    RenderText = Text(g_Tk, width=49, height=22, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=220)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
    RenderText.configure(state='disabled')










#click 버튼
def clickTopText(temp_tk):
    TempFont = font.Font(temp_tk, size=20, weight='bold', family='Consolas')
    MainText = Label(temp_tk, font=TempFont,bg ="blue",fg = "white", text="측정소별 실시간 조회")
    MainText.pack()
    MainText.place(x=70,y=50)
def clickTopText2(temp_tk):
    TempFont = font.Font(temp_tk, size=20, weight='bold', family='Consolas')
    MainText = Label(temp_tk, font=TempFont,bg ="blue",fg = "white", text="시도 별 측정소 위치 조회")
    MainText.pack()
    MainText.place(x=40,y=50)
def clickTopText3(temp_tk):
    TempFont = font.Font(temp_tk, size=20, weight='bold', family='Consolas')
    MainText = Label(temp_tk, font=TempFont,bg ="blue",fg = "white", text="전국 미세먼지 평균 수치")
    MainText.pack()
    MainText.place(x=40,y=50)
def clickTopText4(temp_tk):
    TempFont = font.Font(temp_tk, size=20, weight='bold', family='Consolas')
    MainText = Label(temp_tk, font=TempFont,bg ="blue",fg = "white", text="통합 대기 환경지수\n나쁨 이상 조회")
    MainText.pack()
    MainText.place(x=70,y=50)

def InitInputLable(temp_tk):
        global InputLabel
        TempFont = font.Font(temp_tk, size=15, weight='bold', family='Consolas')
        InputLabel = Entry(temp_tk, font=TempFont,bg ="blue",fg = "white", width=26, borderwidth=12, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=10, y=130)

def clicksecondText(temp_tk):
    TempFont = font.Font(temp_tk, size=10, weight='bold', family='Consolas')
    MainText = Label(temp_tk, font=TempFont, text="ex) 내손동, 동안구.....")
    MainText.pack()
    MainText.place(x=220, y=100)
def clickSearchButton(temp_tk):
    TempFont = font.Font(temp_tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(temp_tk, font=TempFont, text="검색", command='SearchButtonAction')
    SearchButton.pack()
    SearchButton.place(x=330, y=140)
def clickInitRenderText(temp_tk):
    global RenderText
    RenderTextScrollbar = Scrollbar(temp_tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375,y=200)
    TempFont = font.Font(temp_tk, size=10,family='Consolas')
    RenderText = Text(temp_tk, width=49, height=22, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=220)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
    RenderText.configure(state='disabled')
def clickInitRenderText2(temp_tk):
    global RenderText
    RenderTextScrollbar = Scrollbar(temp_tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375,y=200)
    TempFont = font.Font(temp_tk, size=10,family='Consolas')
    RenderText = Text(temp_tk, width=49, height=30, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=170)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
    RenderText.configure(state='disabled')



#클릭 함수
def click_InitSearchButton1():
    c_tk = Tk()
    c_tk.geometry("400x600")
    clickTopText(c_tk)
    clicksecondText(c_tk)
    InitInputLable(c_tk)
    clickSearchButton(c_tk)
    clickInitRenderText(c_tk)


def click_InitSearchButton2():
    c_tk = Tk()
    c_tk.geometry("400x600")
    clickTopText2(c_tk)
    clicksecondText(c_tk)
    InitInputLable(c_tk)
    clickSearchButton(c_tk)
    clickInitRenderText(c_tk)

def click_InitSearchButton3():
    c_tk = Tk()
    c_tk.geometry("400x600")
    clickTopText3(c_tk)
    # clicksecondText(c_tk)
    # InitInputLable(c_tk)
    # clickSearchButton(c_tk)
    clickInitRenderText2(c_tk)
def click_InitSearchButton4():
    c_tk = Tk()
    c_tk.geometry("400x600")
    clickTopText4(c_tk)
    # clicksecondText(c_tk)
    # InitInputLable(c_tk)
    # clickSearchButton(c_tk)
    clickInitRenderText2(c_tk)


#호출부분
m_yebo()
g_Tk.mainloop()

