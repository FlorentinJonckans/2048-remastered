#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import random
import operator
import time

class fonction:
	def __init__(self):
		self.Tab=self.generate()			#Tableau du 2048 Normal
		self.Tab2=self.generateBlind()		#Tableau du 2048 du mode aveugle
		self.x=1	


###################################################################################
#								2048 MODE NORMAL 								  #
###################################################################################


	def generate(self):
		k=0
		tab=[]
		for i in range(4):
			tmp=[]
			for j in range(4):
				tmp.append(0)

			tab.append(tmp)

		while k!=2 :
			c=random.randint(0,3)
			l=random.randint(0,3)

			if tab[l][c]==0 :
				tab[l][c]=2
				k+=1

		return tab

#Ajout d'un 2 ou d'un 4 dans le 2048
	def implemante(self,t): 
		k=0
		while k!=1:
			c=random.randint(0,3)
			l=random.randint(0,3)

			n=random.randint(1,7)

			if n==7 and t[c][l]==0 :
				t[c][l]=4
				k+=1

			elif t[c][l]==0:
				t[c][l]=2
				k+=1

#Fusion entre 2 caseS
	def regroupement(self,tm):

		for i in range (len(tm)-1):
			
			if tm[i]==tm[i+1] :
					tm[i]=tm[i]*2
					tm[i+1]=0

		k=0
		for i in range (len(tm)):
			i=i-k
			if tm[i]==0:
				del tm[i]
				k+=1

		return tm

#Déplacement du 2048 vers la gauche
	def left(self,t):

		for i in range(4):

			tmp=[]
			for j in range (4) :
				if t[i][j]!=0 :
						tmp.append(t[i][j])
		
			tmp=self.regroupement(tmp)
			
			for j in range (4-len(tmp)) :
					tmp.append(0)

			t[i]=tmp

#Déplacement du 2048 vers la droite
	def right(self,t):

		for i in range(4):

			tmp=[]
			for j in range (4) :
				if t[i][3-j]!=0 :
						tmp.append(t[i][3-j])
			tmp=self.regroupement(tmp)
			
			for j in range (4-len(tmp)) :
					tmp.append(0)

			tmp[0],tmp[3]=tmp[3],tmp[0]
			tmp[1],tmp[2]=tmp[2],tmp[1]

			t[i]=tmp

#Déplacement du 2048 vers le haut
	def up(self,t):

		for i in range(4):

			tmp=[]
			for j in range (4) :
				if t[j][i]!=0 :

						tmp.append(t[j][i])
		
			tmp=self.regroupement(tmp)
		
			for j in range (4-len(tmp)) :
					tmp.append(0)
		
			for j in range (4):
				t[j][i]=tmp[j]


#Déplacement du 2048 vers la bas
	def down(self,t):

		for i in range(4):

			tmp=[]
			for j in range (4) :
				if t[3-j][i]!=0 :

						tmp.append(t[3-j][i])

		
			tmp=self.regroupement(tmp)

			for j in range (4-len(tmp)) :
					tmp.append(0)
		
			tmp[0],tmp[3]=tmp[3],tmp[0]
			tmp[1],tmp[2]=tmp[2],tmp[1]

			for j in range (4):
				t[j][i]=tmp[j]

#Calcul Score - défintion qui fonctionne mais problème d'implémentation 
	def score(self,t):
		score=0
		for i in range (4) :
			for j in range(4):
				if t[i][j]!=0 and t[i][j]!=2 :
					k=t[i][j]

					while k!=2 :
						score+=k
						k=k/2

		return score

#Vérifie si le 2048 est plein
	def Plein(self,t):
	
		for i in range(4):
			for j in range(4):
				if t[j][i]==0:
					return False

		return True



