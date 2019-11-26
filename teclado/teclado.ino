//Programa : Teclado matricial 4x4
//Autor : JACKSON

char matriz[4][4] = {
{'1','2','3','A'},
{'4','5','6','B'},
{'7','8','9','C'},
{'*','0','#','D'},
};
 
void setup()
{
  //Pinos ligados aos pinos 1, 2, 3 e 4 do teclado - Linhas
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
   
  //Pinos ligados aos pinos 5, 6, 7 e 8 do teclado - Colunas
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
   
  Serial.begin(9600);
  //Serial.println("Aguardando acionamento das teclas...");
  //Serial.println();
}
 
void loop(){
    char letter = ' ';
    for (int ti = 3; ti<7; ti++){
    //Alterna o estado dos pinos das linhas
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(ti, HIGH);
    //Verifica se alguma tecla da coluna 1 foi pressionada
    if (digitalRead(8) == HIGH){
      letter = identifyCaracter(ti-2, 1);
      printLetter(letter);
      letter = ' ';
      while(digitalRead(8) == HIGH){};
    }
 
    //Verifica se alguma tecla da coluna 2 foi pressionada    
    if (digitalRead(9) == HIGH){
      letter = identifyCaracter(ti-2, 2);
      printLetter(letter);
      letter = ' ';
      while(digitalRead(9) == HIGH){};
    }
     
    //Verifica se alguma tecla da coluna 3 foi pressionada
    if (digitalRead(10) == HIGH){
      letter = identifyCaracter(ti-2, 3);
      printLetter(letter);
      letter = ' ';
      while(digitalRead(10) == HIGH){}
    }
     
    //Verifica se alguma tecla da coluna 4 foi pressionada
    if (digitalRead(11) == HIGH){
      letter = identifyCaracter(ti-2, 4);
      printLetter(letter);
      letter = ' ';
      while(digitalRead(11) == HIGH){} 
    }
   }
   delay(10);
}
 
void imprime_linha_coluna(int x, int y)
{
       Serial.print("Linha : ");
       Serial.print(x);
       Serial.print(" x Coluna : ");
       Serial.print(y);
       delay(500);
       Serial.println();
}

char identifyCaracter(int x, int y){
       //Serial.print("LETRA: ");
       //Serial.print(matriz[(x-1)][(y-1)]);
       //Serial.println();
       //delay(500);
       return matriz[(x-1)][(y-1)];
}

void printLetter(char letter){
  Serial.println(letter);
  delay(500);
}
