#include <WiFi.h>
#include <HTTPClient.h>

WiFiServer server(80);
String recebido;

#include <HTTPClient.h>

// Novas portas Seriais
#define RXD2 16
#define TXD2 17

// Funcao Millis
unsigned long startTime;
unsigned long currentTime;
const unsigned long period = 5000;

// Usuario da rede Wifi
const char* ssid = "******";
// Senha da rede Wifi
const char* password = "********";

void setup() {

  Serial.begin(9600);
  Serial2.begin(9600, SERIAL_8N1, RXD2, TXD2);

  startTime = millis();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  WiFi.mode(WIFI_MODE_STA);
  Serial.print("MacAddress: ");
  Serial.println(WiFi.macAddress());
  Serial.print("Endereco de IP: ");
  Serial.println(WiFi.localIP());
  server.begin();

}

void loop() {

  // -------------------- Start LoRa --------------------
  if (Serial2.available()){
    recebido = Serial2.readString();
    Serial.println(recebido);
  }
  // --------------------- End LoRa ---------------------

  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client.");
    while (client.connected()) {
      if (client.available()) {
        client.println("HTTP/1.1 200 OK");
        client.println("Content-type:text/html");
        client.println();
        if (recebido != ""){
          client.print(recebido);
        }
        break;
      }
    }
  }

  // -------------------- Start Millis() --------------------
  currentTime = millis();
  if (currentTime - startTime >= period)
  {
    startTime = currentTime;
  }
  // --------------------- End Millis() ---------------------
}