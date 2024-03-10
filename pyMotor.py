import RPi.GPIO as GPIO
import time
#Hardware
# Raspberry PI Model B Rev 2
# https://www.etechnophiles.com/raspberry-pi-3-gpio-pinout-pin-diagram-and-specs-in-detail-model-b/
# Software PWM is available on all pins
# Hardware PWM is available on these pins only: GPIO12, GPIO13, GPIO18, GPIO19
# Cytron MDD10A 

# On the Raspberry : 
    # GND          = rang 1 broche 3 -vert jaune vert jaune
    # PWM1 GPIO_12 = rang 1 broche -5 # blanc blanc - PWM
    # PWM2 GPIO-13 = rang 2 broche -4 # bleu marron+blanc
    # DIR1 GPIO_24 = Rang 1 broche 9  # jaune rouge orange 
    # DIR2 GPIO_26 = Rang 2 broche -2 # vert 

# Définition des broches pour le contrôle du premier moteur
pin_motor1_pwm = 12  # Broche PWM pour le premier moteur
pin_motor1_dir = 24  # Broche DIR1 pour le premier moteur

# Définition des broches pour le contrôle du deuxième moteur
pin_motor2_pwm = 13  # Broche PWM pour le deuxième moteur
pin_motor2_dir = 26  # Broche DIR2 pour le deuxième moteur

# Configuration de la bibliothèque RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

# Save the speed to decrease the speed smoothly when quitting theprog
motor1_speed = 0 
motor2_speed = 0

# Configuration des broches en tant que sortie et mettre a zero si jamais une broche était restée HIGH
GPIO.setup(pin_motor1_pwm, GPIO.OUT)
GPIO.output(pin_motor1_pwm, GPIO.LOW)
GPIO.setup(pin_motor1_dir, GPIO.OUT)
GPIO.output(pin_motor1_dir, GPIO.LOW)

GPIO.setup(pin_motor2_pwm, GPIO.OUT)
GPIO.output(pin_motor2_pwm, GPIO.LOW)
GPIO.setup(pin_motor2_dir, GPIO.OUT)
GPIO.output(pin_motor2_dir, GPIO.LOW)
time.sleep(1)

# Création des objets PWM pour contrôler la vitesse des moteurs
motor1 = GPIO.PWM(pin_motor1_pwm, 1000)  # Fréquence de PWM : 1000 Hz
motor2 = GPIO.PWM(pin_motor2_pwm, 1000)

# Démarrage des objets PWM avec un rapport cyclique de 0 (arrêt)
motor1.start(0) # Set an initial value
motor2.start(0) # Set an initial value

# Fonction pour faire tourner le premier moteur dans le sens horaire
def motor1_forward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    global motor1_speed
    GPIO.output(pin_motor1_dir, GPIO.HIGH)
    motor1.ChangeDutyCycle(speed)
    motor1_speed = speed
    print ("motor1_speed = ",motor1_speed)

# Fonction pour faire tourner le premier moteur dans le sens anti-horaire
def motor1_backward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    global motor1_speed
    GPIO.output(pin_motor1_dir, GPIO.LOW)
    motor1.ChangeDutyCycle(speed)
    motor1_speed = speed

# Fonction pour arrêter le premier moteur
def motor1_stop():
    global motor1_speed
    motor1.ChangeDutyCycle(0)
    motor1_speed = 0
    motor1.stop()

# Permet d'arreter le moteur progressivement
def motor1_smooth_stop():
    global motor1_speed
    print (motor1_speed)
    while motor1_speed > 0:
        print (motor1_speed)
        motor1.ChangeDutyCycle(motor1_speed)
        motor1_speed-=0.01
    motor1.stop()

# Fonction pour faire tourner le 2e  moteur dans le sens horaire
def motor2_forward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    global motor2_speed
    GPIO.output(pin_motor2_dir, GPIO.HIGH)
    motor2.ChangeDutyCycle(speed)
    motor2_speed = speed

# Fonction pour faire tourner le 2e  moteur dans le sens anti-horaire
def motor2_backward(speed):
    # PWM     DIR               OUTPUT_A    OUTPUT_B
    # Low     X(Don’t care)     Low         Low
    # High    Low               High        Low
    # High    High              Low         High
    global motor2_speed
    GPIO.output(pin_motor2_dir, GPIO.LOW)
    motor2.ChangeDutyCycle(speed)
    motor2_speed = speed

# Fonction pour arrêter le premier moteur
def motor2_stop():
    motor2.ChangeDutyCycle(0)
    motor2_speed = 0
    motor2.stop()

# Permet d'arreter le moteur progressivement
def motor2_smooth_stop():
    global motor2_speed
    while motor2_speed > 0:
        motor2.ChangeDutyCycle(motor2_speed)
        motor2_speed-=0.01
    motor2.stop()

# Unique command for both motors at the same time
def motors_run (speed1,speed2):
    motor1_backward(speed1)
    motor2_forward(speed2)

    
    
try:
    while True:
        print ("FOnd")
        motors_run (100,100)
        time.sleep(5)
        print ("FOnd gauche")
        motors_run (50,100)
        time.sleep(5)
        print ("FOnd droit")
        motors_run (100,50)
        time.sleep(5)
        print ("court")
        motors_run (50,50)
        time.sleep(5)

except KeyboardInterrupt:
    print ("ctrl C")

finally:
    print ("finally ")
    motor1_smooth_stop()
    motor2_smooth_stop()
    GPIO.cleanup()
