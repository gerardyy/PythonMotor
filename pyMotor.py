import RPi.GPIO as GPIO
import time

# Définition des broches pour le contrôle du premier moteur
motor1_pwm = 18  # Broche PWM pour le premier moteur
motor1_dir = 23  # Broche IN1 pour le premier moteur

# Définition des broches pour le contrôle du deuxième moteur
motor2_pwm = 17  # Broche PWM pour le deuxième moteur
motor2_dir = 22  # Broche IN1 pour le deuxième moteur

# Configuration de la bibliothèque RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

# Configuration des broches en tant que sortie
GPIO.setup(motor1_pwm, GPIO.OUT)
GPIO.setup(motor1_dir, GPIO.OUT)

GPIO.setup(motor2_pwm, GPIO.OUT)
GPIO.setup(motor2_dir, GPIO.OUT)

# Création des objets PWM pour contrôler la vitesse des moteurs
motor1 = GPIO.PWM(motor1_pwm, 100)  # Fréquence de PWM : 100 Hz
motor2 = GPIO.PWM(motor2_pwm, 100)

# Démarrage des objets PWM avec un rapport cyclique de 0 (arrêt)
motor1.start(0)
motor2.start(0)

# Fonction pour faire tourner le premier moteur dans le sens horaire
def motor1_forward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(motor1_dir, GPIO.HIGH)
    motor1.ChangeDutyCycle(speed)

# Fonction pour faire tourner le premier moteur dans le sens anti-horaire
def motor1_backward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(motor1_dir, GPIO.LOW)
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
    GPIO.output(motor2_dir, GPIO.HIGH)
    motor2.ChangeDutyCycle(speed)

# Fonction pour faire tourner le 2e  moteur dans le sens anti-horaire
def motor2_backward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    GPIO.output(motor2_dir, GPIO.LOW)
    motor2.ChangeDutyCycle(speed)

# Fonction pour arrêter le premier moteur
def motor2_stop():
    motor2.ChangeDutyCycle(0)


# Test des fonctions de contrôle des moteurs
try:
    print ("try")
    while True:
        motor1_forward(50)  # Faire tourner le premier moteur dans le sens horaire à 50% de sa vitesse
        motor2_backward(75)  # Faire tourner le deuxième moteur dans le sens horaire à 75% de sa vitesse
        time.sleep(2)

        print ("stop")
        motor1_stop()  # Arrêter le premier moteur
        motor2_stop()  # Arrêter le deuxième moteur
        time.sleep(1)

        print ("forward")
        motor1_forward(60)  # Faire tourner le premier moteur dans le sens anti-horaire à 60% de sa vitesse
        motor2_forward(40)  # Faire tourner le deuxième moteur dans le sens anti-horaire à 40% de sa vitesse
        time.sleep(2)

        print ("stop")
        motor1_stop()  # Arrêter le premier moteur
        motor2_stop()  # Arrêter le deuxième moteur
        time.sleep(1)

except KeyboardInterrupt:
    print ("ctrl C")

finally:
    print ("finally ")
    motor1.stop()
    motor2.stop()
    GPIO.cleanup()
