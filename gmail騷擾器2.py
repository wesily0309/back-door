#準備訊息物件設定
#載入模組
import email.message
import imp
from turtle import delay
#建立訊息物件
msg=email.message.EmailMessage()
#利用物件建立基本設定
print("歡迎使用郵件騷擾器")
print("請先至google帳號啟用不安全的應用程式存取功能")
from_a=input("請輸入寄件人信箱：")
to_b=input("請輸入收件人信箱：")
主旨=input("請輸入信件主旨")
內容=input("請輸入騷擾內容:")
騷擾次數=int(input("騷擾次數:"))
騷擾間隔時間=int(input("輸入間隔時間(ms):"))
msg["From"]=from_a
msg["To"]=to_b
msg["Subject"]=主旨
次數=0
#寄送郵件主要內容
#msg.set_content("測試郵件純文字內容") #純文字信件內容
acc=input("請輸入google gmail帳號：")
password=input("請輸入密碼")
msg.set_content(內容)#信件內容#連線到SMTP Sevver
while 次數<=騷擾次數:
    import smtplib
    #可以從網路上找到主機名稱和連線埠
    server=smtplib.SMTP_SSL("gmail.com",465) #建立gmail連驗
    server.login(acc,password)
    server.send_message(msg)
    server.close() #發送完成後關閉連線
    print(次數)
    次數=次數+1
    delay=騷擾間隔時間





