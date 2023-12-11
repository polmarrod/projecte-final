@namespace
class SpriteKind:
    Shroom = SpriteKind.create()
    Turtle = SpriteKind.create()
    Shell = SpriteKind.create()
def jumpAnimation():
    animation.stop_animation(animation.AnimationTypes.ALL, mario)
    if tall:
        if mario.vx > 0:
            mario.set_image(assets.image("""
                tall_mario_jump_right
            """))
        elif mario.vx < 0:
            mario.set_image(assets.image("""
                tall_mario_jump_left
            """))
    elif mario.vx > 0:
        mario.set_image(assets.image("""
            jump_right
        """))
    elif mario.vx < 0:
        mario.set_image(assets.image("""
            jump_left
        """))

def on_on_overlap(sprite, otherSprite2):
    if sprite.y < otherSprite2.top:
        otherSprite2.vx = 0
        animation.stop_animation(animation.AnimationTypes.ALL, otherSprite2)
        jump()
        otherSprite2.set_image(assets.image("""
            shroom_death
        """))
        pause(450)
        sprites.destroy(otherSprite2)
        info.change_score_by(100)
    else:
        deathMario()
sprites.on_overlap(SpriteKind.player, SpriteKind.Shroom, on_on_overlap)

def on_a_pressed():
    if mario.vy == 0:
        jump()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_hit_wall2(sprite5, location):
    if sprite5.is_hitting_tile(CollisionDirection.RIGHT):
        sprite5.vx = -50
    elif sprite5.is_hitting_tile(CollisionDirection.LEFT):
        sprite5.vx = 50
scene.on_hit_wall(SpriteKind.Shroom, on_hit_wall2)

def on_left_pressed():
    if mario.vy == 0:
        if tall:
            animation.run_image_animation(mario,
                assets.animation("""
                    tall_mario_walk_left
                """),
                150,
                True)
        else:
            animation.run_image_animation(mario,
                assets.animation("""
                    mario_walk_left
                """),
                150,
                True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def deathMario():
    info.stop_countdown()
    info.change_life_by(-1)
    info.set_score(0)
    info.change_countdown_by(400 - info.countdown())
    tiles.set_current_tilemap(tilemap("""
        level_1_2
    """))
    sprites.destroy_all_sprites_of_kind(SpriteKind.Shroom)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Turtle)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Shell)
    tiles.place_on_tile(mario, tiles.get_tile_location(0, 13))
    spawnEnemies()

