@namespace
class SpriteKind:
    images = SpriteKind.create()
    game_option = SpriteKind.create()
def initializeMenu():
    global backgroundmenu, mario, title_onep, title_twop, selector_ig, selector, list2
    backgroundmenu = sprites.create(assets.image("""
        background-menu
    """), SpriteKind.images)
    mario = sprites.create(assets.image("""
        mario_stan_def
    """), SpriteKind.player)
    title_onep = sprites.create(assets.image("""
            title-1-player
        """),
        SpriteKind.game_option)
    title_twop = sprites.create(assets.image("""
            title-2-player
        """),
        SpriteKind.game_option)
    selector_ig = sprites.create(assets.image("""
        selector
    """), SpriteKind.game_option)
    selector = 0
    mario.set_position(40, 99)
    title_onep.set_position(80, 70)
    title_twop.set_position(80, 85)
    title_onep.set_scale(0.9, ScaleAnchor.MIDDLE)
    title_twop.set_scale(0.9, ScaleAnchor.MIDDLE)
    selector_ig.set_scale(0.5, ScaleAnchor.MIDDLE)
    list2 = [title_onep, title_twop]
    changePostionSelector(selector)

def on_down_pressed():
    global selector
    if selector == 0:
        selector = 1
        changePostionSelector(selector)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def changePostionSelector(selection: number):
    selector_ig.set_position(list2[selection].x - 38, list2[selection].y + 1)

def on_up_pressed():
    global selector
    if selector == 1:
        selector = 0
        changePostionSelector(selector)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

list2: List[Sprite] = []
selector = 0
selector_ig: Sprite = None
title_twop: Sprite = None
title_onep: Sprite = None
mario: Sprite = None
backgroundmenu: Sprite = None
initializeMenu()