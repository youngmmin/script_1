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
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="도시 별 \n　 실시간 조회 　　", command=click_InitSearchButton1)
    SearchButton.pack()
    SearchButton.place(x=10,y=180)

def InitSearchButton2():#시도 별 측정소 위치 조회
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text=" 시도 별 측정소 \n  위치 조회   ", command=click_InitSearchButton2)
    SearchButton.pack()
    SearchButton.place(x=10, y=270)


def InitSearchButton3():  # 전국 미세먼지 평균 수치
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text=" 주간 미세먼지\n 평균 수치 조회", command=click_InitSearchButton3)
    SearchButton.pack()
    SearchButton.place(x=10,y=360)

def InitSearchButton4():  # 통합 대기 환경지수 나쁨 이상 조회
    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="전국 대기오염지수\n나쁨 이상 조회", command=click_InitSearchButton4)
    SearchButton.pack()
    SearchButton.place(x=10,y=450)

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
    RenderText = Text(g_Tk, width=30, height=22, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=150, y=180)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
    RenderText.configure(state='disabled')










#click 버튼
def clickTopText(temp_tk):
    TempFont = font.Font(temp_tk, size=20, weight='bold', family='Consolas')
    MainText = Label(temp_tk, font=TempFont,bg ="blue",fg = "white", text="도시별 실시간 조회")
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
    MainText = Label(temp_tk, font=TempFont,bg ="blue",fg = "white", text="전국 대기오염지수\n나쁨 이상 조회")
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
def clickInitRenderText3(temp_tk):
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

