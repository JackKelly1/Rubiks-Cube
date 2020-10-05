class Cubie():
    
    def __init__(self, x, y, z, lenc, colours):
        self.x = x
        self.y = y
        self.z = z
        # length of a cubie side
        self.lenc = lenc
        self.colours = colours
        


    def show(self):
        # sets the color used to draw lines and borders around shapes
        stroke(0)
        # sets the width of the stroke used for lines, points, and the border around shapes
        strokeWeight(8)
        # pushes the current transformation matrix onto the matrix stack
        pushMatrix()
        # specifies an amount to displace objects within the display window
        translate(self.x, self.y, self.z)
        
        r = self.lenc/2
        
        # create the 6 sides of a cubie
        beginShape(QUADS)
        fill(self.colours[0])
        vertex(self.lenc/2, self.lenc/2, self.lenc/2)
        vertex(self.lenc/2, self.lenc/2, -self.lenc/2)
        vertex(self.lenc/2, -self.lenc/2, -self.lenc/2)
        vertex(self.lenc/2, -self.lenc/2, self.lenc/2)
        
        fill(self.colours[1])
        vertex(-self.lenc/2, self.lenc/2, self.lenc/2)
        vertex(-self.lenc/2, self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, -self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, -self.lenc/2, self.lenc/2)
        
        fill(self.colours[2])
        vertex(self.lenc/2, self.lenc/2, self.lenc/2)
        vertex(self.lenc/2, self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, self.lenc/2, self.lenc/2)
        
        fill(self.colours[3])
        vertex(self.lenc/2, -self.lenc/2, self.lenc/2)
        vertex(self.lenc/2, -self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, -self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, -self.lenc/2, self.lenc/2)
        
        fill(self.colours[4])
        vertex(self.lenc/2, self.lenc/2, self.lenc/2)
        vertex(self.lenc/2, -self.lenc/2, self.lenc/2)
        vertex(-self.lenc/2, -self.lenc/2, self.lenc/2)
        vertex(-self.lenc/2 , self.lenc/2, self.lenc/2)
        
        fill(self.colours[5])
        vertex(self.lenc/2, self.lenc/2, -self.lenc/2)
        vertex(self.lenc/2, -self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, -self.lenc/2, -self.lenc/2)
        vertex(-self.lenc/2, self.lenc/2, -self.lenc/2)
        
        # end the creation of the cubie
        endShape()
        # pops the current transformation matrix off the matrix stack
        popMatrix()
