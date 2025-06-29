import csv
import os
from collections import namedtuple
from getpass import getpass

# A biblioteca rich é excelente para criar interfaces de linha de comando mais bonitas
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table

## --- Constantes e Variáveis Globais ---
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_PRODUTOS = 'produtos.csv'
USUARIO_LOGADO = None

# Tuplas nomeadas para organizar os dados
Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])
Livro = namedtuple('Livro', ['id', 'titulo', 'autor', 'ano', 'preco', 'quantidade'])

# Inicialização do console do Rich
console = Console()

#################################################################
#                       FUNÇÕES DE USUÁRIOS                     #
#################################################################

##### CRUD Read (Usuários)
def ler_usuarios(arquivo_csv):
    """
    Lê os usuários de um arquivo CSV e os armazena em um dicionário.
    :param arquivo_csv: (str) Caminho do arquivo CSV de usuários.
    :return: (dict) Dicionário com logins como chaves e tuplas Usuario como valores.
    """
    usuarios = {}
    try:
        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                login, senha, tipo = row
                usuarios[login] = Usuario(login=login, senha=senha, tipo=tipo)
    except FileNotFoundError:
        console.print(f"[bold red]Arquivo de usuários '{arquivo_csv}' não encontrado. Criando um novo.[/bold red]")
        # Se o arquivo não existe, podemos criá-lo aqui ou apenas retornar um dict vazio
    return usuarios

##### CRUD Read (Login)
def fazer_login(usuarios):
    """
    Realiza o login de um usuário, atualizando a variável global USUARIO_LOGADO.
    :param usuarios: (dict) Dicionário de usuários cadastrados.
    :return: None
    """
    global USUARIO_LOGADO
    console.print(Panel('🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.', expand=False, title="Tela de Login"))
    username = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    user = usuarios.get(username)
    if user and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print(f"[bold red]Erro: usuário ou senha incorretos!", style="red")

##### CRUD Create (Usuários)
def cadastrar_usuario(usuarios, arquivo_csv):
    """
    Cadastra um novo usuário no sistema. Apenas gerentes podem criar novos gerentes.
    :param usuarios: (dict) Dicionário de usuários existentes.
    :param arquivo_csv: (str) Caminho do arquivo CSV para salvar o novo usuário.
    :return: (str) Nome do novo usuário ou False em caso de falha.
    """
    console.print(Panel('[bold green]Cadastro de Novo Usuário[/bold green]\nPor favor, insira os dados.', title="Novo Usuário"))
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")

    if nome_usuario in usuarios:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold yellow]{nome_usuario}[/bold yellow]' já existe!")
        return False
    
    senha = getpass("Senha: ")
    tipo = 'funcionario' # Padrão
    if USUARIO_LOGADO and USUARIO_LOGADO.tipo == 'gerente':
        tipo = Prompt.ask("[bold cyan]Tipo (gerente/funcionario)[/bold cyan]", choices=["gerente", "funcionario"], default="funcionario")

    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome_usuario, senha, tipo])
    console.print(f"[bold green]Usuário '{nome_usuario}' cadastrado com sucesso![/bold green]")
    return nome_usuario

##### CRUD Update (Usuários)
def atualiza_senha(usuarios, arquivo_csv):
    """
    Atualiza a senha de um usuário. Gerentes podem alterar qualquer senha, funcionários apenas a sua própria.
    :param usuarios: (dict) Dicionário de usuários.
    :param arquivo_csv: (str) Caminho do arquivo CSV para persistir a alteração.
    :return: (bool) True se a senha foi atualizada, False caso contrário.
    """
    if USUARIO_LOGADO.tipo == 'funcionario':
        nome_usuario = USUARIO_LOGADO.login
        console.print(Panel('[bold yellow]Atualização da Sua Senha[/bold yellow]', title="Atualizar Senha"))
    else: # Gerente
        console.print(Panel('[bold yellow]Atualização de Senha de Usuário[/bold yellow]', title="Atualizar Senha"))
        nome_usuario = Prompt.ask("[bold cyan]Nome do Usuário a ser atualizado[/bold cyan]")

    if nome_usuario not in usuarios:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold yellow]{nome_usuario}[/bold yellow]' não encontrado!")
        return False

    nova_senha = getpass("Nova senha: ")
    usuarios[nome_usuario] = usuarios[nome_usuario]._replace(senha=nova_senha)

    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for u in usuarios.values():
            writer.writerow([u.login, u.senha, u.tipo])
            
    console.print(f"[bold green]Senha do usuário '{nome_usuario}' atualizada com sucesso![/bold green]")
    return True

