from random import randrange as rnd, choice
import tkinter as tk
from tkinter import * 
import math
import time

#print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.title('Gun')
root.geometry('500x400')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

x = 0
y = 0
color = 'red'

class ball():
    def __init__(self, x, y, color):
        """ Constructor ball
        Args:
        x - start pozition of ball of horizontal
        y - start pozition of ball of vertical
        """
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 15
        self.vy = 15
        self.color = color
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 100

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """
        Moves the ball according to it's velocity and time step.
        Changes the ball's velocity due to gravitational force.

        """
        self.g = -1.1
        self.x += self.vx
        self.y -= self.vy - 0.5*self.g**2
        self.vx += 0
        self.vy += self.g
        self.live += -1
        self.set_coords()

        if self.x+self.r <= 0: 
            self.vx = -self.vx
        if self.x+self.r >= 800:
            self.vx = -self.vx
        if self.y+self.r <= 0:
            self.vy = -self.vy
        if self.y+self.r >= 600:
            self.vy = -self.vy
        
    def hittest(self, obj):
        """
           Function check if target is hited by object (obj)
        Args:
            obj
        Returns:
            Return True in case hitting. Otherwise return False.
        """
        # FIXME
        if ((obj.x - self.x) **2  + (obj.y - self.y)**2 <= (self.r + obj.r) ** 2):
            return True
        else:
            return False
    def delete(self):
        canv.delete(self.id)

class gun():
    def __init__(self):
        self.x1 = 20
        self.y1 = 530
        self.x2 = 50
        self.y2 = 500
        self.id = canv.create_line(self.x1, self.y1, self.x2, self.y2, width=7) 
        self.f2_on = 0
        self.f2_power = 10
        self.an = 1
        
        self.down = canv.create_rectangle(self.x1 - 10, self.y1, self.x2 - 5, self.y1 + 15, fill='red')


        
    def gun_move_right(self, event=0):
        if self.x2 <= 785:
            self.x1 += 10
            self.x2 += 10
            canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )
            canv.coords(self.down, self.x1 - 10, self.y1, self.x2 - 5, self.y1 + 15)

    def gun_move_left(self, event=0):
        if self.x1 >= 15:
            self.x1 -= 10
            self.x2 -= 10
            canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )
            canv.coords(self.down, self.x1 - 10, self.y1, self.x2 - 5, self.y1 + 15)

    def fire1_start(self, event):
        self.f2_on = 1
        
    def fire1_end(self, event):
        """Shot the ball.

        Occurs when the mouse button is released.
        The initial values of the ball speed components vx and vy depend on the mouse position.
        """
        global balls1, bullet
        bullet += 1
        new_ball = ball(self.x1, self.y1, 'red')
        new_ball.r += 10
        if (event.x-self.x1) >= 0:
            self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
        else:
            self.an = math.pi + math.atan((event.y-self.y1) / (event.x-self.x1))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls1 += [new_ball]
        self.f2_on = 0
        self.f2_power = 10
    
    def fire2_start(self, event):
        self.f2_on = 1
        
    def fire2_end(self, event):
        """Shot the ball.

        Occurs when the mouse button is released.
        The initial values of the ball speed components vx and vy depend on the mouse position.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x1, self.y1, 'red')
        new_ball.r += 0
        if (event.x-self.x1) >= 0:
            self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
        else:
            self.an = math.pi + math.atan((event.y-self.y1) / (event.x-self.x1))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Targetting. Depends on the mouse position."""
        if event:
            if (event.x-self.x1) >= 0:
                self.an = math.atan((event.y-self.y1) / (event.x-self.x1))
            else:
                self.an = math.pi + math.atan((event.y-self.y1) / (event.x-self.x1))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='pink')
        canv.coords(self.id, self.x1, self.y1,
                    self.x1 + max(self.f2_power, 20) * math.cos(self.an),
                    self.y1 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='pink')

    def delete(self):
        canv.delete(self.id)

