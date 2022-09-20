from turtle import *

#-----------------------------------------
#   CODE OF MAKING OUTTER SELL
#----------------------------------------

color("#1AA34D")
begin_fill()
forward(200)
circle(40,90)
forward(200)
circle(40,90)
forward(200)
circle(40,90)
forward(200)
circle(40,90)
forward(100)
end_fill()

#---------------------------------------------------
# CODE OF SETTING LOCAION FOR MAKING OF INNER SQUARE
#---------------------------------------------------
color("#1AA34D")
begin_fill()
left(90)
forward(35)
left(90)
forward(5)
right(90)
right(90)
end_fill()

#---------------------------------------------
#   CODE OF MAKING THE INNER SQUARE
#-------------------------------------------

color("#FFFFFF")
begin_fill()
forward(90)
circle(20,90)
forward(170)
circle(20,90)
forward(170)
circle(20,90)
forward(170)
circle(20,90)
forward(85)
left(90)
forward(20)
right(90)
end_fill()


color("#1AA34D")
begin_fill()
forward(75)
circle(10,90)
forward(150)
circle(10,90)
forward(150)
circle(10,90)
forward(150)
circle(10,90)
forward(75)
end_fill()

#-----------------------------------------------
#  CODE OF SETTING LOCATION FOR INNER CIRCLE
#---------------------------------------------------

color("#1AA34D")
begin_fill()
left(90)
forward(40)
right(90)
end_fill()

#-----------------------------------------------
#  CODE OF MAKING INNER CIRCLE
#---------------------------------------------------

color("#FFFFFF")
begin_fill()
circle(50,360)
left(90)
forward(15)
right(90)
end_fill()

color("#1AA34D")
begin_fill()
circle(35)
end_fill()

#-----------------------------------------------
#  CODE OF SETTING LOCATION FOR SMALL CIRCLE
#---------------------------------------------------

color("#FFFFFF")
begin_fill()
forward(35)
end_fill()

color("#1AA34D")
begin_fill()
forward(35)
end_fill()

color("#1AA34D")
begin_fill()
left(90)
forward(90)
end_fill()


#-----------------------------------------------
#  CODE OF MAKING SMALL CIRCLE
#---------------------------------------------------

color("#FFFFFF")
begin_fill()
circle(10)
end_fill()

#-----------------------------------------------
#                       ENDING
#---------------------------------------------------

color("#1AA34D")
begin_fill()
right(90)
right(90)
forward(20)
end_fill()
done()