import calc3D as cd
import time
import math as m

if __name__ == '__main__':
    # x = "5*m.sin(thta)*m.cos(phi)"
    # y = "5*m.sin(thta)*m.sin(phi)"
    # z = "5*m.cos(thta)"

    x = "x"
    y = "y"
    z = "x*y/10"

    frame_height = 40
    frame_width = 100

    # define x scale (basically: how much zoom? set to frame sizes for 1x zoom):
    e_1_scale = frame_width
    # define y scale:
    e_2_scale = frame_height

    # define graph tick mark scale (range of values shown on screen):
    e_1tick_scale = 20
    e_2tick_scale = 17

    graph_height = frame_height/(e_2_scale/(e_2tick_scale))
    graph_width = frame_width/(e_1_scale/(e_1tick_scale))

    param = cd.Graph(x, y, z)

    step = 0.2

    voutput = param.makemath(step) # precomputing saves about 50ms
    
    propogate = True

    # start_time = time.time()

    # define Euler angles
    phi = -0.05
    thta = -0.3
    psi = 0.3
    
    if propogate == False:
        rotation_m = param.make_rotation(phi, thta, psi)
        routput = param.makeframe(voutput, rotation_m, frame_width, frame_height, graph_width, graph_height)
        param.printframe(routput, frame_height, frame_width)

    else: param.realtimerender(voutput, frame_width, frame_height, graph_width, graph_height)


    # speed check
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print(elapsed_time)
    
    