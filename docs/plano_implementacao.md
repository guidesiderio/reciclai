# Plano de Implementação

## Fase 1: Modelos e Estrutura do Banco de Dados

- [x] Criar app `core` para funcionalidades principais.
- [x] Definir perfis de usuário (Cidadão, Coletor, Recicladora) estendendo o modelo `User` do Django.
- [x] Criar modelo `Residue` com campos para tipo, peso/unidades, localização, status e a chave estrangeira para o Cidadão.
- [x] Criar modelo `Collection` para registrar a coleta, com chaves estrangeiras para `Residue` e `Collector`, e um campo de status.
- [x] Criar modelo `Reward` para as recompensas, com campos para nome e pontos necessários.
- [x] Criar modelo `UserReward` para associar as recompensas resgatadas aos usuários.

## Fase 2: Views e URLs

- [x] Configurar URLs para as diferentes áreas da aplicação (Cidadão, Coletor, Recicladora).
- [x] Criar views para o Cidadão:
    - [x] Cadastrar resíduo.
    * [x] Solicitar coleta.
    - [x] Acompanhar andamento da coleta.
    - [x] Visualizar pontos e extrato.
    - [x] Visualizar e resgatar recompensas.
- [x] Criar views para o Coletor:
    - [x] Visualizar solicitações de coleta disponíveis.
    - [x] Aceitar uma coleta.
    - [x] Atualizar o status da coleta (Em rota, Coletada, etc.).
- [x] Criar views para a Recicladora:
    - [x] Visualizar resíduos recebidos.
    - [x] Registrar o processamento e encerrar o ciclo.

## Fase 3: Lógica de Negócio e Templates

- [x] Implementar a lógica de atualização de status da coleta.
- [x] Implementar o sistema de pontuação:
    - [x] Creditar pontos ao Cidadão quando a Recicladora confirma o recebimento.
- [x] Implementar a lógica de resgate de recompensas.
- [x] Criar templates HTML básicos para todas as views.

## Fase 4: Testes e Refinamento

- [x] Escrever testes unitários para os modelos e a lógica de negócio.
- [x] Escrever testes de integração para as views e o fluxo completo.
- [x] Refinar a interface do usuário e a experiência.

## Fase 5: Fluxo do Cidadão - Cadastro e Solicitação

- [ ] Implementar o formulário e a view para o cidadão cadastrar um novo resíduo.
- [ ] Criar a funcionalidade para o cidadão solicitar a coleta de um resíduo cadastrado.
- [ ] Desenvolver uma view para o cidadão visualizar o status de suas coletas.

## Fase 6: Fluxo do Coletor - Gerenciamento de Coletas

- [ ] Criar a view para listar as coletas disponíveis (resíduos aguardando coleta).
- [ ] Implementar a lógica para um coletor aceitar uma coleta, associando-a a ele.
- [ ] Desenvolver o formulário e a view para o coletor atualizar o status da coleta (Em rota, Coletada, Entregue).

## Fase 7: Fluxo da Recicladora - Finalização e Pontuação

- [ ] Criar uma view para a recicladora visualizar os resíduos que foram entregues.
- [ ] Implementar a ação de "processar resíduo", que mudará o status do resíduo para "Finalizado".
- [ ] Garantir que, ao finalizar o processo, os pontos correspondentes sejam creditados ao cidadão.

## Fase 8: Integração e Templates

- [ ] Criar os templates HTML para todas as novas views implementadas.
- [ ] Garantir que os URLs estejam configurados corretamente para o novo fluxo.
- [ ] Refinar a interface do usuário para fornecer um fluxo de navegação coeso entre as diferentes etapas.