class target():
    def __init__(self):
        self.live = 1
        self.id = canv.create_oval(0,0,0,0)
        color = (['white'])
        self.new_target(color)
        vx = self.vx = rnd(2, 20)
        vy = self.vy = rnd(2, 20)

    def new_target(self, color):
        """ Initialisation of new target """
        x = self.x = rnd(50, 769)
        y = self.y = rnd(50, 469)
        r = self.r = rnd(20, 30)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def new_target1(self, color):
        """ Initialisation of new target """
        x = self.x = rnd(100, 699)
        y = self.y = rnd(100, 499)
        r = self.r = rnd(10, 15)
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        
    def target_move(self):
        '''move of black ball'''
        x = self.x
        y = self.y
        r = self.r
  
        self.x += self.vx
        self.y += self.vy
        canv.coords(self.id, x-r, y-r, x+r, y+r)

        if self.x+self.r <= 50: 
            self.vx = -self.vx
        if self.x+self.r >= 750:
            self.vx = -self.vx
        if self.y+self.r <= 50:
            self.vy = -self.vy
        if self.y+self.r >= 450:
            self.vy = -self.vy

    def target1_move(self):
        '''move of white ball'''
        x = self.x
        y = self.y
        r = self.r

        if self.x+self.r <= 100:
            self.x += 100
        if self.x+self.r >= 300:
            self.x += -100
        else:
            self.x += choice([-50, -45, -40, -35, -30, 30, 35, 40, 45, 50])
        if self.y+self.r <= 100:
            self.y += 100
        if self.y+self.r >= 450:
            self.y += -100
        else:
            self.y += choice([-50, -45, -40, -35, -30, 30, 35, 40, 45, 50])

        canv.coords(self.id, x-r, y-r, x+r, y+r)
        
    def hit(self):
        """the ball hits the target"""
        global points
        canv.coords(self.id, 0, 0, 0, 0)
        points +=1

    def bomb1(self, event=0):
        global bombs
        new_bomb = ball(self.x, self.y, 'green')
        new_bomb.vx = 0
        new_bomb.vy = self.vy
        new_bomb.r += 20
        new_bomb.live = 100
        bombs += [new_bomb]
        canv.coords(new_bomb,
                self.x - new_bomb.r,
                self.y - new_bomb.r,
                self.x + new_bomb.r,
                self.y + new_bomb.r)

    def bomb2(self, event=0):
        global bombs
        new_bomb = ball(self.x, self.y, 'green')
        new_bomb.vx = 0
        new_bomb.vy = self.vy
        new_bomb.r += 20
        new_bomb.live = 100
        bombs += [new_bomb]
        canv.coords(new_bomb,
                self.x - new_bomb.r,
                self.y - new_bomb.r,
                self.x + new_bomb.r,
                self.y + new_bomb.r)

    def hittest(self, obj):
        """Function check if target is hited by object (obj)
        Args:
            obj
        Returns:
            Return True in case hitting. Otherwise return False.
        """
        m = []
        for i in bombs:
            if (obj.x1 - i.x) **2  + (obj.y1 - i.y)**2 <= (i.r)**2:
                m.append(1)
            else:
                m.append(0)
        if 1 in m:
            return True
        else:
            return False  
        
    def delete(self):
        canv.delete(self.id)

points = 0
g1 = gun()
t1 = target()
t2 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
id_points = canv.create_text(30, 30, text='', font='28')
bullet = 0
balls = []
balls1 = []
bombs = []



def start():
    root.geometry('800x600')
    b1.destroy()
    fra1.destroy()
    rules6.destroy()
    new_game()
    finish()
    
fra1 = Frame(root, width=600, height=600, bg="white")
fra1.place(x=0, y=0)

b1 = Button(text='Start', width=70, height=6)
b1.config(command=start)
b1.place(x=0, y=0)

rules6 = Label(root, text='Push "start" to start', font="Arial 15", bg="white", fg="blue")
rules6.place(x=100, y=225)


def konec():
    quit()

def finish():
    root.geometry('500x300')
    fra2 = Frame(root, width=600, height=600, bg="white")
    fra2.place(x=0, y=0)
    b2 = Button(text='Finish', width=70, height=6)
    b2.config(command=konec)
    b2.place(x=0, y=0)
    rules6 = Label(root, text='You win', font="Arial 15", bg="white", fg="blue")
    rules6.place(x=100, y=100)

def lose():
    root.geometry('550x300')
    fra3 = Frame(root, width=650, height=600, bg="white")
    fra3.place(x=0, y=0)
    b3 = Button(text='Finish', width=77, height=6)
    b3.config(command=konec)
    b3.place(x=0, y=0)
    rules7 = Label(root, text='You lose(', font="Arial 15", bg="white", fg="blue")
    rules7.place(x=180, y=110)
    
def new_game(event=''):
    '''Function of game'''
    global gun, screen1, balls, balls1, bullet, bombs
    t1.new_target1('white')
    t2.new_target('black')
    bullet = 0
    balls = []
    balls1 = []
    bombs = []
    
    '''Function gun with buttons'''
    canv.bind('<Button-1>', g1.fire2_start)                          
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind('<Button-3>', g1.fire1_start)
    canv.bind('<ButtonRelease-3>', g1.fire1_end)
    
    canv.focus_set()
    canv.bind('<Right>', g1.gun_move_right)
    canv.bind('<Left>', g1.gun_move_left)

    canv.bind('d', t1.bomb1)
    canv.bind('a', t2.bomb2)
    
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls1 or balls:
        if t1.live > 0 :
            t1.target1_move()
        if t2.live > 0 :
            t2.target_move()
        if t1.hittest(g1):
            lose()
        if t2.hittest(g1):
            lose()
        for b in bombs:
            b.move()
        for i in range(len(bombs)):
            if bombs[i].live <= 0:
                bombs[i].delete()
                bombs[i] = None 
        bombs = [bomb for bomb in bombs if bomb is not None]
    
        '''White ball with right button - 2'''
        for b in balls1:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.itemconfig(id_points, text = str(points))
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-3>', '')
                canv.bind('<ButtonRelease-3>', '')
                canv.itemconfig(screen1, text='')
                canv.itemconfig(screen1, text='You destroy target for' + str(bullet) + ' shots')
        for i in range(len(balls1)):
            if balls1[i].live <= 0:
                balls1[i].delete()
                balls1[i] = None 
        balls1 = [ball for ball in balls1 if ball is not None]

        '''Black ball with left button - 1'''
        for b in balls:
            b.move()
            if b.hittest(t2) and t2.live:
                t2.live = 0 
                t2.hit()
                canv.itemconfig(id_points, text = str(points))
            if t1.live == 0 and t2.live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='')
                canv.itemconfig(screen1, text='You destroy target for ' + str(bullet) + ' shots')
        for i in range(len(balls)):
            if balls[i].live <= 0:
                balls[i].delete()
                balls[i] = None
        balls = [ball for ball in balls if ball is not None]
                
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)


root.mainloop()
