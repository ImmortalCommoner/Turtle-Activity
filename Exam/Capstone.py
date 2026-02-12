import turtle

CANVAS_HEIGHT = 4100
CANVAS_WIDTH = 5100
CANVAS_SCALE = 4

screen = turtle.Screen()
screen.setup(CANVAS_WIDTH/CANVAS_SCALE, CANVAS_HEIGHT/CANVAS_SCALE)
screen.bgcolor("white")


def coordinates(x, y):
    turtle_x = (x - (CANVAS_WIDTH / 2))/CANVAS_SCALE
    turtle_y = ((CANVAS_HEIGHT / 2) - y)/CANVAS_SCALE
    return turtle_x, turtle_y


t = turtle.Turtle()
t.speed(0)
t.hideturtle

buildingPoints = [
    (4095.96, 3071.61),
  	(4095.96, 2147.62),
  	(3831.92, 3071.61),
  	(4095.96, 3071.61),
  	
]

bottomRightBeamPoints = [
    (4095.96, 2147.62),
    (4095.96, 1952.17),
    (3729.63, 3071.61),
    (3831.92, 3071.61),
    (4095.96, 2147.62),
  	
]

bottomTopBeamPoints = [
    (4095.96, 1952.17),
    (4095.96, 1628.74),
    (3981.98, 1618.58),
    (3084.55, 3071.61),
    (3729.63, 3071.61),
    (4095.96, 1952.17),
      	
]

rightColumnPoints = [
    (4095.96, 1062.77),
    (4095.96, 1628.74),
    (3981.98, 1618.58),
    (3690.57, 2091.09),
    (3765.94, 1058.84),
    (3844.04, 1034.78),
    (4095.96, 1033.54),
    (4095.96, 1062.54),
    (3765.94, 1058.78),
]

rightColumnTwoPoints = [
    (4095.96, 966.07),
    (4095.96, 1033.54),
    (4062.46, 1033.72),
    (4067.54, 965.84),
    (4095.96, 950.79),
    (4095.96, 966.07),
    (4067.54, 965.84),   
]

rightLightPoints = [
    (3678.58, 893.11),
    (3691.68, 887.31),
    (3809.15, 938.12),
    (4078.41, 929.39),
    (4078.89, 959.80),
    (4067.54, 965.84),
    (4062.46, 1033.48),
    (4052.05, 1033.32),
    (4058.49, 941.06), 
    (4078.41, 929.39),
    (4058.49, 941.06), 
    (3812.38, 949.16),
    (3779.81, 941.30),
    (3774.17, 943.84),
    (3678.58, 893.11),
]

rightLightTwoPoints = [
    (3869.76, 893.90),
    (3875.64, 890.65),
    (3950.15, 916.57),
    (3949.56, 917.96),
    (3958.33, 923.00),
    (4095.96, 920.14),
    (4095.96, 929.39),
    (3957.39, 933.16),
    (3954.30, 929.18),
    (3949.42, 930.25),
    (3944.088, 928.06),
    (3939.31, 928.84),
    (3869.76, 893.90),
]

rightLightThreePoints = [
    (4095.96, 906.78),
    (4066.64, 909.14),
    (4000.90, 884.38),
    (3994.89, 884.10),
    (4053.16, 912.73),
    (4064.45, 912.76),
    (4066.58, 916.44),
    (4095.96, 914.58),
    (4095.96, 906.78),
]

whiteOutsideCourt = [
    (3111.35, 3028.72),
    (3084.55, 3071.61),
    (0, 3071.61),
    (0, 1883.63),
    (3111.35, 3028.72),    
]

blueInsideCourt = [
    (3111.35, 3028.72),
    (0, 1883.63),
    (0, 1577.82),
    (396.60, 1514.41),
    (422.12, 1520.14),
    (534.85, 1501.81),
    (533.84, 1493.14),
    (1003.17, 1417.82),
    (1024.11, 1422.43),
    (1110.05, 1408.06),
    (1109.40, 1398.26),
    (1447.76, 1351.13),
    (1474.02, 1352.31),
    (1535.75, 1336.25),
    (1823.33, 1293.10),
    (1843.76, 1295.61),
    (1882.20, 1288.49),
    (1940.94, 1291.85),
    (1940.94, 1296.90),
    (1999.63, 1301.59),
    (2033.29, 1296.75),
    (3741.53, 1389.02),
    (3690.57, 2091.09),
    (3111.35, 3028.72),
]

greyLowfencePoints = [
    (0, 1577.82),
    (1823.33, 1293.10),
    (1819.24, 1229.34),
    (0, 1472.45),
    (0, 1577.82),
    (0, 0),
]

whiteUpperTopBeamPoints = [
    (0, 1230.48),
    (1823.44, 1089.35),
    (1819.64, 1042.57),
    (0, 1156.86),
    (0, 1230.48),
]

whiteUpperFrontBeamPoints = [
    (0, 1156.86),
    (0, 1148.74),
    (1802.75, 1041.46),
    (1819.64, 1042.57),
    (0, 1156.86),
]

# leftFirstColumnPoints
leftFirstFrontColumnPoints = [
    (422.12, 1520.14),
    (534.85, 1501.81),
    (479.33, 1006.26),
    (362.55, 1013.00),
    (422.12, 1520.14),
]