def on_right_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mario)
    if tall:
        mario.set_image(assets.image("""
            tall_mario_right0
        """))
    else:
        mario.set_image(assets.image("""
            mario_right
        """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    animation.stop_animation(animation.AnimationTypes.ALL, mario)
    if tall:
        mario.set_image(assets.image("""
            tall_mario_left
        """))
    else:
        mario.set_image(assets.image("""
            mario_left
        """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_on_overlap2(sprite2, otherSprite22):
    global shell
    if sprite2.y < otherSprite22.top:
        otherSprite22.vx = 0
        animation.stop_animation(animation.AnimationTypes.ALL, otherSprite22)
        jump()
        sprites.destroy(otherSprite22)
        info.change_score_by(100)
        shell = sprites.create(assets.image("""
            shell_sprite
        """), SpriteKind.Shell)
        tiles.place_on_tile(shell, otherSprite22.tilemap_location())
        shell.ay = 350
    else:
        deathMario()
sprites.on_overlap(SpriteKind.player, SpriteKind.Turtle, on_on_overlap2)

def on_right_pressed():
    if mario.vy == 0:
        if tall:
            animation.run_image_animation(mario,
                assets.animation("""
                    tall_mario_walk_right
                """),
                150,
                True)
        else:
            animation.run_image_animation(mario,
                assets.animation("""
                    mario_walk_right
                """),
                150,
                True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def spawnEnemies():
    global shroom, turtle
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        if mario.tilemap_location().column + scene.screen_width() > value.column:
            shroom = sprites.create(assets.image("""
                shroom_sprite0
            """), SpriteKind.Shroom)
            tiles.place_on_tile(shroom, value)
            tiles.set_tile_at(value, assets.tile("""
                transparency16
            """))
            shroom.vx = -20
            animation.run_image_animation(shroom,
                [img("""
                        . . . . . . e e e e . . . . . . 
                                        . . . . . e e e e e e . . . . . 
                                        . . . . e e e e e e e e . . . . 
                                        . . . e e e e e e e e e e . . . 
                                        . . e f f e e e e e e f f e . . 
                                        . e e e d f e e e e f d e e e . 
                                        . e e e d f f f f f f d e e e . 
                                        e e e e d f d e e d f d e e e e 
                                        e e e e d d d e e d d d e e e e 
                                        e e e e e e e e e e e e e e e e 
                                        . e e e e d d d d d d e e e e . 
                                        . . . . d d d d d d d d . . . . 
                                        . . f f d d d d d d d d . . . . 
                                        . f f f f d d d d d d f f . . . 
                                        . f f f f f d d d d f f f . . . 
                                        . . f f f f f . . f f f . . . .
                    """),
                    img("""
                        . . . . . . e e e e . . . . . . 
                                        . . . . . e e e e e e . . . . . 
                                        . . . . e e e e e e e e . . . . 
                                        . . . e e e e e e e e e e . . . 
                                        . . e f f e e e e e e f f e . . 
                                        . e e e d f e e e e f d e e e . 
                                        . e e e d f f f f f f d e e e . 
                                        e e e e d f d e e d f d e e e e 
                                        e e e e d d d e e d d d e e e e 
                                        e e e e e e e e e e e e e e e e 
                                        . e e e e d d d d d d e e e e . 
                                        . . . . d d d d d d d d . . . . 
                                        . . . . d d d d d d d d f f . . 
                                        . . . f f d d d d d d f f f f . 
                                        . . . f f f d d d d f f f f f . 
                                        . . . . f f f . . f f f f f . .
                    """)],
                500,
                True)
            shroom.ay = 160
            shroom.set_bounce_on_wall(False)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile
    """)):
        if mario.tilemap_location().column + scene.screen_width() > value2.column:
            turtle = sprites.create(assets.image("""
                turtle_sprite
            """), SpriteKind.Turtle)
            tiles.place_on_tile(turtle, value2)
            tiles.set_tile_at(value2, assets.tile("""
                transparency16
            """))
            turtle.vx = -20

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def jump():
    jumpAnimation()
    mario.vy = -220
def createPlayer(player2: Sprite):
    scene.camera_follow_sprite(player2)
    tiles.place_on_tile(player2, tiles.get_tile_location(0, 13))
    controller.move_sprite(player2, 100, 0)

def on_on_overlap3(sprite3, otherSprite3):
    otherSprite3.vx = sprite3.vx * 2
    otherSprite3.set_bounce_on_wall(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.Shell, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite):
    global tall
    sprites.destroy(otherSprite)
    tall = 1
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap4)

boost: Sprite = None
turtle: Sprite = None
shroom: Sprite = None
shell: Sprite = None
mario: Sprite = None
tall = 0
scene.on_hit_wall(SpriteKind.player, on_hit_wall)
def on_hit_wall(sprite6: Sprite, location2: tiles.Location):
    if sprite6.is_hitting_tile(CollisionDirection.RIGHT):
        sprite6.vx = -50
    elif sprite6.is_hitting_tile(CollisionDirection.LEFT):
        sprite6.vx = 50
scene.on_hit_wall(SpriteKind.food, on_hit_wall)
tall = 0
info.start_countdown(400)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""))
tiles.set_current_tilemap(tilemap("""
    level_1_2
"""))
if tall:
    mario = sprites.create(assets.image("""
            tall_mario_right0
        """),
        SpriteKind.player)
else:
    mario = sprites.create(assets.image("""
        mario_right
    """), SpriteKind.player)
createPlayer(mario)
mario.ay = 350
info.set_life(3)
info.set_score(0)

def on_on_update():
    global boost
    spawnEnemies()
    for value22 in tiles.get_tiles_by_type(assets.tile("""
        prize_block
    """)):
        if mario.tilemap_location().column == value22.column and mario.tilemap_location().row == value22.row + 1:
            info.change_score_by(10)
            tiles.set_tile_at(value22, assets.tile("""
                myTile1
            """))
    for value222 in tiles.get_tiles_by_type(assets.tile("""
        prize_block_boost
    """)):
        if mario.tilemap_location().column == value222.column and mario.tilemap_location().row == value222.row + 1:
            boost = sprites.create(assets.image("""
                boost_sprite
            """), SpriteKind.food)
            tiles.place_on_tile(boost,
                tiles.get_tile_location(value222.column, value222.row - 1))
            boost.vx = 50
            boost.ay = 160
            tiles.set_tile_at(value222, assets.tile("""
                myTile1
            """))
game.on_update(on_on_update)
