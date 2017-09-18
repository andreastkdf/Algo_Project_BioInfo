# 	3I003 PROJET ALGOLITHMIQUE / ALIGNEMENT DE SEQUENCES ADN 
# 	KOSTAKIS ANDREA - 2963152

# 	PARTIE 4
# 	MISE EN OEUVRE
import sys
import numpy as np
global d_gap
import time
d_gap = 2
 
def d(i,j): # valeurs utilisees pour l execution; exemple sujet
	x = X[i-1]
	y = Y[j-1]

	if(x==y):
		return 0
	elif((x=='A' and y=='T') or (x=='T' and y=='A') or (x=='C' and y=='G') or (x=='G' and y=='C')):
		return 3
	else:
		return 4


def lecture():   # 4.1 : lecture des instances ADN a partir des fichiers .adn	
	global m, n, X, Y #visibles sur les prochaines fonctions
	X = []
	Y = []
	adn_file = open(sys.argv[1],"r")
	print("Hello.\nReading adn file successfully \n\nX and Y length : ")
	m = int(adn_file.readline().rstrip("\n"))
	print"X: m=", m
	n = int(adn_file.readline().rstrip("\n"))
	print"Y: n=", n, "\n"

	sequences = ()	
	sequences = adn_file.read().rstrip("\n").replace(" ","")

	for i in range (m):
		X.append((sequences[i]))
	for j in range (m+1,m+n+1):
		Y.append((sequences[j]))
	print "X: \n",X
	print "Y: \n",Y
	adn_file.close()

	#print len(X)
	#print len(Y)

lecture()

#print X, Y , m , n

def COUT1(): #4.2
	global F
	F=np.empty((m+1,n+1),int)
	F[0,0] = 0
	for i in range (0,m+1):
		F[i,0] = 0
	for j in range (0,n+1):
		F[0,j] = 0
	for i in range(1, m+1):
		for j in range(1,n+1):
			a = F[i-1,j]+d_gap
			b = F[i-1,j-1]+d(i-1,j-1)
			c = F[i,j-1]+d_gap
			F[i,j] = min(a,b,c)
	print "\n--> Valeur alignement cout minimal avec COUT1:",F[m,n]
start_COUT1 = time.time()
COUT1()
end_COUT1 = time.time()
#4.3
def SOL1(): 
	i = m
	j = n
	res = []
	while (i>0 and j>0):
		tmpMin = min(F[i-1][j-1], F[i-1][j], F[i][j-1])
		if(tmpMin == F[i-1][j-1]):
			res.append(i)
			res.append(j) 
			i=i-1
			j=j-1
			#print X[i] , " " , Y[j]
		elif(tmpMin == F[i][j-1]):
			j=j-1
			#print "- " , Y[j]
			res.append(0)
			res.append(j)
		else:
			i=i-1
			#print X[i] , " -"
			res.append(i)
			res.append(0)
	print "Parcours inverse: ", res
	return res


#4.3
def afficherAl():
	global start_SOL1
	global end_SOL1
	start_SOL1 = time.time()
	liste  = SOL1()
	end_SOL1 = time.time()
	l = len(liste)
	for i in range(l-1,0,-2):
		if (liste[i-1] == 0): 
			print '-' , Y[liste[i]-1]
		elif (liste[i] == 0):
			print X[liste[i-1]], '-'
		else:
			print X[liste[i-1]-1],Y[liste[i]-1]

print "Alignement optimal (SOL1) : "
afficherAl()

print "temps d'execution de COUT1: ", (end_COUT1 - start_COUT1), " sec"
print "temps d'execution de SOL1" , (end_SOL1 - start_SOL1), "sec"

file1 = open('timeCOUT1.txt','a')
file1.write(str(m)+' '+str((end_COUT1 - start_COUT1))+'\n')
file1.close()

file2 = open('timeSOL1.txt','a')
file2.write(str(m)+' '+str(end_SOL1 - start_SOL1)+'\n')
file2.close()
