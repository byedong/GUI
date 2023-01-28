from tkinter import *
from tkinter import ttk
import webbrowser

def click_url(site):
    #발행기프로그램
    if site == "printer_sewoo_url" :
        webbrowser.open("http://rfid.7733.co.kr/data/printer/LK-B230.zip")
    if site == "printer_t800_url" :
        webbrowser.open("http://rfid.7733.co.kr/data/printer/t800_221027.zip")
    if site =="printer_bitek_url" :
        webbrowser.open("http://rfid.7733.co.kr/data/printer/BT_002_PRO1360.zip")
    if site =="printer_zin_url" :
        webbrowser.open("http://rfid.7733.co.kr/data/printer/zin.zip")
    if site == "printer_sato_url":
        webbrowser.open("http://rfid.7733.co.kr/data/printer/sato.zip")
    
    #보안프로그램
    if site == "security_markany_url":
        webbrowser.open("http://rfid.7733.co.kr/data/security/Inst_MaWebDRM.exe")
    if site == "security_kcaseagent_url":
        webbrowser.open("http://rfid.7733.co.kr/data/security/KCaseAgent_Installer.exe")

    #리더기프로그램
    if site == "reader_wta350rf_url":
        webbrowser.open("http://rfid.7733.co.kr/data/reader/EDU22-03-21.zip")
    if site == "reader_ker900_url":
        webbrowser.open("http://rfid.7733.co.kr/data/reader/KNS_22_01_06.zip")

    #보고서
    if site == "macro_report_url":
        webbrowser.open("http://rfid.7733.co.kr/data/report/report.zip")



window = Tk()
window.title("RFID관련 자료 / 인성정보 ")
window.geometry('420x240')

tab_control = ttk.Notebook(window)

tab_printer = ttk.Frame(tab_control)
tab_security = ttk.Frame(tab_control)
tab_reader = ttk.Frame(tab_control)
tab_macro = ttk.Frame(tab_control)
tab_etc = ttk.Frame(tab_control)

tab_control.add(tab_printer, text='[발행기]', padding=5)
tab_control.add(tab_security, text='[보안프로그램]', padding=5)
tab_control.add(tab_reader, text='[리더기]', padding=5)
tab_control.add(tab_macro, text='[매크로(수기/보고서)]', padding=5)
tab_control.add(tab_etc, text='[기타]', padding=5)


#lbl2 = Label(tab2, text= '두번째 탭의 라벨')
#lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

#발행기
printer_sewoo_url = "printer_sewoo_url"
printer_sewoo = Button(tab_printer, text='새우 / LK-B230', command=lambda: click_url(printer_sewoo_url), width=15, height=2)
printer_sewoo.grid(column=1, row=1, padx=10, pady=10)

printer_t800_url = "printer_t800_url"
printer_t800 = Button(tab_printer, text='Printronix / T800', command=lambda: click_url(printer_t800_url), width=15, height=2)
printer_t800.grid(column=2, row=1, padx=10, pady=10)

printer_bitek_url = "printer_bitek_url"
printer_bitek = Button(tab_printer, text='바이텍 / Black-Fish', command=lambda: click_url(printer_bitek_url), width=15, height=2)
printer_bitek.grid(column=3, row=1, padx=10, pady=10)

printer_zin_url = "printer_zin_url"
printer_zin = Button(tab_printer, text='진코퍼레이션', command=lambda: click_url(printer_zin_url), width=15, height=2)
printer_zin.grid(column=1, row=2, padx=10, pady=10)

printer_zin_url = "printer_zin_url"
printer_zin = Button(tab_printer, text='진코퍼레이션', command=lambda: click_url(printer_zin_url), width=15, height=2)
printer_zin.grid(column=1, row=2, padx=10, pady=10)

printer_sato_url = "printer_sato_url"
printer_sato = Button(tab_printer, text='SATO', command=lambda: click_url(printer_sato_url), width=15, height=2)
printer_sato.grid(column=2, row=2, padx=10, pady=10)

#보안프로그램
security_markany_url = "security_markany_url"
security_markany = Button(tab_security, text='MarkAny(Inst_MaWebDRM)', command=lambda: click_url(security_markany_url), width=30, height=2)
security_markany.grid(column=1, row=1, padx=10, pady=10)

security_kcaseagent_url = "printer_sato_url"
security_kcaseagent = Button(tab_security, text='KCaseAgent', command=lambda: click_url(security_kcaseagent_url), width=15, height=2)
security_kcaseagent.grid(column=2, row=1, padx=10, pady=10)

#리더기프로그램
reader_wta350rf_url = "reader_wta350rf_url"
reader_wta350rf = Button(tab_reader, text='WTA-350RF(22-03-21)', command=lambda: click_url(reader_wta350rf_url), width=25, height=2)
reader_wta350rf.grid(column=1, row=1, padx=10, pady=10)

reader_ker900_url = "reader_ker900_url"
reader_ker900 = Button(tab_reader, text='KER-900(22-01-06)', command=lambda: click_url(reader_ker900_url), width=25, height=2)
reader_ker900.grid(column=2, row=1, padx=10, pady=10)

#매크로(보고서)
macro_report_url = "macro_report_url"
macro_report = Button(tab_macro, text='보고서(기관제출용)샘플', command=lambda: click_url(macro_report_url), width=25, height=2)
macro_report.grid(column=1, row=1, padx=10, pady=10)


window.mainloop()