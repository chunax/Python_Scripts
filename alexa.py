import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import pyjokes
import time

listner = sr.Recognizer()
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[2].id)


def parler(texte):
    engine.say(texte)
    engine.runAndWait()

def mira():
    try:
        with sr.Microphone() as source:
            print("En train d'écouter")
            parler("Oui ?")
            voice = listner.listen(source)
            commande = listner.recognize_google(voice, language="fr-FR")
            commande = commande.lower()
            print(commande)
            if 'musique' in commande:
                musique = commande.replace('musique', '')
                parler("En train d'écouter " + musique)
                print("En train d'écouter" + musique)
                pywhatkit.playonyt(musique)
            elif 'heure' in commande:
                time = datetime.datetime.now().strftime('%H:%M')
                print(time)
                time = time.split(':')
                parler('Il est ' + time[0] + ' heure ' + time[1])
            elif "wikipédia" in commande:
                personne = commande.replace("wikipédia", ' ')
                wikipedia.set_lang("fr")
                info = wikipedia.summary(personne, 4)
                print(info)
                parler(info)
            elif 'blague' in commande:
                blague = pyjokes.get_joke()
                print(blague)
                parler(blague)
            elif 'lance' in commande:
                if 'lol' in commande:
                    os.startfile(
                        r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JeuALancer\League of Legends', 'open')
                if 'nostale' in commande:
                    os.startfile(
                        r'C:\Users\maxim\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Gameforge Client', 'open')
                if 'steam' in commande:
                    os.startfile(
                        r'C:\Users\maxim\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Steam\Steam','open')
            elif 'cherche' in commande:
                recherche = commande.replace('cherche', '')
                pywhatkit.search(recherche)
                print("Searching...")
            else:
                print("")
    except:
        pass

# Lancer une seule commande
mira()


# Lancer plusieurs commandes (pas totalement focntionnel)
# while True:
#     try:
#         with sr.Microphone() as source:
#             voice = listner.listen(source)
#             commande = listner.recognize_google(voice, language="fr-FR")
#             commande = commande.lower()
#             if 'mira' in commande:
#                 print("En train d'écouter")
#                 parler("Oui ?")
#                 voice = listner.listen(source)
#                 commande = listner.recognize_google(voice, language="fr-FR")
#                 commande = commande.lower()
#                 print(commande)
#                 if 'musique' in commande:
#                     musique = commande.replace('musique', '')
#                     parler("En train d'écouter " + musique)
#                     print("En train d'écouter" + musique)
#                     pywhatkit.playonyt(musique)
#                 elif 'heure' in commande:
#                     time = datetime.datetime.now().strftime('%H:%M')
#                     print(time)
#                     time = time.split(':')
#                     parler('Il est ' + time[0] + ' heure ' + time[1])
#                 elif "wikipédia" in commande:
#                     personne = commande.replace("wikipédia", ' ')
#                     wikipedia.set_lang("fr")
#                     info = wikipedia.summary(personne, 1)
#                     print(info)
#                     parler(info)
#                 elif 'blague' in commande:
#                     blague = pyjokes.get_joke()
#                     print(blague)
#                     parler(blague)

#                 elif 'lance' in commande:
#                     if 'lol' in commande:
#                         os.startfile(
#                             r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JeuALancer\League of Legends', 'open')
#                 elif 'cherche' in commande:
#                     recherche = commande.replace('cherche', '')
#                     pywhatkit.search(recherche)
#                     print("Searching...")
#                 elif 'envoie' in commande:
#                     time = datetime.datetime.now().strftime('%H:%M')
#                     time = time.split(':')
#                     message = commande.replace('envoie', '')
#                     print(int(time[0]))
#                     print(int(time[1]))
#                     if 'lilou' in commande:
#                         message = message.replace('lilou', '')
#                         dest = lilou
#                         pywhatkit.sendwhatmsg(dest,
#                                               message, int(time[0]), int(time[1]) + 3)

#                         print("Successfully Sent!")
#                         parler("Message envoyé")
#                     if 'kevin' in commande:
#                         message = message.replace('kevin', '')
#                         dest = kevin
#                         pywhatkit.sendwhatmsg(dest,
#                                               message, int(time[0]), int(time[1]) + 3)
#                         print("Successfully Sent!")
#                         parler("Message envoyé")
#                     if 'caro' in commande:
#                         message = message.replace('caro', '')
#                         dest = caro
#                         pywhatkit.sendwhatmsg(dest,
#                                               message, int(time[0]), int(time[1]) + 3)
#                         print("Successfully Sent!")
#                         parler("Message envoyé")
#                     if 'alicia' in commande:
#                         message = message.replace('alicia', '')
#                         dest = alicia
#                         pywhatkit.sendwhatmsg(dest,
#                                                 message, int(time[0]), int(time[1]) + 3)
#                         print("Successfully Sent!")
#                         parler("Message envoyé")
#             else:
#                 print("")
#     except:
#         pass
