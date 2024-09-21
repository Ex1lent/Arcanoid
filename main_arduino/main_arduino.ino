#define DIR_DRIVE_1 10
#define DIR_DRIVE_2 12
#define SPEED_DRIVE 11

#define DIR_PUNCH_1 5
#define DIR_PUNCH_2 4
#define SPEED_PUNCH 3


#include "GyverPID.h"

GyverPID regulator(0.1, 0.05, 0.01, 10);


unsigned long t1;

void setup() {
  Serial.begin(9600);
  regulator.setLimits(0, 255);
  pinMode(DIR_DRIVE_1, OUTPUT);
  pinMode(DIR_DRIVE_2, OUTPUT);
  pinMode(SPEED_DRIVE, OUTPUT);

}

void loop() {
  if (Serial.available()>0){
    String s = Serial.readStringUntil('\n');
    Serial.println(s);
    byte ind = s.indexOf(',');
    byte ind1 = s.indexOf(';');
    String s1 = s.substring(0,ind);
    String s2 = s.substring(ind+1,ind1);
    String s3 = s.substring(ind1+1,s.length());
    int x = s2.toInt();
    int x_ball = s3.toInt();
    int punch = s1.toInt();
    if (x_ball > x) {
      Motor(-40);
    } else {
      Motor(40);
    }
  }
}

void Motor(int speed1){
  int dir1 = 0;
  int dir2 = 0;
  if (speed1 <= 0){
     dir1 = 0;
     dir2 = 1;
  } else {
     dir1 = 1;
     dir2 = 0;
  }
  digitalWrite(DIR_DRIVE_1, dir1); 
  digitalWrite(DIR_DRIVE_2, dir2); 
  speed1 = abs(speed1);
  speed1 = constrain(speed1, 0, 255);
  analogWrite(SPEED_DRIVE, speed1);
}
