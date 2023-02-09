character = Actor('character')
character.pos = 10, 50

WIDTH = 500
HEIGHT = character.height + 20

def draw():
    screen.clear ()
    character.draw ()

def update():
    character.left = character.left + 2
    if character.right > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        print("Eek!")

def on_mouse_click(pos):
    if character.collidepoint(pos):
        print("Eek!")
    else:
        print("you missed me!")

def on_mouse_down():
    print("You clicked!")

def on_mouse_down(pos, button):
    if button == mouse.LEFT and character.collidepoint(pos):
        print("Eek!")

def on_mouse_down(pos):
    if character.collidepoint(pos):
        sound.eep.play()
        character.image = 'character_hurt'