##### CRUD Delete (Usuários)
def excluir_usuario(usuarios, arquivo_csv):
    """
    Exclui um usuário do sistema. Apenas gerentes podem fazer isso.
    :param usuarios: (dict) Dicionário de usuários.
    :param arquivo_csv: (str) Caminho do arquivo CSV.
    :return: (bool) True se o usuário foi excluído, False caso contrário.
    """
    console.print(Panel('[bold red]Exclusão de Usuário[/bold red]', title="Excluir Usuário"))
    nome_usuario = Prompt.ask("[bold cyan]Nome do usuário a ser excluído[/bold cyan]")

    if nome_usuario not in usuarios:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold yellow]{nome_usuario}[/bold yellow]' não encontrado!")
        return False
    if nome_usuario == USUARIO_LOGADO.login:
        console.print("[bold red]Erro: Você não pode excluir o seu próprio usuário logado.[/bold red]")
        return False

    del usuarios[nome_usuario] # Remove do dicionário em memória
    
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for u in usuarios.values():
            writer.writerow([u.login, u.senha, u.tipo])

    console.print(f"[bold green]Usuário '{nome_usuario}' excluído com sucesso![/bold green]")
    return True

#################################################################
#                      FUNÇÕES DE PRODUTOS (LIVROS)             #
#################################################################

##### CRUD Read (Livros)
def ler_produtos(arquivo_csv):
    """
    Lê os produtos (livros) de um arquivo CSV e os armazena em um dicionário.
    :param arquivo_csv: (str) Caminho do arquivo CSV de produtos.
    :return: (dict) Dicionário com IDs como chaves e tuplas Livro como valores.
    """
    produtos = {}
    try:
        with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                id_livro, titulo, autor, ano, preco, quantidade = row
                produtos[id_livro] = Livro(
                    id=id_livro,
                    titulo=titulo,
                    autor=autor,
                    ano=int(ano),
                    preco=float(preco),
                    quantidade=int(quantidade)
                )
    except FileNotFoundError:
        console.print(f"[bold red]Arquivo de produtos '{arquivo_csv}' não encontrado. Criando um novo.[/bold red]")
    except ValueError:
        # Lida com o caso do arquivo estar vazio ou com cabeçalho
        pass
    return produtos

##### CRUD Create (Livros)
def cadastrar_livro(produtos, arquivo_csv):
    """
    Cadastra um novo livro no sistema.
    :param produtos: (dict) Dicionário de livros existentes.
    :param arquivo_csv: (str) Caminho do arquivo para salvar o novo livro.
    :return: (bool) True se o livro foi cadastrado com sucesso, False caso contrário.
    """
    console.print(Panel('[bold green]Cadastro de Novo Livro[/bold green]', title="Novo Livro"))
    id_livro = Prompt.ask("[bold cyan]ID do Livro[/bold cyan]")
    if id_livro in produtos:
        console.print(f"[bold red]Erro:[/bold red] Livro com ID '[bold yellow]{id_livro}[/bold yellow]' já existe!")
        return False

    titulo = Prompt.ask("[bold cyan]Título[/bold cyan]")
    autor = Prompt.ask("[bold cyan]Autor[/bold cyan]")
    ano = int(Prompt.ask("[bold cyan]Ano de Publicação[/bold cyan]"))
    preco = float(Prompt.ask("[bold cyan]Preço[/bold cyan]"))
    quantidade = int(Prompt.ask("[bold cyan]Quantidade em Estoque[/bold cyan]"))

    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([id_livro, titulo, autor, ano, preco, quantidade])
    
    console.print(f"[bold green]Livro '{titulo}' cadastrado com sucesso![/bold green]")
    return True