leftFirstTopColumnPoints = [
    (479.33, 1006.26),
    (362.55, 1013.00),
    (329.77, 1010.64),
    (430.48, 1004.50),
    (479.33, 1006.26),
]

leftFirstSideColumnPoints = [
    (362.55, 1013.00),
    (329.77, 1010.64),
    (340.21, 1126.51),
    (343.13, 1125.95),
    (358.85, 1130.67),
    (368.73, 1198.71),
    (346.95, 1200.62),
    (367.41, 1417.94),
    (384.34, 1421.36),
    (396.60, 1514.41),
    (422.12, 1520.14),
    (362.55, 1013.00),
]

# leftSecondColumnPoints
leftSecondFrontColumnPoints = [
    (1024.11, 1422.43),
    (1110.05, 1408.06),
    (1077.07, 985.13),
    (993.68, 988.58),
    (1024.11, 1422.43),
]

leftSecondTopColumnPoints = [
    (1077.07, 985.13),
    (993.68, 988.58),
    (957.98, 987.28),
    (1044.77, 982.29),
    (1077.07, 985.13),
]

leftSecondSideColumnPoints = [
    (957.98, 987.28),
    (993.68, 988.58),
    (1024.11, 1422.43),
    (1003.17, 1417.82),
    (998.01, 1337.04),
    (985.13, 1335.26),
    (970.28, 1151.42),
    (985.48, 1150.31),
    (979.65, 1089.85),
    (969.45, 1088.42),
    (965.36, 1088.42),
    (957.98, 987.28),
]

rightLightThreePoints = [
    (0, 0),
    (0, 0),
]

rightLightThreePoints = [
    (0, 0),
    (0, 0),
]

rightLightThreePoints = [
    (0, 0),
    (0, 0),
]

def drawBuilding():

    # yellow gutter
    t.pu()
    t.goto(coordinates(*buildingPoints[0]))
    t.pd()
    
    t.fillcolor("yellow")
    t.begin_fill()
    for point in buildingPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # column
    t.pu()
    t.goto(coordinates(*bottomRightBeamPoints[0]))
    t.pd()
    
    t.fillcolor("gray")
    t.begin_fill()
    for point in bottomRightBeamPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()
    
    t.pu()
    t.goto(coordinates(*bottomTopBeamPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in bottomTopBeamPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # Right Columns
    t.pu()
    t.goto(coordinates(*rightColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in rightColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    t.pu()
    t.goto(coordinates(*rightColumnTwoPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in rightColumnTwoPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # Light Post
    t.pu()
    t.goto(coordinates(*rightLightPoints[0]))
    t.pd()
    
    t.fillcolor("blue")
    t.begin_fill()
    for point in rightLightPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    t.pu()
    t.goto(coordinates(*rightLightTwoPoints[0]))
    t.pd()
    
    t.fillcolor("blue")
    t.begin_fill()
    for point in rightLightTwoPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    t.pu()
    t.goto(coordinates(*rightLightThreePoints[0]))
    t.pd()
    
    t.fillcolor("blue")
    t.begin_fill()
    for point in rightLightThreePoints:
        
        t.goto(coordinates(*point))
    t.end_fill()
    
    # whiteOutsideCourt
    t.pu()
    t.goto(coordinates(*whiteOutsideCourt[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in whiteOutsideCourt:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # blueInsideCourt
    t.pu()
    t.goto(coordinates(*blueInsideCourt[0]))
    t.pd()
    
    t.fillcolor("blue")
    t.begin_fill()
    for point in blueInsideCourt:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # greyLowfencePoints
    t.pu()
    t.goto(coordinates(*greyLowfencePoints[0]))
    t.pd()
    
    t.fillcolor("grey")
    t.begin_fill()
    for point in greyLowfencePoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # whiteUpperBeamPoints
    t.pu()
    t.goto(coordinates(*whiteUpperTopBeamPoints[0]))
    t.pd()
    
    t.fillcolor("grey")
    t.begin_fill()
    for point in whiteUpperTopBeamPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # whiteUpperFrontBeamPoints
    t.pu()
    t.goto(coordinates(*whiteUpperFrontBeamPoints[0]))
    t.pd()
    
    t.fillcolor("grey")
    t.begin_fill()
    for point in whiteUpperFrontBeamPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # leftFirstColumnPoints
    t.pu()
    t.goto(coordinates(*leftFirstFrontColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in leftFirstFrontColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    t.pu()
    t.goto(coordinates(*leftFirstTopColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in leftFirstTopColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()
    
    t.pu()
    t.goto(coordinates(*leftFirstSideColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in leftFirstSideColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    # leftSecondColumnPoints
    t.pu()
    t.goto(coordinates(*leftSecondFrontColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in leftSecondFrontColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

    t.pu()
    t.goto(coordinates(*leftSecondTopColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in leftSecondTopColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()
    
    t.pu()
    t.goto(coordinates(*leftSecondSideColumnPoints[0]))
    t.pd()
    
    t.fillcolor("white")
    t.begin_fill()
    for point in leftSecondSideColumnPoints:
        
        t.goto(coordinates(*point))
    t.end_fill()

drawBuilding()
screen.mainloop()