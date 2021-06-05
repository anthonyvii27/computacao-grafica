from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, pi
import png 
import sys

a = 90.0

texture = []
radius = 3
height = 4
vertices = 5

def LoadTextures():
    global texture
    texture = glGenTextures(2)

    reader = png.Reader('./textura.png')
    w, h, pixels, meta = reader.read_flat()

    glBindTexture(GL_TEXTURE_2D, texture[0])
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, 
                 GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)


def figure():
    pontos = []
    angulo = (2 * pi) / vertices

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()    
    glPushMatrix()
    glTranslatef(0.0, 1.5, -10)
    glRotatef(90, 1.0, 0.0, 0.0)
    glRotatef(a, 0.0, 0.0, 1.0)
    glBindTexture(GL_TEXTURE_2D, texture[0])

    # Base inferior
    glBegin(GL_POLYGON)
    for i in range(vertices):
        x = radius * cos(i * angulo)
        y = radius * sin(i * angulo)
        pontos += [(x,y)]

        glTexCoord2f(x, y)
        glVertex3f(x/2, y/2, 0.0)
    glEnd()

    # Base superior
    glBegin(GL_POLYGON)
    for x,y in pontos:
        glTexCoord2f(x, y)
        glVertex3f(x/2, y/2, height)
    glEnd()

    # Laterais
    glBegin(GL_QUADS)
    for i in range(vertices):
        glTexCoord2f(0.0, 0.0)
        glVertex3f(pontos[i][0], pontos[i][1],0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f((pontos[i][0]) / 2, (pontos[i][1]) / 2, height)
        glTexCoord2f(1.0, 1.0)
        glVertex3f((pontos[(i+1) % vertices][0]) / 2, (pontos[(i+1) % vertices][1]) / 2, height)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(pontos[(i+1)%vertices][0], pontos[(i+1) % vertices][1], 0)
    glEnd()

    glPopMatrix()

    glutSwapBuffers()

def Draw():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    figure()
    a = a + 0.5
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(200, 200)
    glutCreateWindow("Textura - Tronco de Pirâmide")
    glutDisplayFunc(Draw)
    LoadTextures()
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glDepthFunc(GL_LESS)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glClearDepth(1.0)
    gluPerspective(-45, 800 / 600, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -10)
    glMatrixMode(GL_MODELVIEW)
    glutTimerFunc(10, timer, 1)
    glutMainLoop()

main()