##### CRUD Read (Listar Livros - com ordenação)
def listar_produtos(produtos, chave_ordenacao='titulo'):
    """
    Lista todos os livros em uma tabela formatada, ordenados por uma chave.
    :param produtos: (dict) Dicionário de livros.
    :param chave_ordenacao: (str) Atributo pelo qual os livros devem ser ordenados ('titulo' ou 'preco').
    """
    if not produtos:
        console.print("[bold yellow]Nenhum livro cadastrado.[/bold yellow]")
        return
    
    # Converte os valores do dicionário para uma lista e ordena
    lista_produtos = sorted(list(produtos.values()), key=lambda livro: getattr(livro, chave_ordenacao))

    # Cria a tabela para exibição
    tabela = Table(title=f"Lista de Livros Ordenados por {chave_ordenacao.capitalize()}")
    tabela.add_column("ID", style="cyan")
    tabela.add_column("Título", style="magenta")
    tabela.add_column("Autor", style="green")
    tabela.add_column("Ano", justify="right", style="green")
    tabela.add_column("Preço (R$)", justify="right", style="yellow")
    tabela.add_column("Qtd.", justify="right", style="red")

    for livro in lista_produtos:
        tabela.add_row(livro.id, livro.titulo, livro.autor, str(livro.ano), f"{livro.preco:.2f}", str(livro.quantidade))
    
    console.print(tabela)

##### CRUD Read (Buscar Livro)
def buscar_livro(produtos):
    """
    Busca um livro específico pelo seu ID e exibe seus detalhes.
    :param produtos: (dict) Dicionário de livros.
    """
    id_busca = Prompt.ask("[bold cyan]Digite o ID do livro a ser buscado[/bold cyan]")
    livro = produtos.get(id_busca)

    if livro:
        console.print(Panel(
            f"[bold cyan]Título:[/bold cyan] {livro.titulo}\n"
            f"[bold cyan]Autor:[/bold cyan] {livro.autor}\n"
            f"[bold cyan]Ano:[/bold cyan] {livro.ano}\n"
            f"[bold cyan]Preço:[/bold cyan] R$ {livro.preco:.2f}\n"
            f"[bold cyan]Estoque:[/bold cyan] {livro.quantidade} unidades",
            title=f"Detalhes do Livro - ID {livro.id}"
        ))
    else:
        console.print(f"[bold red]Livro com ID '{id_busca}' não encontrado.[/bold red]")

##### CRUD Update (Livros)
def atualizar_livro(produtos, arquivo_csv):
    """
    Atualiza as informações de um livro existente.
    :param produtos: (dict) Dicionário de livros.
    :param arquivo_csv: (str) Caminho do arquivo CSV para persistir a alteração.
    :return: (bool) True se o livro foi atualizado, False caso contrário.
    """
    id_atualizar = Prompt.ask("[bold cyan]Digite o ID do livro a ser atualizado[/bold cyan]")
    if id_atualizar not in produtos:
        console.print(f"[bold red]Erro:[/bold red] Livro com ID '[bold yellow]{id_atualizar}[/bold yellow]' não encontrado!")
        return False
    
    livro_antigo = produtos[id_atualizar]
    console.print(f"Atualizando o livro: [bold magenta]{livro_antigo.titulo}[/bold magenta]. Deixe em branco para manter o valor atual.")

    titulo = Prompt.ask(f"Novo Título", default=livro_antigo.titulo)
    autor = Prompt.ask(f"Novo Autor", default=livro_antigo.autor)
    ano = int(Prompt.ask(f"Novo Ano", default=str(livro_antigo.ano)))
    preco = float(Prompt.ask(f"Novo Preço", default=str(livro_antigo.preco)))
    quantidade = int(Prompt.ask(f"Nova Quantidade", default=str(livro_antigo.quantidade)))
    
    # Atualiza o dicionário em memória
    produtos[id_atualizar] = Livro(id_atualizar, titulo, autor, ano, preco, quantidade)

    # Reescreve o arquivo CSV com os dados atualizados
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for livro in produtos.values():
            writer.writerow(livro)
    
    console.print(f"[bold green]Livro com ID '{id_atualizar}' atualizado com sucesso![/bold green]")
    return True

