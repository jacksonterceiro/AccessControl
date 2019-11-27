import serial
import fire
import RPi.GPIO as GPIO
from time import sleep
import sys
from datetime import datetime
from datetime import timedelta 

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

PINO_BIPE = 40
PINO_MOTOR = 33
PINO_RELE1 = 7
PINO_RELE2 = 11

#-------------- FUNCOES DE SOM --------------#
def bipOff():
    GPIO.output(PINO_BIPE,GPIO.LOW)

def soundSucess():
    for idx in range(0,4):
        GPIO.output(PINO_BIPE,GPIO.HIGH)
        sleep(0.05) # Delay in seconds
        GPIO.output(PINO_BIPE,GPIO.LOW)
        sleep(0.05) # Delay in seconds

def soundError():
        GPIO.output(PINO_BIPE,GPIO.HIGH)
        sleep(1) # Delay in seconds
        GPIO.output(PINO_BIPE,GPIO.LOW)
        sleep(1) # Delay in seconds

def soundErroSystem():
    GPIO.output(PINO_BIPE,GPIO.HIGH)
    sleep(1) # Delay in seconds
    GPIO.output(PINO_BIPE,GPIO.LOW)
    sleep(0.2) # Delay in seconds

def soundDigito():
    GPIO.output(PINO_BIPE,GPIO.HIGH)
    sleep(0.05) # Delay in seconds
    GPIO.output(PINO_BIPE,GPIO.LOW)


#-------------- FUNCOES PORTA --------------#

def abrirPorta():
    GPIO.output(PINO_MOTOR, GPIO.HIGH)
    sleep(1.5)
    GPIO.output(PINO_MOTOR, GPIO.LOW)

def ligarEletronicos():
    GPIO.output(PINO_RELE1, GPIO.LOW) #INVERTIDO POR CAUSA DO RELE
    GPIO.output(PINO_RELE2, GPIO.LOW) #INVERTIDO POR CAUSA DO RELE

def desligarEletronicos():
    GPIO.output(PINO_RELE1, GPIO.HIGH) #INVERTIDO POR CAUSA DO RELE
    GPIO.output(PINO_RELE2, GPIO.HIGH) #INVERTIDO POR CAUSA DO RELE



def capturaCaractere():
    caracter = None
    caracter = str(comunicacaoSerial.readline().decode('ascii'))
    return caracter[0] #indice 0, primeiro caractere

def capturaSenha():
    senhaAcesso = ""
    for tamSenha in range(0,6):
        senhaAcesso += str(capturaCaractere())
        soundDigito()
    print("Senha: " + senhaAcesso)
    return senhaAcesso

def declaraPinos():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(PINO_BIPE,GPIO.OUT)
    GPIO.setup(PINO_MOTOR, GPIO.OUT)
    GPIO.setup(PINO_RELE1, GPIO.OUT)
    GPIO.setup(PINO_RELE2, GPIO.OUT)

def validaDataCredencial(dadosUsuario, senhaAcesso):
    now = datetime.now() - timedelta(hours=3)

    dataAgendamentoObj = datetime.strptime(dadosUsuario["data_agendamento"], '%Y-%m-%d %H:%M:%S.%f')
    dataSaidaObj = datetime.strptime(dadosUsuario["data_saida"], '%Y-%m-%d %H:%M:%S.%f')
    
    if(dataAgendamentoObj <= now and dataSaidaObj >= now):
        print("AGENDADO PARA: " + str(dataAgendamentoObj) + " ATE: " + str(dataSaidaObj))
        return True
    else:
        print("FORA DO HORARIO/DATA DE AGENDAMENTO: " + str(dataAgendamentoObj))
        return False

    #print ('Current date/time: {}'.format(datetime.datetime.now()))  

def validaCredencial(DB, senhaAcesso):
    dadosUsuario = validaSenha(DB, senhaAcesso)
    if(dadosUsuario != False):
        if(validaDataCredencial(dadosUsuario, senhaAcesso) == True):
            return True

    return False

def validaSenha(DB, senhaAcesso):
    for idx in DB:
        try:
            if(str(idx["token"]) == str(senhaAcesso)):
                return idx
                #return True
        except:
            pass
    return False

def getDadosDB():
    print("PROCESSANDO KEY...")
    return fire.getKey()

def liberarAcesso():
    abrirPorta()
    ligarEletronicos()

def cortarCorrente():
    desligarEletronicos()

#-------- MAIN --------#
declaraPinos()
bipOff()

try:
    while True :
        senhaAcesso = ""
        senhaAcesso = capturaSenha()

        DB = getDadosDB()

        if(validaCredencial(DB, senhaAcesso) == True):
            soundSucess()
            liberarAcesso()
            sleep(4)
            cortarCorrente()
            print("ENTRADA LIBERADA\n")
        else:
            soundError()
            print("ENTRADA REJEITADA\n")

except KeyboardInterrupt:
    soundErroSystem()
    GPIO.cleanup()
