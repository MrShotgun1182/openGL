import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class App:

    def __init__(self):
        self.initailize_glfw()
        self.initialize_opengl()
    
    def initailize_glfw(self) -> None:
        glfw.init()
        glfw.window_hint(
            GLFW_CONSTANTS.GLFW_OPENGL_PROFILE,
            GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(
            GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, 
            GLFW_CONSTANTS.GLFW_TRUE)
        
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "project1", None, None)
        glfw.make_context_current(self.window)

    def initialize_opengl(self) -> None:
        glClearColor(0.1, 0.7, 0.5, 1.0)
        

    def run(self):
        while not glfw.window_should_close(self.window):
            if glfw.get_key(self.window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                break

            glfw.poll_events()

            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)
            # glClearColor(random.random(), random.random(), random.random(), 1.0)


    def quit(self):
        glfw.destroy_window(self.window)
        glfw.terminate()
        

my_app = App()
my_app.run()
my_app.quit()