import RPi.GPIO as GPIO
import time

# GND     = broche 3 à partir du haut -jaune- au bout
# GPIO-16 = broche 3  partir de la fin i- blanc blanc - PWM1
# GPIO_12 = broche 5 à partir de la fin - jaune rouge orange -DIR1
# GPIO_17 = broche 6 à partir du haut autre rangée - vert - DIR2
# GPIO_22 = broche 8 à partir du haut autre rangée - bleu marron+blanc-

# Définition des broches pour le contrôle du premier moteur
pin_motor1_pwm = 16  # Broche PWM pour le premier moteur
pin_motor1_dir = 12  # Broche DIR1 pour le premier moteur

# Définition des broches pour le contrôle du deuxième moteur
pin_motor2_pwm = 17  # Broche PWM pour le deuxième moteur
pin_motor2_dir = 22  # Broche DIR2 pour le deuxième moteur

# Configuration de la bibliothèque RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

# Configuration des broches en tant que sortie
GPIO.setup(pin_motor1_pwm, GPIO.OUT)
GPIO.setup(pin_motor1_dir, GPIO.OUT)

GPIO.setup(pin_motor2_pwm, GPIO.OUT)
GPIO.setup(pin_motor2_dir, GPIO.OUT)

# Création des objets PWM pour contrôler la vitesse des moteurs
motor1 = GPIO.PWM(pin_motor1_pwm, 100)  # Fréquence de PWM : 100 Hz
motor2 = GPIO.PWM(pin_motor2_pwm, 100)

# Démarrage des objets PWM avec un rapport cyclique de 0 (arrêt)
motor1.start(0)
motor2.start(0)

# Fonction pour faire tourner le premier moteur dans le sens horaire
def motor1_forward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(pin_motor1_dir, GPIO.HIGH)
    motor1.ChangeDutyCycle(speed)

# Fonction pour faire tourner le premier moteur dans le sens anti-horaire
def motor1_backward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(pin_motor1_dir, GPIO.LOW)
    motor1.ChangeDutyCycle(speed)

# Fonction pour arrêter le premier moteur
def motor1_stop():
    motor1.ChangeDutyCycle(0)

# Fonction pour faire tourner le 2e  moteur dans le sens horaire
def motor2_forward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(pin_motor2_dir, GPIO.HIGH)
    motor2.ChangeDutyCycle(speed)

# Fonction pour faire tourner le 2e  moteur dans le sens anti-horaire
def motor2_backward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(pin_motor2_dir, GPIO.LOW)
    motor2.ChangeDutyCycle(speed)

# Fonction pour arrêter le premier moteur
def motor2_stop():
    motor2.ChangeDutyCycle(0)


# Test des fonctions de contrôle des moteurs
motor1_forward(50)  # Faire tourner le premier moteur dans le sens horaire à 50% de sa vitesse

try:
   # print ("try")
    while True:
         time.sleep(10)
   #     motor1_forward(50)  # Faire tourner le premier moteur dans le sens horaire à 50% de sa vitesse
   #     motor2_backward(75)  # Faire tourner le deuxième moteur dans le sens horaire à 75% de sa vitesse
   #     time.sleep(2)
#
#        print ("stop")
#        motor1_stop()  # Arrêter le premier moteur
#        motor2_stop()  # Arrêter le deuxième moteur
#        time.sleep(1)
#
#        print ("forward")
#        motor1_forward(60)  # Faire tourner le premier moteur dans le sens anti-horaire à 60% de sa vitesse
#        motor2_forward(40)  # Faire tourner le deuxième moteur dans le sens anti-horaire à 40% de sa vitesse
#        time.sleep(2)
#
#        print ("stop")
#        motor1_stop()  # Arrêter le premier moteur
#        motor2_stop()  # Arrêter le deuxième moteur
#        time.sleep(1)

except KeyboardInterrupt:
    print ("ctrl C")

finally:
    print ("finally ")
    motor1.stop()
    motor2.stop()
    GPIO.cleanup()
