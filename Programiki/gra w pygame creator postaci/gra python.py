import pygame

import element




SZEROKOWSC_EKRANU = 800
WYSOKOSC_EKRANU = 600

obraz_tlo = pygame.image.load('images/background.png')
obraz_bazy_postaci = pygame.image.load('images/base.png')
pygame.init()

ekran = pygame.display.set_mode([SZEROKOWSC_EKRANU,WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

pygame.font.init()
moja_czcionka=pygame.font.SysFont('Comic Sans MS',30)

nakrycie_glowy = element.NakrycieGlowy()

ubranie_element = element.UbranieElment()

oczy_element = element.OczyElement()

bron_element = element.BronElement()

def wypisz_tekst(ekran,tekst,pozycja):
    napis = moja_czcionka.render(tekst,False,(255,255,255))
    ekran.blit(napis,pozycja)


gra_dziala = True
zapisywanie = False
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierznastepny()
            if zdarzenie.key == pygame.K_w:
                oczy_element.wybierznastepny()
            if zdarzenie.key == pygame.K_e:
                ubranie_element.wybierznastepny()
            if zdarzenie.key == pygame.K_r:
                bron_element.wybierznastepny()
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
                
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False      


                



    ekran.blit(obraz_tlo, (0,0))
    ekran.blit(obraz_bazy_postaci,(270,130))
    ekran.blit(ubranie_element.wybierzObraz(),(270, 130))
    ekran.blit(nakrycie_glowy.wybierzObraz(),(270,130))
    ekran.blit(oczy_element.wybierzObraz(),(270,130))
    ekran.blit(bron_element.wybierzObraz(),(270,130))
    wypisz_tekst(ekran, f'[Q] Głowa: {nakrycie_glowy.wybrany}]',(20,100))
    wypisz_tekst(ekran, f'[W] Oczy: {oczy_element.wybrany}]',(20,130))
    wypisz_tekst(ekran, f'[E] Ubranie: {ubranie_element.wybrany}]',(20,160))
    wypisz_tekst(ekran, f'[R] Broń: {bron_element.wybrany}]',(20,190))
    wypisz_tekst(ekran, f'[S] Zapisz:',(20,220))
    if zapisywanie:
        pygame.image.save(ekran,'postac.png')
        zapisywanie = False

    pygame.display.flip()
    zegar.tick(30)

pygame.quit()