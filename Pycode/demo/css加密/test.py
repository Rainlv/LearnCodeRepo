from fontTools.ttLib import TTFont
import matplotlib.pyplot as plt

font = TTFont('font/9afb97e9d81d5585b545f1e262c7647a2272.woff')



font_code_list = font.getGlyphNames()[1:-2]
print(font_code_list)

for j, item in enumerate(font_code_list):
    x = [i[0] for i in font['glyf'][font_code_list[j]].coordinates]
    y = [i[1] for i in font['glyf'][font_code_list[j]].coordinates]

    plt.plot(x, y)
    plt.savefig(f'num/1_{j}.png')
    plt.show()
