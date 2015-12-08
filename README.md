##About
This program draws Spirograph curves using Python and the Turtle library. 

To familiarize yourself with what a Spirograph is as well as to see the mathematical derivation of Spirograph curve equations, visit https://en.wikipedia.org/wiki/Spirograph 

For Turtle documentation, visit https://docs.python.org/2/library/turtle.html

##How to use
Create a new Python file and import the Spirograph module: 
```
from Spirograph import Spirograph
```

The program requires instantiation of a Spirograph. The constructor accepts the radius for the Spirograph's outer circle

```
#create a new Spirograph toy with R = 300
my_spirograph = Spirograph(220)
```

Then, use the two setter methods:

```
my_spirograph.setSmallCircle(65) #sets the radius of the inner circle
my_spirograph.setPen(52, 'lightblue') #sets the distance from the inner circle's center and pen position; sets pen color
```

Now everything is ready to draw the Spirograph curve:
```
my_spirograph.draw()
```

The curves can now be erased by using the clear() method:
```
#wait 5 sec (time delay is the method argument. 120sec limit) and then clear the drawing
my_spirograph.clear(5)
```

Alternatively, it is possible to continue drawing additional Spirograph curves on the same canvas. For example, 

```
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
```

##Randomize colors:
In order to make the Turtle's color randomly change upon completion of each period of the curve, change the randColors variable to True on line 84 in Spirograph.py:

##A full example program 1:
In the following program, three Spirograph curves are drawn on top of one another. Then, then canvas is cleared and two more curves are drawn. IMPORTANT: Note the exitonclick() method on the last line. It will prevent the Turtle window from closing automatically. 

```
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
```

##A full example program 2:
```
from Spirograph import Spirograph

s = Spirograph(309)
s.setSmallCircle(351)
s.setPen(300, 'forest green')

s.draw()


s.setSmallCircle(279)
s.setPen(78,'goldenrod4')

s.draw()
s.t.getscreen().exitonclick()


```




