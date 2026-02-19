import turtle

CANVAS_HEIGHT = 4100
CANVAS_WIDTH = 5100
CANVAS_SCALE = 3.8

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

# leftThirdColumnPoints
leftThirdFrontColumnPoints = [
    (1474.02, 1352.31),
    (1535.75, 1336.25),
    (1519.44, 973.92),
    (1456.53, 978.58),
    (1474.02, 1352.31),
]

leftThirdTopColumnPoints = [
    (1519.44, 973.92),
    (1478.56, 973.14),
    (1422.59, 975.04),
    (1456.28, 978.81),
    (1519.44, 973.92),
]

leftThirdSideColumnPoints = [
    (1447.76, 1351.13),
    (1474.02, 1352.31),
    (1456.28, 978.81),
    (1422.59, 975.04),
    (1425.77, 1063.49),
    (1444.66, 1067.18),
    (1448.04, 1117.12),
    (1427.96, 1118.60),
    (1433.86, 1274.72),
    (1445.53, 1279.16),
    (1447.76, 1351.13),
]

# middle1stColumnPoints
middle1stFrontColumnPoints = [
    (1843.76, 1295.61),
    (1882.20, 1288.49),
    (1880.30, 1224.82),
    (1890.44, 1223.81),
    (1878.31, 967.56),
    (1831.37, 970.90),
    (1843.76, 1295.61),
]

middle1stTopColumnPoints = [
    (1878.31, 967.56),
    (1831.37, 970.90),
    (1800.75, 969.38),
    (1838.75, 967.38),
    (1878.31, 967.56),
]

middle1stSideColumnPoints = [
    (1823.33, 1293.10),
    (1843.76, 1295.61),
    (1831.37, 970.90),
    (1800.75, 969.38),
    (1802.59, 1041.66),
    (1819.65, 1042.72),
    (1820.65, 1089.65),
    (1804.54, 1090.71),
    (1809.49, 1226.39),
    (1819.56, 1227.71),
    (1823.33, 1293.10),
]

# tennisCourtPoints
tennisLeftCourtPoints = [
    (974.56, 1719.41),
    (2365.88, 1375.63),
    (1800.94, 1335.94),
    (346.19, 1589.25),
    (974.56, 1719.41),
    (882.12, 1700.24),
    (1353.58, 1589.22),
    (884.69, 1517.69),
    (412.03, 1603.03),
    (1862.03, 1339.88),
    (1636.31, 1381.81),
    (2076.41, 1419.66),
    (2284.75, 1369.67),
    (1353.58, 1589.22),
    (1100.47, 1550.56),
    (1840.94, 1399.53),
]

tennisRightCourtPoints = [
    (3118.56, 2164.76),
    (3729.13, 1559.14),
    (3736.19, 1469.56),
    (2868.38, 1407.69),
    (1599.66, 1848.33),
    (3118.56, 2164.76),
    (2858.26, 2110.51),
    (3177.78, 1858.32),
    (2185.67, 1710.07),
    (1740.61, 1877.66),
    (2970.78, 1414.81),
    (2796.12, 1480.50),
    (3572.81, 1546.25),
    (3675.05, 1465.08),
    (3177.78, 1858.32),
    (2624.69, 1775.72),
    (3157.32, 1511.26),
]

sportsBuildingBeamPoints = [
    (4095.96, 0),
    (3941.68, 0),
    (2873.81, 179.25),
    (2871.44, 255.94),
    (4095.96, 68.85),
    (4095.96, 0),
]

sportsColourBuildingPoints = [
    (4095.96, 68.85),
    (2871.44, 255.94),
    (2843.62, 1274.00),
    (4095.96, 1329.25),
    (4095.96, 68.85),
]

SportsBuildingTopWindowColourPoints = [
    (2861.13, 624.38), #1
    (2915.22, 619.78),
    (2920.35, 463.35),
    (3034.81, 451.22),
    (3029.18, 610.08),
    (2915.22, 619.78),
    (3103.75, 604.75), #2
    (3108.75, 443.47),
    (3232.56, 430.62),
    (3225.31, 594.37),
    (3103.75, 604.75),
    (3225.31, 594.37), #3
    (3343.00, 585.00),
    (3351.25, 418.37),
    (3484.00, 404.25),
    (3474.94, 574.00),
    (3343.00, 585.00),
    (3474.94, 574.00), #4
    (3561.25, 566.81), 
    (3573.72, 394.21),
    (3716.44, 377.94),
    (3704.12, 555.3), #btr
    (3561.25, 566.81),
    (3842.73, 544.16),
    (3856.12, 360.71),
    (4015.69, 343.19),
    (4000.84, 531.25), #btr
    (3842.73, 544.16),
    (4095.96, 523.47),
]

