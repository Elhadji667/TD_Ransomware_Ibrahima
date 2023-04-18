# TD_Ransomware_Ibrahima
Q1 : Le nom de l'algorithme de chiffrement utilisé dans le fichier xorcrypt.py est XOR (eXclusive OR). Cet algorithme effectue une opération XOR bit à bit entre les données et une clé, qui est répétée pour couvrir toute la longueur des données.

Il n'est pas considéré comme robuste pour plusieurs raisons:

    La clé est réutilisée (en boucle) pour chiffrer les données. Si la clé est plus courte que les données, cela crée des motifs répétitifs qui peuvent être exploités pour casser le chiffrement.
    Si un attaquant a accès à une partie du texte en clair et au texte chiffré correspondant, il peut appliquer l'opération XOR entre les deux pour retrouver la clé.
    L'algorithme XOR est très simple et peut être facilement cassé avec des techniques d'analyse de fréquence ou d'autres méthodes cryptanalytiques.

Q2 : l n'est pas recommandé de hacher directement le sel et la clé, car cela peut affaiblir la sécurité de l'algorithme. La fonction de dérivation de clé (KDF) comme PBKDF2HMAC est spécialement conçue pour générer des clés cryptographiques sécurisées à partir de secrets et de sels. Un HMAC (Hash-based Message Authentication Code) est également une option, mais il est principalement utilisé pour authentifier des messages en utilisant un secret partagé et non pour dériver des clés cryptographiques.

Q3 : il est préférable de vérifier si un fichier token.bin est déjà présent, car cela peut indiquer que le ransomware a déjà été exécuté sur le système cible. Dans ce cas, vous ne voudriez pas écraser les données cryptographiques existantes, car cela rendrait impossible la récupération des fichiers chiffrés avec l'ancien token. En vérifiant l'existence du fichier token.bin, vous vous assurez de ne pas causer de dommages supplémentaires et de ne pas rendre la situation encore plus compliquée pour la victime.







