# Pizza Panic

## Descrição

Pizza Panic é uma emocionante e frenética aventura ambientada em uma movimentada pizzaria. Assuma o papel do ágil pizzaiolo e teste seus reflexos enquanto tenta atender os pedidos dos clientes. Pegue as pizzas voando pela cozinha e entregue-as no balcão antes que o tempo acabe. Mas cuidado! Itens indesejados como panos sujos e pizzas estragadas podem causar danos, então mantenha-se atento e evite-os a todo custo. Conforme avança nas fases, a dificuldade aumenta, oferecendo um desafio cada vez maior. Você tem o que é preciso para se tornar o mestre da pizza?

## Arquitetura

Pizza Panic utiliza a Arquitetura Orientada a Componentes, que divide o jogo em entidades independentes chamadas componentes, que podem ser reutilizadas e combinadas para criar diferentes tipos de objetos de jogo. Isso facilita a modularidade e a reutilização de código. 

## Mecânica do Jogo

- **Balcão de Pedidos:** No início de cada nível, o jogador é apresentado a uma série de pedidos que devem ser atendidos. Cada pedido,equivale a uma pizza coletada.
- **Ação na Cozinha:** A cozinha é o coração do jogo, onde as pizzas são preparadas e lançadas para o pizzaiolo. O jogador deve ficar atento e agir rapidamente para pegar as pizzas no ar.
- **Entrega de Pizzas:** Assim que o pizzaiolo pega uma pizza, ele deve colocá-la no balcão de entregas. Quanto mais rápido o pedido for atendido, maior será a pontuação do jogador.
- **Itens "Ruins":** Durante a movimentada atividade na pizzaria, itens indesejados como panos sujos ou pizzas estragadas podem ser lançados junto com as pizzas. O pizzaiolo deve evitar esses itens, pois eles reduzem seus pontos.
- **Progressão de Fases:** Conforme o jogador avança no jogo, o nível de dificuldade aumenta. Isso significa mais pedidos, maior velocidade de lançamento das pizzas e uma frequência maior de itens "ruins".

## Prototipação

Imagens do protótipo podem ser encontradas [aqui](https://github.com/WesleyGCO/Pizza-Panic/tree/main/Imagens).

## Vídeos

Um vídeo de referência para a mecânica do jogo pode ser encontrado no [jogo do café do Club Penguin](https://www.youtube.com/watch?v=Y_Olby1TKEo).

## Sprites / Animações

Os sprites e animações estão disponíveis [neste link](https://github.com/WesleyGCO/Pizza-Panic/tree/main/Imagens).

## Efeitos Sonoros

- [Pixabay - Efeitos Sonoros de Lançar](https://pixabay.com/pt/sound-effects/search/lan%c3%a7ar/)
- [Jamendo - Efeitos Sonoros para Videogames](https://licensing.jamendo.com/pt/catalogo/projeto/videogame)
- [Pixabay - Músicas para Jogos de Vídeo](https://pixabay.com/pt/music/search/genre/jogos%20de%20v%C3%ADdeo/)

## Como rodar?

Tudo que você precisa fazer é rodar o comando `python .\src\main.py` dentro da pasta do jogo!