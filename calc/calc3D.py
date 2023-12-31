import numpy as np
import math as m
import time


class Graph:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"x = {self.x}\ny = {self.y}\nz = {self.z}"
    
    # makes an array of inital object (graph) data to be later projected
    def makemath(self, step):

        math_arr = []

        for x in self.decimal_range(-7, 7, step):
             for y in self.decimal_range(-7, 7, step):
                  
                  x = eval(self.x)
                  y = eval(self.y)
                  z = eval(self.z)

                  v = np.array([x,y,z])

                  math_arr.append(v)

        return math_arr
    
    def realtimerender(self, voutput, frame_width, frame_height, graph_width, graph_height, phi=-0.05, thta= -0.3, psi= 0.3):
     
        usleep = lambda x: time.sleep(x/1000000.0)

        while True:

            psi += 0.05
            rotation_m = self.make_rotation(phi, thta, psi)

            _routput = self.makeframe(voutput, rotation_m, frame_width, frame_height, graph_width, graph_height)

            self.printframe(_routput, frame_height, frame_width)

            print("\x1b["+ str(frame_height+1) + "A")
            usleep(50000)
                  


    def makeframe(self, math_arr, rotation_m, frame_width, frame_height, graph_width, graph_height):

        # output matrix
        output = [ [' ']*frame_width for i in range(frame_height)]

        for i in range(0, len(math_arr)):
                
                v = math_arr[i]

                r = np.dot(rotation_m, v)
                
                rpos = [int(frame_width/2 + r[1]/graph_width * frame_width),
                int(frame_height/2 - r[2]/graph_height * frame_height)]
                
                if rpos[0] < frame_width and rpos[1] < frame_height and rpos[0] >=0 and rpos[1] >= 0:
                    output[rpos[1]][rpos[0]] = '#'

        return output
        
    def printframe(self, output, frame_height, frame_width):
        # make frame
        for k in range(0, frame_height):
            for j in range(0, frame_width):
                print(output[k][j], end="")
            print("")


    def decimal_range(self, start, stop, increment):
        while start < stop:
            yield start
            start += increment

    # makes a rotation matrix from given Euler angles
    def make_rotation(self, phi, thta, psi):
        
        # consolidated rotation matrix
        cosphi = m.cos(phi)
        sinphi = m.sin(phi)

        costhta = m.cos(thta)
        sinthta = m.sin(thta)

        cospsi = m.cos(psi)
        sinpsi = m.sin(psi)

        rotation_m = np.array([[costhta*cospsi, cospsi*sinthta*sinphi - sinpsi*cosphi, cospsi*sinthta*cosphi + sinpsi*sinphi],
                            [sinpsi*costhta, sinpsi*sinthta*sinphi + cospsi*cosphi, sinpsi*sinthta*cosphi - cospsi*sinphi],
                            [-sinthta, costhta*sinphi, costhta*cosphi]])

        return rotation_m

# TODO: add child classes for graphing axes and other preset objects (cube, torus, etc...)

class Axes(Graph):
     pass

class Torus(Graph):
     pass

class Cube(Graph):
     pass

class Sphere(Graph):
     pass
