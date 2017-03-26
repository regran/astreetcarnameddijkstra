class pHeap:
    def __init__(self):		#constructs new tree array
        self.space = 0 #next empty space
        self.a = []    #tree array

    def push(self, s, d):		#adds s in order with smallest d at top
        swap = [0,0]	#holder for swaps
        check = self.space		#hold location of s
        self.a+=[[s,d]]			#add at space
        while(check!=0 and self.a[check][1]<self.a[int((check-1)/2)][1]): #carry s up heap until it's ordered
            swap[0]=self.a[check][0]
            swap[1]=self.a[check][1]
            self.a[check][0]=self.a[int((check-1)/2)][0]
            self.a[check][1]=self.a[int((check-1)/2)][1]
            if(check/2!=0):
                self.a[int(check/2)-1][0]=swap[0]
                self.a[int(check/2)-1][1]=swap[1]	
            else: 
                self.a[int(check/2)][0]=swap[0]
                self.a[int(check/2)][1]=swap[1]
            check=int((check-1)/2)
        self.space+=1	#move to next space	

    def pop(self):
        swap = [0,0] 	#holder for swaps
        r=self.a[0][0]			#hold return data			
        #check holds location of thing being ordered
        if(self.isEmpty()):			#check if there's something to pop
            return -1
        self.space=self.space-1		#move space back
        self.a[0][0]=self.a[self.space][0]		#move last element to root
        self.a[0][1]=self.a[self.space][1]
        self.a.pop()	#make space empty
        check=0
        while(check<self.space and check*2+1<self.space and (self.a[check][1]>self.a[check*2+1][1] or(check*2+2>=self.space or self.a[check*2+2][1]<self.a[check][1]))):
	#go down heap and swap until ordered
            if(self.space==check*2+2 or self.a[check*2+2][1]>self.a[check*2+1][1]):	#move smaller element up
                swap[0]=self.a[check][0]
                swap[1]=self.a[check][1]
                self.a[check][0]=self.a[check*2+1][0]
                self.a[check][1]=self.a[check*2+1][1]
                self.a[check*2+1][0]=swap[0]
                self.a[check*2+1][1]=swap[1]
                check=check*2+1
            else:
                swap[0]=self.a[check][0]
                swap[1]=self.a[check][1]
                self.a[check][0]=self.a[check*2+2][0]
                self.a[check][1]=self.a[check*2+2][1]
                self.a[check*2+2][0]=swap[0]
                self.a[check*2+2][1]=swap[1]
                check=check*2+2
        return r

    def inspect(self):			#peak at top
        if(self.isEmpty()): return -1
        return self.a[0][0]

    def isEmpty(self):		#check if empty
        return self.space==0

