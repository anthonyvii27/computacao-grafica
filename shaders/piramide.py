from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math 
import sys

dist = 1
qty_lados = 6

def desenha():
	height = 6

	side_rads_size = (2 * math.pi) / qty_lados
	down_radius = 2
	down_vertices = []

	glPushMatrix()
	glTranslatef(0, -2, 0)
	glRotatef(-110, 1.0, 0.0, 0.0)
	
	glBegin(GL_POLYGON)
	for i in range(0, qty_lados):
		x = down_radius * math.cos(i * side_rads_size) - dist
		y = down_radius * math.sin(i * side_rads_size) - dist
		down_vertices += [(x,y)]

		glVertex3f(x, y, 0.0)
	glEnd()

	glBegin(GL_TRIANGLES)
	for i in range(0, qty_lados):
		glNormal3fv(calculaNormal((down_vertices[i][0], down_vertices[i][1], 0.0), (-dist, -dist, height), (down_vertices[(i+1) % qty_lados][0], down_vertices[(i+1) % qty_lados][1], 0.0)))
		glVertex3f(down_vertices[i][0], down_vertices[i][1], 0.0)
		glVertex3f(-dist, -dist, height)
		glVertex3f(down_vertices[(i+1) % qty_lados][0], down_vertices[(i+1) % qty_lados][1], 0.0)
	glEnd()

	glPopMatrix()

def calculaNormal(a, b, c):
    x, y, z = 0, 1, 2
    v0, v1, v2 = a, b, c
    U = (v2[x] - v0[x], v2[y] - v0[y], v2[z] - v0[z])
    V = (v1[x ] -v0[x], v1[y] - v0[y], v1[z] - v0[z])
    N = ((U[y] * V[z] - U[z] * V[y]), (U[z] * V[x] - U[x] * V[z]), (U[x] * V[y] - U[y] * V[x]))
    NLength = sqrt(N[x] * N[x] + N[y] * N[y] + N[z] * N[z])
    return (N[x] / NLength, N[y] / NLength, N[z] / NLength)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 0, 2, 0)
    desenha()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, float(w) / float(h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(20, 10, 0, 0, 0, 0, 0, 10, 0)

def init():
    mat_ambient = (0.2125, 0.1275, 0.054, 1.0)
    mat_diffuse = (0.714, 0.4284, 0.18144, 1.0)
    mat_specular = (0.393548, 0.271906, 0.166721, 1.0)
    mat_shininess = (25.6)

    light_position = (5.0, 5.0, 5.0, 0.0)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_FLAT)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(1024, 768)
    glutCreateWindow("Shader - Pirâmide")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(70, timer, 1)
    init()
    glutMainLoop()

main()