#define DIR_1     4
#define SPEED_1   5
#define SPEED_2   6
#define DIR_2     7
#define HIT       12 //ударник
#define L_SENSOR 10
#define R_SENSOR 11
#include "GyverPID.h"

GyverPID regulator(0.1, 0.05, 0.01, 10);

int base_speed = 75;

unsigned long t1;

void setup() {
  Serial.begin(9600);
  regulator.setLimits(0, 255);
  pinMode(DIR_1, OUTPUT);
  pinMode(DIR_2, OUTPUT);
  pinMode(SPEED_1, OUTPUT);
  pinMode(SPEED_2, OUTPUT);
  pinMode(HIT, OUTPUT);
  pinMode(L_SENSOR, INPUT_PULLUP);
  pinMode(R_SENSOR, INPUT_PULLUP);
}

void loop() {
  if (Serial.available()>0){
    
    String s = Serial.readStringUntil('\n');
    Serial.println(s);
    byte ind = s.indexOf(',');
    String s1 = s.substring(0,ind);
    String s2 = s.substring(ind+1,s.length());
    int x = s1.toInt();
    int x_ball = s2.toInt();
    int
    regulator.setpoint = 50;

  }
}

void motor(int speed1, int speed2){
  int dir1 = 0;
  int dir2 = 0;
  if (speed1 > 0){
     dir1 = 1;
  }
  else{
     dir1 = 0;
  }
  if (speed2 > 0){
     dir2 = 0;
  }
  else{
     dir2 = 1;
  }
  digitalWrite(DIR_1, dir1); 
  digitalWrite(DIR_2, dir2); 
  speed1 = abs(speed1);
  speed2 = abs(speed2);
  speed1 = constrain(speed1, 0, 255);
  speed2 = constrain(speed2, 0, 255);
  analogWrite(SPEED_1, speed1);
  analogWrite(SPEED_2, speed2);
}
