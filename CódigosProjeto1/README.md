


![Etapa Atual](doc/etapaAtualPilhaAplicacao.png){ width=30% }

# Projeto 1 : Client-Server

Essa etapa do projeto consiste na modificação da comunicação em modo loopback
para uma comunicação ponto a ponto entre dois computadores via a interface UART.
Como ilustrado no diagrama a seguir :

![Comunicação entre dois computadores](doc/clientServer.png){ width=100% }

A comunicação entre dois computadores e dois microprocessadores(Arduino) conectados entre si, baseia-se em uma interação entre diferentes camadas entre as duas aplicações. Dessa forma, os códigos foram modificados a partir de uma base dada no projeto 0(loopback). Essa modificação consiste em dividir a aplicação em cliente e servidor; o primeiro, serializa um arquivo e o transmite; enquanto o segundo, é responsável por desserializar o mesmo arquivo e salvá-lo na memória. 



## Código Base

O código possui os seguintes arquivos : server.py; server.py; enlace.py; enlaceTx.py; enlaceRx.py; interfaceFisica.py. Sendo cada um responsável por :

server.py : Código que prepara o computador para receber a imagem do Client.

client.py : Código que transmite a imagem e aguarda o fim da transmissão.

enlace.py : Interface de comunicação entre a aplicação e o enlace.

enlaceTx.py : parte do enlace responsável por transmitir n dados via a camada física (interfaceFisica.py)

enlaceRx.py : parte do enlace responsável por receber n dados via a camada física (interfaceFisica.py)

interfaceFisica.py : Código que lida com o envio dos dados para o Arduino e recebimento.

A figura a seguir faz uma relação dos códigos com cada etapa da comunicação a ser desenvolvida :

(doc/Diagrama.png)






