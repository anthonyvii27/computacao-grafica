from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
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
    glutTimerFunc(15,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ANTHONY VINICIUS - PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(15,timer,1)
glutMainLoop()