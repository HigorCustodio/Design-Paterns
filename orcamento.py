'''
Devido o python não conter restrições de acesso ao código, é utilizado 
a implementação do duble dunder para que se indique que a variável | método em
questão, se trata de uma variável | método interno do objeto, sendo assim, não
deve ser modificado externamente a classe.

Um exemplo para esse caso seria a variável interna self.valor, sempre que é 
instânciado um objeto, seus métodos e variáveis podem ser acessados através 
do ".", porém, como desejamos restringir o acesso externo a essa variável, é 
utilizado os dunders para que ao se inserir o "." após a instância do objeto
a variável em questão não apareça entre os primeiros métodos e propriedades
do objetos, isso age como uma "camuflagem" visto que ainda é possível realizar
a chamada e a alteração desse método | variável, porém, o programador que estiver
fazerndo isso estará sendo avisado que não é recomendado alterar o valor da
variável | método, visto que qualquer quebra de código será de sua 
responsabilidade.

Visto que uma variável é interna de uma classe, porém, o seu valor precisa ser
resgatado fora dela, como posso fazer?
    -   Existirão casos onde será necessário resgatar (get) o valor de uma 
    variável | método interno de um objeto, para isso, podemos implementar um
    método getter:
        ```
            def valor(self):
                return self.__valor
        ```
        • Desta forma, ao se chamar o método self.valor() será retornado o valor
        atribuído a variável interna self.__valor.
        
Como posso chamar um getter de uma variável interna como uma property do objeto?
    -   Em python é possível realizar a chamada de uma variável interna de modo
    que se comporte como uma propriedade do objeto, assim, quando inserido "."
    após a instância de um objeto, aparecerá e será possível acessar a variável
    do objeto.
        ```
        #!Encapsulamento de uma variável(valor):
            #Construtor da classe:
            class Orcamento(object):
                def __init__(self, valor) -> None:
                    self.__valor = valor
                    
                #Construção do getter na classe:
                @property
                def valor(self):
                    return self.__valor
            
            # Chamada externa do getter:
                #Entrada:
                instância_objeto = Orcamento(valor=50)
                print(instância_objeto.valor)
                
                #Saída:
                >>> 50
            #? Essa construção de uma nova propriedade de uma classe irá permitir somente a leitura do valor atribuido à self.__valor, sendo assim, não será possível realizar a edição | atribuir novos valores a variável interna self.__valor.
            
            #? Caso seja necessário settar o valor de self.__valor externamente, pode-se, criar um novo método da classe implementado o decorator @setter.
        ```
'''
class Orcamento(object):
    def __init__(self, valor) -> None:
        self.__valor = valor
    
    @property
    def valor(self):
        return self.__valor
 
 
# if __name__ == "__main__":
#     orcamento = Orcamento(valor=50)
#     # print(orcamento.valor)