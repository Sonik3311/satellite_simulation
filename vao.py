from vbo import VBO

class VAO:
    def __init__(self, app):
        self.ctx = app.ctx
        self.vbo = VBO(app.ctx)
        self.program = app.shaders
        self.vaos = {}

        self.vaos["sphere"] = self.get_vao(
            program = self.program.programs["default"],
            vbo = self.vbo.vbos["sphere"]
        )
        
        self.vaos["trajectory"] = self.get_vao(
            program = self.program.programs["trajectory"],
            vbo = self.vbo.vbos["trajectory"]
        )

    
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribute)])
        return vao
    
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
