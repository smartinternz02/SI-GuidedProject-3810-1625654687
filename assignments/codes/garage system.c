#include <Servo.h>
Servo obj;
const int servo = 5;
const int trig = 2;
const int echo = 3;
void setup()
{
    obj.attach(servo);
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
    Serial.begin(9600);
}

void loop()
{
    digitalWrite(trig, LOW);
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);
    float duration = pulseIn(echo, HIGH);
    float distance = (duration*0.034)/2;
    Serial.println(distance);
    if (distance < 18)
    {
        obj.write(180);
    }
    else
    {
        obj.write(0);
    }
}