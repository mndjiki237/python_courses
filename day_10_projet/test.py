import logging

# 1️⃣ Création d'un logger principal
logger = logging.getLogger("MonApp")
logger.setLevel(logging.DEBUG)  # Niveau minimum de log (tout sera capté)

# 2️⃣ Création d'un gestionnaire pour le fichier
file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)  # Niveau de log pour le fichier

# 3️⃣ Création d'un gestionnaire pour la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Niveau pour la console (ex: on ne veut pas tout le DEBUG ici)

# 4️⃣ Format commun pour les logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 5️⃣ Ajout des gestionnaires au logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 6️⃣ Test des différents niveaux
logger.debug("Mode debug activé (utile pour les développeurs)")
logger.info("Démarrage de l'application...")
logger.warning("Attention : un paramètre est manquant.")
logger.error("Une erreur est survenue !")
logger.critical("Erreur critique : arrêt immédiat.")
