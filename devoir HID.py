import pygame
pygame.init()

#defnition de l'écran et ses paramétre ( longuer et hauteur)
__ecran = pygame.display.set_mode((600, 600))

#Définition du titre de l'interface
pygame.display.set_caption("Mon interface HID")

#definition de la variable affichage
__police = pygame.font.Font(None, 20)
__recup_event =""


#definition de notre boucle infinit
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            __recup_event = event.unicode

    __ecran.fill((255, 255, 255)) # couleur de l'écran par défaut on va mettre en blanc

#  l'affichage sur l'écran
    __affichage_ecran = __police.render("la touche appuyée est:"+ __recup_event, True,(0, 0, 0))
    __ecran.blit(__affichage_ecran, (30, 30))


    pygame.display.flip()

# fermeture du pragramme
pygame.quit()
