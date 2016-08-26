from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *
import sys

global fMoonRot
global fEarthRot
global lightPos

fMoonRot = fEarthRot = 0.
whiteLight = (0.2, 0.2, 0.2, 1.)
sourceLight = (0.8, 0.8, 0.8, 1.)
lightPos = (0., 0., 0., 1.)

def init():
    glClearColor(0., 0., 0., 0.)
    glEnable(GL_CULL_FACE)
    glFrontFace(GL_CCW)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, whiteLight)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, sourceLight)
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)    
    pass

def redraw():
    global fMoonRot
    global fEarthRot
    global lightPos

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    # Move all the scene into view field
    glTranslatef(0., 0., -300.)
    # Set sun color yellow
    glColor3ub(255, 255, 0)
    glDisable(GL_LIGHTING)
    glutSolidSphere(15., 15, 15)
    glEnable(GL_LIGHTING)
    # Settle light source
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos)
    # Rotate coord. system
    glRotatef(fEarthRot, 0., 1., 0.)
    # Draw Earth
    glColor3ub(0, 0, 255)
    glTranslatef(105., 0., 0.)
    glutSolidSphere(15., 15, 15)
    # Rotate coord. system in conjuction with the Earth and draw the Moon
    glColor3ub(200, 200, 200)
    glRotatef(fMoonRot, 0., 1., 0.)
    glTranslatef(30., 0., 0.)
    fMoonRot += 15.
    if fMoonRot > 360.: fMoonRot=0.
    glutSolidSphere(6., 15, 15)
    fEarthRot += 5.
    if fEarthRot > 360.: fEarthRot = 0.
    # Restore matrix state
    glPopMatrix()
    glutSwapBuffers()
    pass

def reshape(w, h):
    h = 1 if h == 0 else h
    fAspect = 1.*w/h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45., fAspect, 1., 425.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    pass

def special(key, x, y):
    pass

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(100, timer, 1)

if __name__ == '__main__':
    print ("init")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Sun Earth and Moon")
    glutDisplayFunc(redraw)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special)
    glutTimerFunc(500, timer, 1)
    init()
    glutMainLoop()
    pass
