from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

def deltaR(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def creating_targets(n, targets):
    for i in range(0, n):
        new_target = target()
        new_target.new_target()
        new_target.live = 1
        targets.append(new_target)

class ball():
    def __init__(self, x, y):
        """ The ball class. Creates a ball, controls it's movement and implement it's rendering.

        Args:
        x - start horizontal position
        y - start povertical position
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.ay = 0.5
        self.yk = 0.98
        self.xk = 0.99
        self.color = choice(['green'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 10

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """ Moves the ball according to it's velocity and time step.
        Changes the ball's velocity due to gravitational force. 
        """
        self.x += self.vx
        self.y += self.vy
        self.vy += self.ay
        self.vy *= self.yk
        self.vx *= self.xk
        if self.x >= 790:
            self.vx *= -1
            self.live -= 1
        if self.x <= 10:
            self.vx *= -1
            self.live -= 1
        if self.y >= 590:
            self.vy *= -1
            self.live -= 1
        if self.y <= 10:
            self.vy *= -1
            self.live -= 1
        if self.live == 0:
            canv.delete(self.id)
            print(1)
        self.set_coords()

    def hittest(self, obj):
        """Function check if target is hited by object (obj)
        Args:
            obj
        Returns:
            Return True in case hitting. Otherwise return False.
        """
        if deltaR(self.x, self.y, obj.x, obj.y) < self.r + obj.r:
            return True
        else:
            return False
        


class gun():
    def __init__(self, x=40, y=300):
        """ The gun class

        Args:
        x - start horizontal position
        y - start povertical position
        """

        self.x = x
        self.y = y
        self.color = 'blue'
        self.live = 30
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=8)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Shot the ball.

        Occurs when the mouse button is released.
        The initial values of the ball speed components vx and vy depend on the mouse position.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(50, 420)
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Targetting. Depends on the mouse position."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def set_coords(self):
        canv.coords(
                self.id,
                self.x ,
                self.y,
                self.x + 30,
                self.y - 30,
        )
        
    def move(self, event):
        self.y += 10
        self.set_coords()


class target():
    def __init__(self):
        """ Initialisation of new target """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        vx = self.vx = rnd(-6, 6)
        vy = self.vy = rnd(-6, 6)
        self.id = canv.create_oval(0,0,0,0)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        self.points = 0
        self.live = 1
        canv.itemconfig(self.id, fill=color)
        self.new_target()

    def new_target(self):
        """ Makes new target """
        x = self.x = rnd(500, 600)
        y = self.y = rnd(400, 500)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """The ball hits the target."""
        canv.delete(self.id)
        self.points += points

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 700:
            self.vx *= -1
        if self.x <= 100:
            self.vx *= -1
        if self.y >= 550:
            self.vy *= -1
        if self.y <= 50:
            self.vy *= -1
        self.set_coords()

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

        
amount_of_targets = 3
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
targets = []
creating_targets(amount_of_targets, targets)

def new_game(event=''):
    global gun, screen1, balls, bullet, targets
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<Up>', g1.move)
    
    z = 0.03
    summa = 0
    for i in range(0, amount_of_targets):
        summa += targets[i].live
    while summa > 0:
        for t in targets:
            t.move()
        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    summa -= 1
        canv.update()
        time.sleep(z)
        g1.targetting()
        g1.power_up()
    coolboy = canv.create_text(200, 30, text = '', font = '28')
    canv.itemconfig(coolboy, text = (str(amount_of_targets) + ' targets were destroyed by ' + str(bullet) + ' shots'))


new_game()

root.mainloop()