##### CRUD Delete (Livros)
def excluir_livro(produtos, arquivo_csv):
    """
    Exclui um livro do sistema.
    :param produtos: (dict) Dicionário de livros.
    :param arquivo_csv: (str) Caminho do arquivo CSV.
    :return: (bool) True se o livro foi excluído, False caso contrário.
    """
    id_excluir = Prompt.ask("[bold cyan]Digite o ID do livro a ser excluído[/bold cyan]")
    if id_excluir not in produtos:
        console.print(f"[bold red]Erro:[/bold red] Livro com ID '[bold yellow]{id_excluir}[/bold yellow]' não encontrado!")
        return False
    
    titulo_excluido = produtos[id_excluir].titulo
    del produtos[id_excluir]

    # Reescreve o arquivo CSV sem o livro excluído
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for livro in produtos.values():
            writer.writerow(livro)
    
    console.print(f"[bold green]Livro '{titulo_excluido}' (ID: {id_excluir}) excluído com sucesso![/bold green]")
    return True

#################################################################
#                           MENUS DO SISTEMA                    #
#################################################################

def menu_inicial():
    """
    Exibe o menu inicial para usuários não logados.
    :return: (str) Opção escolhida pelo usuário.
    """
    console.print(Panel("[bold green]Bem-vindo à Livraria Dev![/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial"))
    console.print("[bold cyan]1.[/bold cyan] Fazer Login")
    console.print("[bold cyan]2.[/bold cyan] Cadastrar-se como Funcionário")
    console.print("[bold cyan]3.[/bold cyan] Sair")
    return Prompt.ask("[bold yellow]Opção[/bold yellow]", choices=["1", "2", "3"])

def menu_gerente():
    """
    Exibe o menu de opções para o usuário 'gerente'.
    :return: (str) Opção escolhida.
    """
    console.print(Panel(f"[bold green]Menu do Gerente | Logado como: {USUARIO_LOGADO.login}[/bold green]", title="Painel do Gerente"))
    console.print("[bold blue]--- Gerenciamento de Livros ---[/bold blue]")
    console.print("[bold cyan]1.[/bold cyan] Adicionar Livro")
    console.print("[bold cyan]2.[/bold cyan] Listar Livros (por Título)")
    console.print("[bold cyan]3.[/bold cyan] Listar Livros (por Preço)")
    console.print("[bold cyan]4.[/bold cyan] Buscar Livro por ID")
    console.print("[bold cyan]5.[/bold cyan] Atualizar Livro")
    console.print("[bold cyan]6.[/bold cyan] Excluir Livro")
    console.print("[bold yellow]--- Gerenciamento de Usuários ---[/bold yellow]")
    console.print("[bold cyan]7.[/bold cyan] Adicionar Usuário")
    console.print("[bold cyan]8.[/bold cyan] Atualizar Senha de Usuário")
    console.print("[bold cyan]9.[/bold cyan] Excluir Usuário")
    console.print("[bold red]0.[/bold red] Logout")
    return Prompt.ask("[bold yellow]Opção[/bold yellow]", choices=[str(i) for i in range(10)])

