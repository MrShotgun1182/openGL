import glfw
from OpenGL.GL import *
import numpy as np

if not glfw.init():
    raise Exception("GLFW could not be initialized!")

window = glfw.create_window(800, 800, "OpenGl square", None, None)

if not window:
    glfw.terminate()
    raise Exception("Window could not be created!")

glfw.make_context_current(window)

square_vertex = np.array([
    -0.2, -0.2, 0.0,
     0.2, -0.2, 0.0,
     0.2,  0.2, 0.0,
    -0.2,  0.2, 0.0
], dtype=np.float32)

square_VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, square_VBO)
glBufferData(GL_ARRAY_BUFFER, square_vertex.nbytes, square_vertex, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
    
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.terminate()
