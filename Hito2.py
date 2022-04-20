import _random
import email
from time import sleep
from tkinter import E, N, Button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
opts= Options()
opts.add_argument("Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36")

Email="cristoballeonvega@gmail.com"
Pass1="test1234"
Pass2="1234test"


driver = webdriver.Chrome('./chromedriver.exe')


#  Registro

print("Registrar usuario")

driver.get('https://avistore.cl/login?create_account=1')

WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')))
imput_buton = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div/div/div/ul/li[2]/a')
print("sleep ",s)
s+=1
sleep(1)
print("A Registrar")

imput_tratamiento = driver.find_element(By.XPATH,'<input name="id_gender" type="radio" value="1" required="">')
print("sleep ",s)
s+=1
sleep(1)

imput_nombre = driver.find_element(By.XPATH,'<input class="form-control" name="firstname" type="text" value="" required="">')
print("sleep ",s)
s+=1
sleep(1)
imput_apellido = driver.find_element(By.XPATH,'<input class="form-control" name="lastname" type="text" value="" required="">')
print("sleep ",s)
s+=1
sleep(1)

imput_email = driver.find_element(By.XPATH,'<input class="form-control" name="email" type="email" value="" required="">')
print("sleep ",s)
s+=1
sleep(1)

imput_pass = driver.find_element(By.XPATH,'<input class="form-control js-child-focus js-visible-password" name="password" type="password" value="" pattern=".{5,}" required="">')
print("sleep ",s)
s+=1
sleep(1)

imput_fecha = driver.find_element(By.XPATH,'<input class="form-control" name="birthday" type="text" value="" placeholder="DD/MM/YYYY">')
print("sleep ",s)
s+=1
sleep(1)

print("seleccioner genero masculino ........")
imput_checbox.click()
print("sleep ",s)
s+=1
sleep(1)
print("insertar nombre ........")
imput_nombre.send_keys(Nombre)
print("sleep ",s)
s+=1
sleep(1)
print("insertar Apellido ........")
imput_apellido.send_keys(Apellido)
print("sleep ",s)
s+=1
sleep(1)

print("insertar correo electronico ........")
imput_email.send_keys(Email)
print("sleep ",s)
s+=1
sleep(1)

print("insertar password ........")
imput_pass.send_keys(Pass1)
print("sleep ",s)
s+=1
sleep(1)
print("insertar fecha de nacimiento ........")
imput_confirmpass.send_keys(Pass1)
print("sleep ",s)
s+=1
sleep(1)

print("click en finalizar registro ........")
# imput_buton.click()




