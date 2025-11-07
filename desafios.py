"""
Desafio Módulo Git

Neste arquivo você encontrará funções **incompletas** que representam
tarefas relacionadas ao aprendizado de Git e GitHub.

Seu objetivo é:
- Criar uma issue para cada função.
- Implementar a função em uma branch específica.
- Fazer commit, criar tag e abrir Pull Request.
- Repetir o processo até concluir todas as funções.

Boa sorte e bons commits! 🚀
"""

msgBoasVindas = "Bem-vindo ao Desavio do Git!"
comandosBasicos = [
    "git init",
    "git status",
    "git add",
    "git commit",
    "git log",
    "git clone",
    "git reset",
    "git push",
    "git pull",
    "git merge",
]


def mostrar_mensagem_inicial():
    """
    Exibe uma mensagem de boas-vindas ao desafio.
    Retorno esperado: string com a mensagem "Bem-vindo ao Desafio de Git!"
    """
    print(msgBoasVindas)


def listar_comandos_git_basicos():
    """
    Retorna uma lista com os principais comandos básicos do Git.
    Exemplo de saída:
    ["git init", "git add", "git commit", "git status", "git push"]
    """
    print(comandosBasicos)


def criar_mensagem_commit(funcao_nome):
    """
    Recebe o nome de uma função e retorna uma mensagem de commit padronizada.
    Exemplo:
    criar_mensagem_commit("listar_comandos_git_basicos") ->
    "Implementa função listar_comandos_git_basicos"
    """
    if funcao_nome == "mostrar_mensagem_inicial":
        return "feature1_5 implementada - Mensagem Boas Vindas"
    elif funcao_nome == "listar_comandos_git_basicos":
        return "feature2_5 implementada - Lista de Comandos Git"
    elif funcao_nome == "criar_mensagem_commit":
        return "feature3_5 implementada - Criar Mensagem Commit"
    elif funcao_nome == "verificar_tag_valida":
        return "feature4_5 implementada - Validar formato TAG"
    elif funcao_nome == "gerar_relatorio_final":
        return "feature5_5 implementada - relatorio final"


def verificar_tag_valida(tag):
    """
    Verifica se uma tag está no formato 'vX.Y' (ex: v1.0, v2.1).
    Retorna True se o formato for válido, caso contrário False.
    """
    formato = True
    if tag[0] == "v":
        formato = formato and True
    else:
        formato = formato and False

    if tag[1] in "123456789":
        formato = formato and True
    else:
        formato = formato and False

    if tag[2] == ".":
        formato = formato and True
    else:
        formato = formato and False

    if tag[3] in "0123456789":
        formato = formato and True
    else:
        formato = formato and False

    return formato


def gerar_relatorio_final(funcoes_concluidas):
    """
    Recebe uma lista com os nomes das funções implementadas
    e retorna uma mensagem final do desafio.

    Exemplo:
    gerar_relatorio_final(["mostrar_mensagem_inicial", "listar_comandos_git_basicos"])
    ->
    "Desafio concluído! 2 funções implementadas com sucesso."
    """
    pass


if __name__ == "__main__":
    print(verificar_tag_valida("v1.1"))
