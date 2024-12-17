# PASSMANA

![PASSMANA Screenshot](https://raw.githubusercontent.com/atlas161/PASSMANA/main/medias/Screenshot.png)

**PASSMANA** est un projet Python de seconde année d'école d'informatique. Ce programme est un gestionnaire de mots de passe simple et sécurisé, développé avec Flask et MariaDB. Il permet de stocker, générer et rechercher des mots de passe.

## Prérequis

- *Python 3.x*
- *MariaDB*
- *pip*

## Installation et Configuration

### Étape 1 : Installer MariaDB

1. **Télécharger MariaDB**
2. **Installer MariaDB**
3. **Démarrer MariaDB**

### Étape 2 : Configurer MariaDB

1. **Se Connecter à MariaDB**
2. **Créer une Base de Données** :
    ```sql
    CREATE DATABASE passmana;
    ```
3. **Créer un Utilisateur** :
    ```sql
    CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword';
    GRANT ALL PRIVILEGES ON passmana.* TO 'newuser'@'localhost';
    FLUSH PRIVILEGES;
    ```
    Remplacez `newuser` et `newpassword` par les informations que vous souhaitez. Ces informations seront utiles pour l'étape 3.3.

### Étape 3 : Configurer l'Application Flask

1. **Cloner le répertoire** :
2. **Installer les dépendances** :
    ```sh
    pip install -r requirements.txt
    ```
3. **Modifier le Fichier `.env`** :
    - Dans le répertoire du projet, modifiez le fichier nommé `.env`.
    - Ajoutez les informations suivantes dans ce fichier :
      ```env
      SECRET_KEY=<CLE_SECRETE>
      DATABASE_URL=mariadb+pymysql://newuser:newpassword@localhost/passmana
      ```
    - Remplacez `<CLE_SECRETE>` par une clé secrète aléatoire générée sur internet ou autre.
    - Remplacez `newuser` et `newpassword` par les informations de votre utilisateur MariaDB (Étape 2.3).

### Étape 4 : Initialiser la Base de Données

**Exécuter le Script d'Initialisation** :
```sh
python database.py
```

### Étape 5 : Exécuter l'Application

**Exécuter PASSMANA** :
```sh
python app.py
```

## Structure du projet
```
PASSMANA/
├── app.py
├── config.py
├── models.py
├── database.py
├── password_generator.py
├── requirements.txt
├── .env
├── README.md
├── static/
│   └── styles.css
└── templates/
    ├── index.html
    └── modifier.html
```

## Contributeurs

- **DISCEPOLI Angelo** - [Contact](mailto:angelo.discepoli161@gmail.com)
- **GAUTRON Matteo** - [Contact](mailto:gautronmatteo@gmail.com)
