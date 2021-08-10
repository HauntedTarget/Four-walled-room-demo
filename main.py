import tkinter as tkin
class Room:
  def __init__(self):
    #class variable init
    self.wallface = 1
    self.door = tkin.Tk()
    self.enter = tkin.Button(self.door,text='Enter',command = self.enterRoom)
    self.enter.pack(side='top')
    tkin.mainloop()
  def enterRoom(self):
    self.door.withdraw()
    self.wall1()
  def wall1(self):
    self.one = tkin.Toplevel()
    self.left = tkin.Button(self.one,text='left',command=self.goleft)
    self.wall = tkin.Label(self.one,text='Wall One')
    self.right = tkin.Button(self.one,text='right',command=self.goright)
    self.left.pack(side='left')
    self.wall.pack(side='left')
    self.right.pack(side='left')
  def wall2(self):
    self.two = tkin.Toplevel()
    self.left = tkin.Button(self.two,text='left',command=self.goleft)
    self.wall = tkin.Label(self.two,text='Wall Two')
    self.right = tkin.Button(self.two,text='right',command=self.goright)
    self.left.pack(side='left')
    self.wall.pack(side='left')
    self.right.pack(side='left')
  def wall3(self):
    self.three = tkin.Toplevel()
    self.left = tkin.Button(self.three,text='left',command=self.goleft)
    self.wall = tkin.Label(self.three,text='Wall Three')
    self.right = tkin.Button(self.three,text='right',command=self.goright)
    self.left.pack(side='left')
    self.wall.pack(side='left')
    self.right.pack(side='left')
  def wall4(self):
    self.four = tkin.Toplevel()
    self.left = tkin.Button(self.four,text='left',command=self.goleft)
    self.wall = tkin.Label(self.four,text='Wall Four')
    self.right = tkin.Button(self.four,text='right',command=self.goright)
    self.left.pack(side='left')
    self.wall.pack(side='left')
    self.right.pack(side='left')
  def goleft(self):
    if self.wallface > 1:
      self.wallface -= 1
    else:
      self.wallface = 4
    self.move()
  def goright(self):
    if self.wallface < 4:
      self.wallface += 1
    else:
      self.wallface = 1
    self.move()
  def move(self): 
    if self.wallface == 1:
      try:
        self.two.destroy()
      except:
        print()
      try:
        self.three.destroy()
      except:
        print()
      try:
        self.four.destroy()
      except:
        print()
      self.wall1()
    if self.wallface == 2:
      try:
        self.one.destroy()
      except:
        print()
      try:
        self.three.destroy()
      except:
        print()
      try:
        self.four.destroy()
      except:
        print()
      self.wall2()
    if self.wallface == 3:
      try:
        self.two.destroy()
      except:
        print()
      try:
        self.one.destroy()
      except:
        print()
      try:
        self.four.destroy()
      except:
        print()
      self.wall3()
    if self.wallface == 4:
      try:
        self.two.destroy()
      except:
        print()
      try:
        self.three.destroy()
      except:
        print()
      try:
        self.one.destroy()
      except:
        print()
      self.wall4()
place = Room()