line_width = 25
img_height = 21

half_spans_horizontal = [[12, 13], #vertical line
                         [12, 13],
                         [12, 13],
                         [9, 13], # centered line, width 7
                         [8, 9],
                         [6, 7, 9, 13],
                         [5, 6, 8, 13],
                         [4, 5, 7, 11],
                         [-1, 3, 4, 5, 7, 11],
                         [5, 6, 8, 13],
                         [-1, 0, 1, 2, 3, 4, 6, 7, 9, 13]
                        ]

for y in range(0, img_height):
    abs_y = 10 - abs(y - 10) 
    xrange = 0
    x1 = half_spans_horizontal[abs_y][xrange]
    x2 = half_spans_horizontal[abs_y][xrange + 1]

    for x in range(0, line_width):
        abs_x = 13 - abs(x - 13)

        if abs_x == x1 and x >= 13 and xrange > 0:
            xrange -= 2

        x1 = half_spans_horizontal[abs_y][xrange]
        x2 = half_spans_horizontal[abs_y][xrange + 1]

        if(abs_x > x1 and abs_x <= x2):
            print('*', end='')
        else:
            print(' ', end='')
        
        if abs_x == x2 and xrange < len(half_spans_horizontal[abs_y]) - 2:
            xrange += 2 
   
        

    
    print('\n', end='')
            