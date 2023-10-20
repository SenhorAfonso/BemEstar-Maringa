
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice, randint
from time import sleep

name_list = ['Pedro', 'Maria', 'José', 'Gabriela']
email_list = ['pedro@gmail.com', 'maria@hotmail.com', 'jose@yahoo.com', 'gabriela@outlook.com']


def create_driver():
    driver = Chrome()
    driver.get('http://192.168.237.67:8000/home')
    driver.fullscreen_window()

    return driver


def make_sign_up(driver: selenium.webdriver.Chrome):
    concluded = True

    print('-' * 35)
    print('Teste Funcional: CADASTRO DE USUÁRIO')

    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
    sleep(0.5)

    try:
        button = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[1]/div/div/a')
        button.click()
    except Exception as e:
        print('Elemento botão "cadastre-se agora!" não encontrado')
        concluded = False
    else:
        print('Elemento botão "cadastre-se agora!" OK!')

    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
    sleep(0.5)

    try:
        name_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[2]')
        name_input.send_keys(choice(name_list))
    except Exception as e:
        print('Elemento "nome input" não encontrado')
        concluded = False
    else:
        print('Elemento "nome input" OK!')

    try:
        email_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[3]')
        email_input.send_keys(choice(email_list))
    except Exception as e:
        print('Element "email input", não encontrado')
        concluded = False
    else:
        print('Elemento "email_input" OK!')

    try:
        password_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[4]')
        confirm_password_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[5]')

        passw = ''
        for i in range(8):
            passw += str(randint(0, 9))

        password_input.send_keys(passw)
        confirm_password_input.send_keys(passw)
    except Exception as e:
        print('Elementos "senha input" ou "confirm senha input" não encontrados')
        concluded = False
    else:
        print('Elemento "senha input" e "confirm senha input" OK!')

    try:
        cpf = ''
        for i in range(11):
            cpf += str(randint(0, 9))

        cpf_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[6]')
        cpf_input.send_keys(cpf)
    except Exception as e:
        print('Elemento "cpf input" não encontrado')
        concluded = False
    else:
        print('Elemento "cpf input" OK!')

    try:
        sus = '7'
        for i in range(6):
            sus += str(randint(0, 9))

        sus_card = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[7]')
        sus_card.send_keys(sus)
    except Exception as e:
        print('Elemento "sus card input" não encontrado')
        concluded = False
    else:
        print('Elemento "sus card input" OK!')

    try:
        sex = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/div[2]/input')
        sex.click()
    except Exception as e:
        print('Elemento "sex input" não encontrado')
        concluded = False
    else:
        print('Elemento "sex input" OK!')

    try:
        birthday = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[8]')
        birthday.click()
        birthday.send_keys('06102003')
    except Exception as e:
        print('Elemento "birthday input" não encontrado')
        concluded = False
    else:
        print('Elemento "birthday input" OK!')

    try:
        is_doctor = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/div[5]/input')
        is_doctor.click()
    except Exception as e:
        print('Elemento "is doctor" não encontrado')
        concluded = False
    else:
        print('Elemento "is doctor" OK!')

    # driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[2]/input[9]').click()

    if concluded:
        print('Conclusão: OK')
    else:
        print('Conclusão: FALHO')
    print('-' * 35)


def make_login(driver: selenium.webdriver.Chrome):
    concluded = True
    print('-' * 35)
    print('Teste funcional: LOGIN DE USUÁRIO')

    driver.fullscreen_window()
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
    sleep(1)

    try:
        user_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[1]/div/input[1]')
        user_input.send_keys('paciente feliz')
    except Exception as e:
        print('Elemento "user input" não encontrado')
        concluded = False
    else:
        print('Elemento "user input" OK!')

    try:
        password_input = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/form[1]/div/input[2]')
        password_input.send_keys('pacientefeliz')
    except Exception as e:
        print('Elemento "user password" não encontrado')
        concluded = False
    else:
        print('Elemento "user input" OK!')


    if concluded:
        print('Conclusão: OK')
    else:
        print('Conclusão: FALHO')
    print('-' * 35)


def main():
    driver = create_driver()
    make_sign_up(driver)
    driver.get('http://192.168.237.67:8000/home')
    sleep(1)
    make_login(driver)


if __name__ == '__main__':
    main()
