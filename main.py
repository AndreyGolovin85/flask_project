from flask import Flask
from utils import candidats_formats, candidat_id, candidat_skills, load_candidates

app = Flask(__name__)


@app.route('/')
def all_candidat():
     candidat = candidats_formats(load_candidates())
     return candidat


@app.route('/candidates/<int:get_id>')
def candidates_id(get_id):
    candidat = candidat_id(get_id)
    return f"<img src={candidat['picture']}>" + candidats_formats([candidat])


@app.route('/skills/<skill>')
def skills(skill):
    candidat = candidat_skills(skill)
    return candidats_formats(candidat)


app.run()
