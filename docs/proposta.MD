# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

Escreva aqui o nome provisório do jogo.



> Corrida do Dinossauro

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1:Guilherme Mello
- Nome 2:Lian
- Nome 3:Pietro lage
- Nome 4:Luiz pegnolate 

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.




Tipo escolhido pelo grupo:

jogo de desviar de obstáculos

## 4. Descrição geral do jogo



Descrição:
O jogo consiste em uma corrida de sobrevivência (Endless Runner) onde o cenário se move continuamente na tela, acompanhado de um placar de pontos. O jogador controla um personagem (ou veículo) podendo se movimentar horizontalmente para a esquerda e para a direita. O objetivo principal é desviar dos diversos obstáculos que vêm em sua direção, sobrevivendo o maior tempo possível para acumular a maior pontuação. Os principais desafios durante a partida incluem o surgimento de barreiras em posições aleatórias, afunilamentos no mapa e o aumento progressivo da velocidade do jogo, exigindo reflexos cada vez mais rápidos

> Escreva aqui.
O jogo consiste em uma corrida de sobrevivência (Endless Runner) onde o cenário se move continuamente na tela, acompanhado de um placar de pontos. O jogador controla um personagem (ou veículo) podendo se movimentar horizontalmente para a esquerda e para a direita. O objetivo principal é desviar dos diversos obstáculos que vêm em sua direção, sobrevivendo o maior tempo possível para acumular a maior pontuação. Os principais desafios durante a partida incluem o surgimento de barreiras em posições aleatórias, afunilamentos no mapa e o aumento progressivo da velocidade do jogo, exigindo reflexos cada vez mais rápidos


## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.



O objetivo principal do jogador é evitar todos os obstáculos que surgem na tela e sobreviver pelo maior tempo possível, buscando alcançar a maior pontuação (high score) antes de inevitavelmente colidir com alguma barreira.


> Escreva aqui.

## 6. Regras principais

Liste as principais regras do jogo.

Regra 1: O personagem movimenta-se apenas no eixo horizontal (esquerda e direita), não podendo ultrapassar os limites laterais da tela.
 Regra 2: A pontuação do jogador aumenta de forma automática e contínua conforme o tempo em que ele permanece vivo na partida.
 Regra 3: A velocidade de descida dos obstáculos (ou do cenário) aumenta progressivamente ao longo do tempo, elevando a dificuldade.
 Regra 4: O jogador inicia a partida com 3 vidas e perde 1 vida cada vez que colide com algum obstáculo.
 Regra 5: A partida é encerrada ("Game Over") assim que as vidas chegarem a zero, momento em que o placar final é exibido e salvo caso seja um novo recorde.


Por se tratar de um jogo de sobrevivência contínua (endless runner), não há um final de fase tradicional. A condição de "vitória" (ou de sucesso na partida) consiste em sobreviver o tempo suficiente para ultrapassar a pontuação máxima anterior, batendo o recorde (High Score) salvo no sistema.


## 8. Condição de derrota ou encerramento

A derrota ocorre quando o jogador colide com os obstáculos repetidas vezes e perde todas as suas 3 vidas. O encerramento da partida acontece imediatamente no momento em que as vidas chegam a zero (Game Over), ou caso o jogador opte por abandonar a partida através de um menu de pausa.


## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Escreva aqui.

## Obstáculos, inimigos ou desafios

Exemplo:## Obstáculos, inimigos ou perigos

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Blocos e barreiras surgem no topo da tela e se movem em direção ao jogador. A frequência de surgimento e a velocidade de movimento desses obstáculos aumentam gradativamente conforme a partida avança.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Ocasionalmente, itens especiais (como vidas extras ou itens que concedem invencibilidade temporária) aparecerão na tela misturados aos obstáculos, exigindo que o jogador arrisque sua posição para coletá-los.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador começa a partida com 3 vidas. A pontuação é baseada no tempo de sobrevivência, aumentando continuamente a cada segundo que o jogador permanece vivo. Cada colisão com um obstáculo subtrai 1 vida.

## 10. Controles previstos

Controles do grupo:

- A / Seta para a esquerda: mover o personagem para a esquerda.
- D / Seta para a direita: mover o personagem para a direita.
- ESC: pausar a partida ou sair do jogo.
- Enter: confirmar opções nos menus (Iniciar, Reiniciar).

## 11. Organização inicial do código

Organização planejada:

- `main`: arquivo principal responsável por inicializar a janela e chamar o menu do jogo.
- `src/jogo`: contém o loop principal (*Game Loop*), controlando a atualização de quadros e a renderização geral.
- `src/entidades`: concentra as regras de movimentação, atributos do jogador e a lógica de geração (spawn) dos obstáculos.
- `src/colisoes`: funções dedicadas a verificar a intersecção geométrica (*hitboxes*) entre o jogador e as barreiras.
- `src/dados`: gerencia a leitura e escrita de arquivos para salvar os recordes (High Score).

## 12. Recursos externos previstos

Recursos previstos:

> Pretendemos utilizar tutoriais e documentações de bibliotecas gráficas apenas como base de referência para a estruturação visual. Imagens simples (*sprites*) e fontes serão obtidas de bancos de recursos gratuitos (assets *royalty-free*).

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementar a detecção de colisões precisa para que o jogador não perca vidas de forma injusta.
- Dificuldade 2: Balancear o aumento gradual de velocidade e frequência dos obstáculos para que o jogo não fique impossível rápido demais.
- Dificuldade 3: Gerenciar a memória e o desempenho ao criar e destruir continuamente os objetos (obstáculos) que entram e saem da tela.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá um loop funcional onde um personagem controlado pelas teclas laterais desvia de obstáculos gerados no topo da tela. Incluirá detecção de colisões que subtrai um sistema básico de 3 vidas, um contador de pontuação baseado no tempo e uma tela de Game Over quando as vidas chegarem a zero.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Implementação de um ranking persistente (salvo em arquivo) que exibe as melhores pontuações no menu inicial.
- Melhoria 2: Inclusão de *power-ups* (como escudos e câmera lenta) e diferentes temas visuais para o cenário.
- Melhoria 3: Adição de efeitos sonoros básicos para pulo/movimento, coleta de itens, colisão e uma trilha sonora de fundo.