SportsBuildingTopWindowOutlinePoints = [
    (2915.22, 619.78),
    (2920.35, 463.35),
    (3034.81, 451.22),
    (3029.18, 610.08),
    (2971.37, 614.75), #mid
    (2975.87, 457.62),
    (3034.81, 451.22),
    (3032.62, 519.87),
    (2918.25, 531.25),
    (2917.25, 566.50),
    (3031.25, 556.50),
    (3029.18, 610.08),
    (3103.75, 604.75),
    (3108.75, 443.47),
    (3232.56, 430.62),
    (3225.31, 594.37),
    (3103.75, 604.75),
    (3163.37, 599.87), #mid
    (3173.25, 437.00),
    (3232.56, 430.62),
    (3229.25, 505.25),
    (3106.62, 515.75),
    (3105.62, 551.12),
    (3227.50, 540.37),
    (3225.31, 594.37),
    (3343.00, 585.00),
    (3351.25, 418.37),
    (3484.00, 404.25),
    (3474.94, 574.00),
    (3343.00, 585.00),
    (3407.86, 579.47),
    (3417.94, 411.06),
    (3484.00, 404.25),
    (3479.76, 482.78),
    (3347.53, 493.69),
    (3345.68, 528.41),
    (3477.94, 516.81),
    (3474.94, 574.00), #4
    (3561.25, 566.81), 
    (3573.72, 394.21),
    (3716.44, 377.94),
    (3704.12, 555.3), #btr
    (3561.25, 566.81),
    (3631.62, 561.75),
    (3644.87, 386.25),
    (3716.44, 377.94),
    (3711.07, 458.38),
    (3568.25, 471.25),
    (3565.42, 509.26),
    (3708.09, 496.78),
    (3704.12, 555.3), #btr
    (3842.73, 544.16),
    (3856.12, 360.71),
    (4015.69, 343.19),
    (4000.84, 531.25), #btr
    (3842.73, 544.16),
    (3921.00, 538.50),
    (3936.00, 353.00),
    (4015.69, 343.19),
    (4009.50, 429.00),
    (3850.00, 444.75),
    (3846.25, 483.75),
    (4006.00, 468.50),
]

sportsBuildingTopStripPoints = [
    #
    (2888.75, 625.50),
    (3263.50, 591.25),
    (3263.00, 609.12),
    (2888.35, 641.35),
    (2888.75, 625.50),
    (3300.86, 588.14),
    (3750.25, 551.87),
    (3748.87, 574.00),
    (3299.93, 607.54),
    (3300.86, 588.14),
    (3796.37, 548.12),
    (4095.96, 523.81),
    (4095.96, 547.37),
    (3794.47, 570.97),
    (3796.37, 548.12),
]

sportsBuildingBottomStripPoints = [
    #bottom
    (4095.96, 851.71),
    (3772.62, 862.00),
    (3770.75, 882.75),
    (4095.96, 873.44),
    (4095.96, 851.71),
    
    (3728.62, 862.94),
    (3287.00, 877.25),
    (3285.50, 895.50),
    (3727.75, 882.50),
    (3728.62, 862.94),

    (3251.50, 877.56),
    (3250.50, 896.75),
    (2880.06, 908.50),
    (2880.62, 889.19),
    (3251.50, 877.56),
    (2853.40, 889.67),
]

SportsBuildingBottomWindowColourPoints = [
    (2906.69, 888.25),
    (3020.05, 886.00),
    (3026.06, 720.54),
    (2911.87, 729.03),
    (2906.69, 888.25),

    (3093.15, 882.82),
    (3212.25, 878.81),
    (3220.19, 708.00),
    (3099.91, 713.78),
    (3093.15, 882.82),

    (3329.50, 877.00),
    (3459.00, 873.00),
    (3469.00, 694.00),
    (3337.50, 702.00),
    (3329.50, 877.00),

    (3542.00, 870.50),
    (3682.00, 866.00),
    (3693.50, 682.50),
    (3553.50, 689.00),
    (3542.00, 870.50),

    (3820.85, 861.26),
    (3971.50, 856.00),
    (3988.75, 664.00),
    (3833.25, 672.50),
    (3820.75, 860.75),
    
    (4071.00, 853.50),
    (4095.96, 853.0),
    (4095.96, 657.50),
    (4088.25, 657.50),
    (4071.00, 853.50),
]

