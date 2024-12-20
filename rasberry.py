import RPi.GPIO as GPIO
import time

def distance_capteurs(PIN_EMETTEUR, PIN_RECEPTEUR, vitesse_signal):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_EMETTEUR, GPIO.OUT)
    GPIO.setup(PIN_RECEPTEUR, GPIO.IN)
    liste_distance = []
    try:
        while True:
            GPIO.output(PIN_EMETTEUR, GPIO.HIGH)  # Emettre un signal
            time.sleep(1e-3)  # Pendant 1 ms
            
            GPIO.output(PIN_EMETTEUR, GPIO.LOW)  # Arreter le signal
            time.sleep(1)  # Attendez 1 seconde entre les transmissions

            debut = time.time()
            fin = time.time()

            while GPIO.input(PIN_RECEPTEUR) == GPIO.LOW:
                debut = time.time()

            while GPIO.input(PIN_RECEPTEUR) == GPIO.HIGH:
                fin = time.time()

            temps_reception = fin - debut
            distance_emetteur_recepteur = temps_reception * vitesse_signal  # calcule de la distance
            liste_distance.append(distance_emetteur_recepteur)
        return liste_distance

    except KeyboardInterrupt:
        GPIO.cleanup()

# Exemple d'utilisation :
PIN_EMETTEUR = 17
PIN_RECEPTEUR = 27
vitesse_signal = 343  # Vitesse du son dans l'air 200C (m/s)

distance_capteurs(PIN_EMETTEUR, PIN_RECEPTEUR, vitesse_signal)

def coordonnees_joueur(PIN_EMETTEUR, PIN_RECEPTEUR_1, PIN_RECEPTEUR_2, PIN_RECEPTEUR_3):
    liste_distance_1 = distance_capteurs(PIN_EMETTEUR, PIN_RECEPTEUR_1, vitesse_signal)
    liste_distance_2= distance_capteurs(PIN_EMETTEUR, PIN_RECEPTEUR_2, vitesse_signal)
    liste_distance_3 = distance_capteurs(PIN_EMETTEUR, PIN_RECEPTEUR_3, vitesse_signal)
    
    liste_abcisses = []
    liste_ordonnees = []
    n = len(liste_distance_1) 
    L = 105 # longueur du terrain 
    l = 68 # largeur du terrain
    
    for i in range(n):
    
        x = (liste_distance_1[i]**2 - liste_distance_3[i]**2 + L**2)/ 2*L
        y = (liste_distance_1[i]**2 - liste_distance_2[i]**2 + l**2)/2*l
        
    liste_abcisses.append(x)
    liste_ordonnees.append(y)
    
    return liste_abcisses, liste_ordonnees
                           
    