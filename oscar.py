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
		print(funcion, args_p)
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
			print "nuevo saldo: " + str(self.saldo) + '\n'
			del self.hilos[TID]

	def abortaTransaccion(TID):
		del self.hilos[TID]
		print str(TID) + " abortado"


def main():
	coordinador = Coordinador(1000)
	coordinador.cierraTransaccion(coordinador.abreTransaccion("retirar", 50))
	coordinador.cierraTransaccion(coordinador.abreTransaccion("depositar", 50))
	coordinador.cierraTransaccion(coordinador.abreTransaccion("incrementarSaldo",100))
	coordinador.cierraTransaccion(coordinador.abreTransaccion("obtenerSaldo"))
	coordinador.cierraTransaccion(coordinador.abreTransaccion("depositar", 25))

"""
	th1 = coordinador.abreTransaccion("incrementarSaldo", 100)
	#th2 = coordinador.abreTransaccion("incrementarSaldo", 200)

	coordinador.cierraTransaccion(th1)
	#coordinador.cierraTransaccion(th2)
"""
#EXECUTE
main()