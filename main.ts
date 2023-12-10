namespace SpriteKind {
    export const images = SpriteKind.create()
    export const game_option = SpriteKind.create()
}

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
    mario.setPosition(40, 99)
    title_onep.setPosition(80, 70)
    title_twop.setPosition(80, 85)
    title_onep.setScale(0.9, ScaleAnchor.Middle)
    title_twop.setScale(0.9, ScaleAnchor.Middle)
    selector_ig.setScale(0.5, ScaleAnchor.Middle)
    list2 = [title_onep, title_twop]
    changePostionSelector(selector)
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (selector == 0) {
        selector = 1
        changePostionSelector(selector)
    }
    
})
function changePostionSelector(selection: number) {
    selector_ig.setPosition(list2[selection].x - 38, list2[selection].y + 1)
}

controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (selector == 1) {
        selector = 0
        changePostionSelector(selector)
    }
    
})
let list2 : Sprite[] = []
let selector = 0
let selector_ig : Sprite = null
let title_twop : Sprite = null
let title_onep : Sprite = null
let mario : Sprite = null
let backgroundmenu : Sprite = null
initializeMenu()
