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
│ │ ├── implementarions/
│ │ │ ├── JogoServiceImpl.py
│ │ │ ├── FaseServiceImpl.py
│ │ │ ├── ItemServiceImpl.py
│ │ ├── repositories/
│ │──assets/
│ │ ├── Imagens/
│ │ ├── Sons e efeitos sonoros/
│ ├── core/
│ │ ├── entities/
│ │ │ ├── Espatula.py
│ │ │ ├── Pano.py
│ │ │ ├── Personagem.py
│ │ │ ├── Pizza.py
│ │ │ ├── Fase.py
│ │ │ ├── FaseUm.py
│ │ │ ├── FaseDois.py
│ │ │ ├── FaseTres.py
│ │ │ ├── FaseQuatro.py
│ │ │ ├── FaseCinco.py
│ │ │ ├── Objeto.py
│ │ │ ├── Vetor.py
│ │ ├── interfaces/
│ │ │ ├── ItemInterface.py
│ │ │ ├── FaseInterface.py
│ │ │ ├── JogoInterface.py
│ │ │ ├── PersonagemInterface.py
│ │ │ ├── TempoInterface.py
│ ├── ports/
│ │ ├── ui/
│ │ │ ├── ItemUI.py
│ │ │ ├── FaseUI.py
│ │ │ ├── JogoUI.py
│ │ │ ├── MenuBordaUI.py
│ │ │ ├── MenuFaseUI.py
│ │ │ ├── MenuInicialUI.py
│ │ │ ├── PlacarFaseUI.py
│ ├── main.py
```

### Benefícios da Arquitetura Hexagonal

- **Separação de Preocupações**: Cada componente tem uma responsabilidade bem definida, facilitando a manutenção e evolução do código.
- **Facilidade de Testes**: Como as regras de negócio estão desacopladas dos detalhes de implementação, é mais fácil testar os componentes isoladamente.
- **Flexibilidade**: Permite trocar facilmente componentes externos (como bibliotecas de UI ou serviços) sem afetar o núcleo do aplicativo.

Essa abordagem facilita a modularidade e a reutilização de código, mantendo a estrutura do software clara e organizada, o que é essencial para o desenvolvimento contínuo e escalável do Pizza Panic.


## Prototipação

Imagens do protótipo podem ser encontradas [aqui](https://github.com/WesleyGCO/Pizza-Panic/tree/main/src/assets/Imagens).

## Vídeos

Um vídeo de referência para a mecânica do jogo pode ser encontrado no [jogo do café do Club Penguin](https://www.youtube.com/watch?v=Y_Olby1TKEo).

## Sprites / Animações

Os sprites e animações estão disponíveis [neste link](https://github.com/WesleyGCO/Pizza-Panic/tree/main/src/assets/Imagens).

## Efeitos Sonoros

- [Pixabay - Efeitos Sonoros de Lançar](https://pixabay.com/pt/sound-effects/search/lan%c3%a7ar/)
- [Jamendo - Efeitos Sonoros para Videogames](https://licensing.jamendo.com/pt/catalogo/projeto/videogame)
- [Pixabay - Músicas para Jogos de Vídeo](https://pixabay.com/pt/music/search/genre/jogos%20de%20v%C3%ADdeo/)

## Deploy

Tudo que você precisa fazer é rodar o comando abaixo dentro da pasta do jogo:

```bash
  python .\src\main.py
```