def menu_funcionario():
    """
    Exibe o menu de opções para o usuário 'funcionario'.
    :return: (str) Opção escolhida.
    """
    console.print(Panel(f"[bold green]Menu do Funcionário | Logado como: {USUARIO_LOGADO.login}[/bold green]", title="Painel do Funcionário"))
    console.print("[bold blue]--- Livros ---[/bold blue]")
    console.print("[bold cyan]1.[/bold cyan] Listar Livros (por Título)")
    console.print("[bold cyan]2.[/bold cyan] Listar Livros (por Preço)")
    console.print("[bold cyan]3.[/bold cyan] Buscar Livro por ID")
    console.print("[bold yellow]--- Minha Conta ---[/bold yellow]")
    console.print("[bold cyan]4.[/bold cyan] Atualizar Minha Senha")
    console.print("[bold red]0.[/bold red] Logout")
    return Prompt.ask("[bold yellow]Opção[/bold yellow]", choices=[str(i) for i in range(5)])

#################################################################
#                           FLUXO PRINCIPAL                     #
#################################################################
if __name__ == "__main__":
    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
    produtos = ler_produtos(ARQUIVO_PRODUTOS)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if USUARIO_LOGADO is None:
            opcao_inicial = menu_inicial()
            if opcao_inicial == '1':
                fazer_login(usuarios)
            elif opcao_inicial == '2':
                if cadastrar_usuario(usuarios, ARQUIVO_USUARIOS):
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS) # Recarrega usuários
            elif opcao_inicial == '3':
                console.print("[bold yellow]Saindo do sistema. Até logo![/bold yellow]")
                break
        else: # Usuário está logado
            if USUARIO_LOGADO.tipo == 'gerente':
                opcao_interna = menu_gerente()
                # Ações do Gerente
                if opcao_interna == '1':
                    if cadastrar_livro(produtos, ARQUIVO_PRODUTOS): produtos = ler_produtos(ARQUIVO_PRODUTOS)
                elif opcao_interna == '2': listar_produtos(produtos, 'titulo')
                elif opcao_interna == '3': listar_produtos(produtos, 'preco')
                elif opcao_interna == '4': buscar_livro(produtos)
                elif opcao_interna == '5':
                    if atualizar_livro(produtos, ARQUIVO_PRODUTOS): produtos = ler_produtos(ARQUIVO_PRODUTOS)
                elif opcao_interna == '6':
                    if excluir_livro(produtos, ARQUIVO_PRODUTOS): produtos = ler_produtos(ARQUIVO_PRODUTOS)
                elif opcao_interna == '7':
                    if cadastrar_usuario(usuarios, ARQUIVO_USUARIOS): usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                elif opcao_interna == '8':
                    if atualiza_senha(usuarios, ARQUIVO_USUARIOS): usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                elif opcao_interna == '9':
                    if excluir_usuario(usuarios, ARQUIVO_USUARIOS): usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                elif opcao_interna == '0': USUARIO_LOGADO = None

            elif USUARIO_LOGADO.tipo == 'funcionario':
                opcao_interna = menu_funcionario()
                # Ações do Funcionário
                if opcao_interna == '1': listar_produtos(produtos, 'titulo')
                elif opcao_interna == '2': listar_produtos(produtos, 'preco')
                elif opcao_interna == '3': buscar_livro(produtos)
                elif opcao_interna == '4':
                    if atualiza_senha(usuarios, ARQUIVO_USUARIOS): usuarios = ler_usuarios(ARQUIVO_USUARIOS)
                elif opcao_interna == '0': USUARIO_LOGADO = None
            
            # Pausa para o usuário ver o resultado antes de limpar a tela
            if USUARIO_LOGADO:
                 Prompt.ask("\n[bold]Pressione Enter para continuar...[/bold]")