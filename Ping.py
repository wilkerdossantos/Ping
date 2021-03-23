import subprocess

class Ping:
    arquivo = open('pingou.txt','w')
    arquivo.close()

    def __init__(self):
        self.lista_ip = self.import_ip()

    def pinga(self):
        for ip in self.lista_ip:
            ping = subprocess.run(['ping','-w','1',f'{ip}'], capture_output=True)
            print(ip, self.valida_ping(ping, ip))

    def valida_ping(self, ping, ip):
        saida = str(ping.stdout)
        indice = saida.find(',') + 2
        if saida[indice] != '1':
            arquivo = open('pingou.txt','a')
            arquivo.write(f'{ip}\n')
            arquivo.close()
            return True
        else:
            return False

    def import_ip(self):
        arquivo = open('ip.txt', 'r')
        lista = [linha.strip() for linha in arquivo]
        arquivo.close()
        return lista

ip = Ping()

ip.pinga()
