Q = 0
V = 0

def on_button_pressed_a():
    global Q
    Q += 1
    basic.show_number(Q)
    if Q > 10:
        Q = 0
        basic.show_number(Q)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            500,
            500,
            255,
            0,
            50,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if Q == V:
        basic.show_leds("""
            . # . # .
                        . . . . .
                        # # # # #
                        # . . . #
                        . # # # .
        """)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.pause(2000)
        game.add_score(1)
        game.add_life(1)
    else:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
            SoundExpressionPlayMode.UNTIL_DONE)
        if V < Q:
            basic.show_leds("""
                . . . # .
                                . . # . .
                                . # . . .
                                . . # . .
                                . . . # .
            """)
            basic.pause(2000)
            game.remove_life(1)
            if game.is_game_over():
                game.game_over()
            basic.pause(2000)
            basic.show_number(Q)
        else:
            basic.show_leds("""
                . # . . .
                                . . # . .
                                . . . # .
                                . . # . .
                                . # . . .
            """)
            basic.pause(2000)
            game.remove_life(1)
            if game.is_game_over():
                game.game_over()
            basic.pause(2000)
            basic.show_number(Q)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global V, Q
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
        SoundExpressionPlayMode.UNTIL_DONE)
    game.set_life(3)
    basic.show_number(game.score())
    basic.pause(2000)
    V = randint(0, 10)
    Q = 0
    basic.show_number(Q)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
