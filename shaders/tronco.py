from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import math

a = 0

cores = ((0,0,1), (1,1,0), (1,0,0), (1,1,0), (1,0,0), (1,1,0), (1,0,0), (0,0,1))

def prisma(raioInferior, raioSuperior):
    pontosBaseSuperior = []
    pontosBaseInferior = []
    N = 6
    H = 2
    angulo = (2*math.pi)/N

    glPushMatrix()
    glTranslatef(0,0,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3fv(cores[0])

    # Base Inferior
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raioInferior * math.cos(i*angulo)
        y = raioInferior * math.sin(i*angulo)
        pontosBaseInferior += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    # Base Superior
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raioSuperior * math.cos(i*angulo)
        y = raioSuperior * math.sin(i*angulo)
        pontosBaseSuperior += [ (x,y) ]
        glVertex3f(x,y,H)
    glEnd()

    # Lados do prisma
    for i in range(0,N):
        glBegin(GL_QUADS)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBaseInferior[i][0],pontosBaseInferior[i][1],0.0)
        glVertex3f(pontosBaseInferior[(i+1)%N][0],pontosBaseInferior[(i+1)%N][1],0.0)
        glVertex3f(pontosBaseSuperior[(i+1)%N][0],pontosBaseSuperior[(i+1)%N][1],H)
        glVertex3f(pontosBaseSuperior[i][0],pontosBaseSuperior[i][1],H)
        glEnd()
    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    prisma(3,2) 
    glPopMatrix()
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
	mat_ambient = (1.0, 0.0, 0.0, 1)
	mat_diffuse = (1.0, 1.0, 1.0, 1)
	mat_specular = (1.0, 1.0, 1.0, 1)
	mat_shininess = (50,)
	light_position = (3.0, -2.0, 3.0, 1.0)
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