SportsBuildingBottomWindowOutlinePoints = [
    (2962.07, 887.77),
    (2966.87, 724.12),
    (2911.87, 729.03),
    (2909.39, 796.56),
    (3023.59, 789.84),
    (3022.17, 826.08),
    (2908.33, 830.67),
    (2906.69, 888.25),

    (3152.19, 880.97),
    (3159.12, 711.37),
    (3099.91, 713.78),
    (3097.22, 787.63),
    (3216.54, 781.71),
    (3215.48, 816.00),
    (3095.37, 821.75),
    (3093.15, 882.82),

    (3393.25, 874.25),
    (3402.00, 697.25),
    (3337.50, 702.00),
    (3333.75, 773.75),
    (3465.00, 766.25),
    (3462.50, 806.25),
    (3332.25, 812.00),
    (3329.50, 877.00),

    (3610.50, 867.50),
    (3622.25, 685.25),
    (3553.50, 689.00),
    (3549.25, 766.25),
    (3688.50, 758.00),
    (3686.00, 798.75),
    (3546.00, 804.25),
    (3542.00, 870.50),

    (3895.80, 858.78),
    (3911.01, 668.22),
    (3833.25, 672.50),
    (3828.63, 750.95),
    (3981.72, 742.46),
    (3978.54, 784.53),
    (3825.45, 791.25),
    (3820.75, 860.75),
    
    (4095.96, 853.0),
    (4095.96, 779.00),
    (4077.00, 780.25),
    (4079.75, 737.50),
    (4095.96, 737.50),
]

SportsBuildingLittleWindowColourPoints = [
    (2901.61, 1065.26),
    (3013.69, 1063.84),
    (3017.58, 961.67),
    (2905.50, 964.14),
    (2901.61, 1065.26),

    (3086.52, 1064.20),
    (3196.48, 1062.43),
    (3200.01, 958.48),
    (3091.41, 960.25),
    (3086.52, 1064.20),

    (3320.50, 1063.00),
    (3449.00, 1063.50),
    (3454.50, 953.00),
    (3326.50, 956.00),
    (3320.50, 1063.00),

    (3532.35, 1063.14),
    (3670.24, 1063.49),
    (3676.96, 950.71),
    (3537.30, 953.53),
    (3532.35, 1063.14),

    (3804.37, 1062.12),
    (3954.50, 1061.37),
    (3964.12, 944.75),
    (3813.00, 949.87),
    (3804.37, 1062.12),

]

SportsBuildingLittleWindowOutlinePoints = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
]


centerColumnWhitePoints = [
    (1940.30, 1235.67),
    (1998.99, 1238.50),
    (2033.290, 1233.55),
    (2030.10, 966.97),
    (1974.95, 966.61),
    (1935.70, 971.21),
    (1940.30, 1235.67),
]

centerColumnGrayPoints = [
    (1940.30, 1235.67),
    (1998.99, 1238.50),
    (2033.290, 1233.55),
    (2033.29, 1296.75),
    (1999.63, 1301.59),
    (1940.94, 1296.90),  
    (1940.30, 1235.67),
]

centerColumnOutlinePoints = [
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
]

centerColumnOutlinePoints = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),

    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
]

nameDirectionPoints = [
    (0, 0),
    (0, 0),
]

