import glm 
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader


class Renderer(object): 
    def __init__(self, screen):
        self.screen = screen
        _,_ , self.width, self.height = screen.get_rect()
        
        glClearColor(0.2, 0.2,0.2, 1)

        glEnable(GL_DEPTH_TEST)
        glViewport(0,0, self.width, self.height)
        self.scene= []
        self.active_shaders = None

    def SetShaders(self, vShader, fShader):
        if vShader is not None and fShader is not None: 
            self.active_shaders = compileProgram( compileShader(vShader, GL_VERTEX_SHADER), 
                                                  compileShader(fShader, GL_FRAGMENT_SHADER)) #compileprogram va a esperar los shadrs a
        else: 
            self.active_shaders= None
            

        
    
    def Render(self): 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.active_shaders is not None: 
            glUseProgram(self.active_shaders) #los shaders activos en ese momento

        for obj in self.scene:
            obj.Render()
    
