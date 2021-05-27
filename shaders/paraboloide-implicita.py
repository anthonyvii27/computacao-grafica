from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

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
    glutTimerFunc(50,timer,1)

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,float(w)/float(h),0.1,50.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
	mat_ambient = (0.0215, 0.1745, 0.0215,1)
	mat_diffuse = (1.0, 1.0, 1.0,1)
	mat_specular = (0.633, 0.727811, 0.633,1)
	mat_shininess = (60,)
	light_position = (0.0, 50.0, 50.0, 1.0)
	glClearColor(0.0,0.0,0.0,0.0)
	glShadeModel(GL_SMOOTH)

	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
	glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_MULTISAMPLE)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
	glutInitWindowSize(800,600)
	glutCreateWindow("Shader - Implicita")
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(desenha)
	glutTimerFunc(50,timer,1)
	glutMainLoop()

main()