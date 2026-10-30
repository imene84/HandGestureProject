int leds[] = {11,9,7,5,3};
int fingerCount = 0;

void setup(){
   Serial.begin(9600);

   for(int i=0; i<5; i++){
      pinMode(leds[i], OUTPUT);
   }
}
void loop() {
    if (Serial.available() > 0) {
        int received = Serial.read();

        Serial.println(received);

        for (int i = 0; i < 5; i++) {
            digitalWrite(leds[i], LOW);
        }

        if (received >= '0' && received <= '5') {
            fingerCount = received - '0';

            for (int i = 0; i < fingerCount; i++) {
                digitalWrite(leds[i], HIGH);
            }
            delay(1000);
        }
    }
}