def clickInitRenderText4(temp_tk):
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
    import http.client
    import urllib.request
    from xml.dom.minidom import parse, parseString
    global city
    key = "LNkyelRj0H1r988h%2FcAj5495bZL4p1wiIv6DU1uI0kCio%2FzjzSm5iPVZs6kxxICTXI6H4%2Bnr3o2lq%2BIF5wxgpw%3D%3D"
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?itemCode=PM10&dataGubun=DAILY&searchCondition=MONTH&pageNo=1&numOfRows=10&ServiceKey=" + key
    c_tk = Tk()
    c_tk.geometry("400x600")
    clickTopText3(c_tk)

    data = urllib.request.urlopen(url).read()
    f = open("mise.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("mise.xml")
    dataTime = doc.getElementsByTagName("dataTime")
    dataGubun = doc.getElementsByTagName("dataGubun")
    item = doc.getElementsByTagName("item")
    gyeongnam = doc.getElementsByTagName("gyeongnam")
    jeju = doc.getElementsByTagName("jeju")
    sejong = doc.getElementsByTagName("sejong")
    seoul = doc.getElementsByTagName("seoul")
    gyeonggi = doc.getElementsByTagName("gyeonggi")
    busan = doc.getElementsByTagName("busan")
    daegu = doc.getElementsByTagName("daegu")
    chungnam = doc.getElementsByTagName("chungnam")
    jeonbuk = doc.getElementsByTagName("jeonbuk")
    jeonnam = doc.getElementsByTagName("jeonnam")
    gyeongbuk = doc.getElementsByTagName("gyeongbuk")
    incheon = doc.getElementsByTagName("incheon")
    gwangju = doc.getElementsByTagName("gwangju")
    daejeon = doc.getElementsByTagName("daejeon")
    ulsan = doc.getElementsByTagName("ulsan")
    gangwon = doc.getElementsByTagName("gangwon")
    chungbuk = doc.getElementsByTagName("chungbuk")

    city = seoul.length
    if city == 0:
        tkinter.messagebox.showwarning("Information", "Information update please")
    else:
        data = []
        gubun = []
        gyeongnamInfo = []
        jejuInfo = []
        sejongInfo = []
        seoulInfo = []
        gyeonggiInfo =[]
        busanInfo = []
        daeguInfo = []
        chungnamInfo =[]
        jeonbukInfo = []
        jeonnamInfo = []
        gyeongbukInfo = []
        incheonInfo = []
        gwangjuInfo = []
        daejeonInfo = []
        ulsanInfo = []
        gangwonInfo = []
        chungbukInfo = []
        index = 0
        while index < city:
            temp1 = str(dataTime[index].firstChild.data)
            temp2 = str(dataGubun[index].firstChild.data)
            temp3 = str(seoul[index].firstChild.data)
            temp4 = str(gyeonggi[index].firstChild.data)
            temp5 = str(busan[index].firstChild.data)
            temp6 = str(daegu[index].firstChild.data)
            temp7 = str(incheon[index].firstChild.data)
            temp8 = str(gwangju[index].firstChild.data)
            temp9 = str(daejeon[index].firstChild.data)
            temp10 = str(ulsan[index].firstChild.data)
            temp11 = str(gangwon[index].firstChild.data)
            temp12 = str(chungbuk[index].firstChild.data)
            temp13 = str(chungnam[index].firstChild.data)
            temp14 = str(jeonbuk[index].firstChild.data)
            temp15 = str(jeonnam[index].firstChild.data)
            temp16 = str(gyeongbuk[index].firstChild.data)
            temp17 = str(gyeongnam[index].firstChild.data)
            temp18 = str(jeju[index].firstChild.data)
            temp19 = str(sejong[index].firstChild.data)

            data.append(temp1)
            gubun.append(temp2)
            seoulInfo.append(temp3)
            gyeonggiInfo.append(temp4)
            busanInfo.append(temp5)
            daeguInfo.append(temp6)
            incheonInfo.append(temp7)
            gwangjuInfo.append(temp8)
            daejeonInfo.append(temp9)
            ulsanInfo.append(temp10)
            gangwonInfo.append(temp11)
            chungbukInfo.append(temp12)
            chungnamInfo.append(temp13)
            jeonbukInfo.append(temp14)
            jeonnamInfo.append(temp15)
            gyeongbukInfo.append(temp16)
            gyeongnamInfo.append(temp17)
            jejuInfo.append(temp18)
            sejongInfo.append(temp19)
            index += 1
    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(c_tk)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(c_tk, size=10, family='Consolas')
        RenderText = Text(c_tk, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)

        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        RenderText.insert(INSERT, "\t하루 평균 미세먼지 수치\t\t\n")

        for i in range(city):
                RenderText.insert(INSERT, "\t Y/M/D :  ")
                RenderText.insert(INSERT, data[i])
                RenderText.insert(INSERT, "\n[서울] : ")
                RenderText.insert(INSERT, seoulInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[경기] : ")
                RenderText.insert(INSERT, gyeonggiInfo[i])
                RenderText.insert(INSERT, "\n[부산] : ")
                RenderText.insert(INSERT, busanInfo [i])
                RenderText.insert(INSERT, "\t\t\t\t[대구] : ")
                RenderText.insert(INSERT, daeguInfo [i])
                RenderText.insert(INSERT, "\n[인천] : ")
                RenderText.insert(INSERT, incheonInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[광주] : ")
                RenderText.insert(INSERT, gwangjuInfo[i])
                RenderText.insert(INSERT, "\n[대전] : ")
                RenderText.insert(INSERT, daejeonInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[울산] : ")
                RenderText.insert(INSERT, ulsanInfo [i])
                RenderText.insert(INSERT, "\n[강원] : ")
                RenderText.insert(INSERT, gangwonInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[충북] : ")
                RenderText.insert(INSERT, chungbukInfo[i])
                RenderText.insert(INSERT, "\n[충남] : ")
                RenderText.insert(INSERT, chungnamInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[전북] : ")
                RenderText.insert(INSERT, jeonbukInfo[i])
                RenderText.insert(INSERT, "\n[전남] : ")
                RenderText.insert(INSERT, jeonnamInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[경북] : ")
                RenderText.insert(INSERT, gyeongbukInfo[i])
                RenderText.insert(INSERT, "\n[경남] : ")
                RenderText.insert(INSERT, gyeongnamInfo[i])
                RenderText.insert(INSERT, "\t\t\t\t[제주] : ")
                RenderText.insert(INSERT, jejuInfo[i])
                RenderText.insert(INSERT, "\n[세종] : ")
                RenderText.insert(INSERT, sejongInfo[i])

                RenderText.insert(INSERT, "\n\n\n")
                i += 1
        RenderText.configure(state='disabled')

    InitRenderText()
    # clicksecondText(c_tk)
    # InitInputLable(c_tk)
    # clickSearchButton(c_tk)
    # clickInitRenderText3(c_tk)

def click_InitSearchButton4():
    from xml.dom.minidom import parse, parseString
    global num3

    c_tk = Tk()
    c_tk.geometry("400x600")
    clickTopText4(c_tk)

    key = "LNkyelRj0H1r988h%2FcAj5495bZL4p1wiIv6DU1uI0kCio%2FzjzSm5iPVZs6kxxICTXI6H4%2Bnr3o2lq%2BIF5wxgpw%3D%3D"
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getUnityAirEnvrnIdexSnstiveAboveMsrstnList?pageNo=1&numOfRows=10&ServiceKey=" + key

    data = urllib.request.urlopen(url).read()
    f = open("DDongham.xml", "wb")
    f.write(data)
    f.close()

    doc = parse("DDongham.xml")
    stationName = doc.getElementsByTagName("stationName")
    num3 = stationName.length

    if num3 == 0:
        tkinter.messagebox.showwarning("Information", "Information update please")
    else:
        station = []

        index = 0
        while index < num3:
            tmp1 = str(stationName[index].firstChild.data)
            station.append(tmp1)
            index += 1

    def InitRenderText():
        global RenderText

        RenderTextScrollbar = Scrollbar(c_tk)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(c_tk, size=10, family='Consolas')
        RenderText = Text(c_tk, width=49, height=30, borderwidth=12, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=10, y=157)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
        RenderText.insert(INSERT, "---------------나쁨이상 지역---------------")


        for i in range(num3):
            RenderText.insert(INSERT, "\n[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "지역 : ")
            RenderText.insert(INSERT, station[i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "오염 상태 : 나쁨이상  외출시 주의")
            RenderText.insert(INSERT, "\n\n")
            i += 1
        RenderText.configure(state='disabled')

    InitRenderText()
    # clicksecondText(c_tk)
    # InitInputLable(c_tk)
    # clickSearchButton(c_tk)
    # clickInitRenderText4(c_tk)



#호출부분
m_yebo()
g_Tk.mainloop()

