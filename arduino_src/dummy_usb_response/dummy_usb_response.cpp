#include <SoftwareSerial.h>
void setup() {
    Serial.begin(115200);
    int sampleNumber = 1000;
    float voltage [sampleNumber];
    float currant [sampleNumber];
    int voltagePin = 0;
    int currantPin = 0;
    float voltageRMS = 0;
    float currantRMS = 0;
    float realPower = 0;
    float imagPower = 0;
}

void loop() {
    unsigned long cycleStart = milis();
    readPower(voltage, currant, sampleNumber, voltagePin, currantPin);
    unsigned long cycleTime = milis() - cycleStart;

    voltageRMS = calculateRms(voltage, sampleNumber);
    currantRMS = calculateRms(currant, sampleNumber);
    calculatePower(voltage, currant, realPower, imagPower, sampleNumber, cycleTime);

    Serial.write('r');  //signals new data
    serialResponse(voltageRMS, currantRMS, realPower, imagPower);
    delay(10000 - milis() + cycleStart);  //waits for measurement cycle to end
}

void serialResponse(float& voltage, float& currant, float& realPower, float& imagPower) {
    bool done = false;
    while (Serial.available() > 0 && !done) {
        char com;
        com = Serial.read();
        switch (com) {
            case 'x':
                Serial.write("Test");
                break;
            case 'u':
                Serial.write(voltage);
                break;
            case 'i':
                Serial.write(currant);
                break;
            case 'p':
                Serial.write(realPower);
                break;
            case 'q':
                Serial.write(imagPower);
                break;
            case 'd':
                done = true;
                break;
            default:
                Serial.write('?');
        }
        Serial.write(com);
    }
}

void readPower(float *voltage, float *currant, int &sampleNumber, int voltagePin, int currantPin) {
    for (int i = sample_number; i != 0; --i) {
        *voltage = analogRead(voltagePin);
        voltage++;
        *currant = analogRead(currantPin);
        currant++;
    }
}

float calculateRms(float *samples, int &sampleNumber) {
    float squares = 0;
    for (int i = sampleNumber; i != 0; --i) {
        squares += *samples * *samples;
        ++samples;
    }
    return sqrt(squares / sampleNumber);
}

void calculatePower(float *voltage, float *currant, float &realPower, float &imagPower, int &sampleNumber, int &time) {
    realPower = 0;
    imagPower = 0;
    float
    for (int i = sampleNumber; i != 0; --i) {
        float power = *(voltage + i) * *(currant + i);
        if (power > 0) {
            realPower += power;
        } else {
            imagPower += power;
        }
    }
    realPower /= time / 1000;
    imagPower /= time / 1000;
}
