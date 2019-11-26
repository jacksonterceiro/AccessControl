## Project Access Control

Repositório destinado ao projeto focado na gestão de entradas e saídas de pessoas em ambiente coworking. Desenvolvido em C (Arduino) e em Python.

Esse desenvolvimento partiu do projeto integrador UNIPE 2019.1 e 2019.2.

___

#### Organização do Projeto

O projeto foi dividido em duas partes:

1. Arduino;
2. Raspberry;

O Arduino é responsavel pela captura dos dados do teclado e enviar atraves da porta serial '/dev/ttyACM0' com baud de 9600 e o Rasberry, por capturar as informações (senhas) escritas na serial, consultar no firebase para identificar se a senha é valida e, em seguida, realizar a liberação da tranca da sala.

#### Arduino

Caminho para rodar o projeto:

    teclado/teclado.ino

#### Raspberry

Caminho para rodar o projeto:

    raspberry/scan_key_arduino.py