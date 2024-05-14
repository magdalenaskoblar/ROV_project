#include <Servo.h>
#include "SerialTransfer.h"

SerialTransfer myTransfer;
byte servoPin1 = 5;
byte servoPin2 = 6;
byte servoPin3 = 9;
byte servoPin4 = 10;
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

signed int signal1 = 1500;
signed int signal2 = 1500;
signed int signal3 = 1500;
signed int signal4 = 1500;
signed int signal5 = 1500;
signed int motor1 = 1500;
signed int motor2 = 1500;

void setup() {
  servo1.attach(servoPin1, 1000, 2000);
  servo2.attach(servoPin2, 1000, 2000);
  servo3.attach(servoPin3, 1000, 2000);
  servo4.attach(servoPin4, 1000, 2000); //ccw

  Serial.begin(9600);
  myTransfer.begin(Serial);

  servo1.writeMicroseconds(1500); // send "stop" signal to ESC.
	servo2.writeMicroseconds(1500); // send "stop" signal to ESC.
	servo3.writeMicroseconds(1500); // send "stop" signal to ESC.
  servo4.writeMicroseconds(1500); // send "stop" signal to ESC.

	delay(50); // delay to allow the ESC to recognize the stopped signal
}


void loop() {
  while (Serial.available()){
  while (myTransfer.available()) {

    int msg[10];  

    // Čitanje podataka iz buffer-a
    myTransfer.rxObj(msg, 0);
    
    signal1 = msg[0];
    signal2 = msg[2]; 
    signal3 = msg[4]; 
    signal4 = msg[6];
    signal5 = msg[8];
  
    motor1 = sqrt(pow(signal1 - 1500, 2) + pow(signal2 - 1500, 2)) + 1500;
    motor2 = sqrt(pow(signal1 - 1500, 2) + pow(signal3 - 1500, 2)) + 1500;

    servo1.writeMicroseconds(motor1);
    servo2.writeMicroseconds(motor2);

    if (signal4 != 1500){ 
      servo3.writeMicroseconds(signal4);
      servo4.writeMicroseconds(signal4); 
    }else if (signal5 != 1500){
      servo3.writeMicroseconds(signal5);
      servo4.writeMicroseconds(signal5);
    }else{
      servo3.writeMicroseconds(1500);
      servo4.writeMicroseconds(1500);
    } 
    delay(2);
}
}
}