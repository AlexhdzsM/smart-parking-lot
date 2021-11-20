//Esracionamiento inteligente
//Se usará arduino para la lectura de los sensores, lo que se mostrará en la interfaz
//También con arduino activaremos las plumas del estacionamiento



//Primero declaramos las variables
//Cajones a sensar
int CA1; // 0
int CA3; // 1
int B2; // 2
int B4; // 3
int C1; // 4
int C3; // 5
int D2; // 6
int D4; // 7


//Servomotores


//Posiciones iniciales


void setup() {
  //Comunicación serial
    Serial.begin(9600);
    delay(30);
  //Asiganción de pines
  pinMode(12, INPUT);
  pinMode(9, INPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
 


  //Asignación de servos

  

}

void loop() {
  //Se leerán los senspres constantemente

  
//Lectura de sensores
  CA1 = digitalRead(12);
  CA3 = digitalRead(8);
  B2 = digitalRead(2);
  B4 = digitalRead(3);
  C1 = digitalRead(4);
  C3 = digitalRead(5);
  D2 = digitalRead(6);
  D4 = digitalRead(7);
  Serial.println(String(CA1) + "," + String(CA3) + "," + String(B2) + "," + String(B4) + "," + String(C1) + "," + String(C3) + "," + String(D2) + "," + String(D4));
  delay(500);


    
  }
    


    
