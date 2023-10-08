def dino_animation(dino_surf, dino_index, dino_rect, dino_jump, dino_walk):

    if dino_rect.bottom < 318:
        dino_surf = dino_jump
        return dino_surf
    else:
        dino_index += 0.1
        if dino_index >= len(dino_walk):
            dino_index = 0
        dino_surf = dino_walk[int(dino_index)]
        return dino_surf
