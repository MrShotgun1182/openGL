import glfw
from OpenGL.GL import *
import numpy as np

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

if not glfw.init():
    raise Exception("GLFW could not be initialized!")

window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Square and Triangle in One Window", None, None)
if not window:
    glfw.terminate()
    raise Exception("Window not created!")

glfw.make_context_current(window)

triangle_vertices = np.array([
    -0.5, -0.5, 0.0,
     0.5, -0.5, 0.0,
     0.0,  0.5, 0.0
], dtype=np.float32)

square_vertices = np.array([
    -0.25, 0.25, 0.0,
     0.25, 0.25, 0.0,
     0.25, -0.25, 0.0,
    -0.25, -0.25, 0.0
], dtype=np.float32)

triangle_VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, triangle_VBO)
glBufferData(GL_ARRAY_BUFFER, triangle_vertices.nbytes, triangle_vertices, GL_STATIC_DRAW)

square_VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, square_VBO)
glBufferData(GL_ARRAY_BUFFER, square_vertices.nbytes, square_vertices, GL_STATIC_DRAW)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    
    glBindBuffer(GL_ARRAY_BUFFER, triangle_VBO)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glDisableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, square_VBO)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glDrawArrays(GL_QUADS, 0, 4)
    glDisableVertexAttribArray(0)

    glfw.swap_buffers(window)
    glfw.poll_events()

glDeleteBuffers(1, [triangle_VBO])
glDeleteBuffers(1, [square_VBO])
glfw.terminate()
