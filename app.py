import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from docx import Document
from docx2pdf import convert

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def substituir_chaves_docx(caminho_docx, dados, caminho_saida):
    doc = Document(caminho_docx)

    for paragrafo in doc.paragraphs:
        for chave, valor in dados.items():
            if chave in paragrafo.text:
                paragrafo.text = paragrafo.text.replace(chave, valor)

    doc.save(caminho_saida)


@app.route("/gerar", methods=["POST"])
def gerar_documentos():
    # 1. Receber o arquivo docx enviado
    arquivo = request.files["arquivo_docx"]
    nome_arquivo = secure_filename(arquivo.filename)
    caminho_docx_original = os.path.join(UPLOAD_FOLDER, nome_arquivo)
    arquivo.save(caminho_docx_original)

    # 2. Dados do formulário convertidos para chaves {campo}
    dados = {f"{{{key}}}": request.form[key] for key in request.form}

    # 3. Gerar o novo docx com dados preenchidos
    caminho_docx_preenchido = os.path.join(OUTPUT_FOLDER, "contrato_preenchido.docx")
    substituir_chaves_docx(caminho_docx_original, dados, caminho_docx_preenchido)

    # 4. Converter DOCX → PDF
    caminho_pdf = os.path.join(OUTPUT_FOLDER, "contrato_final.pdf")
    convert(caminho_docx_preenchido, caminho_pdf)

    return f"""
    <h2>Contrato Gerado!</h2>
    <p><a href='/output/contrato_preenchido.docx'>Baixar arquivo DOCX</a></p>
    <p><a href='/output/contrato_final.pdf'>Baixar arquivo PDF</a></p>
    """


# rota para baixar arquivos
@app.route("/output/<path:filename>")
def baixar(filename):
    from flask import send_from_directory
    return send_from_directory(OUTPUT_FOLDER, filename)


@app.route("/")
def index():
    return "Servidor funcionando!"
    

if __name__ == "__main__":
    app.run(debug=True)