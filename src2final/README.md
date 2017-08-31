

# Projeto 1 : Client-Server

  Essa etapa do projeto consiste na modificação das camadas de enlace do protocolo de comunicação entre os computadores, com o objetivo de tornar a mesma um passo mais independente. Neste projeto será gerado um pacote, que encapsulará os dados (payload) e irá conter outros dados fundamentais para identificação das informações do pacote, como tamanho. Isso irá possibilitar que o server não precise previamente saber o tamanho do arquivo sendo transmitido.

![Comunicação entre dois computadores](doc/clientServer.png){ width=100% }

A comunicação entre dois computadores e dois microprocessadores(Arduino) conectados entre si, baseia-se em uma interação entre diferentes camadas entre as duas aplicações. Dessa forma, os códigos foram modificados a partir de uma base dada no projeto 0(loopback). Essa modificação consiste em dividir a aplicação em cliente e servidor; o primeiro, serializa um arquivo e o transmite; enquanto o segundo, é responsável por desserializar o mesmo arquivo e salvá-lo na memória. 



## Código Final

O código possui os seguintes arquivos : server.py; server.py; enlace.py; enlaceTx.py; enlaceRx.py; interfaceFisica.py. Sendo cada um responsável por :

server.py : Código que prepara o computador para receber a imagem do Client.

client.py : Código que transmite a imagem e aguarda o fim da transmissão.

enlace.py : Interface de comunicação entre a aplicação e o enlace.

enlaceTx.py : Parte do enlace responsável por encapsular os dados em um pacote.

enlaceRx.py : Parte do enlace responsável por receber e desencapsular os dados.

interfaceFisica.py : Código que lida com o envio dos dados para o Arduino e recebimento.

A figura a seguir faz uma relação dos códigos com cada etapa da comunicação a ser desenvolvida :

![Camadas](doc/Diagrama.png)


Além deste diagrama, analisou-se novamente as camadas para saber qual era a relação entre elas e o próprio código, desse modo tem-se que :
