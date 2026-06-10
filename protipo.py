Aqui está o código limpo, sem nenhum comentário:

```python
import pygame
import sys
import random

LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

def inicializar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("Protótipo - Jogo de Desviar")
    relogio = pygame.time.Clock()
    return tela, relogio

def atualizar_jogador(teclas, jogador_rect, velocidade):
    if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and jogador_rect.left > 0:
        jogador_rect.x -= velocidade
    if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and jogador_rect.right < LARGURA_TELA:
        jogador_rect.x += velocidade

def atualizar_obstaculo(obstaculo_rect, velocidade):
    obstaculo_rect.y += velocidade
    if obstaculo_rect.top > ALTURA_TELA:
        return True
    return False

def desenhar_tela(tela, jogador_rect, obstaculo_rect):
    tela.fill(BRANCO)
    pygame.draw.rect(tela, AZUL, jogador_rect)
    pygame.draw.rect(tela, VERMELHO, obstaculo_rect)
    pygame.display.flip()

def main():
    tela, relogio = inicializar_jogo()

    tamanho_jogador = 50
    jogador_rect = pygame.Rect(LARGURA_TELA//2 - tamanho_jogador//2, 
                               ALTURA_TELA - tamanho_jogador - 20, 
                               tamanho_jogador, tamanho_jogador)
    vel_jogador = 7

    tamanho_obstaculo = 50
    obstaculo_rect = pygame.Rect(random.randint(0, LARGURA_TELA - tamanho_obstaculo), 
                                 -tamanho_obstaculo, 
                                 tamanho_obstaculo, tamanho_obstaculo)
    vel_obstaculo = 5

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        atualizar_jogador(teclas, jogador_rect, vel_jogador)
        
        saiu_da_tela = atualizar_obstaculo(obstaculo_rect, vel_obstaculo)
        if saiu_da_tela:
            obstaculo_rect.x = random.randint(0, LARGURA_TELA - tamanho_obstaculo)
            obstaculo_rect.y = -tamanho_obstaculo

        if jogador_rect.colliderect(obstaculo_rect):
            print("Colisão detectada!")
            obstaculo_rect.x = random.randint(0, LARGURA_TELA - tamanho_obstaculo)
            obstaculo_rect.y = -tamanho_obstaculo

        desenhar_tela(tela, jogador_rect, obstaculo_rect)

        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

