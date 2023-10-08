def main_menu(pygame, screen, score, score_font):
    game_font = pygame.font.Font('font/Pixeltype.ttf', 80)

    dino_stand = pygame.image.load(
        'graphics/scenery/map-1/dino.png').convert_alpha()
    dino_stand = pygame.transform.scale2x(dino_stand)
    dino_stand_rect = dino_stand.get_rect(center=(350, 200))

    # pause screen
    game_name = game_font.render('DinoRun', False, '#eeeeee')
    game_name_rect = game_name.get_rect(center=(400, 70))
    game_message = game_font.render('Press space to run', False, '#eeeeee')
    game_message_rect = game_message.get_rect(center=(400, 340))

    #
    screen.fill("#CA3247")
    screen.blit(dino_stand, dino_stand_rect)
    score_message = score_font.render(
        f'Your score: {score}', False, "#eeeeee")
    score_message_rect = score_message.get_rect(center=(400, 330))
    screen.blit(game_name, game_name_rect)

    if score == 0:
        screen.blit(game_message, game_message_rect)
    else:
        screen.blit(score_message, score_message_rect)
