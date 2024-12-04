from database import db

class MotDePasse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(128), nullable=False)
    nom_utilisateur = db.Column(db.String(128), nullable=False)
    mot_de_passe = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<MotDePasse {self.site}>'
