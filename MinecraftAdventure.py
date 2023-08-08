"""
Version Minecraft par Fatih C.
Sources & Aides:
https://www.scaler.com/topics/how-to-clear-screen-in-python/
https://www.101computing.net/python-typing-text-effect/
https://patorjk.com/
https://emojicombos.com/minecraft-steve
https://smallbusiness.chron.com/making-raw-input-lowercase-python-31840.html
https://www.caracterespeciaux.com/p/multiple.html
https://www.reddit.com/r/Minecraft/comments/fu2mdt/i_remade_the_player_inventory_in_ascii_art/
https://towardsdatascience.com/coloured-text-terminal-python-dc5692ee6319
"""

import os
import random
import sys
from time import sleep
import time

personnage = {
    "Coeur ♥": 100,
}
creeper = {
    "Coeur ♥": 50
}

items = [
    "Plume aiguisé    [Permet de contrôler la gravité et de voler]",
    "Oeil d'Enderman   [Permet de se téléporter instantanément à n'importe quel endroit]",
    "Bloc d'obsidienne  [Envoyer l'ennemi en enfer en lui lançant le bloc]",
    "Baton de Blaze   [Permet de contrôler le feu et de lancer des boules de feu]",
    "Boule de neige   [Permet de contrôler le froid et de générer des tempêtes de neige]",
    "Poudre de canon   [Permet de faire exploser les ennemis]",
    "Hâche en or     [Permet de découper l'ennemi en 2, très faible durabilité]",
]


plats_stock = {
    "steak" : 1,
    "pomme" : 2,
    "cookie" : 1,
    "melon" : 1,
    "carotte" : 2,
}

inventaire = {
    "cleCoffre":0,
    "diamant":0
}

prenom = "notch"
version = 0
items_choisi = 0
compteur_frappe = 0

okay_coffre_ouvert = False
okay_chevaux = False
okay_cle = False
okay_creeper_combat = False


# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************

def proposer_actions(actions):
    message = "│ Actions :"
    print(message)
    for action in actions:
        print(f"│ 💡 Tape {action}")
    print(f"│")


def proposer_lieux(mots_cles):
    print(f"│ Se déplacer :")
    for index, mots_cles in enumerate (mots_cles):
        print(f"│ 📍 Tape '{index+1}' pour le lieu: {mots_cles}")

def typingPrint(message):
    for letter in message:
        print(letter, end='', flush=True)
        # sleep(0.05)
        sleep(0.03)

class Encre:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

    RESET = '\033[0m'
    UNDERLINE = '\033[4m'


def minecraft():
    os.system('clear')
    print(f"{Encre.GREEN}.___  ___.  __  .__   __.  _______   ______ .______       ___       _______ .___________.")
    print("|   \/   | |  | |  \ |  | |   ____| /      ||   _  \     /   \     |   ____||           |")
    print("|  \  /  | |  | |   \|  | |  |__   |  ,----'|  |_)  |   /  ^  \    |  |__   `---|  |----`")
    print("|  |\/|  | |  | |  . `  | |   __|  |  |     |      /   /  /_\  \   |   __|      |  |")
    print("|  |  |  | |  | |  |\   | |  |____ |  `----.|  |\  \  /  _____  \  |  |         |  |")
    print(f"|__|  |__| |__| |__| \__| |_______| \______|| _| `._|/__/     \__\ |__|         |__|{Encre.RESET}\n")

def mojang():
    os.system('clear')
    print(f"{Encre.YELLOW}                        ___   __  _______      ___  _______  __    _  _______")
    print("                        |  |_|  ||       |    |   ||   _   ||  |  | ||       |")
    print("                        |       ||   _   |    |   ||  | |  ||   |_| ||    ___|")
    print("                        |       ||  | |  |    |   ||  |_|  ||       ||   | __ ")
    print("                        |       ||  |_|  | ___|   ||       ||  _    ||   ||  |")
    print("                        | ||_|| ||       ||       ||   _   || | |   ||   |_| |")
    print("                        |_|   |_||_______||_______||__| |__||_|  |__||_______|")
    print(f"                                                By Fatih C.{Encre.RESET}\n")


