# automacao de contrato de aluguel
![Python](https://img.shields.io/badge/Python-3.11-blue)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)

## Objetivo:
O objetivo deste projeto é **automatizar a geração de contratos de aluguel** a partir de um documento padrão contendo variáveis pré-definidas, como {nome_locador}, {nacionalidade_locador}, {dia_nascimento_locador}, entre outras.

A ideia é permitir que o usuário preencha um **formulário simples em uma página web**, e o sistema substitua automaticamente essas variáveis dentro do contrato, gerando um **PDF final pronto para uso**, sem necessidade de edição manual.

Esse processo reduz erros, elimina retrabalhos e facilita a criação de documentos personalizados de forma rápida, eficiente e profissional.

## Tecnologias Utilizadas
- Python 3.9+
- flasky
- HTML
- CSS

##  Como Executar o Projeto

```bash
# 1️⃣ Clonar o repositório
git clone https://github.com/CiroKyushima/automacao-de-contrato-de-aluguel.git

# 2️⃣ Instalar as dependências
pip install -r requirements.txt

# 3️⃣ Execute o servidor flasky
python app.py

# 4️⃣ abra o index.html no navegador

# 5️⃣ o contrato utilizado esta na pasta uploads, carregue ele e preencha o formulario

# 6️⃣ finalize e baixe o pdf ou o arquivo docx.

obs: ao rodar o flask, uma pasta de outputs sera criada, nela será salvo tanto o pdf quanto o arquivo docx ja editado!
