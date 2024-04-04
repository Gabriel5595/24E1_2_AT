# Instruções

**Considere o seguinte problema:**

Uma empresa de locação de veículos deseja desenvolver um sistema para gerenciar o processo de locação. Para isso, será necessário realizar o cadastro dos veículos, dos clientes e gerenciar a ação de locação. Os veículos são designados pela placa, modelo, categoria, sendo elas básico, intermediário e luxo, e seu estado atual, podendo estar disponível ou locado. Os clientes são cadastrados pelo nome e sobrenome, CPF e email, além de se relacionar ao veículo locado pela placa. O sistema deve realizar a locação do veículo, verificando quais estão disponíveis e alocando-o ao cliente. No processo de devolução, devem ser informadas quantas diárias foram utilizadas, para que seja emitida a nota para pagamento, constando o valor total do serviço.

Com base no problema apresentado no texto, responda às questões a seguir.

1. Crie um diagrama que descreva a estrutura do sistema, descrevendo a estrutura das entidades VEÍCULO e CLIENTE, bem como a correlação entre elas.
2. Crie uma função que realize o cadastro do veículo, recebendo com passagem uma lista com o banco de dados dos veículos e retorne essa mesma lista com o novo valor de registro atualizado. O campo de disponibilidade deve ter valor -1 para quando o veículo estiver disponível e o índice do cliente que o locou, cado esteja indisponível.
3. Crie uma função que realize o cadastro do cliente, recebendo como passagem uma lista com o banco de dados dos clientes e retorne essa mesma lista com o novo valor de registro atualizado. O nome do cliente deve conter apenas Nome e Sobrenome, devendo ser armazenado em uma lista com duas posições.
4. Crie uma função que realize a busca de um veículo a partir da sua placa. Ela deve receber como passagem a lista contendo o banco de dados de veículos e a placa, e retorne uma lista contendo o índice do veículo desejado.
5. Crie uma função que realize a busca por veículos, tendo como base o estado da locação. Ela deve receber como parâmetros de entrada a lista contendo o banco de dados dos veículos e um parâmetro booleano, que selecionará se a lista retornada será dos veículos disponíveis ou indisponíveis. O valor padrão para esse parâmetro deve ser disponivel=True. O retorno da função deve uma lista contendo os índices de todos os veículos selecionados.
6. Crie uma função que receba como parâmetros a lista contendo o banco de dados dos veículos e uma lista contendo índices de veículo e realize a impressão desses dados.
7. Crie uma função que faça a busca por cliente a partir do seu o nome ou o sobrenome. Deve receber como parâmetros a lista contendo o banco de dados dos clientes, o nome que deve ser localizado e um parâmetro booleano que informe se a busca deve ser realizada pelo nome ou sobrenome. O retorno deve ser uma lista contendo todos os índices onde houveram ocorrência do nome/sobrenome desejados.
8. Crie uma função que imprima os dados de clientes. Ela receberá como parâmetro a lista contendo o banco de dados do cliente e uma lista contendo os índices de clientes e imprimirá os dados dos clientes listados.
9. Crie uma função que realize o aluguel do veículo. Ela deve receber como parâmetros as listas contendo os bancos de dados de veículos e clientes e retorná-los atualizados. A função deve solicitar a placa do veículo e avaliar se ele está disponível para locação. Caso não esteja, deve oferecer ao usuário a opção de inserir uma nova placa ou sair da opção. Caso o veículo esteja disponível, ela deve exibir os dados do veículo e pedir que o usuário confirme que está correto. Caso negativo, ofereça a opção de inserir uma nova placa ou sair. Se estiver correto, solicite o ID do cliente, faça a mesma avaliação e ofereça as mesmas opções apresentadas no caso dos veículos. Se tudo estiver correto, os campos de ‘disponibilidade do veículo’ e de ‘veículo locado’ devem ser atualizados nas respectivas bases de dados e um sumário da operação exibido na tela. A função deve retornar a duas listas atualizadas. 
10. Crie uma função que faça a devolução do veículo, contabilizando o valor total da locação. Deve receber como parâmetros as listas de veículos e de clientes e retornar essas listas atualizadas. Deverá ser solicitado o nome ou o código do cliente. O processo de devolução deve desvincular o veículo do usuário, retornando-o para o estado ’disponível’ e remover o veículo da base do cliente. A contabilização deve ser feita informando o número de diárias utilizadas, relacionando-as ao valor da locação, sendo que o valor de é de R$150,00, R$250,00 e R$400,00 para as categorias básica, intermediária e luxo, respectivamente. 
11. Crie uma função que ofereça ao usuário o menu principal do sistema, sendo elas: Gerenciamento de Frota; Gerenciamento de Clientes; Gerenciamento de Locação; Finalizar.
12. Crie uma função que permita o acesso às funções de Gestão de frota, sendo elas: Cadastro de Veículo; Busca por Placa, Busca por Disponibilidade; Voltar.
13. Crie uma função que permita ao usuário fazer a busca de um veículo por placa e imprima na tela os dados do veículo.
14. Crie uma função que permita ao usuário fazer a busca de veículos por sua disponibilidade, oferecendo a opção de escolha entre disponível ou indisponível e imprime na tela o resultado da busca.
15. Crie uma função que permita o acesso às funções de Gerenciamento de Clientes, sendo elas: Cadastro de Cliente, Busca de Clientes; Voltar.
16. Crie uma função que permita ao usuário fazer a busca por cliente, oferecendo a opção de nome ou sobrenome, e imprima o resultado na tela.
17. Crie uma função que permita o acesso às funções de locação, sendo elas Alugar um Veículo; Devolver um Veículo; Voltar;.
18. Crie as variáveis que serão utilizada para o armazenamento dos bancos de dados utilizados no sistema
19. Construa a estrutura do sistema de forma que seja possível realizar todos os processos necessários.

Realize os seguintes teste de validação:

20. Cadastro de 5 veículos com placas diferentes e categorias diferentes.
21. Cadastro de 3 clientes.
22. Locação de 1 veículo de categoria diferente para cada cliente.
23. Tentativa de 3 locação de veículos indisponíveis.
24. Devolução de todos os veículos.
25. O trabalho deve ser desenvolvido no Google Colab. Gere um PDF contendo a execução de todas as etapas e faça a postagem no Moodle. Além disso, deve ser disponibilizado o link do projeto, com acesso de visualização liberado para o professor e para o monitor da turma.

Assim que terminar, salve os links do Replit em PDF nomeando o arquivo seguindo a regra “nome_sobrenome_DR1_AT.PDF” e poste como resposta a este TP.