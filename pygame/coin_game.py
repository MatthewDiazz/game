WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
character = Actor("character")
character.pos = 100, 100

coin= Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    character.draw()
    coin.draw()
    screen.draw.text(("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("blue")
        screen.draw.text("Final score: " + str (score), topleft=(10, 10), fontsize=60

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
def time_up():
    global game_over
    game_over = True
clock.schedule(time_up, 7.0)

def update():
    global score

    if keyboard.left:
        character.x = character.x - 2
    elif keyboard.right:
        character.x = character.x + 2
    elif keyboard.up:
        character.y = character.y - 2
    elif keyboard.down:
        charcter.y = character.y + 2

    coin_collected = character.colliderect(coin)

    if coin_collected:
        score =
