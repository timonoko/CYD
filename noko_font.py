import sys, os

XF0=0
XF=XF0
YF=200
COLOR=0
display="VIRHE"

def render_row_hmap(data, row, height, width, reverse=False):
    global XF,YF,COLOR,display
    bytes_per_row = (width - 1)//8 + 1
    for col in range(width):
        byte = data[row * bytes_per_row + col // 8]
        if reverse:
            bit = (byte & (1 << (col % 8))) > 0
        else:
            bit = (byte & (1 << (7 - (col % 8)))) > 0
        if bit:
            display.draw_pixel(XF,YF,COLOR)
        XF+=1

def render_row_vmap(data, row, height, width, reverse=False):
    global XF,YF,COLOR,display
    bytes_per_col = (height - 1)//8 + 1
    for col in range(width):
        byte = data[col * bytes_per_col + row//8]
        if reverse:
            bit = (byte & (1 << (7 - (row % 8)))) > 0
        else:
            bit = (byte & (1 << (row % 8))) > 0
        if bit:
            display.draw_pixel(XF,YF,COLOR)
        XF+=1

def render_text(string,font):
    global XF,YF
    myfont=__import__(font, globals(), locals(), [], 0)
    height = myfont.height()
    for row in range(height):
        for char in string:
            data, _, width = myfont.get_ch(char)
            if myfont.hmap():
                render_row_hmap(data, row, height, width, myfont.reverse())
            else:
                render_row_vmap(data, row, height, width, myfont.reverse())
        XF=XF0
        YF+=1

def text(x,y,text,color,font,disp):
    global XF0,XF,YF,COLOR,display
    display=disp
    XF0=x;XF=x
    YF=y-10
    COLOR=color
    render_text(text,font)
    



