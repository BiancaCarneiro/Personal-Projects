#include <Wire.h> 
#include <LiquidCrystal.h>
#define inicio 16

// largura = 16;
// altura  = 2;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);//Define os pinos ligados ao lcd

byte linhaDeChegada[8] = {
  0x1B,
  0x15,
  0x1B,
  0x15,
  0x1B,
  0x15,
  0x1B,
  0x15
};

uint8_t aviaoMal[8] = {
  0x00,
  0x0C,
  0x0D,
  0x1F,
  0x1F,
  0x0D,
  0x0C,
  0x00
};

uint8_t aviaoBom[8] = {
  0x00,
  0x06,
  0x16,
  0x1F,
  0x1F,
  0x16,
  0x06,
  0x00
};

int scroll1 = inicio, scroll2 = inicio + 11;
int botao1, botao2, tempo=400, vertical[5], k;
int count = 0, posicao = 0, enemyP[2];//enemyP é a posicao do inimigo

void setup(){//inicia lcd e botões
  lcd.begin(16,2);
  lcd.createChar(1, aviaoBom);
  lcd.createChar(2, aviaoMal);
  lcd.createChar(3, linhaDeChegada);

  lcd.home();
  pinMode(8,INPUT);
  pinMode(7,INPUT);  
}

void loop(){
  botao1=digitalRead(8);//vai para a esquerda
  botao2=digitalRead(7);//vai para a direita

  if(botao1){//se apertar o botão 1, vai para a posição 0 (direita)
    posicao = 0;
    //ant=0;
  }
  if(botao2){//se apertar o botão 1, vai para a posição 1 (esquerda)
    posicao = 1;
    //ant=1;
  }
  //else posicao=ant;
  
  //Carrinho jogador:
  lcd.setCursor(0, posicao);
  lcd.write(1);
  
  //Posicao inimigos:
  enemyP[0]=scroll1;
  enemyP[1]=scroll2;
  
  //Carrinhos inimigos:
  lcd.setCursor(enemyP[0], 0);
  lcd.write(2);
  vertical[0]=0;
    
  lcd.setCursor(enemyP[1], 1);
  lcd.write(2);
  vertical[1]=1;
 
  delay(tempo);
  
  for(k=0; k<2; k++){
    if(enemyP[k] == 0 && vertical[k] == posicao){
     lcd.clear();
     lcd.print("Game Over!");
     delay(5000);
     scroll1 = inicio;
     scroll2 = inicio+21;
     tempo = 450;
     count = 0;
    }
  }
       
  lcd.clear();
  
  if(scroll1 > 0){
    scroll1--;
    tempo = tempo - 2;
    }
  else{
    scroll1 = scroll2 + 15;
    count++;
  }
  if(scroll2 > 0){
    scroll2--;
    tempo--;
  }
  else{
    scroll2 = scroll1 + 15;
  }
  if(count >= 2){
    lcd.clear();
    scroll1 = inicio;
    tempo = 350;
    while(scroll1 > 0){
      lcd.clear();
      //Carrinho jogador:
      lcd.setCursor(0, posicao);
      lcd.write(1);

      //Linha de Chegada
      lcd.setCursor(scroll1, 0);
      lcd.write(3);
      lcd.setCursor(scroll1, 1);
      lcd.write(3);
		
      delay(tempo);
      scroll1--;
    }
    lcd.clear();
    lcd.write(' ');
    lcd.setCursor(2, 0);
    lcd.print("FINISH!!!");
    lcd.setCursor(2, 1);
    lcd.print("    :)    ");
    delay(5000);
    scroll1 = inicio;
    scroll2 = inicio + 11;
    tempo = 450;
    count = 0;
  }
}