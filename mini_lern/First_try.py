from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # رنگ قرمز برای رأس اول
    glVertex2f(1.0, 1.0)    # مختصات رأس اول
    glColor3f(0.0, 1.0, 0.0)  # رنگ سبز برای رأس دوم
    glVertex2f(-1, -1)     # مختصات رأس دوم
    glColor3f(0.0, 0.0, 1.0)  # رنگ آبی برای رأس سوم
    glVertex2f(0.0, 0.5)      # مختصات رأس سوم
    glColor3f(1, 0.0, 1.0)  # رنگ آبی برای رأس سوم
    glVertex2f(1, -1)      # مختصات رأس سوم
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Simple Triangle")
    glutDisplayFunc(draw_triangle)
    glutMainLoop()

if __name__ == "__main__":
    main()