#Vérifie si un mouvement a été effectué
	def check(self,t,direction):

		tab=[]
		for i in range (4):
			tmp=[]
			for j in range (4):
				tmp.append(t[i][j])
			tab.append(tmp)

		if direction=="Left":
			self.left(tab)

		if direction=="Up":
			self.up(tab)


		if direction=="Right":
			self.right(tab)


		if direction=="Down":
			self.down(tab)

		for i in range (4):
			for j in range (4):
				if tab[i][j]!=t[i][j]:
					return True

		return False

#Vérifie si on a gagné
	def win(self,t):

		for i in range(4):
			for j in range(4):
				if t[i][j]==2048:
					return True 

		return False

#Vérifie si on a perdu
	def lose(self,t):
	
		for i in range(4):
			for j in range(3):
				if t[i][j]==t[i][j+1]:
					return False

		for j in range(3):
			for i in range(4):
				if t[j][i]==t[j+1][i]:
					return False

		if self.Plein(t)==False :
			return False
		return True


###################################################################################
#								2048 MODE AVEUGLE								  #
###################################################################################


	def generateBlind(self):
		k=0
		tab=[]

		for i in range(4):
			tmp=[]
			for j in range(4):
				tmp.append(0)

			tab.append(tmp)

		while k!=4 :
			c=random.randint(0,3)
			l=random.randint(0,3)

			if tab[l][c]==0 :
				tab[l][c]=1
				k+=1

		return tab

	def win2(self,t):

		for i in range(4):
			for j in range(4):
				if t[i][j]==1024:
					return True 

		return False

###################################################################################
#								2048 MODE VS IA									  #
###################################################################################


#Retourne un tableau trié dans l'ordre des meilleurs coups
	def IA(self,t):

		
		dico={}

	
		dico["left"]=self.leftIA(t)
		dico["up"]=self.upIA(t)
		dico["right"]=self.rightIA(t)
		dico["down"]=self.downIA(t)

		dicoTrié = sorted(dico.items(), key=operator.itemgetter(1))

		Tab=[]
		for i in range (4):
			Tab.append(dicoTrié[i][0])
			

		return Tab

#Fusion entre les cases
	def regroupementIA(self,tm):

		x=0
		for i in range (len(tm)-1):

			if tm[i]==tm[i+1] and tm[i]==128 :
				x+=100
			elif tm[i]==tm[i+1] :
				tm[i]=tm[i]*2
				tm[i+1]=0
				x+=3
		return x

#Calcul le nombre de point que donne un certain mouvement
#Plus x est faible, plus le coup est bon pour l'IA

	def leftIA(self,t):
		x=0
		for i in range(4):

			tmp=[]
			
			for j in range (4) :
				if t[i][3-j]!=0 :
						tmp.append(t[i][3-j])

			x+=self.regroupementIA(tmp)

		for j in range (4) :
			if t[j][0]==0 :
				x-=1


		return x
		

	def upIA(self,t):

		x=0
		for i in range(4):
			tmp=[]
			for j in range (4) :
				if t[3-j][i]!=0 :

						tmp.append(t[3-j][i])

			x+=self.regroupementIA(tmp)

		for j in range (4) :
			if t[0][j]==0 :
				x-=1

		return x


	def rightIA(self,t):

		x=0
		for i in range(4):
			tmp=[]
			for j in range (4) :
				if t[i][j]!=0 :
						tmp.append(t[i][j])

			x+=self.regroupementIA(tmp)


		for j in range (4) :
			if t[j][3]==0 :
				x-=1
				
		return x




	def downIA(self,t):

		x=0		
		for i in range(4):
			tmp=[]
			for j in range (4) :
				if t[j][i]!=0 :
					
						tmp.append(t[j][i])
		
			x+=self.regroupementIA(tmp)

		for i in range (4) :
			if t[3][i]==0 :
				x-=1

		return x

#différents niveaux de victoires
	def win3(self,t):

		for i in range(4):
			for j in range(4):
				if t[i][j]==512:
					return True 

		return False


	def win4(self,t):

		for i in range(4):
			for j in range(4):
				if t[i][j]==256:
					return True 

		return False