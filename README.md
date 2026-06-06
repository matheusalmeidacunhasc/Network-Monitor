**Network Monitor** 

Sistema de monitoramento de infraestrutura desenvolvido em Python, capaz de verificar disponibilidade de hosts e serviços HTTP, registrar histórico em
banco de dados, calcular indicadores de disponibilidade e gerar alertas automáticos por e-mail — reproduzindo funcionalidades encontradas em
ferramentas corporativas como o Zabbix. 

**Começando** 
Essas instruções permitirão que você obtenha uma cópia do projeto em operação na suaConsulte Implantação para saber como implantar o projeto em um ambiente ativo. 

**Pré-requisitos** 
O que você precisa para instalar e rodar o projeto: 
Python 3.10 ou superior
MariaDB instalado e rodando
Conta Gmail com senha de app configurada
Git 

**Instalação** 
Clone o repositório: 
git clone https://github.com/seu-usuario/network-monitor.git
cd network-monitor
 Crie e ative o ambiente virtual: 
python3 -m venv venv
source venv/bin/activate
 Instale as dependências: 
pip install -r requirements.txt
 Configure as variáveis de ambiente: 
cp .env.example .env
nano .env
 Preencha o arquivo .env com suas credenciais: 
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=monitoramento
EMAIL_REMETENTE=seu@gmail.com
EMAIL_SENHA=sua_senha_de_app
EMAIL_DESTINATARIO=destino@gmail.com
 Configure o banco de dados no MariaDB: 
CREATE DATABASE monitoramento;
USE monitoramento;
 CREATE TABLE monitoramentos (
id INT AUTO_INCREMENT PRIMARY KEY,
host VARCHAR(100),
status VARCHAR(20),
data_hora DATETIME
);
 Configure os hosts que deseja monitorar no arquivo hosts.yaml: 
hosts:
- nome: Google DNS
tipo: ping
endereco: 8.8.8.8
  - nome: Meu Servidor Web
tipo: http
endereco: http://192.168.1.100máquina local para fins de desenvolvimento e teste. 
 Inicie o monitor: 
python3 monitor.py
 Inicie o dashboard em outro terminal: 
python3 dashboard/dashboard.py
 Acesse o dashboard em: http://localhost:5000 

**Executando os testes** 
Para verificar se o monitoramento está funcionando corretamente, execute o monitor manualmente e observe a saída no terminal: 
python3 monitor.py
 A saída esperada é: 
Google DNS -> True
Cloudflare DNS -> True
Meu Servidor Web -> None
 True indica que o host está online. False ou None indica falha — e um e-mail de alerta será enviado automaticamente. 

**Testes de ponta a ponta** 
As funções de verificação podem ser testadas individualmente antes de rodar o monitor completo. 
Teste de ping: 
from checks import verificar_ping
print(verificar_ping("8.8.8.8"))
# Saída esperada: True
 Teste de HTTP: 
from checks import verificar_http
print(verificar_http("https://google.com"))
# Saída esperada: 200

**Testes de estilo de codificação** 
O projeto segue boas práticas de organização de código Python, com separação de responsabilidades entre os módulos: 
monitor.py → orquestra o fluxo principal
checks.py → responsável apenas pelas verificações
database.py → responsável apenas pela persistência
email_alert.py → responsável apenas pelos alertas

**Implantação** 
Para rodar o projeto em um servidor Linux de forma contínua, configure os serviços como units do systemd. Isso garante que o monitor e o dashboard
iniciem automaticamente com o servidor e se recuperem em caso de falha. 
Crie um arquivo de serviço para o monitor em /etc/systemd/system/network-monitor.service e outro para o dashboard em /etc/systemd
system/network-dashboard.service, apontando para os scripts do projeto. 

**Construído com** 
Python 3 - Linguagem principal
Flask - Framework web para o dashboard
MariaDB - Banco de dados
PyMySQL - Conexão Python com MariaDB
PyYAML - Leitura do arquivo de configuração de hosts
python-dotenv - Gerenciamento de variáveis de ambiente 

**Versão** 
Versão atual: 1.0.0✒️ Autores 
Matheus Cunha - Desenvolvimento e documentação - seu-usuario 

**Licença** 
Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes. 
