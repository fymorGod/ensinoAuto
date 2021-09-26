__ATV__TESTAGEM = By.XPATH, '//*[@id="module-122898"]/div/div/div[2]/div/a/span'
__TEST_SEND_AGAIN = By.XPATH, '//*[@id="yui_3_17_2_1_1632675935201_861"]/a[1]/div[1]/div[3]'
__ICON_NOTIFICATION = By.XPATH, '//*[@id="nav-notification-popover-container"]/div[1]/i'
__NOTIFICATION_CHOICE = By.XPATH, '//*[@id="popover-region-container-6150a8ed2ee9f6150a8ed05dd017"]/div[2]/div/div[1]/div[1]/a[1]/div[1]/div[2]'
__SEARCH_COURSE = By.XPATH, '//*[@id="shortsearchbox"]'
__GO_TO_COURSE = By.XPATH, '//*[@id="coursesearch"]/fieldset/button'
__TOTURIAL_COURSE = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[4]/div/a'
__NIVELAMENTO = By.XPATH, '//*[@id="module-120647"]/div/div/div[2]/div/a/span'
__NIVELAMENTO_CHECK = By.XPATH, '//*[@id="q10210:3_answer0"]'
__UNIDADE_APRENDIZADO = By.XPATH, '//*[@id="section-4"]/div/div[1]/div[2]/button'

URL = 'https://undbclassroom.undb.edu.br/'
def ct_0011(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__DISCIPLINA_TESTAGEM)
    self.click(self.__AV_QUALIS)
    self.click(self.__ADICIONAR_ENVIO)
    self.click(self.__SALVAR_ENVIO)
    result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()
    assert result is False

def ct_0012(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__DISCIPLINA_TESTAGEM)

    self.click(self.__ATV__TESTAGEM)
    self.click(self.__ADICIONAR_ENVIO)
    self.click(self.__SALVAR_ENVIO)
    result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()

    assert result is True

def ct_0013(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__DISCIPLINA_TESTAGEM)

    self.click(self.__ATV__TESTAGEM)
    self.click(self.__ADICIONAR_ENVIO)
    self.click(self.__TEST_SEND_AGAIN)

    self.click(self.__ADICIONAR_ENVIO)
    self.click(self.__SALVAR_ENVIO)
    result = self.driver.find_element(*self.__ALERTA_ENVIO).is_enabled()
    
    assert result is True

def ct_0014(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__ICON_NOTFICATION)

def ct_0015(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__ICON_NOTFICATION)
    sleep(2)
    self.click(self.__NOTIFICATION_CHOICE)


def ct_00116(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.fill(__SEARCH_COURSE, 'Testagem')
    self.click(__GO_TO_COURSE)

def ct_00117(self):
    #Verificação de sucesso no envio
    self.open_page(URL)
    self.click(__TOTURIAL_COURSE )

def ct_00118(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__DISCIPLINA_TESTAGEM)
    self.clik(__NIVELAMENTO)

def ct_00119(self):
    #Verificação de sucesso no envio
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__DISCIPLINA_TESTAGEM)
    self.clik(__NIVELAMENTO)
    self.click(self.__NIVELAMENTO_CHECK)

def ct_00120(self):
    self.ct_0001('insira o usuário!', 'insira sua senha!')
    self.click(self.__DISCIPLINA_TESTAGEM)
    self.click(__UNIDADE_APRENDIZADO)