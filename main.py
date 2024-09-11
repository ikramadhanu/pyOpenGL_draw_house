from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

width, height = 800, 520

def draw_circle(x, y, radius):
    glBegin(GL_LINE_LOOP)
    num_segments = 100
    for i in range(num_segments):
        theta = 2.0 * math.pi * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

def draw_colored_circle(x, y, radius, r, g, b):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r, g, b)
    glVertex2f(x, y)

    num_segments = 100
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

def draw_house():
    glClear(GL_COLOR_BUFFER_BIT)

    # Dinding utama
    glColor3f(0.6, 0.6, 0.6)  # Warna abu-abu
    glBegin(GL_QUADS)
    glVertex2f(80, 60)
    glVertex2f(720, 60)
    glVertex2f(720, 360)
    glVertex2f(80, 360)
    glEnd()

    # Lantai
    glColor3f(0.96, 0.87, 0.70) 
    glBegin(GL_QUADS)
    glVertex2f(80, 60)
    glVertex2f(40, 20)
    glVertex2f(760, 20)
    glVertex2f(720, 60)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(80, 60)
    glVertex2f(40, 20)
    glVertex2f(760, 20)
    glVertex2f(720, 60)
    glVertex2f(80, 60)
    glEnd()

    # Atap
    glColor3f(0.6, 0.6, 0.6)  # Warna abu-abu
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 480)
    glVertex2f(720, 360)
    glVertex2f(80, 360)
    glEnd()

    # Atap kanan
    glColor3f(0.5, 0.2, 0.1)  # Warna cokelat tua
    glBegin(GL_QUADS)
    glVertex2f(400, 500)
    glVertex2f(400, 480)
    glVertex2f(760, 345)
    glVertex2f(770, 360)
    glEnd()

    # Atap kiri
    glColor3f(0.5, 0.2, 0.1)  # Warna cokelat tua
    glBegin(GL_QUADS)
    glVertex2f(400, 500)
    glVertex2f(400, 480)
    glVertex2f(40, 345)
    glVertex2f(30, 360)
    glEnd()

    # Segitiga
    glColor3f(0.3, 0.3, 0.3)  # Warna abu-abu tua
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 450)
    glVertex2f(270, 400)
    glVertex2f(530, 400)
    glEnd()

    # Tembok kiri
    glColor3f(0, 0, 0)  #hitam
    glBegin(GL_QUADS)
    glVertex2f(80, 370)
    glVertex2f(200, 370)
    glVertex2f(200, 40)
    glVertex2f(80, 40)
    glEnd()
    glColor3f(0.3, 0.3, 0.3)  # Warna abu-abu
    glBegin(GL_QUADS)
    glVertex2f(200, 370)
    glVertex2f(200, 40)
    glVertex2f(300, 40)
    glVertex2f(300, 370)
    glEnd()

    glColor3f(0.6, 0.6, 0.6)  # garis di tembok hitam
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 340)
    glVertex2f(180, 340)
    glEnd()     
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 310)
    glVertex2f(180, 310)
    glEnd()     
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 280)
    glVertex2f(180, 280)
    glEnd()     
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 250)
    glVertex2f(180, 250)
    glEnd()      
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 220)
    glVertex2f(180, 220)
    glEnd()    
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 190)
    glVertex2f(180, 190)
    glEnd()    
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 160)
    glVertex2f(180, 160)
    glEnd()     
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 130)
    glVertex2f(180, 130)
    glEnd()      
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 100)
    glVertex2f(180, 100)
    glEnd()       
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 70)
    glVertex2f(180, 70)
    glEnd()    

    # Kanopi hitam
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(500, 340)
    glVertex2f(540, 340)
    glVertex2f(540, 40)
    glVertex2f(500, 40)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(300, 340)
    glVertex2f(500, 340)
    glVertex2f(500, 300)
    glVertex2f(300, 300)
    glEnd()


    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(580, 340)
    glVertex2f(600, 340)
    glVertex2f(600, 40)
    glVertex2f(580, 40)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(640, 340)
    glVertex2f(660, 340)
    glVertex2f(660, 40)
    glVertex2f(640, 40)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(700, 340)
    glVertex2f(720, 340)
    glVertex2f(720, 40)
    glVertex2f(700, 40)
    glEnd()

    # Kanopi putih
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(180, 300)
    glVertex2f(180, 290)
    glVertex2f(560, 290)
    glVertex2f(560, 300)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(180, 280)
    glVertex2f(180, 270)
    glVertex2f(560, 270)
    glVertex2f(560, 280)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(570, 260)
    glVertex2f(730, 260)
    glVertex2f(730, 250)
    glVertex2f(570, 250)
    glEnd()

    # Pintu
    glColor3f(0.5, 0.2, 0.1)  # Warna cokelat tua
    glBegin(GL_QUADS)
    glVertex2f(340, 60)
    glVertex2f(340, 230)
    glVertex2f(460, 230)
    glVertex2f(460, 60)
    glEnd()

    # Garis pintu
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(340, 60)
    glVertex2f(460, 60)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(340, 230)
    glVertex2f(460, 230)
    glEnd() 
    glBegin(GL_LINE_STRIP)
    glVertex2f(460, 230)
    glVertex2f(460, 60)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(400, 60)
    glVertex2f(400, 220)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(350, 220)
    glVertex2f(450, 220)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(450, 220)
    glVertex2f(450, 60)
    glEnd()
    glBegin(GL_LINE_STRIP)
    glVertex2f(350, 220)
    glVertex2f(350, 60)
    glEnd()

    # Jendela kiri
    glColor3f(0.5, 0.2, 0.1)  # Warna coklat tua
    glBegin(GL_QUADS)
    glVertex2f(220, 230)
    glVertex2f(280, 230)
    glVertex2f(280, 90)
    glVertex2f(220, 90)
    glEnd()

    glColor3f(0.88, 0.93, 0.95)  # kaca
    glBegin(GL_QUADS)
    glVertex2f(230, 220)
    glVertex2f(270, 220)
    glVertex2f(270, 100)
    glVertex2f(230, 100)
    glEnd()

    glColor3f(1, 1, 1)  # Warna putih
    glBegin(GL_QUADS)
    glVertex2f(190, 240)
    glVertex2f(310, 240)
    glVertex2f(310, 230)
    glVertex2f(190, 230)
    glEnd()
    glColor3f(1, 1, 1)  # Warna putih
    glBegin(GL_QUADS)
    glVertex2f(280, 230)
    glVertex2f(290, 230)
    glVertex2f(290, 90)
    glVertex2f(280, 90)
    glEnd()
    glColor3f(1, 1, 1)  # Warna putih
    glBegin(GL_QUADS)
    glVertex2f(210, 230)
    glVertex2f(220, 230)
    glVertex2f(220, 90)
    glVertex2f(210, 90)
    glEnd()

    # Jendela kanan
    glColor3f(0.5, 0.2, 0.1)  # Warna coklat tua
    glBegin(GL_QUADS)
    glVertex2f(600, 230)
    glVertex2f(640, 230)
    glVertex2f(640, 90)
    glVertex2f(600, 90)
    glEnd()

    glColor3f(0.5, 0.2, 0.1)  # Warna coklat tua
    glBegin(GL_QUADS)
    glVertex2f(700, 230)
    glVertex2f(660, 230)
    glVertex2f(660, 90)
    glVertex2f(700, 90)
    glEnd()

    glColor3f(0.88, 0.93, 0.95)  # Kaca
    glBegin(GL_QUADS)
    glVertex2f(610, 220)
    glVertex2f(630, 220)
    glVertex2f(630, 100)
    glVertex2f(610, 100)
    glEnd()

    glColor3f(0.88, 0.93, 0.95)  # Kaca
    glBegin(GL_QUADS)
    glVertex2f(670, 220)
    glVertex2f(690, 220)
    glVertex2f(690, 100)
    glVertex2f(670, 100)
    glEnd()


    # Lingkaran ventilasi
    draw_colored_circle(360, 250, 10, 0.3, 0.3, 0.3)
    draw_colored_circle(400, 250, 10, 0.3, 0.3, 0.3)
    draw_colored_circle(440, 250, 10, 0.3, 0.3, 0.3)

    # Lingkaran kaca ventilasi
    draw_colored_circle(360, 250, 6, 0.88, 0.93, 0.95)
    draw_colored_circle(400, 250, 6, 0.88, 0.93, 0.95)
    draw_colored_circle(440, 250, 6, 0.88, 0.93, 0.95)

    glFlush()

def main():
    glutInit()
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Ilham Khefi Ramadhanu")
    glClearColor(0.53, 0.81, 0.92, 1.0) 
    gluOrtho2D(0, width, 0, height)
    glutDisplayFunc(draw_house)
    glutMainLoop()

if __name__ == "__main__":
    main()