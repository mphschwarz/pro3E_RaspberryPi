void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
}
void loop() {
  if(Serial.available() > 0) {
    char com;
    com = Serial.read();
    switch (com){
      case 'x':
        Serial.write("Test\0");
        break;
      case 'u':
        Serial.write("V\0");
        Serial.write("o\0");
        break;
      case 'i': 
        Serial.write('A');
        break;
      default:
        Serial.write('?');
    }
    Serial.write(com);
  }
}
