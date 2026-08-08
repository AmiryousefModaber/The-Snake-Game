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

        is_fruit = (cell.color == consts.fruit_color)

        self.cells.append(new_head)
        cell.set_color(self.color)

        if not is_fruit:
            tail = self.cells.pop(0)
            self.game.get_cell(tail).set_color(consts.back_color)
        


    def handle(self, keys):
        for k in keys:
            if k in self.keys:
                new_dir = self.keys[k]
                if  (new_dir == 'UP' and self.direction != 'DOWN') or \
                    (new_dir == 'DOWN' and self.direction != 'UP') or \
                    (new_dir == 'LEFT' and self.direction != 'RIGHT') or \
                    (new_dir == 'RIGHT' and self.direction != 'LEFT'):
                    self.direction = new_dir
                    break

            

