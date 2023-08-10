#TODO: Reimplementar métodos

class Fracao:
    
    __numerador = None
    __denominador = None
    
    def __init__(self, numerador:int, denominador:int) -> None:
        """_summary_

        Args:
            numerador (int): _description_
            denominador (int): _description_
        """
        self.numerador = numerador
        self.denominador = denominador

    @property        
    def denominador(self):
        return self.__denominador
    
    @denominador.setter
    def denominador(self, denominador):
        if denominador == 0:
            raise ValueError('Erro! Denominador não pode ser zero.')
        
        self.__denominador = denominador
        
    @property
    def numerador(self):
        return self.__numerador
    
    @numerador.setter
    def numerador(self, numerador):
        self.__numerador = numerador
                
    def soma(self, fracao):
        """_summary_

        Args:
            fracao (Fracao): _description_

        Returns:
            Fracao: _description_
        """
        numerador =  fracao.denominador*self.numerador + fracao.numerador*self.denominador
        denominador = fracao.denominador*self.denominador
        
        return Fracao(numerador, denominador)
    
    def subtracao(self, fracao):
        
        numerador =  fracao.denominador*self.numerador - fracao.numerador*self.denominador
        denominador = fracao.denominador*self.denominador
        
        return Fracao(numerador, denominador)
    
    def multiplicacao(self, fracao):
        
        numerador =  self.numerador * fracao.numerador
        denominador = fracao.denominador * self.denominador
        
        return Fracao(numerador, denominador)
    
    def divisao(self, fracao):
        
        numerador =  self.numerador * fracao.denominador
        denominador = fracao.numerador * self.denominador
        
        return Fracao(numerador, denominador)
    @property
    def apresenta(self):
        return f"{self.numerador}/{self.denominador}"
    
f1 = Fracao(5,5)
print(f1.apresenta)
f1.denominador = 2


