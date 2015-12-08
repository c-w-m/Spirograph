from Spirograph import Spirograph

s = Spirograph(309)
s.setSmallCircle(351)
s.setPen(300, 'forest green')

s.draw()


s.setSmallCircle(279)
s.setPen(78,'goldenrod4')

s.draw()
s.t.getscreen().exitonclick()

