from png import write_png


EGA2RGB = [
    (0x00, 0x00, 0x00),
    (0x00, 0x00, 0xAA),
    (0x00, 0xAA, 0x00),
    (0x00, 0xAA, 0xAA),
    (0xAA, 0x00, 0x00),
    (0xAA, 0x00, 0xAA),
    (0xAA, 0x55, 0x00),
    (0xAA, 0xAA, 0xAA),
    (0x55, 0x55, 0x55),
    (0x55, 0x55, 0xFF),
    (0x55, 0xFF, 0x55),
    (0x55, 0xFF, 0xFF),
    (0xFF, 0x55, 0x55),
    (0xFF, 0x55, 0xFF),
    (0xFF, 0xFF, 0x55),
    (0xFF, 0xFF, 0xFF),
]


def rle(filename_in, filename_out, w, h):
    pixels = []
    bytes = open(filename_in, 'rb').read()

    state = 0
    for d in bytes:
        if state == 0:
            if d == 0x02:
                state = 1
            else:
                a, b = divmod(d, 16)
                pixels.append(EGA2RGB[a])
                pixels.append(EGA2RGB[b])
        elif state == 1:
            run = d
            state = 2
        elif state == 2:
            for i in range(run):
                a, b = divmod(d, 16)
                pixels.append(EGA2RGB[a])
                pixels.append(EGA2RGB[b])
            state = 0

    write_png(filename_out, w, h, pixels)


rle("ULT/START.EGA", "start.png", 320, 200)
rle("ULT/KEY7.EGA", "key7.png", 320, 200)
rle("ULT/RUNE_0.EGA", "rune_0.png", 320, 200)
rle("ULT/RUNE_1.EGA", "rune_1.png", 320, 200)
rle("ULT/RUNE_2.EGA", "rune_2.png", 320, 200)
rle("ULT/RUNE_3.EGA", "rune_3.png", 320, 200)
rle("ULT/RUNE_4.EGA", "rune_4.png", 320, 200)
rle("ULT/RUNE_5.EGA", "rune_5.png", 320, 200)
rle("ULT/STONCRCL.EGA", "stonecircle.png", 320, 200)
rle("ULT/HONESTY.EGA", "honesty.png", 320, 200)
rle("ULT/COMPASSN.EGA", "compassion.png", 320, 200)
rle("ULT/VALOR.EGA", "valor.png", 320, 200)
rle("ULT/JUSTICE.EGA", "justice.png", 320, 200)
rle("ULT/SACRIFIC.EGA", "sacrifice.png", 320, 200)
rle("ULT/HONOR.EGA", "honor.png", 320, 200)
rle("ULT/SPIRIT.EGA", "spirit.png", 320, 200)
rle("ULT/HUMILITY.EGA", "humility.png", 320, 200)
rle("ULT/TRUTH.EGA", "truth.png", 320, 200)
rle("ULT/LOVE.EGA", "love.png", 320, 200)
rle("ULT/COURAGE.EGA", "courage.png", 320, 200)
