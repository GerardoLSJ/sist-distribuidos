import threading
import time

class Coordinador():
	saldo = 0
	def __init__(self,saldo_inicial):
		self.saldo = saldo_inicial
		self.hilos = {}
		self.resultado = 0
	
	def obtenerSaldo(self):
		self.resultado = self.saldo

	def incrementarSaldo(self, porcentaje):
		self.resultado = self.saldo + self.saldo * (porcentaje * 0.01)
		#print (porcentaje, self.resultado, self.saldo)


	def depositar(self, monto):
		self.resultado = self.saldo + monto

	def retirar(self,monto):
		aux = self.saldo - monto

		if aux >= 0: 
			self.resultado = aux

		else:
			self.resultado = -1

	def abreTransaccion(self, funcion, args_p = None):
		hilo = {}
		#print(funcion,args_p)
		if funcion == "obtenerSaldo":
			hilo = threading.Thread(target=self.obtenerSaldo)
		
		elif funcion == "incrementarSaldo":
			hilo = threading.Thread(target=self.incrementarSaldo, args=(args_p,))
		
		elif funcion == "depositar":
			hilo = threading.Thread(target=self.depositar, args=(args_p,))
		
		elif funcion == "retirar":
			hilo = threading.Thread(target=self.retirar, args=(args_p,))
		else:
			print "No entra"
		
		hilo_name = hilo.getName()
		self.hilos[hilo_name] = hilo
		#print(self.hilos)
		return hilo_name


	def cierraTransaccion(self, TID):
		hilo = self.hilos[TID]
		
		hilo.start()
		hilo.join()
		
		#print('cierraTransaccion',self.resultado)
		if self.resultado == -1:
			print "No puedes retirar tanto"
		
		else:
			self.saldo = self.resultado
			print "nuevo saldo: " + str(self.saldo)
			del self.hilos[TID]

	def abortaTransaccion(TID):
		del self.hilos[TID]
		print str(TID) + " abortado"


def main():
	coordinador = Coordinador(1000)
	#th1 = coordinador.abreTransaccion("incrementarSaldo", 50)
	#th2 = coordinador.abreTransaccion("obtenerSaldo")
	#th3 = coordinador.abreTransaccion("depositar", 50)
	th4 = coordinador.abreTransaccion("retirar", 50)
	#time.sleep(0.5)
	th5 = coordinador.abreTransaccion("depositar",100)
	#time.sleep(0.5)
	th6 = coordinador.abreTransaccion("incrementarSaldo",100)
	#time.sleep(0.5)
	th7 = coordinador.abreTransaccion("obtenerSaldo")
	
	#coordinador.cierraTransaccion(th1)
	#coordinador.cierraTransaccion(th2)
	#coordinador.cierraTransaccion(th3)
	coordinador.cierraTransaccion(th4)
	coordinador.cierraTransaccion(th5)
	coordinador.cierraTransaccion(th6)
	coordinador.cierraTransaccion(th7)

	time.sleep(1)
	print('delay 1 seg')
	coordinador.cierraTransaccion(th6)
"""
	th1 = coordinador.abreTransaccion("incrementarSaldo", 100)
	#th2 = coordinador.abreTransaccion("incrementarSaldo", 200)

	coordinador.cierraTransaccion(th1)
	#coordinador.cierraTransaccion(th2)
"""
#EXECUTE
main()