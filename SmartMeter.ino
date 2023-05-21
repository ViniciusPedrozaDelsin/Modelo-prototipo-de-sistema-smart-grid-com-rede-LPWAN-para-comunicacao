#include <LiquidCrystal_I2C.h>

// Portas Seriais LoRa
#define RXD2 16
#define TXD2 17
bool estado = 0;

// Display Lcd
LiquidCrystal_I2C lcd(0x27,16,2);

// Função Millis
unsigned long startTime;
unsigned long currentTime;
const unsigned long period = 5000;

// Variaveis Sensor de Tensão
int pin_tensao = 36;
int maior_valor = 0;
int tensao_inst;
float Vpp;
float tensao_rms;
int i = 0;

// Variaveis Sensor de Corrente
int pin_corrente = 34;
int maior_valor_cor = 0;
int corrente_inst;
float Ipp;
float corrente_rms;
int j = 0;

// Variaveis Frequencia da Rede
double freq = 0;
int k = 0;

void setup() {
  pinMode(pin_tensao, INPUT);
  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, RXD2, TXD2);
  lcd.init();
  lcd.setBacklight(HIGH);
  delay(500);
  startTime = millis();
}

void loop() {
  // --------------------Start Millis() --------------------
  currentTime = millis();


  // -------------------- Sensor de Tensao --------------------
  // Definicao do maior valor
  tensao_inst = analogRead(pin_tensao);
  if(tensao_inst > 1868 && tensao_inst < 1872){
    k = k + 1;
    //delay(1);
  }
  if (i < 30000){
    if (maior_valor <= tensao_inst){
      maior_valor = tensao_inst;
    }
  }else{
    Vpp = map(maior_valor,1870,2200,0,180);
    tensao_rms = Vpp/1.414;
    //Serial.print("Tensão de pico: ");
    //Serial.println(Vpp);
    //Serial.print("Tensão RMS: ");
    //Serial.println(tensao_rms);

    // Display no LCD
    lcd.setCursor(9,0);
    //lcd.print("Vp ");
    //lcd.setCursor(12,0);
    lcd.print(Vpp);
    lcd.setCursor(9,1);
    //lcd.print("Vr ");
    //lcd.setCursor(12,1);
    lcd.print(tensao_rms);

    //Serial.println(maior_valor);
    maior_valor = 0;
    i = 0;
  }

  // Contador Sensor Tensão
  i++;

  // -------------------- Sensor de Corrente --------------------
  // Definicao do maior valor
  corrente_inst = analogRead(pin_corrente);
  if (j < 30000){
    if (maior_valor_cor <= corrente_inst){
      maior_valor_cor = corrente_inst;
    }
  }else{
    Ipp = map(maior_valor_cor,1938,2655,0,5);
    //Ipp = ((maior_valor_cor - 1938) * 0.2) / 15;
    corrente_rms = Ipp/1.414;
    //Serial.print("Corrente de pico: ");
    //Serial.println(Ipp);
    //Serial.print("Corrente RMS: ");
    //Serial.println(corrente_rms);

    // Display no LCD
    lcd.setCursor(0,0);
    //lcd.print("Ip ");
    //lcd.setCursor(3,0);
    lcd.print(Ipp);
    lcd.setCursor(0,1);
    //lcd.print("Ir ");
    //lcd.setCursor(3,1);
    lcd.print(corrente_rms);

    //Serial.println(maior_valor_cor);
    maior_valor_cor = 0;
    j = 0;
  }

  // Contador Sensor Corrente
  j++;
  
  currentTime = millis();
  if (currentTime - startTime >= period)
  {
    freq = (k*1000) / 5000;
    Serial.print("k: ");
    Serial.println(k);
    Serial.print("Frequencia: ");
    Serial.println(freq);
    Serial.print("Tensao: ");
    Serial.println(tensao_rms);
    Serial.print("Corrente: ");
    Serial.println(corrente_rms);
    k = 0;

    // Lora
    Serial2.println(tensao_rms);
    Serial2.println(corrente_rms);
    Serial2.println(freq);

    startTime = currentTime;
  }

}