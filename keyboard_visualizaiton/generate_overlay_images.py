#!/bin/python3

from PIL import Image, ImageDraw, ImageFont
bg = "szczys_corne.jpg"
scp = "Source Code Pro Bold for Powerline.otf"
test_img = Image.open(bg)

def get_blank_img(x=1280, y=720):
    return Image.new('RGBA', (x, y), color=(0, 0, 0, 0))

class kp:
    def __init__(self, text, x, y, pt=44, fill=None, font=None, rotate=None):
        self.text=text
        self.x=x
        self.y=y
        self.pt=pt
        self.fill=fill
        self.font=font
        self.rotate=rotate

        if fill is None:
            self.fill=(255,255,255)
        else:
            self.fill=fill

        if font is None:
            self.font="Source Code Pro Bold for Powerline.otf"
        else:
            self.font=font

    def plot_rotated(self, img):
        font = ImageFont.truetype(self.font, self.pt)
        txt = Image.new('RGBA', (500,50), color=(0,0,0,0))
        dl = ImageDraw.Draw(txt)
        dl.text((0, 0), self.text, fill=self.fill, font=font)
        w = txt.rotate(self.rotate, expand=1)
        box = w.getbbox()
        crop = w.crop(box)
        img.paste(crop, (self.x, self.y), crop)

    def plot(self, img):
        if self.text is None:
            return
        if (self.rotate):
            self.plot_rotated(img)
        else:
            font = ImageFont.truetype(self.font, self.pt)
            dl = ImageDraw.Draw(img)
            dl.text((self.x,self.y), self.text, fill=self.fill, font=font)

layer_base = (
    kp("esc", 86, 199, 26), kp("q", 156, 183, 44), kp("w", 224, 167, 44), kp("e", 294, 159, 44), kp("r", 360, 167, 44), kp("t", 433, 174, 44),
    kp("alt", 86, 266, 26), kp("a", 156, 250, 44), kp("s", 224, 234, 44), kp("d", 294, 226, 44), kp("f", 360, 234, 44), kp("g", 433, 241, 44),
    kp("shft", 86, 340, 18), kp("z", 156, 317, 44), kp("x", 224, 301, 44), kp("c", 294, 293, 44), kp("v", 360, 301, 44), kp("b", 433, 308, 44),
    kp("ctrl", 322, 400, 18), kp("ent", 396, 414, 26, rotate=-18), kp("tab", 478, 421, 30, rotate=57),

    kp("y", 849, 169, 44), kp("u", 920, 165, 44), kp("i", 987, 164, 44), kp("o", 1058, 174, 44), kp("p", 1126, 193, 40), kp("del", 1178, 210, 23),
    kp("h", 849, 248, 44), kp("j", 920, 234, 44), kp("k", 987, 233, 44), kp("l", 1058, 246, 44), kp(";", 1126, 259, 40), kp("'", 1186, 259, 44),
    kp("n", 849, 316, 44), kp("m", 920, 308, 44), kp(",", 987, 298, 44), kp(".", 1058, 310, 44), kp("/", 1126, 332, 40), kp("func", 1174, 348, 18),
    kp("bksp", 778, 404, 30, rotate=-57), kp("sp", 864, 410, 40, rotate=18), kp("shft", 946, 400, 18)
    )

layer_lower = (
    kp(None, 86, 199, 26), kp("!", 156, 183, 44), kp("@", 224, 167, 44), kp("#", 294, 159, 44), kp("$", 360, 167, 44), kp("%", 433, 174, 44),
    kp(None, 86, 266, 26), kp("1", 156, 250, 44), kp("2", 224, 234, 44), kp("3", 294, 226, 44), kp("4", 360, 234, 44), kp("5", 433, 241, 44),
    kp(None, 86, 340, 18), kp(None, 156, 317, 44), kp(None, 224, 301, 44), kp("~", 294, 293, 44), kp("`", 360, 306, 44), kp(None, 423, 327, 22),
    kp(None, 322, 400, 18), kp(None, 396, 414, 26, rotate=-18), kp(None, 482, 421, 30, rotate=57),

    kp("^", 849, 169, 44), kp("&", 920, 165, 44), kp("*", 987, 164, 44), kp("(", 1058, 174, 44), kp(")", 1126, 193, 40), kp("bksp", 1175, 210, 20),
    kp("6", 849, 248, 44), kp("7", 920, 234, 44), kp("8", 987, 233, 44), kp("9", 1058, 246, 44), kp("0", 1126, 259, 40), kp(None, 1186, 259, 44),
    kp("tmux", 836, 330, 22), kp("[{<", 914, 320, 24), kp(">}]", 981, 312, 24), kp(".", 1058, 310, 44), kp(None, 1126, 332, 40), kp(None, 1174, 348, 18),
    kp("F12", 785, 414, 30, rotate=-57), kp(None, 864, 410, 40, rotate=18), kp(":", 954, 384, 44)
    )

