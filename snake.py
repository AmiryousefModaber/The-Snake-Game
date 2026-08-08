import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        head = self.get_head()
        new_head = (self.val(head[0] + self.dx[self.direction]), self.val(head[1] + self.dy[self.direction]))

        cell = self.game.get_cell(new_head)

        is_blocked = (cell.color == consts.block_color)
        if not is_blocked:
            for snake in self.game.snakes:
                if new_head in snake.cells:
                    is_blocked = True
                    break

        if is_blocked:
            self.game.kill(self)
            return
        


    def handle(self, keys):
        for k in keys:
            if k in self.keys:
                if k == 'w':
                    if self.direction != 'DOWN':
                        self.direction = "UP"
                        break

                if k == 's':
                    if self.direction != "UP":
                        self.direction = "DOWN"
                        break

                if k == 'a':
                    if self.direction != "RIGHT":
                        self.direction = "LEFT"
                        break

                if k == 'd':
                    if self.direction != "LEFT":
                        self.direction = "RIGHT"
                        break
