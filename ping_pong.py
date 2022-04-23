
from pygame import*

width, height = 600,500
window = display.set_mode((width, height))

backgraund_color = (200,255,255)
window.fill(backgraund_color)
display.set_caption('Ping Pong')



game = True
clock = time.Clock()
FPS = 60

while game:
	for e in event.get():
		if e.type == QUIT:
			game = False

	display.update()
	clock.tick(FPS)
