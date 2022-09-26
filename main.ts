let Q = 0
let V = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Q += 1
    basic.showNumber(Q)
    if (Q > 10) {
        Q = 0
        basic.showNumber(Q)
    }
    
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 500, 500, 255, 0, 50, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    control.reset()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (Q == V) {
        basic.showLeds(`
            . # . # .
                        . . . . .
                        # # # # #
                        # . . . #
                        . # # # .
        `)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
        basic.pause(2000)
        game.addScore(1)
        game.addLife(1)
    } else {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.UntilDone)
        if (V < Q) {
            basic.showLeds(`
                . . . # .
                                . . # . .
                                . # . . .
                                . . # . .
                                . . . # .
            `)
            basic.pause(2000)
            game.removeLife(1)
            if (game.isGameOver()) {
                game.gameOver()
            }
            
            basic.pause(2000)
            basic.showNumber(Q)
        } else {
            basic.showLeds(`
                . # . . .
                                . . # . .
                                . . . # .
                                . . # . .
                                . # . . .
            `)
            basic.pause(2000)
            game.removeLife(1)
            if (game.isGameOver()) {
                game.gameOver()
            }
            
            basic.pause(2000)
            basic.showNumber(Q)
        }
        
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.UntilDone)
    game.setLife(3)
    basic.showNumber(game.score())
    basic.pause(2000)
    V = randint(0, 10)
    Q = 0
    basic.showNumber(Q)
})
