from calc3D import Surface


if __name__ == '__main__':

    x = "t_1"
    y = "t_2"
    z = "t_1*t_2/10"

    param = Surface(x, y, z)

    print(param)