from os.path import abspath
from inspect import getsourcefile

class ShaderProgram:
    def __init__(self, ctx):
        self.path = abspath(getsourcefile(lambda:0)).replace("shader_program.py", "")
        self.ctx = ctx
        self.programs = {}
        #self.programs['default'] = self.get_program('default')
        #self.programs['trajectory'] = self.get_program('trajectory')
    
    def get_program(self, shader_name):
        with open(self.path+f'program/{shader_name}.vert') as file:
            vertex_shader = file.read()
        
        with open(self.path+f'program/{shader_name}.frag') as file:
            fragment_shader = file.read()
        
        program = self.ctx.program(vertex_shader=vertex_shader,fragment_shader=fragment_shader)
        return program
    
    def load_program(self, name):
        self.programs[name] = self.get_program(name)
    
    def destroy(self):
        [program.release() for program in self.programs.values()]

