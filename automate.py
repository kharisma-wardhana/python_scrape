from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep 

def main():
    print('Automate Program Use Selenium')
    url = input('Please input url to automate: \n')

    list_element_xpath = []
    list_step = []
    command = ''
    while(True):
        print('type "exit" to end')
        xpath = input('Please input xpath base on step that u want to checker : \n')
        if xpath == 'exit':
            break
        print('click')
        print('input')
        command = input('Please input command to check in that element : \n')
        list_element_xpath.append(xpath)
        list_step.append(command)


    print('Open chrome')
    driver = Chrome()
    driver.maximize_window()
    driver.get(url)

    print('Execute step')
    step_itteration = 0
    for step in list_step:
        element = driver.find_element_by_xpath(list_element_xpath[step_itteration])
        if step == 'click':
            element.click()
        elif step == 'input':
            data = input('Please input data that want to input : \n')
            element.send_keys(data)
        step_itteration = step_itteration + 1
        sleep(2)

if __name__ == '__main__':
    main()