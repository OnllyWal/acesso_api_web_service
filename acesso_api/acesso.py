from acesso_api.maquinas import usuarios

#Gera login e Senha do aluno
def gerar_login_senha(nome_aluno):
    arquivo_de_ips = "/home/wal/APIPropos/acesso_api_web_service/acesso_api/ip.txt"
    login_novo = f"{nome_aluno.lower().replace(' ', '.')}"
    senha_novo = login_novo + "123"
    usuario_de_acesso = "fbro"
    senha_de_acesso="F!n0$BR0"
    return usuarios(arquivo_de_ips, usuario_de_acesso, senha_de_acesso, login_novo, senha_novo)