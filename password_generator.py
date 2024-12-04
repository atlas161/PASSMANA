import random
import string

def generer_mot_de_passe(longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_speciaux):
    caracteres = ''
    if inclure_majuscules:
        caracteres += string.ascii_uppercase
    if inclure_minuscules:
        caracteres += string.ascii_lowercase
    if inclure_chiffres:
        caracteres += string.digits
    if inclure_speciaux:
        caracteres += string.punctuation

    if not caracteres:
        caracteres = string.ascii_letters + string.digits + string.punctuation

    mot_de_passe = []
    if inclure_majuscules:
        mot_de_passe.append(random.choice(string.ascii_uppercase))
    if inclure_minuscules:
        mot_de_passe.append(random.choice(string.ascii_lowercase))
    if inclure_chiffres:
        mot_de_passe.append(random.choice(string.digits))
    if inclure_speciaux:
        mot_de_passe.append(random.choice(string.punctuation))

    while len(mot_de_passe) < longueur:
        mot_de_passe.append(random.choice(caracteres))

    random.shuffle(mot_de_passe)

    return ''.join(mot_de_passe)
