# TD_Ransomware_Ibrahima
Q1 : Le nom de l'algorithme de chiffrement utilisé dans le fichier xorcrypt.py est XOR (eXclusive OR). Cet algorithme effectue une opération XOR bit à bit entre les données et une clé, qui est répétée pour couvrir toute la longueur des données.

Il n'est pas considéré comme robuste pour plusieurs raisons:

    La clé est réutilisée (en boucle) pour chiffrer les données. Si la clé est plus courte que les données, cela crée des motifs répétitifs qui peuvent être exploités pour casser le chiffrement.
    Si un attaquant a accès à une partie du texte en clair et au texte chiffré correspondant, il peut appliquer l'opération XOR entre les deux pour retrouver la clé.
    L'algorithme XOR est très simple et peut être facilement cassé avec des techniques d'analyse de fréquence ou d'autres méthodes cryptanalytiques.

Q2 : l n'est pas recommandé de hacher directement le sel et la clé, car cela peut affaiblir la sécurité de l'algorithme. La fonction de dérivation de clé (KDF) comme PBKDF2HMAC est spécialement conçue pour générer des clés cryptographiques sécurisées à partir de secrets et de sels. Un HMAC (Hash-based Message Authentication Code) est également une option, mais il est principalement utilisé pour authentifier des messages en utilisant un secret partagé et non pour dériver des clés cryptographiques.

Q3 : il est préférable de vérifier si un fichier token.bin est déjà présent, car cela peut indiquer que le ransomware a déjà été exécuté sur le système cible. Dans ce cas, vous ne voudriez pas écraser les données cryptographiques existantes, car cela rendrait impossible la récupération des fichiers chiffrés avec l'ancien token. En vérifiant l'existence du fichier token.bin, vous vous assurez de ne pas causer de dommages supplémentaires et de ne pas rendre la situation encore plus compliquée pour la victime.


B1: Dans cette partie, l'idée est d'envoyer les fichiers de la victime au CNC (centre de contrôle et de commande) pour pouvoir les revendre à la victime en cas de besoin. Cela ajoute une autre source de revenus pour l'attaquant et rend l'attaque plus efficace.

B2: Le chiffrement XOR est vulnérable à une attaque connue sous le nom d'attaque "known-plaintext". Si l'attaquant dispose d'un fichier chiffré et de sa version en clair, il peut facilement retrouver la clé. Le script suivant démontre comment récupérer la clé:

B3: La bibliothèque cryptography offre de nombreuses options fiables pour le chiffrement, comme l'utilisation de l'AES (Advanced Encryption Standard) avec un mode d'opération comme GCM (Galois/Counter Mode). L'utilisation d'une méthode de chiffrement symétrique moderne comme l'AES-GCM garantit une sécurité accrue.

Pour implémenter cette solution, vous devrez remplacer la méthode de chiffrement XOR actuelle par l'AES-GCM.

B4: Pour créer un binaire avec pyinstaller, exécutez la commande suivante dans votre terminal: pyinstaller --onefile your_script.py

B5: Le binaire créé se trouvera dans le dossier dist qui sera créé dans le répertoire courant.








