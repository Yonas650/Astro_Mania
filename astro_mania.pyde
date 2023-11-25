add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)

class Spaceship: #central commanding spaceship that the player controls with the mouse movement
  def __init__(self):
    self.spaceship_image = loadImage(path + "/images/spaceship_stripes.png")
    self.frame = 0
    self.crops = [ [0, 0, 100, 80] , [ 100, 0, 200, 80] , [200, 0, 200, 80] ] #necessary crop ratios in spaceship_stripes.png for animation
    self.current_crop = []
    self.i = 0
  def display(self): #displays the central spaceship, based on the mouse movement and background map bounadries
    self.frame = self.frame + 1
    if self.frame%5==0: #condition responsible for central spaceship animation (blinking sequence)
        self.i = self.i + 1
        if self.i == 2:
            self.i = 0
    self.current_crop = self.crops[self.i]
    
    if mouseX>50 and mouseX<950 and  mouseY>40 and mouseY<660:# makes the cursor align to the center of the spaceship and below are all the other conditions for displaying the spaceship within the boundaries of the map
        image(self.spaceship_image, mouseX-50, mouseY-40, 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseY>=660 and mouseX>=950:
        image(self.spaceship_image, 900, 620 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseY>=660 and mouseX<=50:
        image(self.spaceship_image, 0, 620 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseY<=40 and mouseX<=50:
        image(self.spaceship_image, 0, 0 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseY<=40 and mouseX>=950:
        image(self.spaceship_image, 900, 0 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
        #corner cases
    if mouseY>=660 and mouseX>50 and mouseX<950:
        image(self.spaceship_image, mouseX-50, 620 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseY<=40 and mouseX>50 and mouseX<950:
        image(self.spaceship_image, mouseX-50, 0 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseX<=50 and mouseY>40 and mouseY<660:
        image(self.spaceship_image, 0, mouseY - 40 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
    if mouseX>=950 and mouseY>40 and mouseY<660:  
        image(self.spaceship_image, 900, mouseY - 40 , 100, 80, self.current_crop[0], self.current_crop[1], self.current_crop[2], self.current_crop[3])
        #edge cases       

class Asteroid: #asteroid class, we have several instances of asteroids in the game which spawn randomly at predetermined times and move in straight line motion, and players should avoid collision with it
    def __init__(self):
        self.asteroid_image = loadImage(path + "/images/asteroid.png")
        self.xi = 1100
        self.xf = 0
        self.yi = 0
        self.yf = 0
        self.speed = 5
        self.spawn()
        
    def move(self): #method responsible for displaying the movement of the asteroid properly

        if self.yi == self.yf:
            self.xi = self.xi - self.speed
            if self.xi + 50 >= 0:
                image(self.asteroid_image, self.xi, self.yi, 60, 50)
                
        if self.yi < self.yf:
            self.xi = self.xi - self.speed
            self.yi = self.yi + self.speed/2
            if self.xi + 50 >= 0 and self.yf >= self.yi:
                image(self.asteroid_image, self.xi, self.yi, 60, 50)
        
        if self.yi > self.yf:
            self.xi = self.xi - self.speed
            self.yi = self.yi - self.speed/2
            if self.xi + 50 >= 0 and self.yf <= self.yi:
                image(self.asteroid_image, self.xi, self.yi, 60, 50)
                
        
    def spawn(self): #the method responsible for random locations 
        x = random.randint(0, 1)
        if x == 0:
            self.yi = random.randint(0, 150)
            self.yf = random.randint(700, 800)
        if x == 1:
            self.yi = random.randint(700, 800)
            self.yf = random.randint(0, 150)
            
class BigAsteroid: #another class similiar to one above but the object, the asteorid, is bigger in size, (200x200) so its harder for players to avoid it. It also gets spawned randomly at predetermined time (towards the end of the game) but it can also spawn based on chance if player picks up the power orb
    def __init__(self):
        self.big_asteroid_image = loadImage(path + "/images/big_asteroid.png")
        self.xi = 1100
        self.xf = 0
        self.yi = 0
        self.yf = 0
        self.speed = 5
        self.spawn()
        
 
    def move(self): #method responsible for displaying the movement of the  big asteroid properly
    

        if self.yi == self.yf:
            self.xi = self.xi - self.speed
            if self.xi + 200 >= 0:
                image(self.big_asteroid_image, self.xi, self.yi, 200, 200)
                
        if self.yi < self.yf:
            self.xi = self.xi - self.speed
            self.yi = self.yi + self.speed/2
            if self.xi + 200 >= 0 and self.yf >= self.yi:
                image(self.big_asteroid_image, self.xi, self.yi, 200, 200)
        
        if self.yi > self.yf:
            self.xi = self.xi - self.speed
            self.yi = self.yi - self.speed/2
            if self.xi + 200 >= 0 and self.yf <= self.yi:
                image(self.big_asteroid_image, self.xi, self.yi, 200, 200)
                
        
    def spawn(self): #the method responsible for random locations 
        x = random.randint(0, 1)
        if x == 0:
            self.yi = random.randint(0, 150)
            self.yf = random.randint(700, 800)
        if x == 1:
            self.yi = random.randint(700, 800)
            self.yf = random.randint(0, 150)
            
            
class Enemy: #the enemy spaceship class which spawns enemy spaceships at predetermined times at randomized locations. Unlike asteroids, the enemy spaceship actively tracks the location of the central spaceship, so central spaceship must keep moving to avoid collision. 
  def __init__(self):

    self.enemy_spaceship_image = loadImage(path + "/images/enemy_spaceship.gif")
    self.x_current = 0
    self.y_current = 0
    self.random_positions() #randomizes spaceship position
    self.x_initial = self.x_current
    self.y_initial = self.y_current
    self.m = 0 #y ratio changer
    self.n = 0 #x ratio changer
    self.speed = 3
 
    
  def random_positions(self): #randomized position
      x = 0
      x = random.randint(0, 1)
      if x == 0:
          self.x_current = random.randint(0, 1000)
          self.y_current = 800
      else:
          self.x_current = 1100
          self.y_current = random.randint(0, 700)
          
      
      
          
  def move(self): #method responsible for tracking the spaceship and making the enemy spaceship follow its locations at certain speed


    self.ratio() #gives variability to motion, since several enemy spaceships will be spawned, they will have randomized ratios for change in x and y, hence giving them randomized motion, which will make them more unique and make players perceive them as distinct objects, instead of getting displayed over each other after they have settled. 
    
    #conditions responsible for different kinds of motions based on where the central spaceship is at in relation to enemy spaceship
    if self.x_current > mouseX and self.y_current > mouseY:
        self.x_current = self.x_current - self.speed*self.n
        self.y_current = self.y_current - self.speed*self.m
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    if self.x_current < mouseX and self.y_current < mouseY:
        self.x_current = self.x_current + self.speed*self.n
        self.y_current = self.y_current + self.speed*self.m
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    if self.x_current > mouseX and self.y_current < mouseY:
        self.x_current = self.x_current - self.speed*self.n
        self.y_current = self.y_current + self.speed*self.m
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    if self.x_current < mouseX and self.y_current > mouseY:
        self.x_current = self.x_current + self.speed*self.n
        self.y_current = self.y_current - self.speed*self.m
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)  
    if self.x_current<=mouseX and self.y_current== mouseY:
        self.x_current=self.x_current + self.speed*self.n
        self.y_current = self.y_current   
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    if self.x_current>=mouseX and self.y_current== mouseY:
        self.x_current=self.x_current + self.speed*self.n
        self.y_current = self.y_current   
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    if self.x_current==mouseX and self.y_current<= mouseY:
        self.x_current=self.x_current
        self.y_current = self.y_current +self.speed*self.m  
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    if self.x_current==mouseX and self.y_current>= mouseY:
        self.x_current=self.x_current
        self.y_current = self.y_current-self.speed*self.m   
        image(self.enemy_spaceship_image, self.x_current, self.y_current, 60, 60)
    
          
          

  def ratio(self): #gives spaceships variability in motion
      if self.x_current ==self.x_initial  or self.y_current == self.y_initial: #is needed to be called only once so that values dont drastically change
        try:
            self.m = random.uniform(1, 1.7)
            self.n = random.uniform(1, 1.7)
        
        except:
            print()
      
    
class Powerup: #powerup class which is responsible for powerup orbs. There are total of 2 orbs in the game spawned at different times which player may choose to pickup or completely avoid it. 
    def __init__(self):
        self.powerup_image = loadImage(path + "/images/orb_sprites.png")
        self.frame = 0
        self.crops = [ [0, 0, 20, 20] , [20, 0, 40, 20], [40, 0, 60, 20], [60, 0, 80, 20], [80, 0, 100, 20], [100, 0, 120, 20], ] #ratios needed for proper cropping
        self.current_crop = []
        self.i = 0
        self.x = 0
        self.y = 0
        self.random_position()
        self.luck_speed_increase = False
        self.luck_number_decrease = False
        self.luck_speed_decrease = False
        self.luck_asteroid_summon = False
        self.random_buff()
    
    def display(self): #responsible for displaying the orb
        
        self.frame = self.frame + 1

        if self.frame%5==0:
            self.i = self.i + 1
            if self.i == 5:
                self.i = 0
        self.current_crop = self.crops[self.i]
        image(self.powerup_image, self.x, self.y, 20, 20, self.current_crop[0],  self.current_crop[1],  self.current_crop[2],  self.current_crop[3] )
        
    def random_position(self): #randomizes orb position
        self.x = random.randint(0, 950)
        self.y = random.randint(0, 650)
        
    def random_buff(self): #once two power up orbs are created at the start of the game they are given random chances of either increasing the speed of enemy ship, decreasing it, summonning large asteorids, or making an enemy spaceship stop - all upon collision. This gives players the unique option to take the risk to make the game easier. As you can see, out of four scenarios, two mnake it easier and two make it harder, which is more fair and balanced. 
        x = random.randint(0, 3)
        if x == 0:
            self.luck_speed_increase = True
        if x == 1:
            self.luck_number_decrease = True
        if x == 2:
            self.luck_speed_decrease = True
        if x == 3:
            self.luck_asteroid_summon = True

        
class Game: #class responsible for instatiating many of the aforementioned objects and giving the game more definite mechanics and characteristics as well as the sound effects and endgame startgame conditions
    def __init__(self):
      self.background_image = loadImage(path + "/images/starfield.png")
      self.game_won_image = loadImage(path + "/images/game_won_screen.png")
      self.game_lost_image = loadImage(path + "/images/game_lost_screen.png")
      self.spaceship = Spaceship()
      self.enemy_spaceship = Enemy()
      self.bg_sound = player.loadFile(path + "/sounds/background.mp3")
      self.bg_sound.loop()
      self.gameover_sound = player.loadFile(path + "/sounds/gameover.wav")
      self.orb = Powerup()
      self.orb2 = Powerup()
      self.col_sound = player.loadFile(path + "/sounds/collisionpo.wav")
      self.time = 0
      self.time_seconds = 0 #keeps track of the overall time in seconds
      self.gameover=False
      self.timeover =110 #the game ends at 110 seconds, i.e player won
      self.orbcol=False 
      self.orbcol2= False
      self.win=False
      self.bigasteroidmove = False
      self.bigasteroidmove2 = False
      self.col_c = 0
      self.col2_c = 0

      self.enemy_spaceship2 = Enemy()
      self.enemy_spaceship3 = Enemy()
      self.enemy_spaceship4 = Enemy()
      self.enemy_spaceship5 = Enemy()
      
      self.asteroid2 = Asteroid()
      self.asteroid3 = Asteroid()
      self.asteroid4 = Asteroid()
      self.asteroid5 = Asteroid()
      self.asteroid6 = Asteroid()
      self.asteroid7 = Asteroid()
      self.asteroid8 = Asteroid()
      self.asteroid9 = Asteroid()
      self.asteroid10 = Asteroid()
      self.asteroid11 = Asteroid()
      self.asteroid12 = Asteroid()
      self.asteroid13 = Asteroid()
      self.asteroid14 = Asteroid()
      self.asteroid15 = Asteroid()
      self.asteroid16 = Asteroid()
      self.asteroid17 = Asteroid()
      self.asteroid18 = Asteroid()
      self.asteroid19 = Asteroid()
      self.asteroid20 = Asteroid()
      self.asteroid21 = Asteroid()
      self.asteroid22 = Asteroid()
      self.asteroid23 = Asteroid()
      self.asteroid24 = Asteroid()
      self.asteroid25 = Asteroid()
      self.asteroid26 = Asteroid()
      self.asteroid27 = Asteroid()
      self.asteroid28 = Asteroid()
      self.asteroid29 = Asteroid()
      self.asteroid30 = Asteroid()
      self.asteroid31 = Asteroid()
      
      
      self.big_asteroid2 = BigAsteroid()
      self.big_asteroid3 = BigAsteroid()
      self.big_asteroid4 = BigAsteroid()
      self.big_asteroid5 = BigAsteroid()
      self.big_asteroid6 = BigAsteroid()
      self.big_asteroid7 = BigAsteroid()

    

    def display(self):
      self.check_gameover()
      if self.gameover==False:
         image(self.background_image, 0,0)
         self.time = self.time + 1
         self.time_seconds = self.time/60
    
    #print(mouseX,mouseY)
          
      self.spaceship.display()
     
      self.enemy_spaceship.move()
      
      self.soundswitch()
      
      #the condition below is responsible for the first power orb. 
      if self.time_seconds >=35 and self.time_seconds <=39: #dissapears after 4 seconds automatically
          if self.orbcol == False: #stops displaying it as soon as there is collision
              self.orb.display()
              
          if self.col_c == 0:  
              self.collorb()

          if self.orbcol:
            
            if self.orb.luck_number_decrease == True and self.col_c ==0:
                self.enemy_spaceship.speed = 0 #stops the enemy spaceship
                self.col_c = 1 #gets changed to 1, thereby won't enter any of the luck conditions so that even if the image of the orb is not desplayed , the player won't be able to pick up the phantom orb, by just going over and over the same palce.
    
            if self.orb.luck_speed_increase == True  and self.col_c ==0:
                self.enemy_spaceship.speed = 5
                self.enemy_spaceship2.speed = 5 #makes two spaceships faster
                self.col_c = 1
           
            if self.orb.luck_speed_decrease == True  and self.col_c ==0:
                self.enemy_spaceship.speed = 1
                self.enemy_spaceship2.speed = 1 #makes twospaceships slower
                self.col_c = 1
            
            if self.orb.luck_asteroid_summon == True  and self.col_c ==0:
                self.bigasteroidmove = True #spawns two big asteroids
                self.col_c = 1 
         
      #fix for bigasteroidmove, player may choose to select the orb towards the end of its 4 second lifespan and in that case, the big asteroid won't have the chance to move through entire map and would dissapear once 4 seconds is up. Those two conditions fix that for both orbs. 
      if self.time_seconds >=35 and self.time_seconds <= 50:
          if self.bigasteroidmove == True:
              self.big_asteroid2.move()
              self.big_asteroid3.move()
              
      if self.time_seconds >=75 and self.time_seconds <= 90:
          if self.bigasteroidmove2 == True:
              self.big_asteroid6.move()
              self.big_asteroid7.move()
        
         
      if self.time_seconds >=50 and self.time_seconds <=74: #so that in case player chooses not to pick first power ring, second one still works
          self.col_c = 1
          
      if self.time_seconds >=75 and self.time_seconds <=79:  #similiar methodology applies to the second orb as the first orb
          
          if self.orbcol2 == False:
              self.orb2.display()
              
          if self.col2_c == 0:  
              self.collorb()
          
          if self.orbcol2:
            if self.orb2.luck_number_decrease == True and self.col2_c ==0:
                self.enemy_spaceship3.speed = 0
                self.col2_c = 1
    
            if self.orb2.luck_speed_increase == True and self.col2_c ==0:
                self.enemy_spaceship3.speed = 5
                self.enemy_spaceship4.speed = 5
                self.col2_c = 1

            if self.orb2.luck_speed_decrease == True and self.col2_c ==0:
                self.enemy_spaceship3.speed = 1
                self.enemy_spaceship4.speed = 1
                self.col2_c = 1
      
            if self.orb2.luck_asteroid_summon == True and self.col2_c ==0:
                self.bigasteroidmove2 = True
                self.col2_c = 1

      #conditions responsible for displaying the spaceship
      if self.time_seconds >=15: 
            self.enemy_spaceship2.move()
      if self.time_seconds >=30: 
            self.enemy_spaceship3.move()
      if self.time_seconds >= 45:
            self.enemy_spaceship4.move()
      if self.time_seconds >=60: 
            self.enemy_spaceship5.move()

      #conditions responsible for displaying the asteorids
      if self.time_seconds >=8: 
            self.asteroid2.move()
      if self.time_seconds >=16: 
            self.asteroid3.move()
      if self.time_seconds >=24: 
            self.asteroid4.move()
      if self.time_seconds >=32: 
            self.asteroid5.move()
      if self.time_seconds >=40: 
            self.asteroid6.move()
      if self.time_seconds >=48: 
        self.asteroid7.move()
      if self.time_seconds >=56: 
        self.asteroid8.move()
      if self.time_seconds >=64: 
        self.asteroid9.move()
      if self.time_seconds >=72: 
        self.asteroid10.move()
        self.asteroid11.move()
      if self.time_seconds >=80: 
        self.asteroid12.move()
        self.asteroid13.move()
        self.asteroid14.move()
        self.asteroid15.move()
      if self.time_seconds >=88: 
        self.asteroid16.move()
        self.asteroid17.move()
        self.asteroid18.move()
        self.asteroid19.move()
        self.asteroid20.move()
        self.asteroid21.move()
        self.asteroid22.move()
        self.asteroid23.move() 
        
      if self.time_seconds >=100: 
          self.big_asteroid4.move()
          self.big_asteroid5.move() 
          self.asteroid24.move()
          self.asteroid25.move()
          self.asteroid26.move()
          self.asteroid27.move() 
          self.asteroid28.move()
          self.asteroid29.move()
          self.asteroid30.move()
          self.asteroid31.move() 
      
      print(self.time_seconds)
      
      if self.gameover==True:
          background(255, 255, 255)
      self.timer()
      self.gam()
      
    def collorb(self): #method for detecting collision of the central spaceship with the orbs and make the power orb sound
        if self.col_c ==0 and mouseX-90<=self.orb.x<=mouseX+90 and mouseY-80<=self.orb.y<=mouseY+80:
            self.orbcol=True
            self.col_sound.rewind()
            self.col_sound.play()
        if self.col_c==1 and mouseX-90<=self.orb2.x<=mouseX+90 and mouseY-80<=self.orb2.y<=mouseY+80:
            self.orbcol2 = True
            self.col_sound.rewind()
            self.col_sound.play()
            
    def colchecker(self):
            self.col_sound.rewind()
            self.col_sound.play()
      
    def soundswitch(self):#switches sounds when the spaceship is crushed by the asteroids and enemy spaceships
        if self.gameover==True and self.time_seconds <self.timeover:
            self.bg_sound.close()
            self.gameover_sound.play()

    def check_gameover(self): #detects collisions of objects and central commanding spaceship for the gameover, loss condition
        
         if mouseY-40<=self.enemy_spaceship.y_current<=mouseY+40 and mouseX-50<=self.enemy_spaceship.x_current<=mouseX+50:
             self.gameover=True
         if mouseY-40<=self.enemy_spaceship2.y_current<=mouseY+40 and mouseX-50<=self.enemy_spaceship2.x_current<=mouseX+50:
             self.gameover=True
         if mouseY-40<=self.enemy_spaceship3.y_current<=mouseY+40 and mouseX-50<=self.enemy_spaceship3.x_current<=mouseX+50:
             self.gameover=True
         if mouseY-40<=self.enemy_spaceship4.y_current<=mouseY+40 and mouseX-50<=self.enemy_spaceship4.x_current<=mouseX+50:
             self.gameover=True
         if mouseY-40<=self.enemy_spaceship5.y_current<=mouseY+40 and mouseX-50<=self.enemy_spaceship5.x_current<=mouseX+50:
             self.gameover=True
   
         if mouseY-90<=self.asteroid2.yi<=mouseY+90 and mouseX-30<=self.asteroid2.xi<=mouseX+30:
             self.gameover=True 
         if mouseY-90<=self.asteroid3.yi<=mouseY+90 and mouseX-30<=self.asteroid3.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid4.yi<=mouseY+90 and mouseX-30<=self.asteroid4.xi<=mouseX+30:
             self.gameover=True         
         if mouseY-90<=self.asteroid5.yi<=mouseY+90 and mouseX-30<=self.asteroid5.xi<=mouseX+30:
             self.gameover=True 
         if mouseY-90<=self.asteroid6.yi<=mouseY+90 and mouseX-30<=self.asteroid6.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid7.yi<=mouseY+90 and mouseX-30<=self.asteroid7.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid8.yi<=mouseY+90 and mouseX-30<=self.asteroid8.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid9.yi<=mouseY+90 and mouseX-30<=self.asteroid9.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid10.yi<=mouseY+90 and mouseX-30<=self.asteroid10.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid11.yi<=mouseY+90 and mouseX-30<=self.asteroid11.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid12.yi<=mouseY+90 and mouseX-30<=self.asteroid12.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid13.yi<=mouseY+90 and mouseX-30<=self.asteroid13.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid14.yi<=mouseY+90 and mouseX-30<=self.asteroid14.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid15.yi<=mouseY+90 and mouseX-30<=self.asteroid15.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid16.yi<=mouseY+90 and mouseX-30<=self.asteroid16.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid17.yi<=mouseY+90 and mouseX-30<=self.asteroid17.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid18.yi<=mouseY+90 and mouseX-30<=self.asteroid18.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid19.yi<=mouseY+90 and mouseX-30<=self.asteroid19.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid20.yi<=mouseY+90 and mouseX-30<=self.asteroid20.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid21.yi<=mouseY+90 and mouseX-30<=self.asteroid21.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid22.yi<=mouseY+90 and mouseX-30<=self.asteroid22.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid23.yi<=mouseY+90 and mouseX-30<=self.asteroid23.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.big_asteroid2.yi<=mouseY+90 and mouseX-30<=self.big_asteroid2.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.big_asteroid3.yi<=mouseY+90 and mouseX-30<=self.big_asteroid3.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.big_asteroid4.yi<=mouseY+90 and mouseX-30<=self.big_asteroid4.xi<=mouseX+30:
             self.gameover=True   
         if mouseY-90<=self.big_asteroid5.yi<=mouseY+90 and mouseX-30<=self.big_asteroid5.xi<=mouseX+30:
             self.gameover=True 
         if mouseY-90<=self.big_asteroid6.yi<=mouseY+90 and mouseX-30<=self.big_asteroid6.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.big_asteroid7.yi<=mouseY+90 and mouseX-30<=self.big_asteroid7.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid24.yi<=mouseY+90 and mouseX-30<=self.asteroid24.xi<=mouseX+30:
             self.gameover=True 
         if mouseY-90<=self.asteroid25.yi<=mouseY+90 and mouseX-30<=self.asteroid25.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid26.yi<=mouseY+90 and mouseX-30<=self.asteroid26.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid27.yi<=mouseY+90 and mouseX-30<=self.asteroid27.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid28.yi<=mouseY+90 and mouseX-30<=self.asteroid28.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid29.yi<=mouseY+90 and mouseX-30<=self.asteroid29.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid30.yi<=mouseY+90 and mouseX-30<=self.asteroid30.xi<=mouseX+30:
             self.gameover=True
         if mouseY-90<=self.asteroid31.yi<=mouseY+90 and mouseX-30<=self.asteroid31.xi<=mouseX+30:
             self.gameover=True
                 
    def timer(self):
        if self.time_seconds==self.timeover:
            self.gameover=True
            
    def gam(self): #displays gameover images, loss or win
        if self.gameover==True and self.time_seconds!=self.timeover:
            image(self.game_lost_image, 0,0)
            textSize(25)
            text('\nYou survived for: '+str(self.time_seconds)+' seconds',320,50)
            
        if self.time_seconds==self.timeover:
            image(self.game_won_image, 0,0)    

game = Game()

click_start = False

hor_l = 180
ver_l = 100
x=410
y = 590

def setup():
    size(1000, 700)
    background(255, 255, 255)
    
    
def mouseClicked():#detects mouse click
    global game
    if game.gameover: #restart condition
        game.bg_sound.close()
        game.gameover_sound.close()
        game.col_sound.close()
        game=Game()    
   
    global click_start
    global hor_l
    global ver_l 
    global x
    global y 

    if mouseX>= x and mouseX<= x + hor_l and mouseY>=y and mouseY<=y+ver_l: #yellow overlay on start button
        click_start = True

def draw():
    global click_start
    global hor_l 
    global ver_l 
    global x
    global y 
    if click_start == False: #displays the start menu
         start_menu = loadImage(path + "/images/start_menu.png")
         image(start_menu, 0,0)
         if mouseX>= x and mouseX<= x + hor_l and mouseY>=y and mouseY<=y+ver_l: #yellow overlay on start button
             noFill()
             strokeWeight(3)
             stroke(255, 255, 0)
             rect(x-2, y + 2, hor_l, ver_l - 46)

    if click_start == True: #displays the game
            background(255, 255, 255)
            noCursor()
            sec = second()
            game.display()
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
            
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
            
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
            
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
            
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
        
    
    

    
    


    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

    
    
    
    
    
    

    
    
