import turtle as trtl
#generating game...
wn = trtl.Screen()
leftfighterImage = "leftfighter.gif"
wn.addshape(leftfighterImage)
rightfighterImage = "rightfighter.gif"
wn.addshape(rightfighterImage)
#gameoverImage = "gamover1.gif"
#wn.addshape(gameoverImage)
#create background
  #sky
trtl.Screen().bgcolor("deep sky blue")
background = trtl.Turtle()
background.penup()
background.goto(-350,-200)
background.pendown()
x = -350
y = -200
dirt = 0
  #dirt floor
while(dirt < 7):
  background.pencolor("brown")
  background.fillcolor("brown")
  background.begin_fill()
  background.setheading(90)
  background.forward(60)
  background.setheading(0)
  background.forward(100)
  background.setheading(270)
  background.forward(60)
  background.setheading(180)
  background.forward(100)
  background.end_fill()
  x = x + 100
  background.penup()
  background.goto(x,y)
  background.pendown()
  dirt+=1
background.hideturtle()  











#create health bar1
healthbar1 = trtl.Turtle()
healthbar11 = trtl.Turtle()
healthbar12 = trtl.Turtle()
healthbar13 = trtl.Turtle()


#first portion
healthbar1.fillcolor("red")
healthbar1.begin_fill()
healthbar1.penup()
healthbar1.goto(-355,210)
healthbar1.pendown()
healthbar1.forward(30)
healthbar1.setheading(270)
healthbar1.forward(30)
healthbar1.setheading(180)
healthbar1.forward(30)
healthbar1.setheading(90)
healthbar1.forward(30)
healthbar1.end_fill()
healthbar1.hideturtle()
#second portion
healthbar11.fillcolor("red")
healthbar11.begin_fill()
healthbar11.penup()
healthbar11.goto(-325,210)
healthbar11.pendown()
healthbar11.forward(30)
healthbar11.setheading(270)
healthbar11.forward(30)
healthbar11.setheading(180)
healthbar11.forward(30)
healthbar11.setheading(90)
healthbar11.forward(30)
healthbar11.end_fill()
healthbar11.hideturtle()
#third portion
healthbar12.fillcolor("red")
healthbar12.begin_fill()
healthbar12.penup()
healthbar12.goto(-295,210)
healthbar12.pendown()
healthbar12.forward(30)
healthbar12.setheading(270)
healthbar12.forward(30)
healthbar12.setheading(180)
healthbar12.forward(30)
healthbar12.setheading(90)
healthbar12.forward(30)
healthbar12.end_fill()
healthbar12.hideturtle()
#fourth portion
healthbar13.fillcolor("red")
healthbar13.begin_fill()
healthbar13.penup()
healthbar13.goto(-265,210)
healthbar13.pendown()
healthbar13.forward(30)
healthbar13.setheading(270)
healthbar13.forward(30)
healthbar13.setheading(180)
healthbar13.forward(30)
healthbar13.setheading(90)
healthbar13.forward(30)
healthbar13.end_fill()
healthbar13.hideturtle()
#decreasing health
healthbar14 = trtl.Turtle()
healthbar15 = trtl.Turtle()
healthbar16 = trtl.Turtle()
healthbar17 = trtl.Turtle()

  


  
  
  

#create health bar2
#create health bar1
healthbar2 = trtl.Turtle()
healthbar21 = trtl.Turtle()
healthbar22 = trtl.Turtle()
healthbar23 = trtl.Turtle()


  #first portion
healthbar2.fillcolor("red")
healthbar2.begin_fill()
healthbar2.penup()
healthbar2.goto(230,210)
healthbar2.pendown()
healthbar2.forward(30)
healthbar2.setheading(270)
healthbar2.forward(30)
healthbar2.setheading(180)
healthbar2.forward(30)
healthbar2.setheading(90)
healthbar2.forward(30)
healthbar2.end_fill()
healthbar2.hideturtle()
#second portion
healthbar21.fillcolor("red")
healthbar21.begin_fill()
healthbar21.penup()
healthbar21.goto(260,210)
healthbar21.pendown()
healthbar21.forward(30)
healthbar21.setheading(270)
healthbar21.forward(30)
healthbar21.setheading(180)
healthbar21.forward(30)
healthbar21.setheading(90)
healthbar21.forward(30)
healthbar21.end_fill()
healthbar21.hideturtle()
#third portion
healthbar22.fillcolor("red")
healthbar22.begin_fill()
healthbar22.penup()
healthbar22.goto(290,210)
healthbar22.pendown()
healthbar22.forward(30)
healthbar22.setheading(270)
healthbar22.forward(30)
healthbar22.setheading(180)
healthbar22.forward(30)
healthbar22.setheading(90)
healthbar22.forward(30)
healthbar22.end_fill()
healthbar22.hideturtle()
#fourth portion
healthbar23.fillcolor("red")
healthbar23.begin_fill()
healthbar23.penup()
healthbar23.goto(320,210)
healthbar23.pendown()
healthbar23.forward(30)
healthbar23.setheading(270)
healthbar23.forward(30)
healthbar23.setheading(180)
healthbar23.forward(30)
healthbar23.setheading(90)
healthbar23.forward(30)
healthbar23.end_fill()
healthbar23.hideturtle()
#decreasing health
healthbar24 = trtl.Turtle()
healthbar25 = trtl.Turtle()
healthbar26 = trtl.Turtle()
healthbar27 = trtl.Turtle()

