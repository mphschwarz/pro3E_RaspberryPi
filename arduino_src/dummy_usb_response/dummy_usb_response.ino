void setup() {
  Serial.begin(115200); // use the same baud-rate as the python side
}
void loop() {
  if(Serial.available() > 0) {
    char com;
    com = Serial.read();
    switch (com){
      case 'x':
        Serial.write("Test");
        break;
      case 'u': 
        Serial.write('V');
        Serial.write('o');
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
