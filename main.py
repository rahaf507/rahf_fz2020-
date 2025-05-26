raha = 0
def on_gesture_shake():
    global rahaf 
    rahaf=30+10
    basic.show_number(raha)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
