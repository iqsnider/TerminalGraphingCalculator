import calc3D as cd







if __name__ == '__main__':

    x = "t_1"
    y = "t_2"
    z = "t_1*t_2/10"

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



    param = cd.Surface(x, y, z)

    step = 0.02
    rotation_m = cd.make_rotation(0.1, 0.2, 0.25)

    voutput = param.makemath(step)

    routput = param.makeframe(voutput, rotation_m, frame_width, frame_height, graph_width, graph_height)

    # make frame
    for k in range(0, frame_height):
        for j in range(0, frame_width):
            print(routput[k][j], end="")
        print("") 