class CalculadorImpostos(object):
    
    def realiza_calculo(self, orcamento, imposto):
        if imposto == "ISS":
            imposto_calculado = orcamento.valor * 0.1
        if imposto == "ICMS":
            imposto_calculado = orcamento.valor * 0.06
        return imposto_calculado
        '''
        Utilizando o paradigma procedural, para cada imposto que será 
        implementado, será implementado um "if | elif | else" dentro do 
        método self.realiza_calculo().
        
        Essa escolha de paradigma pode resultar em alguns "problemas"
        futuramente ao se utilizar o código:
        Possíveis problemas:
            •   Duplicidade de código:
                - Ao se implementar o paradigma procedural neste exemplo,
                caso seja necessário implementar o cálculo do imposto em
                outra parte do código, não será possível a utilização do
                mesmo código devido não ser possível acessar a lógica 
                interna desse método, logo, será necessário criar em um
                novo local o mesmo códigom o que irá gerar duplicidade de
                um mesmo código, o que é considerado uma má prática.
            
            •   Crescimento do código:
                - Sempre que necessário a implementação de um novo imposto
                para o cálculo, será necessário a criação de mais um 
                "if|elif" o que em dado momento poderá resultar um código 
                extremamente grande quer irá realizar somente uma seleção
                do imposto.
            
        '''
    
if __name__ == "__main__":
    from orcamento import Orcamento
    
    calculador = CalculadorImpostos()
    
    orcamento = Orcamento(valor=500)
    
    print(round(calculador.realiza_calculo(
        orcamento=orcamento, imposto="ISS")))
    print(round(calculador.realiza_calculo(
        orcamento=orcamento, imposto="ICMS")))