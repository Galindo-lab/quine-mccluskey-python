
# Documentacion 
# https://github.com/Galindo-lab/quine-mccluskey-python

_D='DATO INVALIDO'
_C='?\n'
_B=True
_A=None
def remove_nones(a):
	i=0
	while _B:
		if i>=len(a):break
		if a[i]==_A:a.pop(i)
		else:i+=1
def diferencias(a,b):
	count=0
	for i in range(len(a)):
		if a[i]!=b[i]:count+=1
	return count
def bindigits(number,digits):return '{0:0{1}b}'.format(number,digits)
def es_numerico(value):
	try:int(value);return _B
	except ValueError:return False
class Termino:
	def __init__(self,variables,implicantes):self.implicantes=implicantes;self.variables=variables;self.representacion=''
	def __str__(self):foo=self.representacion+' '+str(self.implicantes);return foo
	@classmethod
	def por_minterminos(cls,variables,implicantes):foo=Termino(variables,implicantes);foo.regenerar();return foo
	def combine(self,a):implicantes=tuple(set(self.implicantes+a.implicantes));variables=self.variables;foo=Termino.por_minterminos(variables,implicantes);return foo
	def regenerar(self):
		b=bindigits(self.implicantes[0],self.variables);output=[_A]*self.variables
		for implicante in self.implicantes:
			a=bindigits(implicante,self.variables)
			for i in range(len(a)):output[i]='-'if a[i]!=b[i]else b[i]
			b=''.join(output)
		self.representacion=''.join(output)
	def es_adyacente(self,b):return diferencias(self.representacion,b.representacion)==1
def captura_entero(message=''):
	while _B:
		foo=input(message+_C)
		if es_numerico(foo):break
		print(_D)
	return int(foo)
def captura_list(message='',separator=','):foo=input(message+_C).split(separator);return[int(e)for e in foo if es_numerico(e)]
def captura_char(message='',end=_C):
	while _B:
		foo=input(message+end)
		if len(foo)>0:break
		print(_D)
	return foo[0]
def en_rango(numero_variables,activaciones,redundancias):
	A='FUERA DE RANGO';lim=(2<<numero_variables-1)-1
	for i in range(len(activaciones)):
		if activaciones[i]>lim:print(activaciones[i],A);activaciones[i]=_A
	for i in range(len(redundancias)):
		if redundancias[i]>lim:print(redundancias[i],A);redundancias[i]=_A
	remove_nones(activaciones);remove_nones(redundancias)
def duplicados(activaciones,redundancias):activaciones_set=set(activaciones);redundancias[:]=list(set(redundancias)-activaciones_set);activaciones[:]=list(activaciones_set)
def extraer_primos(nvariables,terminos):
	a=[];b=[];primos=[];existentes=[]
	for termino in terminos:a.append(Termino.por_minterminos(nvariables,[termino]))
	while len(a)!=0:
		for i in a:
			cnv=0
			for j in a:
				if not i.es_adyacente(j):continue
				cnv+=1;termino=i.combine(j)
				if not termino.representacion in existentes:b.append(termino);existentes.append(termino.representacion)
			if cnv==0:primos.append(i)
		a=b.copy();b=[]
	return primos
def esenciales(primos,minter):
	indice_esenciales=[];foo=[]
	for i in minter:
		freq=0;term=_A
		for count in range(len(primos)):
			j=primos[count]
			if not i in j.implicantes:continue
			if freq==1:term=_A;break
			freq+=1;term=count
		if term!=_A and not term in indice_esenciales:indice_esenciales.append(term)
	for i in indice_esenciales:foo.append(primos[i]);primos[i]=_A
	remove_nones(primos);return foo
def terminos_faltantes(esenciales,minterminos):
	terminos=set([])
	for i in esenciales:terminos=terminos|set(i.implicantes)
	faltantes=set(minterminos)-terminos;return list(faltantes)
def captura_tabla(variables):
	A='-----+---------+-----';activaciones=[];redundancias=[];print(A);print(' DEC | BIN     | OUT ');print(A)
	for i in range(2<<variables-1):
		message=' %3d | %s%s |  '%(i,bindigits(i,variables),' '*(7-variables));foo=captura_char(message,end='')
		if foo=='-':redundancias.append(i)
		elif foo=='1':activaciones.append(i)
	print(A);return activaciones,redundancias
def x():
	A='---------------------';print('');print(A);print('      REDUCCION      ');print('  DE FUNCION LOGICA  ');print(A);print('');entrada=captura_char('1.Lista // 2.Tabla');numero_variables=captura_entero('NUMERO DE VARIABLES')
	if entrada=='2':print('');minterminos,redundancias=captura_tabla(numero_variables)
	else:minterminos=captura_list('ACTIVACION');redundancias=captura_list('REDUNDANCIAS')
	print('');duplicados(minterminos,redundancias);en_rango(numero_variables,minterminos,redundancias);print(minterminos);print(redundancias);print('');print(A);print('      RESULTADO      ');print(A);print('');todos_los_terminos=minterminos+redundancias;primos=extraer_primos(numero_variables,todos_los_terminos);terminos_esenciales=esenciales(primos,minterminos);faltantes=terminos_faltantes(terminos_esenciales,minterminos);print('ESENCIALES:')
	for i in terminos_esenciales:print(i)
	print('');print('NO ESENCIALES:',faltantes)
	for i in primos:print(i)
	print('')
x()
