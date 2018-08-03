#include <Servo.h> 
 
Servo myservo; 

int incomingByte;
void setup() 
{ 
  myservo.attach(9); 

  Serial.begin(9600);  
} 
 
void loop() {
  
  while(Serial.available() > 0){
    incomingByte = Serial.parseInt();
    if(Serial.read() == '\n') 
    { 
      myservo.write(incomingByte);
    }   
    
  }
}
