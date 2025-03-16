import glfw
from OpenGL.GL import *
import numpy as np

if not glfw.init():
    raise Exception("GLFW could not be initialized!")

window = glfw.create_window(800, 800, "OpenGL Triangle", None, None)
if not window:
    glfw.terminate()
    raise Exception("Window could not be created!")

glfw.make_context_current(window)

vertex = np.array([
    -0.5, -0.5, 0.0,
     0.5, -0.5, 0.0,
     0.0,  0.5, 0.0
], dtype=np.float32)

VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertex.nbytes, vertex, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

while not glfw.window_should_close(window):
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(window)
    glfw.poll_events()
    
glfw.terminate()