import numpy as np

SOLVER = 'PHYS'
#ODE : good big orbits, no info (используйтя для +- точного соотношения орбиты и земли)
#PHYS: VERY SLOW with big orbits, a lot of info (need to scale down simulation size like 10000km orbit radius -> 10m orbit radius so there are not a lot of calculations)

G_FACTOR = 11 #не трогать
if SOLVER == "ODE":
    #Change if your solver is ODE
    M = 5.972 * 10 ** 24 # Масса земли
    R = 6371000 # Радиус земли
    r = 473000 #Высота спутника
    SCALE = 10**6 #Насколько уменьшить размер симуляции (я всё рисую в 10 метрах, когда орбиты могуть быть размером в тысячи км)
    VELOCITY = 6000 #Скорость спутника
    
    POSITION = 1 # не используется солвером ODE
    ATMOSPHERE = 10  # не используется солвером ODE
    A_DENSITY = 1 # не используется солвером ODE
    LOOP_STOP = False # не используется солвером ODE
else:
    #Change if your solver is PHYS
    M = 1000000
    R = 3 #не трогать
    r = 1 
    SCALE = 1 
    VELOCITY = np.array([0,0.05,0.02], dtype=np.float32)
    POSITION = np.array([4,0,0])
    ATMOSPHERE = 1 # 0 <= x <= 1 высота атмосферы
    A_DENSITY = 1 #плотность атмосферы
    LOOP_STOP = False #Должны ли мы считать только 1 круг или продолжать делать после 1-го другие



