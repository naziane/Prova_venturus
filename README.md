## Utilização da aplicação 

##Pre-requisitos##
1. Tenha python 3.8 instalado na sua máquina;
2. Tenha o pip instalado na sua maquina;
5. Baixe o ChromeDriver compativel com seu navegador e adicione no diretório(/usr/local/bin/chromedriver);

##Baixando o projeto##
1. Acesse o repositorio e copie (https://github.com/naziane/Prova_venturus.git) 
2. Abra uma aba no terminal e execute: "sudo git clone https:https://github.com/naziane/Prova_venturus.git"

##Criando env para compilar o projeto##
1. Para instalar a virtualenv execute o comando no terminal: "sudo pip install virtualenv"
2. Inicializando o ambiente execute o comando: "virtualenv env"
3: Ativando o ambiente execute o comando: "source ENV/bin/activate" 


##Instalando as libs##
1. Execute o comando pip para instalar as libs "sudo pip install -r requirements.txt"
2. Tenha o pytest --html = report.html instalado (pip install pytest-html)

##Executando os testes##
1. Execute o comando: "py.test --html=report.html" irá executar os testes automatizados e será visualizado no report.html
2. Abra o arquivo report.html para visualizar o relatório de execução dos testes.