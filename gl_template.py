from OpenGL.GL import * 
from OpenGL.GLU import * 
from OpenGL.GLUT import *
import sys

global fMoonRot
global fEarthRot

fMoonRot = fEarthRot = 0.

def init():
    glClearColor(0., 0., 0., 0.)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    pass

def redraw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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

if __name__ == '__main__':
    print ("init")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"GL Template")
    glutDisplayFunc(redraw)
    glutReshapeFunc(reshape)
    glutSpecialFunc(special)
    init()
    glutMainLoop()
    pass
