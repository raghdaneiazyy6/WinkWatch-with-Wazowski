int enA = 10;
int in1 = 9;
int in2 = 8;
// motor two
int enB = 5;
int in3 = 7;
int in4 = 6;

int motorDirection = 1; // 0 for one direction, 1 for the other direction, 2 for static

void setup()
{
  // set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
}

void controlMotors(int direction)
{
  if (direction == 1) // forward
  {
    // Move in one direction
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
  }
  else if (direction == 0) // backward 
  {

    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
  }
  else if (direction == 2)
  {
    // Static state, motors are off
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
  }

  // Set the speed to a fixed value (e.g., 200 out of possible range 0~255)
  analogWrite(enA, 200);
  analogWrite(enB, 200);
  delay(1000);
}

void loop()
{
  // Depending on the value of motorDirection, move in one direction, the other, or stay static
  controlMotors(motorDirection);


  delay(1000); // Delay before changing direction
}
