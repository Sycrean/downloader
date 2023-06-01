import pygame
import time

# Initialisierung von Pygame
pygame.init()

# Festlegung der Fenstergröße
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mein Spiel")

# Goldvariablen
gold = 0
gold_per_second = 1
last_gold_time = time.time()

# Upgradevariablen
upgrade_cost = 10
upgrade_step = 10
upgrade_multiplier = 1.5
upgrade_active = False

# Schriftart für den Goldtext und Upgrade-Hinweis
font = pygame.font.Font(None, 36)

# Hauptspiel-Loop
running = True
while running:
    # Ereignisschleife
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                if gold >= upgrade_cost:
                    gold -= upgrade_cost
                    upgrade_cost += upgrade_step
                    gold_per_second += 5
                    upgrade_active = True

    # Aktuelle Zeit erfassen
    current_time = time.time()

    # Gold pro Sekunde hinzufügen
    if current_time - last_gold_time >= 1:
        gold += gold_per_second
        last_gold_time = current_time

    # Hintergrund zeichnen
    window.fill((255, 255, 255))

    # Goldtext zeichnen
    gold_text = font.render("Gold: " + str(gold), True, (0, 0, 0))
    window.blit(gold_text, (10, 10))

    # Upgrade-Text zeichnen
    upgrade_text = font.render("Upgrade kaufen (" + str(upgrade_cost) + " Gold)", True, (0, 0, 0))
    window.blit(upgrade_text, (10, 50))

    # Upgrade Hinweis-Text zeichnen
    upgrade_hint_text = font.render("Drücke 'U' für Upgrade", True, (0, 0, 0))
    window.blit(upgrade_hint_text, (10, 90))

    # Upgrade aktivieren
    if upgrade_active:
        upgrade_active_text = font.render("Upgrade aktiv!", True, (0, 0, 0))
        window.blit(upgrade_active_text, (10, 130))

    # Aktualisierung des Fensters
    pygame.display.flip()

# Beenden von Pygame
pygame.quit()
