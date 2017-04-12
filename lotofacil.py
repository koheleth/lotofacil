#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
#  lotofacil.py
#
#  Copyright 2017 Marcos Aurélio Chaves <marcos@HP-Pavilion-Sleekbook-14-PC>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from xlrd import open_workbook,cellname
import collections
from math import *

def ler(arq_xls):
	workbook = open_workbook(arq_xls)
	sheet = workbook.sheet_by_index(0)

	for i in xrange(sheet.nrows):
		yield sheet.row_values(i)

def sorteio():
	for i in range(15):
		print(i)

def combinacao(n, p):
	if (n>=p):
		return factorial(n)/(factorial(p)*factorial(n-p))
	else:
		return 0

def aranjo(n,p):
	if (n>=p):
		return factorial(n)/factorial(n-p))
	else:
		return 0

def main(args):
	pares = [4,6,8,10,12,14,16,18,20,22,24]#11
	impares = [1,9,15,21,25]#5
	primos = [2,3,5,7,11,13,17,19,23]#9
	todos = range(1, 16)
	valores = range(15)
	vimpares = 0
	vpares = 0
	vprimos = 0
	frequeciaPadroes = open('frequenciaPadroes.txt', 'w')
	fPadroes = []
	listaPadroes = open('listaPadroes.txt', 'w')
	lPadroes = []
	frequenciaDezenas = open('frequenciaDezenas.txt', 'w')
	fDezenas = []
	listaDezenas = open('listaDezenas.txt', 'w')
	lDezenas = []
	combNumeros = []
	listaGeral = []
	sorteios = 0
	print('Iniciando os calculos')
	for linha in ler('D_LOTFAC.xls'):
		sorteios +=1
		lDezenas.append(' '+str(linha)+'\n')
		for coluna in linha[2:]:

			for i in impares:
				if (coluna == i):
					vimpares += 1

			for p in pares:
				if (coluna == p):
					vpares += 1

			for np in primos:
				if (coluna == np):
					vprimos += 1

			for t in todos:
				if (coluna == t):
					valores[t-1] += 1
		#print(str(linha[0])+' - '+str(linha[1]) + ' -> '+ str(vprimos)+'NP + '+ str(vimpares)+'i + '+str(vpares)+'P' )
		lPadroes.append(str(linha[0])+' - '+str(linha[1]) + ' -> '+ str(vprimos)+'NP + '+ str(vimpares)+'i + '+str(vpares)+'P \n' )
		listaGeral.append(str(vprimos)+'NP+'+ str(vimpares)+'i+'+str(vpares)+'P')
		vimpares = 0
		vpares = 0
		vprimos = 0

	print('Calculando as frequencia das dezenas')
	for i in todos:
		fDezenas.append('Numero '+str(i)+' = '+str(valores[i-1])+'\n')

	print('Calculando as frequencia dos padrões')
	c=collections.Counter(listaGeral)
	dic = c.most_common(50)

	percentual = 0
	for i in dic:
		#print(str(i[1])+' - '+str(sorteios)+' - '+str((i[1] / float(sorteios))))
		percentual = (i[1] / float(sorteios))*100
		fPadroes.append(str(i[0])+' = '+str(i[1])+' ('+str(percentual)+'%) \n')

	frequeciaPadroes.writelines(fPadroes)
	frequeciaPadroes.close

	listaPadroes.writelines(lPadroes)
	listaPadroes.close

	frequenciaDezenas.writelines(fDezenas)
	frequenciaDezenas.close

	listaDezenas.writelines(lDezenas)
	listaDezenas.close
	#print(str(combinacao(11,5)*combinacao(5,3)*combinacao(9,7))+ ' combinacoes ')
	print('Total de sorteios: '+str(sorteios))
	print('Feito!!!!!!')

	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
