import threading
import time

saldo_global = 0
lock = threading.Lock()

class Transaccion():
	def __init__(self):
		self.saldo = saldo_global

	def get_saldo(self):
		return self.saldo

	def obtenerSaldo(self):
		self.saldo = saldo_global

	def incrementarSaldo(self, porcentaje):
		self.saldo = self.saldo + self.saldo * (porcentaje * 0.01)
		#print (porcentaje, self.saldo, saldo_global)

	def depositar(self, monto):
		self.saldo = self.saldo + monto

	def retirar(self,monto):
		aux = self.saldo - monto

		if aux >= 0: 
			self.saldo = aux
		else:
			self.saldo = -1




class Coordinador():
	def __init__(self,saldo_inicial):
		#self.saldo = saldo_global
		self.hilos = {}
		self.tmp = 0

	def abreTransaccion(self, funcion, args_p = None):
		# LOCK RECURSO GLOBAL lock(saldo_global)
		lock.acquire()
		t = Transaccion()
		return t 



	def cierraTransaccion(self, TID):


    	lock.release() # release lock, no matter what

		hilo = self.hilos[TID]
		
		hilo.start()
		#hilo.join()
		
		#print('cierraTransaccion',self.tmp)
		if self.tmp == -1:
			print "No puedes retirar tanto"
			#TODO:
			#this.abortaTransaccion()
		
		else:
			#saldo_global = self.tmp
			saldo_global = self.tmp
			print "nuevo saldo: " + str(saldo_global) + '\n'
			del self.hilos[TID]

	def abortaTransaccion(TID):
		del self.hilos[TID]
		print str(TID) + " abortado"


	def execHilos(self,):
		for hilo in self.hilos:
			hilo.start()

def main():
	coordinador = Coordinador(1000)

	#TODO CAMBIOS 
	
	# t1 = coordinador.abreTransaccion()
	# t1.deposita(100)
	# t1.retira(50)
	# t1.cierraTransaccion()
	
	# t2 = coordinador.abreTransaccion()
	# t2.deposita(100)
	# t2.retira(50)
	# t2.cierraTransaccion()
	
	# for i in range(100):
	# 	coordinador.cierraTransaccion(coordinador.abreTransaccion("retirar", 1))
	# 	coordinador.cierraTransaccion(coordinador.abreTransaccion("depositar", 1))

	# coordinador.cierraTransaccion(coordinador.abreTransaccion("incrementarSaldo",100))
	# coordinador.cierraTransaccion(coordinador.abreTransaccion("obtenerSaldo"))
	# coordinador.cierraTransaccion(coordinador.abreTransaccion("depositar", 25))

"""
	th1 = coordinador.abreTransaccion("incrementarSaldo", 100)
	#th2 = coordinador.abreTransaccion("incrementarSaldo", 200)

	coordinador.cierraTransaccion(th1)
	#coordinador.cierraTransaccion(th2)
"""
#EXECUTE
main()