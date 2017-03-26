class pHeap:
	def __init__(self):		#constructs new tree array
		space = 0 #next empty space
		a = [[]]    #tree array

	def push(self, s, d):		#adds s in order with smallest d at top
		swap = [0,0]	#holder for swaps
		check = space		#hold location of s
		a[space][0]=s			#add at space
		a[space][1]=d
		while(check!=0 and a[check][1]<a[(check-1)/2][1]): #carry s up heap until it's ordered
			swap[0]=a[check][0]
			swap[1]=a[check][1]
			a[check][0]=a[(check-1)/2][0]
			a[check][1]=a[(check-1)/2][1]
			if(check/2!=0):
				a[check/2-1][0]=swap[0]
				a[check/2-1][1]=swap[1]
			
			else: 
				a[check/2][0]=swap[0]
				a[check/2][1]=swap[1]
			check=(check-1)/2
		space+=1	#move to next space	

		
	def pop(self):
		swap = [0,0] 	#holder for swaps
		r=a[0][0]			#hold return data			
                #check holds location of thing being ordered
		if(isEmpty()):			#check if there's something to pop
			return -1

		space=space-1		#move space back
		a[0][0]=a[space][0]		#move last element to root
		a[0][1]=a[space][1]
		a[space][0]=a[space+1][0]	#make space empty
		a[space][1]=a[space+1][1]
		check=0
		while(check<space and check*2+1<space and (a[check][1]>a[check*2+1][1] or a[check*2+2][1]<a[check][1])):
		#go down heap and swap until ordered
			if(a[check*2+2][1]>a[check*2+1][1] or space==check*2+2):	#move smaller element up
				swap[0]=a[check][0]
				swap[1]=a[check][1]
				a[check][0]=a[check*2+1][0]
				a[check][1]=a[check*2+1][1]
				a[check*2+1][0]=swap[0]
				a[check*2+1][1]=swap[1]
				check=check*2+1
			else:
				swap[0]=a[check][0]
				swap[1]=a[check][1]
				a[check][0]=a[check*2+2][0]
				a[check][1]=a[check*2+2][1]
				a[check*2+2][0]=swap[0]
				a[check*2+2][1]=swap[1]
				check=check*2+2

		return r
	def inspect(self):			#peak at top
		if(isEmpty()): return -1
		return a[0][0]

	def isEmpty(self):		#check if empty
		return space==0
	
