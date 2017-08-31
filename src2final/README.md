

# Projeto 2 : Datagrama

  Essa etapa do projeto consiste na modificação das camadas de enlace do protocolo de comunicação entre os computadores, com o objetivo de tornar a mesma um passo mais independente. Neste projeto será gerado um pacote, que encapsulará os dados (payload) e irá conter outros dados fundamentais para identificação das informações do pacote, como tamanho. Isso irá possibilitar que o server não precise previamente saber o tamanho do arquivo sendo transmitido.



## Código Final

O código possui os seguintes arquivos : server.py; server.py; enlace.py; enlaceTx.py; enlaceRx.py; interfaceFisica.py. Sendo cada um responsável por :

server.py : Código que prepara o computador para receber a imagem do Client.

client.py : Código que transmite a imagem e aguarda o fim da transmissão.

enlace.py : Interface de comunicação entre a aplicação e o enlace.

enlaceTx.py : Parte do enlace responsável por encapsular os dados em um pacote.

enlaceRx.py : Parte do enlace responsável por receber e desencapsular os dados.

interfaceFisica.py : Código que lida com o envio dos dados para o Arduino e recebimento.


##Informações do Header e End Of Package

O header (Head) e End Of Package (EOP) são as partes do pacote que servirão de referência para o server, se localizando dentro do pacote, assim ele saberá qual tamanho do próprio Head e EOP, tamanho do payload, e com isso o recebimento será mais preciso quanto à perda de dados e corrompimento de dados.
