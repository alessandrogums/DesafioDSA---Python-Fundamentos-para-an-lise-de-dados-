class BubbleSort(object):
    def __init__(self,vetor):
        self.vetor=vetor

    def sortear(self):
        try:
            for x in range(len(self.vetor)):
                for y in range(x+1,len(self.vetor)):
                    if   self.vetor[y] < self.vetor[x]:
                        self.vetor[x],self.vetor[y]= self.vetor[y],self.vetor[x]
            return self.vetor and len(self.vetor)
        except TypeError:
           return 'None não pode ser avaliado!'
