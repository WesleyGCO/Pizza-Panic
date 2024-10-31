# Pizza Panic

## Descrição

Pizza Panic é uma emocionante e frenética aventura ambientada em uma movimentada pizzaria. Assuma o papel do ágil pizzaiolo e teste seus reflexos enquanto tenta atender os pedidos dos clientes. Pegue as pizzas voando pela cozinha para acumular pontos antes que o tempo acabe. Mas cuidado! Itens indesejados como panos sujos e pizzas estragadas podem diminuir a sua pontuação, então mantenha-se atento e evite-os a todo custo. Conforme avança nas fases, a dificuldade aumenta, oferecendo um desafio cada vez maior. Você tem o que é preciso para se tornar o mestre da pizza?

## Arquitetura

Pizza Panic utiliza a Arquitetura Hexagonal (ou Arquitetura de Portos e Adaptadores), que promove a separação de preocupações e facilita a manutenção e evolução do software. Essa arquitetura é dividida em três camadas principais:

### Núcleo (Core)
- **Entidades (Entities)**: Contém as classes de negócios e lógica de domínio fundamentais para o jogo, como `Pizza`, `Pano`, `Espatula` e `Personagem`.
- **Interfaces(Interfaces)**: Define as interfaces que especificam contratos que os adaptadores externos devem seguir.

### Portas (Ports)
- **Interface de Usuário (UI)**: Implementações que lidam com a apresentação dos dados ao usuário. Isso inclui os elementos visuais e interativos do jogo, renderizando os gráficos e recebendo entradas do usuário.

### Adaptadores (Adapters)
- **Implementações (Implementations)**: Implementações dos serviços definidos nas interfaces do núcleo. Eles contêm a lógica de aplicação, como a criação, movimentação e reinício dos itens/personagem.
- **Repositórios (Repositories)**: Abstração da forma como os dados da aplicação são armazenados e recuperados. Eles atuam como uma camada intermediária entre a lógica de negócio (casos de uso e entidades) e a infraestrutura de persistência (banco de dados, arquivos, etc.)

### Estrutura de Diretórios

```bash
├── src/
│ ├── adapters/
│ │ ├── primary/
│ │ │ ├── sons/
│ │ │ ├── sprites/
│ │ │ ├── ui/
│ │ │ │ ├── fase_ui.py
│ │ │ │ ├── jogo_ui.py
│ │ │ │ ├── menu_borda_ui.py
│ │ │ │ ├── menu_fase_ui.py
│ │ │ │ ├── menu_inicial_ui.py
│ │ │ │ ├── menu_perdeu_ui.py
│ │ │ ├── use_cases/
│ │ │ │ ├── gerenciar_fase.py
│ │ │ │ ├── gerenciar_item.py
│ │ │ │ ├── gerenciar_jogo.py
│ │ │ │ ├── gerenciar_menus.py
│ │ │ │ ├── gerenciar_personagem.py
│ │ │ │ ├── gerenciar_placar.py
│ │ ├── pygame_input_adapter.py
│ │ ├── pygame_output_adapter.py
│ ├── application/
│ │ ├── models/
│ │ │ ├── Fase.py
│ │ │ ├── Item.py
│ │ │ ├── Jogo.py
│ │ │ ├── Objeto.py
│ │ │ ├── Personagem.py
│ │ │ ├── Sprites.py
│ │ │ ├── Vetor.py
│ ├── config/
│ │ ├── config.py
│ ├── core/
│ │ ├── interfaces/
│ │ │ ├── FaseInterface.py
│ │ │ ├── ItemInterface.py
│ │ │ ├── JogoInterface.py
│ │ │ ├── PersonagemInterface.py
│ │ │ ├── PlacarInterface.py
│ │ │ ├── TempoInterface.py
│ │ ├── services/
│ │ │ ├── fase_servico.py
│ │ │ ├── item_servico.py
│ │ │ ├── jogo_servico.py
│ │ │ ├── personagem_servico.py
│ │ │ ├── placar_servico.py
│ │ │ ├── pontuacao_servico.py
│ │ │ ├── randomizacao_servico.py
│ │ │ ├── tempo_servico.py
│ ├── test/
│ │ ├── test_fase_service_movimento.py
│ ├── main.py
│ ├── settings.json
│ ├── requirements.txt
```

### Benefícios da Arquitetura Hexagonal

- **Separação de Preocupações**: Cada componente tem uma responsabilidade bem definida, facilitando a manutenção e evolução do código.
- **Facilidade de Testes**: Como as regras de negócio estão desacopladas dos detalhes de implementação, é mais fácil testar os componentes isoladamente.
- **Flexibilidade**: Permite trocar facilmente componentes externos (como bibliotecas de UI ou serviços) sem afetar o núcleo do aplicativo.

Essa abordagem facilita a modularidade e a reutilização de código, mantendo a estrutura do software clara e organizada, o que é essencial para o desenvolvimento contínuo e escalável do Pizza Panic.

## Vídeos

Um vídeo de referência para a mecânica do jogo pode ser encontrado no [jogo do Empilha a Pilha do Club Penguin](https://www.youtube.com/watch?v=Y_Olby1TKEo).

## Sprites / Animações

Os sprites e animações estão disponíveis [neste link](https://github.com/WesleyGCO/Pizza-Panic/tree/main/src/adapters/primary/sprites).

## Efeitos Sonoros

- [Pixabay - Efeitos Sonoros de Lançar](https://pixabay.com/pt/sound-effects/search/lan%c3%a7ar/)
- [Jamendo - Efeitos Sonoros para Videogames](https://licensing.jamendo.com/pt/catalogo/projeto/videogame)
- [Pixabay - Músicas para Jogos de Vídeo](https://pixabay.com/pt/music/search/genre/jogos%20de%20v%C3%ADdeo/)

## Dependências

Basta usar o comando a seguir para instalar a única biblioteca `pip install pygame`

## Deploy

Tudo que você precisa fazer é rodar o comando abaixo dentro da pasta src do jogo:

```bash
  python .\main.py
```