layer_raise = (
    kp(None, 86, 199, 26), kp("del", 152, 200, 23), kp(None, 224, 167, 44), kp("-", 294, 159, 44), kp("+", 360, 167, 44), kp("PgUp", 423, 191, 20),
    kp(None, 86, 266, 26), kp("Home", 148, 270, 20), kp("End", 218, 250, 20), kp("_", 294, 226, 44), kp("=", 360, 234, 44), kp("PgDn", 423, 261, 20),
    kp(None, 86, 340, 18), kp("<", 156, 325, 44), kp(">", 224, 309, 44), kp("Copy", 280, 315, 20), kp("Paste", 347, 321, 18), kp(";", 433, 316, 44),
    kp(None, 318, 396, 23), kp(None, 396, 414, 26, rotate=-18), kp(None, 478, 421, 30, rotate=57),

    kp(None, 849, 169, 44), kp(None, 920, 165, 44), kp(None, 987, 164, 44), kp("\\", 1058, 174, 44), kp("|", 1126, 193, 40), kp(None, 1178, 210, 23),
    kp(u"\u2190", 849, 243, 44), kp(u"\u2193", 920, 234, 44), kp(u"\u2191", 987, 229, 44), kp(u"\u2192", 1058, 241, 44), kp(None, 1126, 259, 40), kp(None, 1186, 259, 44),
    kp("pause", 837, 336, 16), kp(None, 920, 308, 44), kp(None, 987, 298, 44), kp("vol-", 1048, 330, 20), kp("vol+", 1114, 350, 20), kp(None, 1174, 348, 18),
    kp(None, 778, 404, 30, rotate=-57), kp(None, 864, 410, 40, rotate=18), kp("alt", 946, 400, 23)
    )

layer_function = (
    kp("BT_Clr", 86, 208, 14), kp("F1", 156, 193, 30), kp("F2", 224, 177, 30), kp("F3", 294, 169, 30), kp("F4", 360, 177, 30), kp("F5", 433, 184, 30),
    kp(None, 86, 266, 26), kp("F11", 146, 260, 30), kp("F12", 210, 244, 30), kp(None, 294, 226, 44), kp(None, 360, 234, 44), kp(None, 433, 241, 44),
    kp(None, 86, 340, 18), kp("BT0", 146, 329, 30), kp("BT1", 214, 313, 30), kp("BT2", 282, 305, 30), kp("BT3", 348, 313, 30), kp("BT4", 421, 320, 30),
    kp(None, 322, 400, 18), kp(None, 396, 414, 26, rotate=-18), kp(None, 478, 421, 30, rotate=57),

    kp("F6", 849, 179, 30), kp("F7", 920, 175, 30), kp("F8", 987, 174, 30), kp("F9", 1058, 184, 30), kp("F10", 1112, 203, 30), kp(None, 1178, 210, 23),
    kp("LED", 838, 255, 28), kp(None, 920, 234, 44), kp(None, 987, 233, 44), kp(None, 1058, 246, 44), kp(None, 1126, 259, 40), kp(None, 1186, 259, 44),
    kp(None, 849, 316, 44), kp(None, 920, 308, 44), kp(None, 987, 298, 44), kp(None, 1058, 310, 44), kp(None, 1126, 332, 40), kp(None, 1174, 348, 18),
    kp(None, 778, 404, 30, rotate=-57), kp(None, 864, 410, 40, rotate=18), kp("alt", 946, 400, 23)
    )

def make_overlay(fname, keyset, bg_file=None):
    try:
        img = Image.open(bg_file)
    except:
        img = get_blank_img()
        

    for k in keyset:
        k.plot(img)

    img.save(fname)

make_overlay("overlay_base.png", layer_base)
make_overlay("overlay_lower.png", layer_lower)
make_overlay("overlay_raise.png", layer_raise)
make_overlay("overlay_function.png", layer_function)
#make_overlay("overlay_function.png", layer_function, bg_file=bg)
