from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from database import db, create_app
from models import MotDePasse
from password_generator import generer_mot_de_passe
import re

app = create_app()

@app.route('/')
def index():
    query = request.args.get('query', '')
    if query:
        mots_de_passe = MotDePasse.query.filter(
            (MotDePasse.site.ilike(f'%{query}%')) |
            (MotDePasse.nom_utilisateur.ilike(f'%{query}%')) |
            (MotDePasse.mot_de_passe.ilike(f'%{query}%'))
        ).order_by(MotDePasse.id.desc()).all()
    else:
        mots_de_passe = MotDePasse.query.order_by(MotDePasse.id.desc()).all()
    return render_template('index.html', mots_de_passe=mots_de_passe, query=query)

@app.route('/ajouter', methods=['POST'])
def ajouter_mot_de_passe():
    site = request.form['site']
    nom_utilisateur = request.form['nom_utilisateur']
    mot_de_passe = request.form['mot_de_passe']

    if not valider_mot_de_passe(mot_de_passe):
        flash('Le mot de passe doit contenir au moins 8 caractères, une majuscule, un chiffre et un caractère spécial.', 'error')
        return redirect(url_for('index'))

    nouveau_mot_de_passe = MotDePasse(site=site, nom_utilisateur=nom_utilisateur, mot_de_passe=mot_de_passe)
    db.session.add(nouveau_mot_de_passe)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier_mot_de_passe(id):
    mot_de_passe = MotDePasse.query.get_or_404(id)
    if request.method == 'POST':
        mot_de_passe.site = request.form['site']
        mot_de_passe.nom_utilisateur = request.form['nom_utilisateur']
        mot_de_passe.mot_de_passe = request.form['mot_de_passe']

        if not valider_mot_de_passe(mot_de_passe.mot_de_passe):
            flash('Le mot de passe doit contenir au moins 8 caractères, une majuscule, un chiffre et un caractère spécial.', 'error')
            return redirect(url_for('modifier_mot_de_passe', id=id))

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('modifier.html', mot_de_passe=mot_de_passe)

@app.route('/generer_mot_de_passe', methods=['GET'])
def generer_mot_de_passe_route():
    longueur = int(request.args.get('longueur', 12))
    inclure_majuscules = request.args.get('inclure_majuscules') == 'true'
    inclure_minuscules = request.args.get('inclure_minuscules') == 'true'
    inclure_chiffres = request.args.get('inclure_chiffres') == 'true'
    inclure_speciaux = request.args.get('inclure_speciaux') == 'true'

    mot_de_passe = generer_mot_de_passe(longueur, inclure_majuscules, inclure_minuscules, inclure_chiffres, inclure_speciaux)
    return jsonify(mot_de_passe=mot_de_passe)

@app.route('/supprimer/<int:id>', methods=['POST'])
def supprimer_mot_de_passe(id):
    mot_de_passe = MotDePasse.query.get_or_404(id)
    db.session.delete(mot_de_passe)
    db.session.commit()
    return redirect(url_for('index'))

def valider_mot_de_passe(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False
    if not re.search(r'[A-Z]', mot_de_passe):
        return False
    if not re.search(r'[a-z]', mot_de_passe):
        return False
    if not re.search(r'[0-9]', mot_de_passe):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', mot_de_passe):
        return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
