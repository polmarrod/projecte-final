@namespace
class SpriteKind:
    images = SpriteKind.create()
    game_option = SpriteKind.create()
    coinOne = SpriteKind.create()
    coinTwo = SpriteKind.create()

def on_up_pressed():
    global selector
    if selector == 1:
        selector = 0
        changePostionSelector(selector)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_destroyed(sprite2):
    global listCoinIndex
    listCoinIndex = 0
sprites.on_destroyed(SpriteKind.coinTwo, on_on_destroyed)

def initializeMenu():
    global backgroundmenu, mario, title_onep, title_twop, selector_ig, selector, coins, spriteCoinBrillante, spriteCoinOscura, listCoins, list2
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
    coins = 0
    spriteCoinBrillante = sprites.create(assets.image("""
        coin one
    """), SpriteKind.coinOne)
    spriteCoinOscura = sprites.create(assets.image("""
        coin two
    """), SpriteKind.coinTwo)
    listCoins = [spriteCoinBrillante, spriteCoinOscura]
    mario.set_position(40, 99)
    title_onep.set_position(80, 70)
    title_twop.set_position(80, 85)
    title_onep.set_scale(0.9, ScaleAnchor.MIDDLE)
    title_twop.set_scale(0.9, ScaleAnchor.MIDDLE)
    selector_ig.set_scale(0.5, ScaleAnchor.MIDDLE)
    list2 = [title_onep, title_twop]
    changePostionSelector(selector)
    buildCabecera()

def on_on_destroyed2(sprite):
    global listCoinIndex
    listCoinIndex = 1
sprites.on_destroyed(SpriteKind.coinOne, on_on_destroyed2)

def buildCabecera():
    global score, scr, x, strTemp, y, strCoins, textScore, titleScore, titleCoins, listCoinIndex, titleTime, spriteCoinOscura, spriteCoinBrillante
    score = 0
    scr = convert_to_text(score)
    x = len(scr)
    while x < 7:
        strTemp = "" + strTemp + "0"
        x += 1
    y = len(convert_to_text(coins))
    while y < 2:
        strCoins = "" + strCoins + "0"
        y += 1
    strCoins = "" + strCoins + convert_to_text(coins)
    strTemp = "" + strTemp + scr
    textScore = textsprite.create(strTemp)
    titleScore = textsprite.create("SCORE")
    titleCoins = textsprite.create("X" + strCoins)
    listCoinIndex = 1
    titleTime = textsprite.create("TIME")
    titleScore.set_max_font_height(1)
    titleTime.set_max_font_height(1)
    textScore.set_max_font_height(1)
    titleScore.set_position(30, 3)
    titleTime.set_position(123, 3)
    textScore.set_position(30, 10)
    titleCoins.set_position(79, 9)
    colocateCoin(spriteCoinBrillante)
    colocateCoin(spriteCoinOscura)
    while True:
        pause(500)
        if listCoinIndex == 0:
            sprites.destroy(spriteCoinBrillante)
            spriteCoinOscura = sprites.create(assets.image("""
                coin two
            """), SpriteKind.coinTwo)
            colocateCoin(spriteCoinOscura)
        else:
            sprites.destroy(spriteCoinOscura)
            spriteCoinBrillante = sprites.create(assets.image("""
                coin one
            """), SpriteKind.coinOne)
            colocateCoin(spriteCoinBrillante)
def changePostionSelector(selection: number):
    selector_ig.set_position(list2[selection].x - 38, list2[selection].y + 1)

def on_down_pressed():
    global selector
    if selector == 0:
        selector = 1
        changePostionSelector(selector)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def colocateCoin(mySprite: Sprite):
    mySprite.set_position(65, 9)
titleTime: TextSprite = None
titleCoins: TextSprite = None
titleScore: TextSprite = None
textScore: TextSprite = None
strCoins = ""
y = 0
strTemp = ""
x = 0
scr = ""
score = 0
list2: List[Sprite] = []
listCoins: List[Sprite] = []
spriteCoinOscura: Sprite = None
spriteCoinBrillante: Sprite = None
coins = 0
selector_ig: Sprite = None
title_twop: Sprite = None
title_onep: Sprite = None
mario: Sprite = None
backgroundmenu: Sprite = None
listCoinIndex = 0
selector = 0
initializeMenu()