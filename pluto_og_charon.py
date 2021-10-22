from vpython import *

G = 6.67e-11

t = 0
dt = 1e3
tmax = 2e6

origo = vec(0,0,0)
mean_dist = 19.599e6 # m

pluto = sphere(pos=origo, vel=origo, radius=1189.9e3)
charon = sphere(pos=mean_dist * vec(1, 0, 0), vel=origo, radius=606e3)

center = sphere(radius=charon.radius * 0.7, color=color.red)

charon_vel_y = 0.211e3 * 1.06# m/s
charon.vel = vec(0, charon_vel_y, 0)

pluto.m =  1.309e22 # kg
charon.m = 1.62e21  # kg

def euler_cromer(dt, *objects):
    for obj in objects:
        obj.vel = obj.vel + obj.a * dt
        obj.pos = obj.pos + obj.vel * dt

plot = graph()
pos = gcurve()
plot2 = graph()
speed = gcurve()

attach_trail(center, color=color.red)
attach_trail(pluto)
attach_trail(charon)

while True:

    R = (pluto.m * pluto.pos + charon.m * charon.pos) / (pluto.m + charon.m)

    center.pos = R

    pluto.r = pluto.pos - charon.pos
    charon.r = charon.pos - pluto.pos

    pluto.a = -G * charon.m * pluto.r.hat / pluto.r.mag2
    charon.a = -G * pluto.m * charon.r.hat / charon.r.mag2

    euler_cromer(dt, pluto, charon)


    pos.plot(t, pluto.r.mag)
    speed.plot(t, (pluto.vel - charon.vel).mag)
    t += dt
    rate(60)
