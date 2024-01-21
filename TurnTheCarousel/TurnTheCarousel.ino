/*==========================================================================
// Author : Zayeed and Shah (Circuit Breakers)
//==========================================================================
*/
// Definitions Arduino pins connected to input H Bridge
int IN1 = 4;
int IN2 = 5;
int ENA = 6;
int infraredPin = A1;
int speed = 50;
int startTime;
bool delayRunning = false;
int delayStart = 0;
int moving = false;
int movingToWhite = false;
int movingToBlack = false;
int IRVal = 0;

void setup()
{
// Set the output pins
pinMode(IN1, OUTPUT);
pinMode(IN2, OUTPUT);
pinMode(ENA, OUTPUT);
Serial.begin(9600);

}

void loop()
{

  // Serial.println(IRVal);
  analogWrite(ENA, 150); // PWM

  String a = Serial.readString();

  Serial.println(a);

  //handle strings
//  switch (a){
//    case "black":
//      moveToBlack();
//      break;
//
//    case "white":
//      moveToWhite();
//      break;
//
//    default:
//      turnMotorOFF();
//      break;
//  }
//  

  
  if (a == "white\n"){
    IRVal = analogRead(infraredPin);
     while(IRVal > 300){
      Serial.println(IRVal);
      turnMotorON();
      IRVal = analogRead(infraredPin);
     }
  turnMotorOFF();
  }
  if (a == "black\n"){
      IRVal = analogRead(infraredPin);
      while(IRVal < 800){
      Serial.println(IRVal);
      turnMotorON();
      IRVal = analogRead(infraredPin);
     }
  turnMotorOFF();
 }
}

bool moveToWhite(){
  
  int IRVal = analogRead(infraredPin);
  // if white is found
  if (IRVal < 100){

    
    turnMotorOFF();
    return true;

//    if (!delayRunning)
//      delayStart = millis();
//      delayRunning = true;
//    
//    if (delayRunning && (millis() - delayStart <= 1000))
//      turnMotorON();
//    else
//      turnMotorOFF();
  }
  //if black
  else{
    turnMotorON();
    return false;
  }
}

bool moveToBlack(){
  
  int IRVal = analogRead(infraredPin);
  // if white is found
  if (IRVal > 100){

    
      turnMotorOFF();
      return true;
      
//    if (!delayRunning)
//      delayStart = millis();
//      delayRunning = true;
//    
//    if (delayRunning && (millis() - delayStart <= 1000))
//      turnMotorON();
//    else
//      turnMotorOFF();
  }
  //if white
  else{
    turnMotorON();
    return false;
  }
}


void turnMotorON(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
}

void turnMotorOFF(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, HIGH);
}

void delayMotor(int milliseconds) { // the led task
  // check if delay has timed out after 10sec == 10000mS
  if (delayRunning && ((millis() - delayStart) >= 500)) {
    delayRunning = false; // // prevent this code being run more then once
    turnMotorOFF();
    Serial.println("Turned LED Off");
  }
}
