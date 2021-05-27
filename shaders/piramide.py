from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
 
a = 0

def piramide():
    glPushMatrix()
    glTranslatef(0,0,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(10.0,1.0,0.0,0.0)
    glColor3fv((1.0,1.0,0.0))

    glBegin(GL_POLYGON)

    glVertex3f( 0.0, 1.0, 0.0)    
    glVertex3f(-1.0,-1.0, 1.0) 
    glVertex3f( 1.0,-1.0, 1.0)
    glVertex3f( 1.0,-1.0,-1.1)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)   
    glEnd()

    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    piramide() 
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
	mat_ambient = (1.0, 1.0, 1.0,1)
	mat_diffuse = (1.0, 1.0, 1.0,1)
	mat_specular = (1.0, 1.0, 1.0,1)
	mat_shininess = (60,)
	light_position = (3.0, 0.0, 0.0, 3.0)
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
	glutCreateWindow("Shader - Pirâmide")
	init()
	glutReshapeFunc(reshape)
	glutDisplayFunc(desenha)
	glutTimerFunc(50,timer,10)
	glutMainLoop()

main()