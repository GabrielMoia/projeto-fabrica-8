from flask import Flask, render_template, url_for

app = Flask(__name__)


pacientes = [
    {
        "id": 1,
        "nome": "Mariana Lopes",
        "idade": 28,
        "condicao": "Hipertensão",
        "image": "https://randomuser.me/api/portraits/women/45.jpg"
    },
    {
        "id": 2,
        "nome": "Rafael Souza",
        "idade": 34,
        "condicao": "Asma Crônica",
        "image": "https://randomuser.me/api/portraits/men/32.jpg"
    },
    {
        "id": 3,
        "nome": "Cláudia Ferreira",
        "idade": 52,
        "condicao": "Diabetes Tipo 2",
        "image": "https://randomuser.me/api/portraits/women/65.jpg"
    }
]

medicos = [
    {
        "id": 1,
        "nome": "Dr. André Costa",
        "especialidade": "Cardiologista",
        "anos_experiencia": 12,
        "image": "https://randomuser.me/api/portraits/men/21.jpg"
    },
    {
        "id": 2,
        "nome": "Dra. Juliana Martins",
        "especialidade": "Endocrinologista",
        "anos_experiencia": 9,
        "image": "https://randomuser.me/api/portraits/women/34.jpg"
    },
    {
        "id": 3,
        "nome": "Dr. Henrique Almeida",
        "especialidade": "Pediatra",
        "anos_experiencia": 15,
        "image": "https://randomuser.me/api/portraits/men/50.jpg"
    }
]

@app.route("/")
def home():
    return render_template('index.html')

# Listar pacientes
@app.route("/pacientes")
def listar_pacientes():
    return render_template("listar_pacientes.html", pacientes=pacientes)

# Detalhes do paciente
@app.route("/pacientes/<int:paciente_id>")
def detalhes_paciente(paciente_id):
    for paciente in pacientes:
        if paciente["id"] == paciente_id:
            return render_template("detalhe_paciente.html", paciente=paciente)
    return "Paciente não encontrado", 404

# Listar médicos
@app.route("/medicos")
def listar_medicos():
    return render_template("listar_medicos.html", medicos=medicos)

# Detalhes do médico
@app.route("/medicos/<int:medico_id>")
def detalhe_medico(medico_id):
    for medico in medicos:
        if medico["id"] == medico_id:
            return render_template("detalhe_medico.html", medico=medico)
    return "Médico não encontrado", 404

if __name__ == "__main__":
    app.run(debug=True)
