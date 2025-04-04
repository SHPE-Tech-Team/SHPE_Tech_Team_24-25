#define STEP_PIN 2
#define DIR_PIN 3

void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);
  Serial.begin(9600); // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read command from Python script
    if (command == 'L') {         // Move left
      digitalWrite(DIR_PIN, LOW);
      for (int i = 0; i < 200; i++) { // Adjust steps as needed
        digitalWrite(STEP_PIN, HIGH);
        delayMicroseconds(800);       // Adjust speed as needed
        digitalWrite(STEP_PIN, LOW);
        delayMicroseconds(800);
      }
    } else if (command == 'R') {   // Move right
      digitalWrite(DIR_PIN, HIGH);
      for (int i = 0; i < 200; i++) {
        digitalWrite(STEP_PIN, HIGH);
        delayMicroseconds(800);
        digitalWrite(STEP_PIN, LOW);
        delayMicroseconds(800);
      }
    }

    if (command == 'U') {
        digitalWrite(DIR_PIN, LOW);
        for (int i = 0; i < 200; i++) { // Adjust steps as needed
            digitalWrite(STEP_PIN, HIGH);
            delayMicroseconds(800);       // Adjust speed as needed
            digitalWrite(STEP_PIN, LOW);
            delayMicroseconds(800);
        }
        } else if (command == 'D') {   // Move down
        digitalWrite(DIR_PIN, HIGH);
        for (int i = 0; i < 200; i++) {
            digitalWrite(STEP_PIN, HIGH);
            delayMicroseconds(800);
            digitalWrite(STEP_PIN, LOW);
            delayMicroseconds(800);
        }
    }
  }
}
