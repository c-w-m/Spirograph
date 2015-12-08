from Spirograph import Spirograph
#create a new Spirograph toy with R = 300
my_spirograph = Spirograph(220)

#Draw one curve
my_spirograph.setSmallCircle(65)
my_spirograph.setPen(52, 'lightblue')
my_spirograph.draw()

#draw another on top of the first. Same small circle, different pen slot
my_spirograph.setPen(64, 'aquamarine')
my_spirograph.draw()

#draw one more with different small circle and a different pen slot
my_spirograph.setSmallCircle(279)
my_spirograph.setPen(278, 'yellow')
my_spirograph.draw()

#wait 5 sec and get a new sheet of paper
my_spirograph.clear(5)

#draw another spirograph
my_spirograph.setSmallCircle(76)
my_spirograph.setPen(75,'pink')
my_spirograph.draw()

#one more on top of it 
my_spirograph.setSmallCircle(300)
my_spirograph.setPen(299)

#IMPORTANT: add this line to make sure the program doesn't exit automatically
my_spirograph.t.getscreen().exitonclick()