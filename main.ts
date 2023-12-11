namespace SpriteKind {
    export const images = SpriteKind.create()
    export const game_option = SpriteKind.create()
    export const coinOne = SpriteKind.create()
    export const coinTwo = SpriteKind.create()
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (selector == 1) {
        selector = 0
        changePostionSelector(selector)
    }
    
})
sprites.onDestroyed(SpriteKind.coinTwo, function on_on_destroyed(sprite2: Sprite) {
    
    listCoinIndex = 0
})
function initializeMenu() {
    
    backgroundmenu = sprites.create(assets.image`
        background-menu
    `, SpriteKind.images)
    mario = sprites.create(assets.image`
        mario_stan_def
    `, SpriteKind.Player)
    title_onep = sprites.create(assets.image`
            title-1-player
        `, SpriteKind.game_option)
    title_twop = sprites.create(assets.image`
            title-2-player
        `, SpriteKind.game_option)
    selector_ig = sprites.create(assets.image`
        selector
    `, SpriteKind.game_option)
    selector = 0
    coins = 0
    spriteCoinBrillante = sprites.create(assets.image`
        coin one
    `, SpriteKind.coinOne)
    spriteCoinOscura = sprites.create(assets.image`
        coin two
    `, SpriteKind.coinTwo)
    listCoins = [spriteCoinBrillante, spriteCoinOscura]
    mario.setPosition(40, 99)
    title_onep.setPosition(80, 70)
    title_twop.setPosition(80, 85)
    title_onep.setScale(0.9, ScaleAnchor.Middle)
    title_twop.setScale(0.9, ScaleAnchor.Middle)
    selector_ig.setScale(0.5, ScaleAnchor.Middle)
    list2 = [title_onep, title_twop]
    changePostionSelector(selector)
    buildCabecera()
}

sprites.onDestroyed(SpriteKind.coinOne, function on_on_destroyed2(sprite: Sprite) {
    
    listCoinIndex = 1
})
function buildCabecera() {
    
    score = 0
    scr = convertToText(score)
    x = scr.length
    while (x < 7) {
        strTemp = "" + strTemp + "0"
        x += 1
    }
    y = convertToText(coins).length
    while (y < 2) {
        strCoins = "" + strCoins + "0"
        y += 1
    }
    strCoins = "" + strCoins + convertToText(coins)
    strTemp = "" + strTemp + scr
    textScore = textsprite.create(strTemp)
    titleScore = textsprite.create("SCORE")
    titleCoins = textsprite.create("X" + strCoins)
    listCoinIndex = 1
    titleTime = textsprite.create("TIME")
    titleScore.setMaxFontHeight(1)
    titleTime.setMaxFontHeight(1)
    textScore.setMaxFontHeight(1)
    titleScore.setPosition(30, 3)
    titleTime.setPosition(123, 3)
    textScore.setPosition(30, 10)
    titleCoins.setPosition(79, 9)
    colocateCoin(spriteCoinBrillante)
    colocateCoin(spriteCoinOscura)
    while (true) {
        pause(500)
        if (listCoinIndex == 0) {
            sprites.destroy(spriteCoinBrillante)
            spriteCoinOscura = sprites.create(assets.image`
                coin two
            `, SpriteKind.coinTwo)
            colocateCoin(spriteCoinOscura)
        } else {
            sprites.destroy(spriteCoinOscura)
            spriteCoinBrillante = sprites.create(assets.image`
                coin one
            `, SpriteKind.coinOne)
            colocateCoin(spriteCoinBrillante)
        }
        
    }
}

function changePostionSelector(selection: number) {
    selector_ig.setPosition(list2[selection].x - 38, list2[selection].y + 1)
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (selector == 0) {
        selector = 1
        changePostionSelector(selector)
    }
    
})
function colocateCoin(mySprite: Sprite) {
    mySprite.setPosition(65, 9)
}

let titleTime : TextSprite = null
let titleCoins : TextSprite = null
let titleScore : TextSprite = null
let textScore : TextSprite = null
let strCoins = ""
let y = 0
let strTemp = ""
let x = 0
let scr = ""
let score = 0
let list2 : Sprite[] = []
let listCoins : Sprite[] = []
let spriteCoinOscura : Sprite = null
let spriteCoinBrillante : Sprite = null
let coins = 0
let selector_ig : Sprite = null
let title_twop : Sprite = null
let title_onep : Sprite = null
let mario : Sprite = null
let backgroundmenu : Sprite = null
let listCoinIndex = 0
let selector = 0
initializeMenu()
