
# Projeto 4 : Fragmentamcão e Detecção de Erros

![Etapa Atual](doc/etapaAtualPilhaEnlace.png)

A etapa 4 do projeto consiste em implementar uma detecção mais eficiente de possíveis erros no pacote causados pela má transmissão. Para isso o método utilizado será o de fragmentação do pacote em porções menores, facilitando a detecção de arquivos corrompidos e sua retransmissão, acelerando o processo de transmissão como um todo. Para checagem de erros serão feitos o checksum, procedimento simples do cálculo do tamanho do pacote para checar se o tamanho inicial enviado pelo cliente confere com o payload recebido pelo servidor. E o CRC (Ciclic Redundancy Check, Verificação Cíclica de Redundância), método bem mais preciso do que o checksum para checagem de erros, consiste na realização de contas matemáticas com valores dos pacotes, caso o valor final seja igual ao fornecido pelo client o pacote muito provavelmente estará conforme o previsto, caso contrário muito provavelmente estará fora dos conformes.

A implementação consistirá em modificar a camada enlace da comunicação
