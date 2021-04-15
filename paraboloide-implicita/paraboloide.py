from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from math import pi, cos, sin

a = 0

m = 50
n = 50
x0 = -1
y0 = -1
xf = 1
yf = 1
dx = (xf - x0) / m
dy = (yf - y0) / n

def f(i,j):
    return i**2 - j**2

def mesh():
    glPushMatrix()
    glRotatef(a, 2.0, 1.0, 1.0)
    
    for i in range(0, n):
        y = y0 + i * dy   
        glColor3fv(((1.0 * (i + 1) / (m - 1)), 0, 1 - (1.0 * (i + 1) / (m - 1))))
        glBegin(GL_QUAD_STRIP)

        for j in range(0,m):
            x = x0 + j * dx
            glVertex3f(x, y, f(x,y))
            glVertex3f(x, y + dy, f(x, y + dy))
            
        glEnd()

    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1024,1024)
glutCreateWindow("Paraboloide Com Equacao Implicita")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1)
glutMainLoop()