#create characters
#ryu
ryu = trtl.Turtle()
ryu.shape(leftfighterImage)
ryu.penup()
ryu.goto(-200,-65)
#bison
bison = trtl.Turtle()
bison.shape(rightfighterImage)
bison.penup()
bison.goto(200,-65)
#game simulation
#first attack(ryu)

count = 0
while(count < 70):
  ryu.forward(5)
  count +=1

if(abs(ryu.xcor() - bison.xcor() <= 20)):
  if(abs(ryu.ycor() - bison.ycor() <= 20)):
    healthbar24.fillcolor("white")
    healthbar24.begin_fill()
    healthbar24.penup()
    healthbar24.goto(230,210)
    healthbar24.pendown()
    healthbar24.forward(30)
    healthbar24.setheading(270)
    healthbar24.forward(30)
    healthbar24.setheading(180)
    healthbar24.forward(30)
    healthbar24.setheading(90)
    healthbar24.forward(30)
    healthbar24.end_fill()
    healthbar24.hideturtle()
   
    count1 = 0
    ryu.setheading(180)
    while(count1 < 50):
      ryu.forward(7)


      count1+=1 
#second attack(bison)
count = 0
bison.setheading(180)
while(count < 70):
  bison.forward(5)
  count +=1

if(abs(ryu.xcor() - bison.xcor() <= 20)):
  if(abs(ryu.ycor() - bison.ycor() <= 20)):
    healthbar14.fillcolor("white")
    healthbar14.begin_fill()
    healthbar14.penup()
    healthbar14.goto(-265,210)
    healthbar14.pendown()
    healthbar14.forward(30)
    healthbar14.setheading(270)
    healthbar14.forward(30)
    healthbar14.setheading(180)
    healthbar14.forward(30)
    healthbar14.setheading(90)
    healthbar14.forward(30)
    healthbar14.end_fill()
    healthbar14.hideturtle()
   
    count1 = 0
    bison.setheading(0)
    while(count1 < 50):
      bison.forward(7)


      count1+=1 

#third attack(ryu)
count2 = 0
ryu.setheading(0)
while(count2 < 70):
  ryu.forward(5)
  count2 +=1

if(abs(ryu.xcor() - bison.xcor() <= 20)):
  if(abs(ryu.ycor() - bison.ycor() <= 20)):
    healthbar25.fillcolor("white")
    healthbar25.begin_fill()
    healthbar25.penup()
    healthbar25.goto(260,210)
    healthbar25.pendown()
    healthbar25.forward(30)
    healthbar25.setheading(270)
    healthbar25.forward(30)
    healthbar25.setheading(180)
    healthbar25.forward(30)
    healthbar25.setheading(90)
    healthbar25.forward(30)
    healthbar25.end_fill()
    healthbar25.hideturtle()
   
    count21 = 0
    ryu.left(180)
    while(count21 < 50):
      ryu.forward(7)


      count21+=1 
#fourth attack(bison)
count2 = 0
bison.setheading(180)
while(count2 < 70):
  bison.forward(5)
  count2 +=1

if(abs(ryu.xcor() - bison.xcor() <= 20)):
  if(abs(ryu.ycor() - bison.ycor() <= 20)):
    healthbar15.fillcolor("white")
    healthbar15.begin_fill()
    healthbar15.penup()
    healthbar15.goto(-295,210)
    healthbar15.pendown()
    healthbar15.forward(30)
    healthbar15.setheading(270)
    healthbar15.forward(30)
    healthbar15.setheading(180)
    healthbar15.forward(30)
    healthbar15.setheading(90)
    healthbar15.forward(30)
    healthbar15.end_fill()
    healthbar15.hideturtle()
   
    count21 = 0
    bison.setheading(0)
    while(count21 < 50):
      bison.forward(7)


      count21+=1 





#final special attack
#ryu.setheading(0)
#ryu.setheading(90)
#ryu.forward(50)
ryu.setheading(0)
count3 = 0
while(count3 < 23):
  ryu.forward(15)
  count3 +=1

if(abs(ryu.xcor() - bison.xcor() <= 20)):
  if(abs(ryu.ycor() - bison.ycor() <= 20)):
    healthbar26.fillcolor("white")
    healthbar26.begin_fill()
    healthbar26.penup()
    healthbar26.goto(290,210)
    healthbar26.pendown()
    healthbar26.forward(30)
    healthbar26.setheading(270)
    healthbar26.forward(30)
    healthbar26.setheading(180)
    healthbar26.forward(30)
    healthbar26.setheading(90)
    healthbar26.forward(30)
    healthbar26.end_fill()
    healthbar26.hideturtle()
    healthbar27.fillcolor("white")
    healthbar27.begin_fill()
    healthbar27.penup()
    healthbar27.goto(320,210)
    healthbar27.pendown()
    healthbar27.forward(30)
    healthbar27.setheading(270)
    healthbar27.forward(30)
    healthbar27.setheading(180)
    healthbar27.forward(30)
    healthbar27.setheading(90)
    healthbar27.forward(30)
    healthbar27.end_fill()
    healthbar27.hideturtle()
    
   
    count31 = 0
    ryu.left(180)
    while(count31 < 50):
      ryu.forward(7)


      count31+=1 

#m bison dies      

bison.forward(500)
#shows who won
listWhoWon = [1,2,3,4,5]
for i in listWhoWon: 
  if(i < 5): 
    print("Ryu wins!!!!")
trtl.Screen().bgcolor("black")

#ryu exits stadium
ryu.setheading(180)
ryu.forward(500)
#game is offically over
#gameOver = trtl.Turtle()
#gameOver.shape(gameoverImage)
#gameOver.penup()
#gameOver.goto(0,100)





















wn.mainloop()
