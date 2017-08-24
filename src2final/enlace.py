#REALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
# Importa pacote de tempo
import time

# Construct Struct
from construct import *

# Interface Física
from interfaceFisica import fisica

# enlace Tx e Rx
from enlaceRx import RX
from enlaceTx import TX

class enlace(object):
    """ This class implements methods to the interface between Enlace and Application
    """

    def __init__(self, name):
        """ Initializes the enlace class
        """
        self.fisica      = fisica(name)
        self.rx          = RX(self.fisica)
        self.tx          = TX(self.fisica)
        self.connected   = False

    def enable(self):
        """ Enable reception and transmission
        """
        self.fisica.open()
        self.rx.threadStart()
        self.tx.threadStart()

    def disable(self):
        """ Disable reception and transmission
        """
        self.rx.threadKill()
        self.tx.threadKill()
        time.sleep(1)
        self.fisica.close()


    def sendData(self, data):
        """ Send data over the enlace interface
        """

        #Início do protocolo

        self.StructEop()
        self.StructHead()
       
        #Encapuslamento do arquivo--> ENVIO
       	package = Package(data).buildPackage()
        self.tx.sendBuffer(data)

    def getData(self, size):
        """ Get n data over the enlace interface
        Return the byte array and the size of the buffer
        """
        data,size = self.rx.unbuildDataPacket()
        return(data,len(data),size)


    #ESTRUTURA HEAD
    def headStruct(self):
        self.headStruct = 0xAA
        self.headStruct = Struct("start"/ Int16ub,
                                "size"/ Int16ub)

    #HEAD IMPLEMENTADO
    def buildHead(self,datAlen):
        head = self.headStruct.build(dict(
                                    start = self.headStart,
                                    size = datAlen))
        
        return head

    #ESTRUTURA End Of Packet(EOP)
    def EopStruct(self):

        self.endStart = 0xFF
        self.endStruct = Struct("Otavio"/Int8ub,
                                "Manoel"/Int8ub,
                                "Ricardo"/Int8ub)

    #EOP IMPLEMENTADO
    def buildEop(self):
        end = self.endStruct.build(dict(
                                    Otavio = 0x04,
                                    Manoel = 0x05,
                                    Ricardo = 0x06))
        return end


    def buildDataPacket(self,data):
        pack = self.buildHead(len(data))
        print(len(data)) # Printar o size 

        #CONCATENAÇÃO DO HEADER,DATALEN E O END OF PACKET
        pack += data
        pack += self.buildEop()
        
        return pack







