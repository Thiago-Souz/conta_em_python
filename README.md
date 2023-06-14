# conta_em_python

Uma classe de Conta Bancária que permite realizar operações básicas como depósito, saque, transferência e extrato.

Uso
Você pode usar a classe Conta para criar objetos de contas bancárias e realizar as seguintes operações:

python
Copy code
# Criando uma instância da classe Conta
minha_conta = Conta(numero, titular, saldo, limite)

# Realizando um depósito
minha_conta.deposita(valor)

# Realizando um saque
minha_conta.saca(valor)

# Realizando uma transferência para outra conta
minha_conta.transfere(destino, valor)

# Obtendo o extrato da conta
minha_conta.extrato()
Métodos
__init__(self, numero, titular, saldo, limite)
Construtor da classe Conta. Recebe os parâmetros numero, titular, saldo e limite para inicializar os atributos da conta.

extrato(self)
Imprime o extrato da conta, mostrando o saldo e o titular.

deposita(self, valor)
Realiza um depósito na conta, adicionando o valor informado ao saldo.

__saque_disponivel(self, saque)
Verifica se o valor de saque informado é menor ou igual ao limite disponível na conta.

saca(self, valor)
Realiza um saque na conta, diminuindo o valor informado do saldo. Caso o valor de saque seja maior que o limite disponível, exibe uma mensagem de saldo indisponível.

transfere(self, destino, valor)
Realiza uma transferência de valor da conta atual para uma conta de destino. Utiliza o método saca() para realizar o saque e o método deposita() da conta de destino para realizar o depósito.

Propriedades
A classe Conta também possui as seguintes propriedades:

saldo: Retorna o saldo da conta.
titular: Retorna o titular da conta.
limite: Retorna o limite de saque da conta.
Contribuição
Contribuições são bem-vindas! Para sugestões, melhorias ou correções, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT.
