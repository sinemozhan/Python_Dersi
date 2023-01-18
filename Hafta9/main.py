"""
Fare ve klavye kontrol kütüphanesi
"""
import pyautogui

pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)

screenWidth , screenHeight = pyautogui.size()
print("ekran çözünürlüğü:" , screenWidth , screenHeight)

"""
webviev
Tkinter---pthonla beraber gelir(builtin function)
"""

from tkinter import *

window=Tk()

window.title("hello word")
lbl =Label(window , text ="Kullanıcı Girişi")
window.geometry("500x400")

pyautogui.prompt(text='Lütfen adınızı giriniz.', title='Kullanıcı Adı' , default='')
'Sinem'
pyautogui.alert(text='Kullanıcı Adı Yanlış.', title='Kullanıcı Adı', button="Tamam");

pyautogui.password(text='Lütfen şifrenizi giriniz.', title='Kullanıcı Şifresi' , mask="*")
pyautogui.alert(text='Şifre Yanlış.', title='Kullanıcı Şifresi', button="Tamam");



"""
Programın biz çarpıya basınca kapanması için
"""
window.mainloop()





