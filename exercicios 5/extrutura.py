'''a. Identifique a estrutura de dados mais apropriada entre: lista, tupla,
conjunto (set) e dicionário (dict).
b. Justifique sua escolha em 2 ou 3 frases. Sua justificativa deve
considerar pelo menos duas das seguintes características:
i. Mutabilidade: Os dados precisam ser alterados (adicionados,
removidos, modificados) após a criação?
ii. Ordenação: A ordem dos elementos é importante e deve ser
mantida?
iii. Unicidade: Os elementos devem ser únicos, sem duplicatas?
iv. Acesso/Busca: Como os dados serão acessados? Por um índice
numérico, por uma chave específica, ou apenas verificando a
existência de um item?'''

#Cenário 1: Lista de Tarefas (To-Do List): Você está criando um aplicativo simples de lista de tarefas. Um usuário precisa armazenar suas tarefas do dia. Ele deve ser capaz de adicionar novas tarefas, marcar tarefas como concluídas (removê-las) e ver as tarefas na ordem em que foram adicionadas.
# Estrutura de dados :Lista
# Justificativa :Os dados teram alterações conforme o uso, sendo sua ordenação importante, onde seu elementos seram acessados por itens. 


#Cenário 2: Coordenadas RGB de uma Cor: Em um software de design gráfico, você precisa representar uma cor específica, como o vermelho puro da Google, que é composto pelos valores (234, 67, 53). Esses três valores (Vermelho, Verde, Azul) sempre andam juntos, em uma ordem fixa, e nunca devem ser alterados individualmente para não corromper a representação da cor.
#Estrutura de Dados: Tupla
#Justificativa: A ordem dos elementos são importante  e eles não devem ser alterados apos a criação.

#Cenário 3: Inscrições em um Sorteio: Você está organizando um sorteio online. As pessoas se inscrevem fornecendo seu número de CPF. Para garantir que o sorteio seja justo, cada pessoa só pode se inscrever uma única vez. A ordem de inscrição não importa, mas você precisa de uma forma muito rápida de verificar se um CPF já foi cadastrado para evitar duplicatas.
#Estrutura de Dados:Dicionario(conjunto)
#Justificativa: Os elementos deve ser unicos e acessados por uma chave especifica.


#Cenário 4: Cadastro de Clientes: Você está desenvolvendo um sistema para uma loja.Para cada cliente, você precisa armazenar várias informações: nome, e-mail e telefone. Você precisa ser capaz de buscar rapidamente todas as informações de um cliente usando seu e-mail como identificador único.
#Estrutura de Dados:Dicionario
#Justificativa: Os elementos deve ser unicos e acessados por uma chave especifica.


#Cenário 5: Permissões de Usuário em um Sistema: Em um sistema complexo, cada usuário pode ter um conjunto de permissões (ex: 'admin', 'editor', 'visualizador').Essas permissões são fixas e definidas no momento da criação do perfil do usuário e não devem ser alteradas durante a sessão. O sistema precisa verificar rapidamente se um usuário possui uma determinada permissão.
#Estrutura de Dados:Tupla(conjunto)
#justificativa: Os dados não devem ser alterados e os elementos devem ser unicos