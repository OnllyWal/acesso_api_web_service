import requests
from acesso_api.acesso import gerar_login_senha
#from defesa_api.pre_process import start_doc_process, txt_edit_6lines
#from defesa_api.text_chamado import text_chamado

def get_emails(endpoint_url):
    try:
        # Faz a requisição GET para o endpoint Flask
        response = requests.get(endpoint_url)
        response.raise_for_status()  # Verifica se houve erro HTTP
        emails = response.json()  # Converte a resposta JSON para um objeto Python (lista de dicionários)
        return emails
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados do endpoint: {e}")
        return []
    

def process_email(email):
    # Manipula os dados recebidos conforme a necessidade
    student_name = email['origin_name']
    login, senha = gerar_login_senha(student_name)
    email['titulo'] = f"Login e senha de {student_name}"
    email['corpo'] = f"Olá,\n\nO login é: {login} e a senha é: {senha}.\n\nAtenciosamente,\nEquipe PPComp"
    email['status'] = "Processado"
    id = email['id']
    return email, id

def update_email(email,id):
    response = requests.put(f"http://172.19.113.12:5000/emails/{id}", json=email)
    print(response.json)