def drawBuilding():
  
    def drawSportsBuildingPoints():

        def drawSportsBuildingColumnPoints():
            # BeamColor
            t.pu()
            t.goto(coordinates(*sportsBuildingBeamPoints[0]))
            t.pd()
            
            t.fillcolor("gray")
            t.begin_fill()
            for point in sportsBuildingBeamPoints:
                
                t.goto(coordinates(*point))
            t.end_fill()
                
        drawSportsBuildingColumnPoints()

        # BuildingColor
        t.pu()
        t.goto(coordinates(*sportsColourBuildingPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in sportsColourBuildingPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()

        def drawSportsBuildingWindowPoints():
            def drawSportsBuildingWindowColourPoints():
                # WindowColor
                t.pu()
                t.goto(coordinates(*SportsBuildingTopWindowColourPoints[0]))
                t.pd()

                t.fillcolor("gray")
                t.begin_fill()
                
                for point in SportsBuildingTopWindowColourPoints:
                    t.goto(coordinates(*point))
                
                t.end_fill()
            
            drawSportsBuildingWindowColourPoints()
            
            def drawSportsBuildingTopWindowOutlinePoints():
                # windowOutline
                t.pu()
                t.goto(coordinates(*SportsBuildingTopWindowOutlinePoints[0]))
                t.pd()
                
                t.color("black")
                for point in SportsBuildingTopWindowOutlinePoints:
                    t.goto(coordinates(*point))
            
            drawSportsBuildingTopWindowOutlinePoints()

            #bottom
            def drawSportsBuildingBottomWindowColourPoints():
                # WindowColor
                t.pu()
                t.goto(coordinates(*SportsBuildingBottomWindowColourPoints[0]))
                t.pd()

                t.fillcolor("gray")
                t.begin_fill()
                
                for point in SportsBuildingBottomWindowColourPoints:
                    t.goto(coordinates(*point))
                
                t.end_fill()
            
            drawSportsBuildingBottomWindowColourPoints()
            
            def drawSportsBuildingBottomWindowOutlinePoints():
                # windowOutline
                t.pu()
                t.goto(coordinates(*SportsBuildingBottomWindowOutlinePoints[0]))
                t.pd()
                
                t.color("black")
                for point in SportsBuildingBottomWindowOutlinePoints:
                    t.goto(coordinates(*point))
            
            drawSportsBuildingBottomWindowOutlinePoints()

            #Little
            def drawSportsBuildingLittleWindowColourPoints():
                # WindowColor
                t.pu()
                t.goto(coordinates(*SportsBuildingLittleWindowColourPoints[0]))
                t.pd()

                t.fillcolor("gray")
                t.begin_fill()
                
                for point in SportsBuildingLittleWindowColourPoints:
                    t.goto(coordinates(*point))
                
                t.end_fill()
            
            drawSportsBuildingLittleWindowColourPoints()
            
            def drawSportsBuildingLittleWindowOutlinePoints():
                # windowOutline
                t.pu()
                t.goto(coordinates(*SportsBuildingLittleWindowOutlinePoints[0]))
                t.pd()
                
                t.color("black")
                for point in SportsBuildingLittleWindowOutlinePoints:
                    t.goto(coordinates(*point))
            
            drawSportsBuildingLittleWindowOutlinePoints()
            
        drawSportsBuildingWindowPoints()

        #sportsBuildingStripPoints
        def drawSportsBuildingTopStripPoints():
            t.pu()
            t.goto(coordinates(*sportsBuildingTopStripPoints[0]))
            t.pd()
            
            t.fillcolor("yellow")
            t.begin_fill()
            for point in sportsBuildingTopStripPoints:
                
                t.goto(coordinates(*point))
            t.end_fill()

        drawSportsBuildingTopStripPoints()

        def drawSportsBuildingBottomStripPoints():
            t.pu()
            t.goto(coordinates(*sportsBuildingBottomStripPoints[0]))
            t.pd()
            
            t.fillcolor("yellow")
            t.begin_fill()
            for point in sportsBuildingBottomStripPoints:
                
                t.goto(coordinates(*point))
            t.end_fill()

        drawSportsBuildingBottomStripPoints()
            
    drawSportsBuildingPoints()

    def drawYellowGutter():
        # yellow gutter
        t.pu()
        t.goto(coordinates(*buildingPoints[0]))
        t.pd()
        
        t.fillcolor("yellow")
        t.begin_fill()
        for point in buildingPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawYellowGutter()

    def drawColumn():
        # column
        t.pu()
        t.goto(coordinates(*bottomRightBeamPoints[0]))
        t.pd()
        
        t.fillcolor("gray")
        t.begin_fill()
        for point in bottomRightBeamPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawColumn()

    def drawBeam():
    
        t.pu()
        t.goto(coordinates(*bottomTopBeamPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in bottomTopBeamPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawBeam()

    def drawRightColumns():
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
    
    drawRightColumns()

    def drawRightLightPost():
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
    
    drawRightLightPost()

    def drawWhiteOutsideCourt():
        
        # whiteOutsideCourt
        t.pu()
        t.goto(coordinates(*whiteOutsideCourt[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in whiteOutsideCourt:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawWhiteOutsideCourt()

    def drawblueInsideCourt():
        # blueInsideCourt
        t.pu()
        t.goto(coordinates(*blueInsideCourt[0]))
        t.pd()
        
        t.fillcolor("blue")
        t.begin_fill()
        for point in blueInsideCourt:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawblueInsideCourt()

    def drawgreyLowfencePoints():

        # greyLowfencePoints
        t.pu()
        t.goto(coordinates(*greyLowfencePoints[0]))
        t.pd()
        
        t.fillcolor("grey")
        t.begin_fill()
        for point in greyLowfencePoints:
            
            t.goto(coordinates(*point))
        t.end_fill()

    drawgreyLowfencePoints()

    def drawWhiteUpperBeams():
        # whiteUpperBeamPoints
        t.pu()
        t.goto(coordinates(*whiteUpperTopBeamPoints[0]))
        t.pd()
        
        t.fillcolor("grey")
        t.begin_fill()
        for point in whiteUpperTopBeamPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawWhiteUpperBeams()

    def drawWhiteUpperFrontBeams():
        # whiteUpperFrontBeamPoints
        t.pu()
        t.goto(coordinates(*whiteUpperFrontBeamPoints[0]))
        t.pd()
        
        t.fillcolor("grey")
        t.begin_fill()
        for point in whiteUpperFrontBeamPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawWhiteUpperFrontBeams()
    
    def drawLeftColumns():
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

        # leftThirdColumnPoints
        t.pu()
        t.goto(coordinates(*leftThirdFrontColumnPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in leftThirdFrontColumnPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()

        t.pu()
        t.goto(coordinates(*leftThirdTopColumnPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in leftThirdTopColumnPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
        
        t.pu()
        t.goto(coordinates(*leftThirdSideColumnPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in leftThirdSideColumnPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawLeftColumns()

    def drawMiddleColumns():
        # middle1stColumnPoints
        t.pu()
        t.goto(coordinates(*middle1stFrontColumnPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in middle1stFrontColumnPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()

        t.pu()
        t.goto(coordinates(*middle1stTopColumnPoints[0]))
        t.pd()
        
        t.fillcolor("white")
        t.begin_fill()
        for point in middle1stTopColumnPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
        
        t.pu()
        t.goto(coordinates(*middle1stSideColumnPoints[0]))
        t.pd()
        
        t.color("black")
        t.fillcolor("white")
        t.begin_fill()
        for point in middle1stSideColumnPoints:
            
            t.goto(coordinates(*point))
        t.end_fill()
    
    drawMiddleColumns()
    
    def drawTennisCourt():
        # Tennis Court
        t.pu()
        t.goto(coordinates(*tennisLeftCourtPoints[0]))
        t.pd()
        
        t.color("white")
        for point in tennisLeftCourtPoints:
            
            t.goto(coordinates(*point))

        t.pu()
        t.goto(coordinates(*tennisRightCourtPoints[0]))
        t.pd()
        
        t.color("white")
        for point in tennisRightCourtPoints:
            
            t.goto(coordinates(*point))
    
    drawTennisCourt()

    def drawCenterColumnPoints():
            def drawCenterColumnWhitePoints():
                # WindowColor
                t.pu()
                t.goto(coordinates(*centerColumnWhitePoints[0]))
                t.pd()

                t.fillcolor("white")
                t.begin_fill()
                
                for point in centerColumnWhitePoints:
                    t.goto(coordinates(*point))
                
                t.end_fill()
            
            drawCenterColumnWhitePoints()

            def drawCenterColumnGrayPoints():
                # WindowColor
                t.pu()
                t.goto(coordinates(*centerColumnGrayPoints[0]))
                t.pd()

                t.fillcolor("gray")
                t.begin_fill()
                
                for point in centerColumnGrayPoints:
                    t.goto(coordinates(*point))
                
                t.end_fill()
            
            drawCenterColumnGrayPoints()
            
            def drawCenterColumnOutlinePoints():
                # windowOutline
                t.pu()
                t.goto(coordinates(*centerColumnOutlinePoints[0]))
                t.pd()
                
                t.color("black")
                for point in centerColumnOutlinePoints:
                    t.goto(coordinates(*point))
            
            drawCenterColumnOutlinePoints()
            
    drawCenterColumnPoints()


    # return to black outline
    t.color("black")
        

drawBuilding()
screen.mainloop()