def creeperCombat():
    print("\n")
    print("\n")
    print("\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
    print("🟥                                                                        🟥")
    if personnage['Prenom'] == "alex" or personnage['Prenom'] == "Alex":
        print("🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🟧🟧🟧🟧🟧🟧🟧🟧  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩                                    🟧🟧🟧🟧🟧🟧🟧🟧  🟥")
        print(f"{Encre.RED}🟥  🟩⬛⬛🟩🟩⬛⬛🟩             __   _____             🟧🟧🟧🟧🏻🏻🟧🟧  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩             \ \ / / __|            🟧🟧🟧🏻🏻🏻🏻🟧  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩              \ V /\__ \            🏻⬜🟩🏻🏻🟩⬜🏻  🟥")
        print(f"🟥  🟩🟩⬛⬛⬛⬛🟩🟩               \_/ |___/            🏻🏻🏻🏻🏻🏻🏻🏻  🟥{Encre.RESET}")
        print("🟥  🟩🟩⬛🟩🟩⬛🟩🟩                                    🏻🏻🏻🟪🟪🏻🏻🏻  🟥")
        print("🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🏻🏻🏻🏻🏻🏻🏻🏻  🟥")
    elif personnage['Prenom'] == "steve" or personnage['Prenom'] == "Steve":
        print("🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    ⬛⬛⬛⬛⬛⬛⬛⬛  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩                                    ⬛⬛⬛⬛⬛⬛⬛⬛  🟥")
        print(f"{Encre.RED}🟥  🟩⬛⬛🟩🟩⬛⬛🟩             __   _____             ⬛🏽🏽🏽🏽🏽🏽⬛  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩             \ \ / / __|            🏽🏽🏽🏽🏽🏽🏽🏽  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩              \ V /\__ \            🏽⬜🟦🏽🏽🟦⬜🏽  🟥")
        print(f"🟥  🟩🟩⬛⬛⬛⬛🟩🟩               \_/ |___/            🏽🏽🏽🟫🟫🏽🏽🏽  🟥{Encre.RESET}")
        print("🟥  🟩🟩⬛🟩🟩⬛🟩🟩                                    🏽🏽⬛🏽🏽⬛🏽🏽  🟥")
        print("🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🏽🏽⬛⬛⬛⬛🏽🏽  🟥")
    elif personnage['Prenom'] == "notch":
        print("🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🟧🟧🟧🟧🟧🟧🟧🟧  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩                                    🟧🏽🏽🏽🏽🏽🏽🟧  🟥")
        print(f"{Encre.RED}🟥  🟩⬛⬛🟩🟩⬛⬛🟩             __   _____             🟧🏽🏽🏽🏽🏽🏽🟧  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩             \ \ / / __|            🏽🏽🏽🏽🏽🏽🏽🏽  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩              \ V /\__ \            🏽⬜🟧🏽🏽🟧⬜🏽  🟥")
        print(f"🟥  🟩🟩⬛⬛⬛⬛🟩🟩               \_/ |___/            🏽🏽🏽🟫🟫🏽🏽🏽  🟥{Encre.RESET}")
        print("🟥  🟩🟩⬛🟩🟩⬛🟩🟩                                    🏽🏽⬛🏽🏽⬛🏽🏽  🟥")
        print("🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🏽🏽⬛⬛⬛⬛🏽🏽  🟥")
    print("🟥                                                                        🟥")
    print(f"     {Encre.GREEN}Creeper : " + str(creeper["Coeur ♥"]) + f" ♥                                       {Encre.BLUE}" + personnage['Prenom'] + " : " + str(personnage["Coeur ♥"]) + " ♥\n")


def skinAttaqueCreeper():
    print("\n")
    print("\n")
    print("\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
    print("🟥                                                                              🟥")
    if personnage['Prenom'] == "alex" or personnage['Prenom'] == "Alex":
        print(f"{Encre.GREEN}🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🟦    🟧🟧🟧🟧🟧🟧🟧🟧  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩                                🟦🟪⬜    🟧🟧🟧🟧🟧🟧🟧🟧  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩          🟪 __   _____       🟦🟪        🟧🟧🟧🟧🏻🏻🟧🟧  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩        🟪   \ \ / / __|     🟦🟪         🟧🟧🟧🏻🏻🏻🏻🟧  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩    🟪⬜⬜⬜⬜\ V /\__ \⬜⬜⬜🟪🟪🟦      🏻⬜🟩🏻🏻🟩⬜🏻  🟥")
        print("🟥  🟩🟩⬛⬛⬛⬛🟩🟩        🟪     \_/ |___/     🟦🟪         🏻🏻🏻🏻🏻🏻🏻🏻  🟥")
        print("🟥  🟩🟩⬛🟩🟩⬛🟩🟩          🟪                  🟦🟪        🏻🏻🏻🟪🟪🏻🏻🏻  🟥")
        print(f"🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                🟦🟪⬜    🏻🏻🏻🏻🏻🏻🏻🏻  🟥{Encre.RESET}")

    elif personnage['Prenom'] == "steve" or personnage['Prenom'] == "Steve":
        print(f"{Encre.GREEN}🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🟦    ⬛⬛⬛⬛⬛⬛⬛⬛  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩                                🟦🟪⬜    ⬛⬛⬛⬛⬛⬛⬛⬛  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩          🟪 __   _____       🟦🟪        ⬛🏽🏽🏽🏽🏽🏽⬛  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩        🟪   \ \ / / __|     🟦🟪         🏽🏽🏽🏽🏽🏽🏽🏽  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩    🟪⬜⬜⬜⬜\ V /\__ \⬜⬜⬜🟪🟪🟦      🏽⬜🟦🏽🏽🟦⬜🏽  🟥")
        print("🟥  🟩🟩⬛⬛⬛⬛🟩🟩        🟪     \_/ |___/     🟦🟪         🏽🏽🏽🟫🟫🏽🏽🏽  🟥")
        print("🟥  🟩🟩⬛🟩🟩⬛🟩🟩          🟪                  🟦🟪        🏽🏽⬛🏽🏽⬛🏽🏽  🟥")
        print(f"🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                🟦🟪⬜    🏽🏽⬛⬛⬛⬛🏽🏽  🟥{Encre.RESET}")
    elif personnage['Prenom'] == "notch":
        print(f"{Encre.GREEN}🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                    🟦    🟧🟧🟧🟧🟧🟧🟧🟧  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩                                🟦🟪⬜    🟧🏽🏽🏽🏽🏽🏽🟧  🟥")
        print("🟥  🟩⬛⬛🟩🟩⬛⬛🟩          🟪 __   _____       🟦🟪        🟧🏽🏽🏽🏽🏽🏽🟧  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩        🟪   \ \ / / __|     🟦🟪         🏽🏽🏽🏽🏽🏽🏽🏽  🟥")
        print("🟥  🟩🟩🟩⬛⬛🟩🟩🟩    🟪⬜⬜⬜⬜\ V /\__ \⬜⬜⬜🟪🟪🟦      🏽⬜🟧🏽🏽🟧⬜🏽  🟥")
        print("🟥  🟩🟩⬛⬛⬛⬛🟩🟩        🟪     \_/ |___/     🟦🟪         🏽🏽🏽🟫🟫🏽🏽🏽  🟥")
        print("🟥  🟩🟩⬛🟩🟩⬛🟩🟩          🟪                  🟦🟪        🏽🏽⬛🏽🏽⬛🏽🏽  🟥")
        print(f"🟥  🟩🟩🟩🟩🟩🟩🟩🟩                                🟦🟪⬜    🏽🏽⬛⬛⬛⬛🏽🏽  🟥{Encre.RESET}")
    print("🟥                                                      🟦                      🟥")
    print(f"     {Encre.GREEN}Creeper : " + str(creeper["Coeur ♥"]) + f" ♥                                             {Encre.BLUE}" + personnage['Prenom'] + " : " + str(personnage["Coeur ♥"]) + f" ♥{Encre.RESET}\n")


def creeperAttaqueSkin():
    print("\n")
    print("\n")
    print("\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥")
    print("🟥                                                                              🟥")
    if personnage['Prenom'] == "alex" or personnage['Prenom'] == "Alex":
        print(f"{Encre.RED}🟥  🟧🟧🟧🟧🟧🟧🟧🟧                                    🟩    🟩🟩🟩🟩🟩🟩🟩🟩  🟥")
        print("🟥  🟧🟧🟧🟧🟧🟧🟧🟧                                🟩🟥🟩    🟩⬛⬛🟩🟩⬛⬛🟩  🟥")
        print("🟥  🟧🟧🟧🟧🏻🏻🟧🟧          🟥 __   _____       🟩🟥        🟩⬛⬛🟩🟩⬛⬛🟩  🟥")
        print("🟥  🟧🟧🟧🏻🏻🏻🏻🟧        🟥   \ \ / / __|     🟩🟥         🟩🟩🟩⬛⬛🟩🟩🟩  🟥")
        print("🟥  🏻⬜🟩🏻🏻🟩⬜🏻    🟥🟩🟩🟩🟩\ V /\__ \🟩🟩🟩🟥🟥🟩      🟩🟩🟩⬛⬛🟩🟩🟩  🟥")
        print("🟥  🏻🏻🏻🏻🏻🏻🏻🏻        🟥     \_/ |___/     🟩🟥         🟩🟩⬛⬛⬛⬛🟩🟩  🟥")
        print("🟥  🏻🏻🏻🟪🟪🏻🏻🏻          🟥                  🟩🟥        🟩🟩⬛🟩🟩⬛🟩🟩  🟥")
        print(f"🟥  🏻🏻🏻🏻🏻🏻🏻🏻                                🟩🟥🟩    🟩🟩🟩🟩🟩🟩🟩🟩  🟥{Encre.RESET}")
    elif personnage['Prenom'] == "steve" or personnage['Prenom'] == "Steve":
        print(f"{Encre.RED}🟥  ⬛⬛⬛⬛⬛⬛⬛⬛                                    🟩    🟩🟩🟩🟩🟩🟩🟩🟩  🟥")
        print("🟥  ⬛⬛⬛⬛⬛⬛⬛⬛                                🟩🟥🟩    🟩⬛⬛🟩🟩⬛⬛🟩  🟥")
        print(f"🟥  ⬛🏽🏽🏽🏽🏽🏽⬛          🟥 __   _____       🟩🟥        🟩⬛⬛🟩🟩⬛⬛🟩  🟥{Encre.RESET}")
        print("🟥  🏽🏽🏽🏽🏽🏽🏽🏽        🟥   \ \ / / __|     🟩🟥         🟩🟩🟩⬛⬛🟩🟩🟩  🟥")
        print("🟥  🏽⬜🟦🏽🏽🟦⬜🏽    🟥🟩🟩🟩🟩\ V /\__ \🟩🟩🟩🟥🟥🟩      🟩🟩🟩⬛⬛🟩🟩🟩  🟥")
        print("🟥  🏽🏽🏽🟫🟫🏽🏽🏽        🟥     \_/ |___/     🟩🟥         🟩🟩⬛⬛⬛⬛🟩🟩  🟥")
        print("🟥  🏽🏽⬛🏽🏽⬛🏽🏽          🟥                  🟩🟥        🟩🟩⬛🟩🟩⬛🟩🟩  🟥")
        print(f"🟥  🏽🏽⬛⬛⬛⬛🏽🏽                                🟩🟥🟩    🟩🟩🟩🟩🟩🟩🟩🟩  🟥{Encre.RESET}")
    elif personnage['Prenom'] == "notch":
        print(f"{Encre.RED}🟥  🟧🟧🟧🟧🟧🟧🟧🟧                                    🟩    🟩🟩🟩🟩🟩🟩🟩🟩  🟥")
        print("🟥  🟧🏽🏽🏽🏽🏽🏽🟧                                🟩🟥🟩    🟩⬛⬛🟩🟩⬛⬛🟩  🟥")
        print("🟥  🟧🏽🏽🏽🏽🏽🏽🟧          🟥 __   _____       🟩🟥        🟩⬛⬛🟩🟩⬛⬛🟩  🟥")
        print("🟥  🏽🏽🏽🏽🏽🏽🏽🏽        🟥   \ \ / / __|     🟩🟥         🟩🟩🟩⬛⬛🟩🟩🟩  🟥")
        print("🟥  🏽⬜🟧🏽🏽🟧⬜🏽    🟥🟩🟩🟩🟩\ V /\__ \🟩🟩🟩🟥🟥🟩      🟩🟩🟩⬛⬛🟩🟩🟩  🟥")
        print("🟥  🏽🏽🏽🟫🟫🏽🏽🏽        🟥     \_/ |___/     🟩🟥         🟩🟩⬛⬛⬛⬛🟩🟩  🟥")
        print("🟥  🏽🏽⬛🏽🏽⬛🏽🏽          🟥                  🟩🟥        🟩🟩⬛🟩🟩⬛🟩🟩  🟥")
        print(f"🟥  🏽🏽⬛⬛⬛⬛🏽🏽                                🟩🟥🟩    🟩🟩🟩🟩🟩🟩🟩🟩  🟥{Encre.RESET}")
    print("🟥                                                      🟩                      🟥")
    print(f"     {Encre.BLUE}" + personnage['Prenom'] + " : " + str(personnage["Coeur ♥"]) + " ♥                                               " + f"{Encre.GREEN}Creeper : " + str(creeper["Coeur ♥"]) + f" ♥{Encre.RESET}\n")


def skin(text):
    if personnage['Prenom'] == "alex" or personnage['Prenom'] == "Alex":
        print("🟧🟧🟧🟧🟧🟧🟧🟧")
        print("🟧🟧🟧🟧🟧🟧🟧🟧")
        print("🟧🟧🟧🟧🏻🏻🟧🟧")
        print("🟧🟧🟧🏻🏻🏻🏻🟧")
        print(f"🏻⬜🟩🏻🏻🟩⬜🏻     {Encre.BLUE}──────────────────────────────────────────────────────────────")
        print(f"🏻🏻🏻🏻🏻🏻🏻🏻     < Alex : {Encre.RESET}" + text + f" {Encre.BLUE}>")
        print(f"🏻🏻🏻🟪🟪🏻🏻🏻     {Encre.BLUE}──────────────────────────────────────────────────────────────")
        print(f"{Encre.RESET}🏻🏻🏻🏻🏻🏻🏻🏻\n")
    elif personnage['Prenom'] == "steve" or personnage['Prenom'] == "Steve":
        print("⬛⬛⬛⬛⬛⬛⬛⬛")
        print("⬛⬛⬛⬛⬛⬛⬛⬛")
        print("⬛🏽🏽🏽🏽🏽🏽⬛")
        print("🏽🏽🏽🏽🏽🏽🏽🏽")
        print(f"🏽⬜🟦🏽🏽🟦⬜🏽     {Encre.BLUE}──────────────────────────────────────────────────────────────")
        print(f"🏽🏽🏽🟫🟫🏽🏽🏽     < Steve : {Encre.RESET}" + text + f" {Encre.BLUE}>")
        print(f"🏽🏽⬛🏽🏽⬛🏽🏽     {Encre.BLUE}──────────────────────────────────────────────────────────────")
        print(f"{Encre.RESET}🏽🏽⬛⬛⬛⬛🏽🏽\n")
    elif personnage['Prenom'] == "notch":
        print("🟧🟧🟧🟧🟧🟧🟧🟧")
        print("🟧🏽🏽🏽🏽🏽🏽🟧")
        print("🟧🏽🏽🏽🏽🏽🏽🟧")
        print("🏽🏽🏽🏽🏽🏽🏽🏽")
        print(f"🏽⬜🟧🏽🏽🟧⬜🏽     {Encre.BLUE}──────────────────────────────────────────────────────────────")
        print(f"🏽🏽🏽🟫🟫🏽🏽🏽     < Notch : {Encre.RESET}" + text + f" {Encre.BLUE}>")
        print(f"🏽🏽⬛🏽🏽⬛🏽🏽     {Encre.BLUE}──────────────────────────────────────────────────────────────")
        print(f"{Encre.RESET}🏽🏽⬛⬛⬛⬛🏽🏽\n")


def mapLocalisation():
    print(f"{Encre.YELLOW}🟧🟨🟨🟧🟧                                          🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
    print("🟧🟨🟨🟧  🟧                                      🟨⬛                              ⬛🟨")
    print("🟨🟧🟧                                          🟨⬛  📍 Ferme à XP de Creeper        ⬛🟨")
    print("🟨🟨🟧  🟧                                    🟨⬛                                      ⬛🟨")
    print("🟧🟧     🟧                                 🟨  ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛  🟨")
    print("  🟧                                        🟨  ⬛                                      ⬛  🟨")
    print("                                                ⬛    📍 Bibliothèque                   ⬛")
    print("                                                ⬛    📍 Cafetériat                     ⬛")
    print("       ⬛⬛⬛⬛⬛                               ⬛                                      ⬛")
    print("     ⬛⬛🟦⬛🟦⬛⬛                             ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    print("     ⬛🟦🟦⬛🟦🟦⬛ 📍 Écurie                   ⬛                                      ⬛")
    print("     ⬛⬛⬛⬛⬛⬛⬛                             ⬛    📍 Place du Village               ⬛")
    print("     ⬛🟦      🟦⬛                             🟫    📍 Comptoir du villageois         ⬛")
    print("  🌳 ⬛🟦   🐴 🟦⬛ 🌲          🌳     🌲       🟫                                      ⬛")
    print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜")
    print(f"🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜{Encre.RESET}\n")

def steve():
    print("\n⬛⬛⬛⬛⬛⬛⬛⬛")
    print("⬛⬛⬛⬛⬛⬛⬛⬛")
    print("⬛🏽🏽🏽🏽🏽🏽⬛")
    print("🏽🏽🏽🏽🏽🏽🏽🏽")
    print("🏽⬜🟦🏽🏽🟦⬜🏽")
    print("🏽🏽🏽🟫🟫🏽🏽🏽")
    print("🏽🏽⬛🏽🏽⬛🏽🏽")
    print("🏽🏽⬛⬛⬛⬛🏽🏽\n")
def alex():
    print("\n🟧🟧🟧🟧🟧🟧🟧🟧")
    print("🟧🟧🟧🟧🟧🟧🟧🟧")
    print("🟧🟧🟧🟧🏻🏻🟧🟧")
    print("🟧🟧🟧🏻🏻🏻🏻🟧")
    print("🏻⬜🟩🏻🏻🟩⬜🏻")
    print("🏻🏻🏻🏻🏻🏻🏻🏻")
    print("🏻🏻🏻🟪🟪🏻🏻🏻")
    print("🏻🏻🏻🏻🏻🏻🏻🏻\n")

def notch():
    print("\n🟧🟧🟧🟧🟧🟧🟧🟧")
    print("🟧🏽🏽🏽🏽🏽🏽🟧")
    print("🟧🏽🏽🏽🏽🏽🏽🟧")
    print("🏽🏽🏽🏽🏽🏽🏽🏽")
    print("🏽⬜🟧🏽🏽🟧⬜🏽")
    print("🏽🏽🏽🟫🟫🏽🏽🏽")
    print("🏽🏽⬛🏽🏽⬛🏽🏽")
    print("🏽🏽⬛⬛⬛⬛🏽🏽\n")

def villageois(text):
        print("🟫🟫🟫🟫🟫🟫🟫🟫")
        print("🟫🟫🟫🟫🟫🟫🟫🟫")
        print("🟫🟫🟫🟫🟫🟫🟫🟫")
        print("🟫🟫🟫🟫🟫🟫🟫🟫")
        print("🟫⬛⬛⬛⬛⬛⬛🟫")
        print(f"🟫⬜🟩🟫🟫🟩⬜🟫      {Encre.YELLOW}──────────────────────────────────────────────────────────────")
        print(f"🟫🟫🟫🟧🟧🟫🟫🟫     < Villegeois: {Encre.RESET}" + text + f" .. {Encre.YELLOW}>")
        print(f"🟫🟫⬛🟧🟧⬛🟫🟫      {Encre.YELLOW}──────────────────────────────────────────────────────────────")
        print(f"{Encre.RESET}🟫🟫🟫🟧🟧🟫🟫🟫")
        print("➖➖➖🟧🟧\n")

def villageois_libraire(text):
    print("🟧🟧🟧🟧🟧🟧🟧🟧")
    print("🟧🟧🟫🟫🟫🟫🟧🟧")
    print("🟧🟫🟫🟫🟫🟫🟫🟧")
    print("🟧🟫🟫🟫🟫🟫🟫🟧")
    print("🟫⬛⬛⬛⬛⬛⬛🟫")
    print(f"🟫⬜🟦🟫🟫🟦⬜🟫      {Encre.YELLOW}──────────────────────────────────────────────────────────────")
    print(f"🟫🟫🟫🟧🟧🟫🟫🟫     < Libraire: {Encre.RESET}" + text + f" .. {Encre.YELLOW}>")
    print(f"🟧🟫⬛🟧🟧⬛🟫🟧      {Encre.YELLOW}──────────────────────────────────────────────────────────────")
    print(f"{Encre.RESET}🟧🟫🟫🟧🟧🟫🟫🟧")
    print("➖➖➖🟧🟧\n")

def villageois_chevaux(text):
    print("\n    🟨🟨🟨🟨🟨🟨🟨")
    print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
    print("   🏽🏽🏽🏽🏽🏽🏽🏽")
    print(f"   🏽⬜🟩🏽🏽🟩⬜🏽      {Encre.YELLOW}──────────────────────────────────────────────────────────────")
    print(f"   🏽🏽🏽🟫🟫🏽🏽🏽     < Palefrenier Soigneur: {Encre.RESET}" + text + f" .. {Encre.YELLOW}>")
    print(f"   🏽🏽⬛🏽🏽⬛🏽🏽      {Encre.YELLOW}──────────────────────────────────────────────────────────────")
    print(f"{Encre.RESET}   🏽🏽⬛⬛⬛⬛🏽🏽\n")
    
def inventaireAffiche():
    print("\n╔═════════════════════════════════════╗")
    print("║╔══════════════════╗                 ║")
    if personnage['Prenom'] == "steve" or personnage['Prenom'] == "Steve":
        print("║║ ⬛⬛⬛⬛⬛⬛⬛⬛ ║╔═══╦═══╗        ║")
        print("║║ ⬛🏽🏽🏽🏽🏽🏽⬛ ║║   ║   ║   ╔═══╗║")
        print("║║ 🏽🏽🏽🏽🏽🏽🏽🏽 ║╠═══╬═══╣━━▶║   ║║")
        print("║║ 🏽🏽🏽🏽🏽🏽🏽🏽 ║║   ║   ║   ╚═══╝║")
        print("║║ 🏽⬜🟦🏽🏽🟦⬜🏽 ║╚═══╩═══╝        ║")
        print("║║ 🏽🏽🏽🟫🟫🏽🏽🏽 ║                 ║")
        print("║║ 🏽🏽⬛🏽🏽⬛🏽🏽 ║                 ║")
        print("║║ 🏽🏽⬛⬛⬛⬛🏽🏽 ║                 ║")
    elif personnage['Prenom'] == "alex" or personnage['Prenom'] == "Alex":
        print("║║ 🟧🟧🟧🟧🟧🟧🟧🟧 ║╔═══╦═══╗        ║")
        print("║║ 🟧🟧🟧🟧🟧🟧🟧🟧 ║║   ║   ║   ╔═══╗║")
        print("║║ 🟧🟧🟧🟧🏻🏻🟧🟧 ║╠═══╬═══╣━━▶║   ║║")
        print("║║ 🟧🟧🟧🏻🏻🏻🏻🟧 ║║   ║   ║   ╚═══╝║")
        print("║║ 🏻⬜🟩🏻🏻🟩⬜🏻 ║╚═══╩═══╝        ║")
        print("║║ 🏻🏻🏻🏻🏻🏻🏻🏻 ║                 ║")
        print("║║ 🏻🏻🏻🟪🟪🏻🏻🏻 ║                 ║")
        print("║║ 🏻🏻🏻🏻🏻🏻🏻🏻 ║                 ║")
    elif personnage['Prenom'] == "notch" or personnage['Prenom'] == "Notch":
        print("║║ 🟧🟧🟧🟧🟧🟧🟧🟧 ║╔═══╦═══╗        ║")
        print("║║ 🟧🏽🏽🏽🏽🏽🏽🟧 ║║   ║   ║   ╔═══╗║")
        print("║║ 🟧🏽🏽🏽🏽🏽🏽🟧 ║╠═══╬═══╣━━▶║   ║║")
        print("║║ 🏽🏽🏽🏽🏽🏽🏽🏽 ║║   ║   ║   ╚═══╝║")
        print("║║ 🏽⬜🟧🏽🏽🟧⬜🏽 ║╚═══╩═══╝        ║")
        print("║║ 🏽🏽🏽🟫🟫🏽🏽🏽 ║                 ║")
        print("║║ 🏽🏽⬛🏽🏽⬛🏽🏽 ║                 ║")
        print("║║ 🏽🏽⬛⬛⬛⬛🏽🏽 ║                 ║")
    print("║╚══════════════════╝                 ║")
    print("║╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗║")
    output = "║║"
    if plats_stock.get("carotte") and plats_stock["carotte"] > 0:
        output += "🥕" + str(plats_stock["carotte"]) + "║"
    else:
        output += "   " + "║"
    if plats_stock.get("melon") and plats_stock["melon"] > 0:
        output += "🍉" + str(plats_stock["melon"]) + "║"
    else:
        output += "   " + "║"
    if plats_stock.get("cookie") and plats_stock["cookie"] > 0:
        output += "🍪" + str(plats_stock["cookie"]) + "║"
    else:
        output += "   " + "║"
    if plats_stock.get("pomme") and plats_stock["pomme"] > 0:
        output += "🍎" + str(plats_stock["pomme"]) + "║"
    else:
        output += "   " + "║"
    if plats_stock.get("steak") and plats_stock["steak"] > 0:
        output += "🥩" + str(plats_stock["steak"]) + "║"
    else:
        output += "   " + "║"
    output += "   ║   ║   ║   ║║"
    print(output)
    # print("║║🥕" + plats_stock.get("carotte") + "║🍉" + plats_stock.get("melon") + "║🍪" + plats_stock.get("cookie") + "║🍎" + plats_stock.get("pomme") + "║🥩"+plats_stock.get("steak") + "║   ║   ║   ║   ║║")
    print("║╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣║")
    print("║║   ║   ║   ║   ║   ║   ║   ║   ║   ║║")
    print("║╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣║")
    print("║║   ║   ║   ║   ║   ║   ║   ║   ║   ║║")
    print("║╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝║")
    print("║╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗║")
    # print("║║💎1║🗝 1║   ║   ║   ║   ║   ║   ║   ║║")
    output = "║║"
    if inventaire.get("cleCoffre") and inventaire["cleCoffre"] > 0:
        output += "🗝 " + str(inventaire["cleCoffre"]) + "║"
    else:
        output += "   " + "║"
    if inventaire.get("diamant") and inventaire["diamant"] > 0:
        output += "💎" + str(inventaire["diamant"]) + "║"
    else:
        output += "   " + "║"
    output += "   ║   ║   ║   ║   ║   ║   ║║"
    print(output)
    print("║╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝║")
    print("╚═════════════════════════════════════╝")


# ********************************************************************************
# INTRODUCTION
# ********************************************************************************


def intro():
    mojang()
    print(f"{Encre.YELLOW},----.                                                                                          ,----. ")
    print("|    |                                                                                          |    | ")
    print("|  .-',-----.,-----.                                                                            `-.  | ")
    print("|  |  '-----''-----'                                                                              |  | ")
    print("|  |  ,-----.,-----.                                                                              |  | ")
    print("|  '-.'-----''-----'                                                                            .-'  | ")
    print("|    |                                                                                          |    | ")
    print(f"`----'                                                                                          `----' {Encre.RESET}\n")
    sleep(1)
    mojang()
    print(f"{Encre.YELLOW},----.                                                                                          ,----. ")
    print("|    |                                                                                          |    | ")
    print("|  .-',-----.,-----.,-----.,-----.,-----.,-----.                                                `-.  | ")
    print("|  |  '-----''-----''-----''-----''-----''-----'                                                  |  | ")
    print("|  |  ,-----.,-----.,-----.,-----.,-----.,-----.                                                  |  | ")
    print("|  '-.'-----''-----''-----''-----''-----''-----'                                                .-'  | ")
    print("|    |                                                                                          |    | ")
    print(f"`----'                                                                                          `----' {Encre.RESET}\n")
    sleep(1)
    mojang()
    print(f"{Encre.YELLOW},----.                                                                                          ,----. ")
    print("|    |                                                                                          |    | ")
    print("|  .-',-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.                    `-.  | ")
    print("|  |  '-----''-----''-----''-----''-----''-----''-----''-----''-----''-----'                      |  | ")
    print("|  |  ,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.                      |  | ")
    print("|  '-.'-----''-----''-----''-----''-----''-----''-----''-----''-----''-----'                    .-'  | ")
    print("|    |                                                                                          |    | ")
    print(f"`----'                                                                                          `----' {Encre.RESET}\n")
    sleep(1)
    mojang()
    print(f"{Encre.YELLOW},----.                                                                                          ,----. ")
    print("|    |                                                                                          |    | ")
    print("|  .-',-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,----.`-.  | ")
    print("|  |  '-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''----'  |  | ")
    print("|  |  ,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,----.  |  | ")
    print("|  '-.'-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''----'.-'  | ")
    print("|    |                                                                                          |    | ")
    print(f"`----'                                                                                          `----' {Encre.RESET}\n")
    sleep(1)
    mojang()
    print(f"{Encre.YELLOW},----.                                                                                          ,----. ")
    print("|    |                                                                                          |    | ")
    print("|  .-',-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,----.`-.  | ")
    print("|  |  '-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''----'  |  | ")
    print("|  |                                    EN COURS DE CHARGEMENT                                 |  | ")
    print("|  |  ,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,-----.,----.  |  | ")
    print("|  '-.'-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''-----''----'.-'  | ")
    print("|    |                                                                                          |    | ")
    print(f"`----'                                                                                          `----' {Encre.RESET}\n")
    sleep(2)
    minecraft()

    typingPrint("Pour spawn dans le Village des Merveilles, tu dois créer ton personnage !\n")
    typingPrint("Commence par choisir déjà ton skin !\n")
    sleep(1)
    alex()
    print(f"   : {Encre.BLUE}Alex{Encre.RESET}\n")
    steve()
    print(f"   : {Encre.BLUE}Steve{Encre.RESET}\n")
    typingPrint("\n■ Quel personnage es-tu ? ")
    prenom = str(input("► ")).lower()
    if prenom == "alex" or prenom == "steve":
        personnage ["Prenom"] = prenom
    else:
        personnage ["Prenom"] = "notch"
        typingPrint(f"\nCe prénom correspond à aucun des personnages, tu seras donc {Encre.BLUE}Notch{Encre.RESET} !\n")
        sleep(1)

    typingPrint(f"\n■ Quelle est la version de ton launcher ? {Encre.BLUE}Entre 1.7.X & 1.19.X{Encre.RESET} ")
    try:
        version = float(input("► "))
        if version < 1 or version > 2:
            raise ValueError(f"{Encre.RED}Version hors limite{Encre.RESET}")
        personnage["Version"] = version
    except ValueError as e:
        print(f"\nCette version n'est pas compatible au jeu. Tu seras à la version par défaut en {Encre.BLUE}1.8 {Encre.RESET}!")
        personnage["Version"] = 1.8
        sleep(1)



    # Afficher la liste des items et choisir une
    print("\nVoici les différents items enchantés !\n")
    for index, alter in enumerate (items):
        print(f"{Encre.BLUE}N°{Encre.YELLOW}{index+1} {Encre.BLUE}: {Encre.BLUE}{alter}{Encre.RESET}")
        # print(f"Item enchanté n°{index+1} : {alter}")

    sleep(0.5)
    typingPrint("\n■ Quel item enchanté souhaites-tu avoir ? ")
    # Si le joueur ne fait pas un choix qui est dans la liste alors on lui en donne un au hasard
    try:
        items_choisi = int(input("► Choix n° : "))
        if items_choisi < 1 or items_choisi > len(items):
            raise ValueError
        personnage["Item enchanté"] = items[items_choisi-1]
    except ValueError:
        personnage["Item enchanté"] = random.choice(items)
    sleep(0.3)
    minecraft()
    typingPrint(f"{Encre.UNDERLINE}Voici ton personnage ! :{Encre.RESET}\n")
    sleep(0.3)

    if prenom == "alex":
        alex()
    elif prenom == "steve":
        steve()
    else:
        notch()

    for key,value in personnage.items():
        print(f"{key} : {Encre.BLUE}{value}{Encre.RESET}")

    sleep(2)
    typingPrint(f"\n{Encre.UNDERLINE}Téléportation dans le Village des Merveilles dans 5..")
    sleep(1)
    typingPrint("4..")
    sleep(1)
    typingPrint("3..")
    sleep(1)
    typingPrint("2..")
    sleep(1)
    typingPrint(f"1..{Encre.RESET}")
    sleep(1)
    lieu_place_village()



# ********************************************************************************
# ACCUEIL
# ********************************************************************************


def lieu_place_village():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es dans sur la Place du Village des Merveilles.\n")
    sleep(1)
    while True:
        print("\n┌────────────────────────────────────────")
        proposer_actions(["(O) pour: Observer 👁", "(E) pour: Inventaire 🎒", "(P) pour: Déconnecter ⛩"])
        proposer_lieux(["Au comptoir du villageois", "Premier Étage ∆", "Écurie à chevaux"])
        reponse = input("├─> ").lower() 
        print("└────────────────────────────────────────")

        if reponse == "deconnecter" or reponse == "déconnecter" or reponse == "p":
            exit()
        elif reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Une grande entrée en pierre avec des torches lumineuses sur les murs et un comptoir d'accueil en bois avec un villageois derrière.\n")

        elif reponse == "inventaire" or reponse == "e":
            inventaireAffiche()
        
        elif reponse == "1":
            lieu_comptoir()

        elif reponse == "2":
            lieu_premier_etage()

        elif reponse == "3":
            lieu_ecurie()


def lieu_ecurie():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es dans l'écurie à chevaux du Village des Merveilles.\n")
    sleep(1)   
    while True:
        print("\n┌────────────────────────────────────────")
        if okay_chevaux == False:
            proposer_actions(["(O) pour: Observer 👁", "(C) pour: Caresser le cheval", "(E) pour: Inventaire 🎒"])
        else:
            proposer_actions(["(O) pour: Observer 👁", "(E) pour: Inventaire 🎒"])
        proposer_lieux(["Retour à la Place du Village"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Tu es dans une écurie avec 5 chevaux blancs et un cheval noir. Il y a une forte odeur de foin.\n")
            typingPrint(f"👁 Le palefrenier soigneur s'occupe de ses chevaux et te regarde de loin en même temps.\n")

        elif reponse == "cheval" or reponse == "c":
            if okay_chevaux == False:
                cheval_approche()
        elif reponse == "inventaire" or reponse == "e":
            inventaireAffiche()
        elif reponse == "1":
            lieu_place_village()

def cheval_approche():
    minecraft()
    mapLocalisation()
    print("∇ Tu es devant un cheval noir placé à côté d'un chariot de foin.\n")
    sleep(1)    
    villageois_chevaux("Salut ! Fais attention à ce cheval, il peut être agressif des fois !")
    sleep(3)
    skin("Oh ! Merci de m'avoir prévenu !")
    sleep(4)
    villageois_chevaux("Pas de soucis ! As-tu quelques instants pour m'aider s'il te plait ?")
    while True:
        print("\n┌────────────────────────────────────────")
        proposer_actions(["(O) pour: Oui ✅", "(N) pour: Non 🚫"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")
        if reponse == "oui" or reponse == "o":
            skin("Euhh oui, dites-moi ? Qu'est ce que je peux faire ?")
            sleep(2)
            villageois_chevaux("Génial !")
            sleep(2)
            villageois_chevaux("La semaine dernière, nous avions fait une course de chevaux")
            sleep(3)
            villageois_chevaux("Notre cheval noir a aisement gagné !")
            sleep(3)
            villageois_chevaux("J'ai malheuresement perdu sa médaille.. je suspecte qu'il soit dans le foin !")
            sleep(4)
            skin("Ah ! C'est très dommage, vous n'avez pas de chance")
            sleep(3)
            villageois_chevaux("Peux-tu fouiller dedans pour essayer de le retrouver ? Tu ne partiras pas les mains vides d'ici si tu peux m'aider !")
            sleep(4)
            skin("Cela me parait comme un jeu d'enfant, je vais voir ça !")
            sleep(1.5)
            while True:
                print("\n┌────────────────────────────────────────")
                proposer_actions(["(S) pour: Sauter dans le foin 🍂 "])
                reponse = input("├─> ").lower()
                print("└────────────────────────────────────────")
                if reponse == "sauter" or reponse == "s":
                    minecraft()
                    typingPrint("Tu viens de sauter dans le foin. Fouille fond en comble pour essayer de trouver la médaille.")
                    while True:
                        print("\n┌────────────────────────────────────────")
                        proposer_actions(["(F) pour: Fouiller 🖐"])
                        reponse = input("├─> ").lower()
                        print("└────────────────────────────────────────")
                        if reponse == "fouiller" or reponse == "f":
                            typingPrint("Tu viens de fouiller dans le foin.\n")
                            sleep(1)
                            typingPrint("Il y a une lumière qui tape sur un objet métallique.\n")
                            typingPrint("\nTu peux y jeter un oeil.\n")
                            while True:
                                print("\n┌────────────────────────────────────────")
                                proposer_actions(["(J) pour: Jeter un oeil 👁"])
                                reponse = input("├─> ").lower()
                                print("└────────────────────────────────────────")
                                if reponse == "jeter" or reponse == "j":
                                    skin("Ah ! Je crois avoir trouvé quelque chose par ici !")
                                    sleep(2)
                                    villageois_chevaux("Déjà ? Mais tu as été super rapide ?!")
                                    sleep(2)
                                    skin("Eh oui ! Je vous avais dis que ça allait être un jeu d'enfant")
                                    sleep(2)
                                    typingPrint("Félicitations ! Tu as trouvé la médaille.\n")
                                    sleep(2)
                                    inventaire["diamant"] += 1
                                    global okay_chevaux
                                    okay_chevaux = True
                                    villageois_chevaux(f"Merci bien ! Je reprend notre médaille et je te donne un {Encre.BLUE}diamant 💎{Encre.RESET} pour te remercier ! " + "[" + str(inventaire["diamant"]) + f"/3 💎]")
                                    sleep(3)
                                    while True:
                                        print("\n┌────────────────────────────────────────")
                                        proposer_actions(["(R) pour: Remercier 👌🏼", "(E) pour: Inventaire 🎒"])
                                        reponse = input("├─> ").lower()
                                        print("└────────────────────────────────────────")

                                        if reponse == "remercier" or reponse == "r":
                                            skin("Oh ! Merci bien c'est très sympa de votre part !")
                                            sleep(3)
                                            lieu_ecurie()
                                        elif reponse == "inventaire" or reponse == "e":
                                            inventaireAffiche()

        elif reponse == "non" or reponse == "n":
            skin("Non désolé, je n'ai actuellement pas le temps !")
            sleep(3)
            villageois_chevaux("Oh ! Tempis, je vais essayer de me débrouiller tout seul.")
            sleep(3)
            villageois_chevaux("N'hésite pas à revenir me voir si tu penses pouvoir m'aider !")
            while True:
                print("\n┌────────────────────────────────────────")
                proposer_actions(["(P) pour: Partir ⛩"])
                reponse = input("├─> ").lower()
                print("└────────────────────────────────────────")
                if reponse == "partir" or reponse == "p":
                    skin("Ça marche! Belle journée et bon courage à vous.")
                    sleep(3)
                    lieu_ecurie()


def lieu_comptoir():
    minecraft()
    mapLocalisation()
    print("∇ Tu es devant le comptoir de la Place du Village des Merveilles.\n")
    sleep(1)
    while True:
        print("\n┌────────────────────────────────────────")
        if inventaire["diamant"] >= 3:
            proposer_actions(["(O) pour: Observer 👁", "(M) pour: 🖐💎 Montrer 🖐💎", "(C) pour: Rentrer dans le coffre 🧰","(E) pour: Inventaire 🎒"])
        else:
            proposer_actions(["(O) pour: Observer 👁", "(P) pour: Parler 🗣", "(C) pour: Rentrer dans le coffre 🧰", "(E) pour: Inventaire 🎒"])
        proposer_lieux(["Quitter le comptoir"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Tu es devant le comptoir d'accueil en bois avec derrière un villageois ayant un gros nez.")
            typingPrint(f"👁 Il y a une petite ambiance sympatique avec une musique de fond.\n")

        elif reponse == "parler" or reponse == "montrer" or reponse == "m" or reponse == "p":
            montrer_diams()

        elif reponse == "coffre" or reponse == "c":
            dans_coffre()

        elif reponse == "inventaire" or reponse == "e":
            inventaireAffiche()
        elif reponse == "1":
            lieu_place_village()


def montrer_diams():
    if inventaire["diamant"] >= 3:
        skin("Hello le monsieur au gros nez ! Regarde ce que j'ai dans mes mains !")
        sleep(4)
        villageois(f"Oh mais que vois-je ! Tu as réussi à réunir les {Encre.BLUE}3 diamants {Encre.RESET}💎 de ce village ?!")
        sleep(4)
        villageois("Je ne pensais pas que t'aurais pu les trouver mais tu as été plus doué !")
        sleep(4)
        skin("Eh oui ! J'y ai réussi !")
        sleep(4)
        villageois("Le portail s'ouvrira d'ici peu !")
        sleep(2)
        print("──⬛⬛⬛⬛⬛")
        print("⬛⬛🌫️🌫️🌫️🌫️🌫️🌫️⬛⬛")
        print("⬛🌫️🌫️🟪🟪🌫️🌫️🌫️🌫️⬛")
        print("⬛🌫️🟪🌫️🌫️🌫️🌫️🌫️🌫️🌫️⬛")
        print("⬛🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️⬛")
        print("⬛🌫️🌫️🌫️🌫️🟪🟪🌫️🌫️⬛")
        print("⬛🌫️🌫️🌫️🟪🌫️🌫️🟪🌫️⬛                 Ouverture du portail du Aether en cours..")
        print("⬛🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️🌫️⬛")
        print("⬛🌫️🟪🌫️🌫️🌫️🌫️🌫️🌫️🌫️⬛")
        print("⬛🌫️🟪🌫️🌫️🟪🌫️🌫️🌫️⬛")
        print("⬛🌫️🌫️🟪🌫️🌫️🌫️🌫️🌫️🌫️⬛")
        print("⬛⬛🌫️🌫️🌫️🌫️🌫️⬛⬛")
        print("──⬛⬛⬛⬛⬛\n")
        sleep(2)
        skin("Oui je le vois ! Merci et aurevoir le monsieur au gros nez !")
        sleep(3)
        villageois("Aurevoir " + personnage['Prenom'] + " !")
        sleep(2)
        typingPrint(f"Félicitations, vous avez réuni suffisamment de {Encre.BLUE}diamants 💎 {Encre.RESET}pour ouvrir le portail du Aether !")
        sleep(2) 
        while True:
            print("\n┌────────────────────────────────────────")
            proposer_actions(["(P) pour: Portail ✨", "(S) pour: Suicide 🥀"])
            reponse = input("├─> ").lower()
            print("└────────────────────────────────────────")

            if reponse == "portail" or reponse == "p":
                mojang()
                print("➖➖🟫🟫🟫🟫🟫")
                print("➖🟫🟨🟨🟨🟨🟨🟫")
                print("➖🟫🟨⬜⬜🟨🟨🟫")
                print("➖🟫🟧🟧🟨🟧🟧🟫")
                print("➖🟫⬜🟩🟧⬜🟩🟫")
                print("➖🟫🟩🟩⬜🟩🟩🟫")
                print("➖🟫🟧🟧🟨🟧🟧🟫                  " + personnage['Prenom'] + " à terminé le jeu.")
                print("🟫🟫🟫🟧🟨🟧🟫🟫🟫")
                print("🟫🟨🟫🟫🟧🟫🟫🟨🟫")
                print("➖🟫🟨⬜🟨🟨🟨🟫")
                print("➖🟫🟫🟫🟫🟫🟫🟫")
                print("➖➖🟫🟨🟨🟨🟫")
                print("➖➖➖🟫🟫🟫")
                typingPrint(f"Bien joué à toi petit bg.")
                exit()
            elif reponse == "suicide" or reponse == "s":
                mojang()
                typingPrint(personnage['Prenom'] + " s'est suicidé 🥀.\n")
                typingPrint(f"Fin du jeu.")
                exit()

    else:
        skin("Bonjour Monsieur !")
        sleep(2)
        villageois(f"Bonjour ! Bienvenue au village.")
        sleep(1)
        villageois(f"N'hésite pas à venir me voir lorsque t'auras {Encre.BLUE}3 diamants{Encre.RESET} 💎 !" + "[" + str(inventaire["diamant"]) + f"/3 💎]")
        sleep(2)
        while True:
            print("\n┌────────────────────────────────────────")
            proposer_actions(["(P) pour: Partir ⛩", "(I) pour: Informations 💎"])
            reponse = input("├─> ").lower()
            print("└────────────────────────────────────────")
            if reponse == "partir" or reponse == "p":
                skin("Ca marche ! Je vais voir ça.")
                sleep(2)
                lieu_comptoir()
            elif reponse == "informations" or reponse == "information" or reponse == "i":
                skin("Comment ça ? Pouvez-vous me donnez plus d'informations s'il vous plait ?")
                sleep(2)
                villageois("Ahah ! Ca se voit que tu es nouveau !")
                sleep(2)
                villageois("Tu comprendras de toi même lorsque tu te baladera dans le Village des Merveilles !")
                sleep(2)
                while True:
                    print("\n┌────────────────────────────────────────")
                    proposer_actions(["(R) pour: Remercier 👌🏼"])
                    reponse = input("├─> ").lower()
                    print("└────────────────────────────────────────")

                    if reponse == "remercier" or reponse == "r":
                        skin("Ca marche ! Je vais voir ça.")
                        sleep(2)
                        lieu_comptoir()

def dans_coffre():
    global okay_coffre_ouvert
    if inventaire["cleCoffre"] >= 1 and okay_coffre_ouvert == False:
        inventaire["cleCoffre"] -= 1
        inventaire["diamant"] += 1
        okay_coffre_ouvert = True
        villageois("Que fais-tu ici avec ma clé 🗝 dans t'es mains ?! N'as-tu pas honte ?")
        sleep(4)
        villageois("Bon, je sais pas quel était ton but mais je reprends ma clé 🗝 ! Merci bien !")
        sleep(4)
        villageois(f"Je suis pas méchant, je te donne un {Encre.BLUE}diamant{Encre.RESET} [" + str(inventaire["diamant"]) + "/3 💎] pour quand même te remercier !")
        sleep(4)
        typingPrint("Ouf ! Heureusement qu'il a été sympatique quand même !\n")
        typingPrint(f"Tu repars avec un {Encre.BLUE}diamant{Encre.RESET} 💎 dans ton inventaire ! " + "[" + str(inventaire["diamant"]) + "/3 💎]")
        while True:
            print("\n┌────────────────────────────────────────")
            proposer_actions(["(R) pour: Remercier 👌🏼", "(E) pour: Inventaire 🎒"])
            reponse = input("├─> ").lower()
            print("└────────────────────────────────────────")

            if reponse == "remercier" or reponse == "r":
                skin("Merci beaucoup ! Désolé quand même..")
                sleep(2)
                lieu_place_village()
            elif reponse == "inventaire" or reponse == "e":
                inventaireAffiche()
            
    else:
        villageois("Eh ! Mais est-ce que tu es un imbécile ? Ta essayé de rentrer dans un coffre avec ton gros corps là ?")
        sleep(3)
        villageois("Bref ! Tu n'as pas le droit de rentrer dans ce coffre !")
        sleep(3)
        while True:
            print("\n┌────────────────────────────────────────")
            proposer_actions(["(P) pour: Se pardonner 👐", "(F) pour: Fuir 🏃"])
            reponse = input("├─> ").lower()
            print("└────────────────────────────────────────")

            if reponse == "pardonner" or reponse == "p":
                skin("Excusez-moi, cela n'arrivera plus !")
                sleep(3)
                villageois("Je te pardonne pour cette fois ! D'ailleurs, avant que je te retourne derrière le comptoir,")
                sleep(3)
                villageois(f"Reviens me voir lorsque t'auras t'es {Encre.BLUE}3 diamants{Encre.RESET} 💎 !")
                sleep(4)
                lieu_place_village()
                
            elif reponse == "fuir" or reponse == "f":
                villageois("Ehhhh ! Où tu vas ?! Je vais te rattraper tu verras !")
                sleep(3)
                villageois(f"Si la prochaine fois tu n'as pas t'es {Encre.BLUE}3 diamants{Encre.RESET} 💎, tu verras toi !")
                sleep(4)
                typingPrint("💢 Tu viens de fuir au premier étage pour t'échapper du villegeois ! Il sera très enervé la prochaine fois que tu le verras...\n")
                sleep(3)
                lieu_premier_etage()

# ********************************************************************************
# PREMIER ETAGE
# ********************************************************************************

def lieu_premier_etage():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es au premier étage du batiment.\n")
    sleep(1)

    while True:
        print("\n┌────────────────────────────────────────")
        proposer_actions(["(O) pour: Observer 👁", "(E) pour: Inventaire 🎒"])
        proposer_lieux(["Descendre à la Place du Village ∇", "Deuxième étage ∆", "Bibliothèque", "Caféteria"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Des couloirs très spaciaux menant à des salles privées et des pièces communes pour les habitants du village.\n")
            typingPrint(f"👁 Des fenêtres pour laisser entrer la lumière naturelle et des lanternes pour éclairer les couloirs la nuit.\n")

        elif reponse == "inventaire" or reponse == "e":
            inventaireAffiche()
        elif reponse == "1":
            lieu_place_village()
        elif reponse == "2":
            lieu_deuxieme_etage()
        elif reponse == "3":
            bibliotheque()
        elif reponse == "4":
            cafeteria()


def cafeteria():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es dans la caféteria du premier étage.\n")
    sleep(1)

    while True:
        print("\n┌────────────────────────────────────────")
        proposer_actions(["(O) pour: Observer 👁", "(E) pour: Manger 🍎"])
        proposer_lieux(["Retour au Premier étage ◄"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "quitter":
            lieu_place_village()
        if reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Il y a des tables pour manger et un comptoir en bloc de quartz pour commander de la nourriture.")
            typingPrint(f"👁 Il y a également des fenêtres pour laisser entrer la lumière naturelle et des lanternes pour éclairer l'espace la nuit.\n")
        
        if reponse == "1":
            lieu_premier_etage()

        elif reponse == "manger" or reponse == "e": 
            inventaireAffiche()
            for key,value in plats_stock.items():
                print(f"Il te reste {value} : {key}")
            typingPrint("\n■ Quel plat veux-tu manger ? ")
            plat_mange = str(input("► ")).lower()
            if plat_mange in plats_stock and plats_stock[plat_mange] > 0:
                plats_stock[plat_mange] -= 1
                personnage ["Coeur ♥"] = personnage ["Coeur ♥"] + 10
                typingPrint("\nHmmm délicieux ! Tu viens de manger 1 " + plat_mange + " !\n")
                typingPrint(f"Tu as désormais " + str(personnage["Coeur ♥"]) + " ♥.")
                sleep(1)
            else:
                cafeteria
                sleep(0.5)
                print("Désolé, ce plat n'est plus disponible.")

def bibliotheque():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es dans la bibliothèque du premier étage.\n")
    sleep(1)

    while True:
        print("\n┌────────────────────────────────────────")
        proposer_actions(["(O) pour: Observer 👁", "(L) pour: Lire 📜", "(E) pour: Inventaire 🎒"])
        proposer_lieux(["Retour au Premier étage ◄"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "observer" or reponse == "o":
            bibliotheque_libraire()

        if reponse == "lire" or reponse == "l":
            print(f"{Encre.YELLOW}    __________________   __________________")
            print(".-/|                  \ /                  |\-.")
            print("||||  Le secret des    |                   ||||")
            print("||||     diams 💎      |       ~~*~~       ||||")
            print("||||      ~~*~~        |                   ||||")
            print("||||                   |                   ||||")
            print("|||| La personne ayant |  Il doit aller    ||||")
            print("|||| trouver les 3     |  voir le villag-  ||||")
            print(f"|||| {Encre.BLUE}diamants{Encre.YELLOW} dans ce  |  -eois principal  ||||")
            print("|||| village, pourra   |  du village !     ||||")
            print("|||| ouvrir le portail |                   ||||")
            print("||||     du Aether     |                   ||||")
            print("||||                   |                   ||||")
            print("||||__________________ | __________________||||")
            print("||/===================\|/===================\||")
            print(f"`--------------------~___~-------------------''{Encre.RESET}")

        elif reponse == "1":
            lieu_premier_etage()

        elif reponse == "inventaire" or reponse == "e":
            inventaireAffiche()

def bibliotheque_libraire():
    typingPrint("\n👁 Tu es dans bibliothèque, avec une table d'enchantement et des enclumes au fond de la salle.\n")
    global okay_cle
    if okay_cle == False:
        typingPrint(f"👁 Il y a un villagois libraire qui y travaille qui te regarde de loin.")
    else:
        typingPrint(f"\n👁 Il y a plus personne dans la bibliothèque.\n")
        sleep(3)
    while True:
        print("\n┌────────────────────────────────────────")
        if okay_cle == False:
            proposer_actions(["(O) pour: Observer 👁", "(P) pour: Parler 🗣 "])
        else:
            bibliotheque()
        proposer_lieux(["Retour au Premier étage ◄"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "1":
            lieu_premier_etage()
        if reponse == "observer" or reponse == "o":
            bibliotheque_libraire()

        elif reponse == "parler" or reponse == "p" and okay_cle == False:
            minecraft()
            inventaire["cleCoffre"] += 1
            okay_cle = True
            villageois_libraire("Salut " + personnage['Prenom'] + " ! Heureusement que t'es venu. J'ai fait une petite bêtise et j'aurai besoin de toi")
            sleep(4)
            villageois_libraire("J'ai volé la clé 🗝  du coffre du villegeois de l'accueil, j'ai peur de la redéposer à son endroit !")
            sleep(4)
            skin("Et donc ? Que veux-tu que j'y fasse ?")
            sleep(4)
            villageois_libraire("Bah en fait, je vais te donner et te téléporter à la place du Village où tu trouveras le coffre !")       
            sleep(4)
            typingPrint('\nLe libraire vient de te donner sa clé 🗝 ! Il va te téléporter à la Place du Village, tu pourras fouiller le coffre du villageois!\n')
            sleep(2)
            while True:
                print("\n┌────────────────────────────────────────")
                proposer_actions(["(R) pour: Remercier 👌🏼", "(E) pour: Inventaire 🎒"])
                reponse = input("├─> ").lower()
                print("└────────────────────────────────────────")

                if reponse == "remercier" or reponse == "r":
                    skin("Ça marche ! Je vais faire de mon mieux pour rester discret.")
                    sleep(3)
                    lieu_place_village()
                elif reponse == "inventaire" or reponse == "e":
                    inventaireAffiche()

# ********************************************************************************
# DEUXIEME ETAGE
# ********************************************************************************

def lieu_deuxieme_etage():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es au deuxième étage du batiment.\n")
    sleep(1)

    while True:
        print("\n┌────────────────────────────────────────")
        proposer_actions(["(O) pour: Observer 👁","(D) pour: Écouter 👂" ,"(E) pour: Inventaire 🎒"])
        proposer_lieux(["Descendre au Premier étage ∇", "Ferme à XP de Creeper 🔰"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Cet étage est dédié l'entraînement des héros du Village. Un grand espace sombre construit en cobblestone et des lanternes partout avec des portraits de certains héros du village.")
            typingPrint(f"\n👁 Il y aurait des portes qui mènent aux entraînement, des portes pour les zones de repos et une grande ferme à XP de Creeper.")
            typingPrint(f"\n👁 Tu peux écouter à travers les portes ce qu'il se passe à l'intérieur.\n")

        elif reponse == "écouter" or reponse == "ecouter" or reponse == "d":
            typingPrint("\n👂 À la porte de gauche, t'entends le bruit des épées se taper entre elles. Surement des héros du Village des Merveilles qui s'entrainent")
            typingPrint(f"\n👂 À la porte de droite, t'entends les bruits des Creepers en train d'être exécuté dans des pièges. {Encre.UNDERLINE}La serrure de la porte semble être ouverte.{Encre.RESET}\n")

        elif reponse == "inventaire" or reponse == "e":
            inventaireAffiche()
        elif reponse == "1":
            lieu_premier_etage()

        elif reponse == "2":
            lieu_ferme_xp_creeper()


def lieu_ferme_xp_creeper():
    minecraft()
    mapLocalisation()
    typingPrint("∇ Tu es dans la ferme à XP de Creeper !\n")
    sleep(1)

    while True:
        print("\n┌────────────────────────────────────────")
        global okay_creeper_combat
        if okay_creeper_combat == False:
            proposer_actions(["(O) pour: Observer 👁","(F) pour: Farmer 🔰"])
        else:
            proposer_actions(["(O) pour: Observer 👁"])
        proposer_lieux(["Retour au Deuxieme étage ◄"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")

        if reponse == "1":
            lieu_deuxieme_etage()

        if reponse == "observer" or reponse == "o":
            typingPrint("\n👁 Une zone en cobblestone dédiée à la collecte de l'XP des creepers. Il y a des pièges pour les creepers, des zones de récupération d'XP et des zones de stockage pour des items.\n")
        
        if reponse == "1":
            lieu_premier_etage()

        elif reponse == "farmer" or reponse == "f" and okay_creeper_combat == False:
            compteur_frappe = 0
            creeper["Coeur ♥"]=50
            minecraft()
            mapLocalisation()
            typingPrint("∇ Tu es rentrer dans l'endroit pour farmer les XP de Creeper ! Attention, c'est une zone dangereuse\n")
            sleep(1.5)
            print("\n───⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
            print("───⬛🟩⬜🟩🟩🟩⬜🟩🟩🟩🟩⬛")
            print("───⬛🟩⬜🟩🟩🟩⬜🟩🟩🟩🟩⬛")
            print("───⬛🟩🟩⬛⬛🟩⬛⬛⬛🟩🟩⬛")
            print("───⬛🟩🟩⬛⬛⬜🟩⬛⬛🟩⬛⬛")
            print("───⬛🟩🟩🟩🟩⬛⬛🟩🟩⬛⬛⬛")
            print("───⬛⬜⬛🟩⬛⬛⬛⬛🟩🟩⬛⬛")
            print("───⬛🟩🟩🟩⬛⬛⬛⬛🟩⬛⬛⬛")
            print(f"───⬛🟩🟩🟩⬛🟩🟩⬛🟩🟩⬛⬛           {Encre.RED}Un creeper sauvage est sorti de son piège ! Attention !{Encre.RESET}")
            print("───⬛⬛🟩🟩🟩🟩🟩🟩🟩⬜🟩⬛")
            print("───⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
            print("─────⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛")
            print("─────⬛⬜⬛🟩🟩🟩🟩🟩🟩⬛")
            print("─────⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛")
            print("─────⬛🟩🟩⬜🟩🟩🟩🟩🟩⬛")
            print("─────⬛⬛🟩🟩🟩🟩🟩⬛⬜⬛")
            print("─────⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛")
            print("─────⬛🟩🟩🟩🟩🟩🟩⬛🟩⬛")
            print("─────⬛⬛🟩🟩⬜🟩🟩🟩🟩⬛")
            print("─────⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛")
            print("⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛")
            print("⬛⬛🟩🟩🟩⬛🟩🟩🟩🟩⬛⬜🟩🟩⬛⬛")
            print("⬛⬜🟩⬛🟩⬛🟩🟩🟩🟩⬛🟩🟩🟩🟩⬛")
            print("⬛🟩🟩🟩🟩⬛🟩🟩🟩🟩⬛🟩🟩🟩🟩⬛")
            print("⬛⬛🟩⬛🟩⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬛")
            print("⬛⬛⬛⬛⬛⬛──────⬛⬛⬛⬛⬛⬛\n")
            sleep(2)
            typingPrint("Il va falloir sortir les coups et l'item magique pour survivre !\n")
            sleep(2)
            while personnage["Coeur ♥"] > 0 and creeper ["Coeur ♥"] > 0:
                creeperCombat()
                if compteur_frappe >= 2:
                    sleep(1)
                    personnage["Coeur ♥"] = personnage["Coeur ♥"]-30
                    if compteur_frappe >= 3:
                        personnage["Coeur ♥"] = personnage["Coeur ♥"]-45
                    creeperAttaqueSkin()
                    typingPrint("Le creeper t'a balancé une TNT ! Il te reste plus beaucoup de coeurs ♥ !\n")
                    sleep(1.5)
                    print("\n┌───===================================ж")
                    proposer_actions(["(F) pour: Frapper 🗡", "(M) pour: 🔮 Item magique 🔮", "(P) pour: Fuir 🏃"])
                else:
                    print("\n┌───===================================ж")
                    proposer_actions(["(F) pour: Frapper 🗡", "(P) pour: Fuir 🏃"])
                reponse = str(input("├─ж ")).lower()

                if reponse == "frapper" or reponse == "f":
                    sleep(0.5)
                    creeper["Coeur ♥"] = creeper["Coeur ♥"]-15
                    personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                    compteur_frappe += 1
                elif reponse == "fuir" or reponse == "p":
                    typingPrint("Tu es en train de courir vers le deuxième étage pour t'échapper du Creeper !\n")
                    sleep(2)
                    lieu_deuxieme_etage()

                elif reponse == "item magique" or reponse == "item" or reponse == "m":
                    if compteur_frappe >= 2:
                        if personnage["Item enchanté"].startswith("Plume aiguisé"):
                            creeper["Coeur ♥"] = creeper["Coeur ♥"]-50
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé la Plume aiguisé, tu as contrôlé la gravité et attaqué le Creeper !\n")
                        elif personnage["Item enchanté"].startswith("Oeil d'Enderman"):
                            creeper["Coeur ♥"] = creeper["Coeur ♥"]-50
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé l'Oeil d'Enderman, tu t'es téléporté derrière le Creeper et découpé depuis son cou !\n")
                        elif personnage["Item enchanté"].startswith("Bloc d'obsidienne"):
                            creeper["Coeur ♥"] = 0
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé le Bloc d'obsidienne, tu as envoyé le Creeper en enfer !\n")
                        elif personnage["Item enchanté"].startswith("Baton de Blaze"):
                            creeper["Coeur ♥"] = creeper["Coeur ♥"]-50
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé le Baton de Blaze, tu as contrôlé le feu et attaqué le Creeper !\n")
                        elif personnage["Item enchanté"].startswith("Boule de neige"):
                            creeper["Coeur ♥"] = creeper["Coeur ♥"]-50
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé la Boule de neige, tu as contrôlé le froid et attaqué le Creeper !\n")
                        elif personnage["Item enchanté"].startswith("Poudre de canon"):
                            creeper["Coeur ♥"] = 0
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé la Poudre de canon, tu as fait exploser le Creeper !\n")
                        elif personnage["Item enchanté"].startswith("Hâche en or"):
                            creeper["Coeur ♥"] = 0
                            personnage["Coeur ♥"] = personnage["Coeur ♥"]-10
                            skinAttaqueCreeper()
                            typingPrint("ж Tu as utilisé la Hâche en or, tu as découpé le Creeper en 2 !\n")
                        else:
                            typingPrint("ж Tu n'as pas d'item enchanté utilisable.")

            if personnage["Coeur ♥"]<=0:
                    sleep(1)
                    print(f"{Encre.RED}───⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
                    print("───⬛🟩⬜🟩🟩🟩⬜🟩🟩🟩🟩⬛")
                    print("───⬛🟩⬜🟩🟩🟩⬜🟩🟩🟩🟩⬛")
                    print("───⬛🟩🟩⬛⬛🟩⬛⬛⬛🟩🟩⬛")
                    print("───⬛🟩🟩⬛⬛⬜🟩⬛⬛🟩⬛⬛")
                    print("───⬛🟩🟩🟩🟩⬛⬛🟩🟩⬛⬛⬛")
                    print("───⬛⬜⬛🟩⬛⬛⬛⬛🟩🟩⬛⬛")
                    print("───⬛🟩🟩🟩⬛⬛⬛⬛🟩⬛⬛⬛")
                    print("───⬛🟩🟩🟩⬛🟩🟩⬛🟩🟩⬛⬛")
                    print("───⬛🟩🟩⬛🟩🟩🟩⬜🟩⬛🟩⬛")
                    print("───⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
                    print("─────⬛🟩🟩🟩🟩🟩🟩🟩⬛⬛")
                    print("─────⬛⬜⬛🟩🟩🟩🟩🟩🟩⬛                         Tu as perdu !")
                    print("─────⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛")
                    print("─────⬛🟩🟩⬜🟩🟩🟩🟩🟩⬛           .______     ______     ______   .___  ___.")
                    print("─────⬛⬛🟩🟩🟩🟩🟩⬛⬜⬛           |   _  \   /  __  \   /  __  \  |   \/   | ")
                    print("─────⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛           |  |_)  | |  |  |  | |  |  |  | |  \  /  | ")
                    print("─────⬛🟩🟩🟩🟩🟩🟩⬛🟩⬛           |   _  <  |  |  |  | |  |  |  | |  |\/|  | ")
                    print("─────⬛⬛🟩🟩⬜🟩🟩🟩🟩⬛           |  |_)  | |  `--'  | |  `--'  | |  |  |  | ")
                    print("─────⬛🟩🟩🟩🟩🟩🟩🟩🟩⬛           |______/   \______/   \______/  |__|  |__| ")
                    print("⬛⬛⬛⬛⬛⬛🟩🟩🟩🟩⬛⬛⬛⬛⬛⬛")
                    print("⬛⬛🟩🟩🟩⬛🟩🟩🟩🟩⬛⬜🟩🟩⬛⬛")
                    print("⬛⬜🟩⬛🟩⬛🟩🟩🟩🟩⬛🟩🟩🟩🟩⬛")
                    print("⬛🟩🟩🟩🟩⬛🟩🟩🟩🟩⬛🟩🟩🟩🟩⬛")
                    print("⬛⬛🟩⬛🟩⬛⬛⬛⬛⬛⬛⬛⬜⬛⬜⬛")
                    print(f"⬛⬛⬛⬛⬛⬛──────⬛⬛⬛⬛⬛⬛{Encre.RESET}\n")
                    exit()

            elif creeper["Coeur ♥"]<=0:
                sleep(1)
                minecraft()
                okay_creeper_combat = True
                inventaire["diamant"] += 1
                print(f"{Encre.BLUE}───────⬛⬛⬛⬛")
                print("─────⬛⬜⬜⬜⬜⬛")
                print("────⬛🟦🟦🟦🟦🟦⬜⬛")
                print("────⬛🟦🟦🟦🟦🟦⬜⬛⬛")
                print("──⬛⬛🟦🟦🟦🟦🟦🟦⬜⬛")
                print("──⬛🟦⬛🟦🟦🟦🟦🟦⬜⬛⬛      Tu as battus le Creeper !")
                print("⬛🟦🟦⬛🟦🟦🟦🟦🟦🟦⬜⬛     __          _______ _   _ ")
                print("⬛🟦⬛🟦🟦🟦🟦🟦🟦🟦⬜⬛     \ \        / /_   _| \ | |")
                print("⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛      \ \  /\  / /  | | |  \| |")
                print("──⬛🟦🟦⬛⬛⬛⬛🟦🟦⬛         \ \/  \/ /   | | | . ` |")
                print("──⬛🟦⬛🟦🟦🟦🟦⬛🟦⬛          \  /\  /   _| |_| |\  |")
                print("───⬛⬛🟦🟦🟦🟦⬛⬛⬛            \/  \/   |_____|_| \_|")
                print("────⬛⬛🟦🟦🟦🟦⬛⬛")
                print(f"────────⬛⬛⬛⬛{Encre.RESET}\n")
                sleep(1)
                typingPrint(f"Félicitations ! Tu as pu gagner ce Creeper et tu repars avec {Encre.BLUE}1 diamant{Encre.RESET} [" + str(inventaire["diamant"]) + "/3 💎] !")
                sleep(3)
                while True:
                    print("\n┌────────────────────────────────────────")
                    proposer_actions(["(P) pour: Partir ⛩ ", "(E) pour: Inventaire 🎒"])
                    reponse = input("├─> ").lower()
                    print("└────────────────────────────────────────")
                    if reponse == "partir" or reponse == "p":
                        lieu_deuxieme_etage()
                    elif reponse == "inventaire" or reponse == "e":
                        inventaireAffiche()


# ********************************************************************************
# EXECUTION
# ********************************************************************************

if __name__ == "__main__":
    intro()
    mojang()
    print(f"Fin du jeu.")


#todo: afficher le nombre de plat restant dans inv
#todo: mettre coffre du villageois en action OK. faire l'écuerie OK
#todo: ajouter lettre devant action OK , finir la fin OK


