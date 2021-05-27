from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

from math import pi, cos, sin
 
a = 0
n1 = 50
n2 = 50
r = 1.5

def f(i,j):
    theta = ((pi * i) / (n1 -1)) - (pi / 2)
    phi = 2 * pi * j / (n2 - 1)

    x = r * cos(theta) * cos(phi)
    y = r * sin(theta)
    z = r * cos(theta) * sin(phi)

    return x, y**2, z

def mesh():
    glPushMatrix()
    glRotatef(a,-3.0,3.0,1.0)
    
    for i in range(round(n1/2)):
        glBegin(GL_QUAD_STRIP)
        
        for j in range(n2):
            glColor3fv(((1.0 * (i + 1) / (n1 - 1)), 0, 1.0 - (1.0 * (i + 1) / (n1 - 1))))
            x, y, z = f(i,j)
            glVertex3f(x,y,z)
            
            glColor3fv(((1.0 * (i + 1) / (n1 - 1)), 0, 1.0 - (1.0 * (i + 1) / (n1 - 1))))
            x, y, z = f(i + 1, j)
            glVertex3f(x,y,z)

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
    glutTimerFunc(50,timer,10)

def reshape(w,h):
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45,float(w)/float(h),0.5,40.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0,1,10,0,0,0,0,1,0)

def init():
	mat_ambient = (1.0, 0.1745, 0.0215,1)
	mat_diffuse = (0.07568, 0.61424, 0.07568,1)
	mat_specular = (0.633, 0.727811, 0.633,1)
	mat_shininess = (60,)
	light_position = (0.0, 0.0, 0.0, 3.0)
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
	glutCreateWindow("Shader - Revolucao")
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(desenha)
	glutTimerFunc(50,timer,10)
	glutMainLoop()

main()