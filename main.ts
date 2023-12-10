namespace SpriteKind {
    export const Shroom = SpriteKind.create()
    export const Turtle = SpriteKind.create()
    export const Shell = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Shroom, function (sprite, otherSprite2) {
    if (sprite.y < otherSprite2.top) {
        otherSprite2.vx = 0
        animation.stopAnimation(animation.AnimationTypes.All, otherSprite2)
        jump()
        otherSprite2.setImage()
        pause(450)
        sprites.destroy(otherSprite2)
        info.changeScoreBy(100)
    } else {
        deathMario()
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mario.vy == 0) {
        jump()
    }
})
scene.onHitWall(SpriteKind.Shroom, function (sprite5, location) {
    if (sprite5.isHittingTile(CollisionDirection.Right)) {
        sprite5.vx = -50
    } else if (sprite5.isHittingTile(CollisionDirection.Left)) {
        sprite5.vx = 50
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Turtle, function (sprite2, otherSprite22) {
    if (sprite2.y < otherSprite22.top) {
        otherSprite22.vx = 0
        animation.stopAnimation(animation.AnimationTypes.All, otherSprite22)
        jump()
        sprites.destroy(otherSprite22)
        info.changeScoreBy(100)
        shell = sprites.create(, SpriteKind.Shell)
        tiles.placeOnTile(shell, otherSprite22.tilemapLocation())
        shell.ay = 350
    } else {
        deathMario()
    }
})
function walkAnimation () {
    if (mario.vx > 0) {
        animation.runImageAnimation(
        mario,
        [],
        100,
        false
        )
    } else if (mario.vx < 0) {
        animation.runImageAnimation(
        mario,
        [],
        100,
        false
        )
    }
}
info.onLifeZero(function () {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Shell, function (sprite3, otherSprite3) {
    otherSprite3.vx = sprite3.vx * 2
    otherSprite3.setBounceOnWall(true)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite4, otherSprite) {
    sprites.destroy(otherSprite)
})
let boost: Sprite = null
let shell: Sprite = null
let mySprite: Sprite = null
let mario: Sprite = null
scene.onHitWall(SpriteKind.Player, on_hit_wall)
function on_hit_wall(sprite6: Sprite, location2: tiles.Location) {
    if (sprite6.isHittingTile(CollisionDirection.Right)) {
        sprite6.vx = -50
    } else if (sprite6.isHittingTile(CollisionDirection.Left)) {
        sprite6.vx = 50
    }
    
}
scene.onHitWall(SpriteKind.Food, on_hit_wall)
info.startCountdown(400)
scene.setBackgroundImage()
tiles.setCurrentTilemap(0)
mario = sprites.create(, SpriteKind.Player)
createPlayer(mySprite)
game.onUpdate(function () {
    spawnEnemies()
    for (let value22 of tiles.getTilesByType(assets.tile`prize_block`)) {
        if (mario.tilemapLocation().column == value22.column && mario.tilemapLocation().row == value22.row + 1) {
            info.changeScoreBy(10)
            tiles.setTileAt(value22, assets.tile`myTile1`)
        }
    }
    for (let value222 of tiles.getTilesByType(assets.tile`prize_block_boost`)) {
        if (mario.tilemapLocation().column == value222.column && mario.tilemapLocation().row == value222.row + 1) {
            boost = sprites.create(, SpriteKind.Food)
            tiles.placeOnTile(boost, tiles.getTileLocation(value222.column, value222.row - 1))
            boost.vx = 50
            boost.ay = 160
            tiles.setTileAt(value222, assets.tile`myTile1`)
        }
    }
})
game.onUpdate(function () {
    if (mario.vy == 0) {
        walkAnimation()
    }
})
