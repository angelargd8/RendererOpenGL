import glm 
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from numpy import array, float32


class Buffer(object):
    def __init__(self,data):
        self.vertBuffer = array(data, dtype=float32)
             
        #vertex buffer object
        self.VBO = glGenBuffers(1) #genera 1 buffer
        
        #vertex array object
        self.VAO = glGenVertexArrays(1)     

        
    def Render(self): 
        #primero atar a la tarjta de video vbo, vao
        #bind = atar
        #ATAR LOS buffers a la tarjeta de video
        glBindBuffer(GL_ARRAY_BUFFER ,self.VBO)
        glBindVertexArray(self.VAO)
        
        # mandar la informacion de vertices 
        glBufferData(GL_ARRAY_BUFFER,           #bufferID, en el que se guarda la informacion
                     self.vertBuffer.nbytes,    #buffer size in the bytes
                     self.vertBuffer,           #buffer data
                     GL_STATIC_DRAW)            #usage 
        
        #atributos
        
        #atributo de posiciones
        glVertexAttribPointer(0,                    #attribute number
                              3,                    #size de datos
                              GL_FLOAT,             #type
                              GL_FALSE,             #is it normalized?
                              4 * 3,                #stride size in bytes
                              ctypes.c_void_p(0))   #offset
        
        glEnableVertexAttribArray(0)
        
        glDrawArrays(GL_TRIANGLES, 0, len(self.vertBuffer) // 3) #3 es la cantidad de datos
        

        
    
