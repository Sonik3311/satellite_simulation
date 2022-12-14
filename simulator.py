import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def odefun(x, t, G, M):
    v = x[3:6]
    r = -G * M * x[0:3] / ((np.linalg.norm(x[0:3]))**3)
    return [v[0], v[1], v[2], r[0], r[1], r[2]]

class Satellite:
    def __init__(self, mass=1, pos=np.array((0,0,0),dtype=np.float32), velocity=np.array((0,0,0),dtype=np.float32)):
        self.mass = mass
        self.pos = pos
        self.velocity = velocity
        self.acceleration = np.array([0,0,0],dtype=np.float32)

class Planet:
    def __init__(self, mass=10, pos=np.array((0,0,0),dtype=np.float32), radius=1):
        self.mass = mass
        self.pos = pos
        self.radius = radius

class SimulatorEngine:
    def __init__(self, args):
        self.G = 6.6743 * 10**-args["Gfactor"]
        self.M = args["PlanetMass"]
        self.Mr = args["PlanetRadius"]
        self.Or = args["OrbitHeight"] + args["PlanetRadius"]
        self.scale = args["scale"]
        self.startPos = args["initPos"]
        self.startSpeed = args["initSpeed"]
        self.atmosphere = args["Atmosphere"]
        self.density = args["Density"]
        self.LS = args["LS"]

        self.satellite = Satellite(mass=100, pos=self.startPos, velocity=self.startSpeed)
        self.planet = Planet(mass=self.M, pos=np.array([0,0,0]), radius=self.Mr)
        

    def solveODE(self):
        points = []

        North = -43.07 * np.pi / 180
        East = -61.50 * np.pi / 180

        startPos = np.array([np.cos(North) * np.cos(East), np.cos(North) * np.sin(East), np.sin(North)])

        orbit_n = self.get_orbit_normal(startPos, 90, False)
        tau = np.cross(orbit_n, startPos)
        r0 = startPos * self.Or
        v0 = tau * self.startSpeed

        x0 = [r0[0], r0[1], r0[2], v0[0], v0[1], v0[2]]
        tspan = np.linspace(0, 24 * 3600, num = 1000)
        solution = odeint(odefun, x0, tspan, rtol=1e-13, atol= 1e-14, args=(self.G, self.M))
        x, y, z = solution[:, 0], solution[:, 1], solution[:, 2]
        for i in range(len(x)):
            points.append([x[i]/self.scale, y[i]/self.scale, z[i]/self.scale])
        return points, None
    
    def get_orbit_normal(self, r, orbit_incl, switch):
        phi = orbit_incl * np.pi / 180
        z = np.cos(phi)
        p1 = -r[1] / r[0]
        p2 = -z * r[2] / r[0]
        a = p1 ** 2 + 1
        b = 2 * p1 * p2
        c = p2 ** 2 - np.sin(phi) ** 2
        y1 = ((-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        y2 = ((-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        x1 = p1 * y1 + p2
        x2 = p1 * y2 + p2
        n1 = np.array([x1, y1, z])
        n2 = np.array([x2, y2, z])

        if switch:
            return n1
        else:   
            return n2
    
    def simulatePHYS(self):
        points = []
        velocity = []
        energy = [[],[],[]]

        points.append(self.satellite.pos/self.scale)
        entered = True
        prev_state = True
        
        for i in range(50000):
            entered = np.linalg.norm(self.satellite.pos-self.startPos) < 0.5*self.scale
            if ((entered == False and prev_state == False) or (entered == False and prev_state == True) or (entered == True and prev_state == True)) or not self.LS: #check if we completed an orbital loop. Useless in big systems, so i might remove it
                dist = np.linalg.norm(self.satellite.pos - self.planet.pos)
                
                if dist <= self.Mr: #Collision Check
                    break
                
                if dist <= self.Mr+self.atmosphere: #atmosphere check
                    speed = np.linalg.norm(self.satellite.velocity)
                    dragforce = self.density * speed*speed
                    drag = -self.satellite.velocity/speed * dragforce
                    self.satellite.velocity = self.satellite.velocity + drag
                
                dir = (self.planet.pos - self.satellite.pos) / dist
                forceMagnitude = ((self.satellite.mass * self.planet.mass) / dist**2) * self.G
                forcevec = dir * forceMagnitude
                self.satellite.velocity = self.satellite.velocity + forcevec
                self.satellite.pos = self.satellite.pos + self.satellite.velocity
                velocity.append(self.satellite.velocity)
                points.append(self.satellite.pos/self.scale)

                #energy
                Ek = (self.G*self.satellite.mass*self.planet.mass)/2*dist
                Ep = 0.5*-self.G * self.planet.mass*self.satellite.mass * 1 * dist
                energy[0].append([Ek])
                energy[1].append([Ep])
                energy[2].append([Ek+Ep])
                
            else:
                points.append(self.startPos/self.scale)
                break
            prev_state = entered
        #plt.plot(energy)
        plt.plot(energy[0], label='E kinetic')
        plt.plot(energy[1], label='E potential')
        plt.plot(energy[2], label='E total')
        plt.legend()
        plt.savefig('energy.png')
            
        return points, velocity
        