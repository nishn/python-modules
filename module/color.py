#!/usr/bin/env python
# coding: UTF-8

import colorsys

class RGB:
    def __init__(self, red, green, blue):
        if isinstance( red, int ) and isinstance( green, int ) and isinstance( blue, int ):
            self.rgb = ( red, green, blue )
        elif isinstance( red, float ) and isinstance( green, float ) and isinstance( blue, float ):
            tmp = ( red*255, green*255, blue*255 )
            self.rgb = tuple(map( int, tmp ))
        else:
            raise ValueError( "rgb: invalud initialization" )
        
    def to_rgb( self ):
        return '#%02x%02x%02x' % self.rgb

    def __add__( self, rhs ):
        return RGB( *tuple([ self.rgb[i] + rhs.rgb[i] for i in range(3) ]) )
    
    def __sub__( self, rhs ):
        return RGB( *tuple([ self.rgb[i] - rhs.rgb[i] for i in range(3) ]) )

    def __mul__( self, n ):
        return RGB( *tuple([ int(self.rgb[i] * n) for i in range(3) ]) )
    
    def __div__( self, n ):
        return RGB( *tuple([ int(self.rgb[i] / n) for i in range(3) ]) )

    def __repr__( self ):
        return self.to_rgb()

    def brightness( self ):
        return sum(self.rgb)

    def HSV( self ):
        M = max( self.rgb ) / 255.0
        m = min( self.rgb ) / 255.0
        return 0.0 if M == 0.0 and m == 0.0 else ( M - m ) / M

    def HLS( self ):
        M = max( self.rgb ) / 255.0
        m = min( self.rgb ) / 255.0
        if M == 0.0 and m == 0.0 or M == 1.0 and m == 1.0:
            return 0.0
        else:
            return ( M - m ) / ( 1 - abs( M + m - 1 ) )

def RGB_check( arg ):
    if isinstance( arg, RGB ):
        return arg
    elif isinstance( arg, tuple ):
        return RGB( *arg )
        
def RGB_cmap( start, end, x ):
    if x < 0.0 or 1.0 < x:
        raise ValueError("cmap : x out of range")
    start = RGB_check(start)
    end   = RGB_check(end)
    
    if x == 1.0:
        return end
    return start + ( end - start )*x


class HSV:
    def __init__( self, h, s, v ):
        self.hsv = ( h, s, v )
        
    def __add__( self, rhs ):
        return HSV( *tuple([ self.hsv[i] + rhs.hsv[i] for i in range(3) ]) )
    
    def __sub__( self, rhs ):
        return HSV( *tuple([ self.hsv[i] - rhs.hsv[i] for i in range(3) ]) )

    def __mul__( self, n ):
        return HSV( *tuple([ self.hsv[i] * n for i in range(3) ]) )
    
    # def __div__( self, n ):
    #     return color( *tuple([ int(self.hsv[i] / n) for i in range(3) ]) )

    def gradation(self, h, s, v, x):
        return self + ( HSV( h, s, v ) - self ) * x
    
    def to_rgb(self):
        return RGB(*colorsys.hsv_to_rgb( *self.hsv )).to_rgb()

    def __repr__(self):
        return self.to_rgb()

def HSV_check( arg ):
    if isinstance( arg, HSV ):
        return arg
    elif isinstance( arg, tuple ):
        return HSV(*arg)
    else:
        raise TypeError( "invalid type for HSV initialization" )
    
    
def HSV_cmap( start, end, x ):
    if x < 0.0 or 1.0 < x:
        raise ValueError( "HSV_cmap : x is out of range [0.0, 1.0]" )
    
    return HSV_check( start ).gradation( end[0], end[1], end[2], x ).to_rgb()
    
if __name__ == "__main__":
    def test( start, end, n ):
        ret = '<table><tbody><tr>'
        for i in range( n ):
            col = RGB_cmap( RGB(*start), RGB(*end), float(i)/(n-1) )
            ret += '<td bgcolor=%s>%4.2f<br>%s<br>%s<br>%4.2f<br>%4.2f</td>' % ( col, float(i)/(n-1),
                                                                                 col, col.brightness(),
                                                                                 col.HSV(), col.HLS() )
        ret += '</tr></tbody></table>\n'
        return ret


    def HSV_test( start, end, n ):
        ret = '<table><tbody><tr>'
        for i in range( n ):
            col = HSV(*start).gradation( end[0], end[1], end[2], float(i)/(n-1) ).to_rgb()
            ret += '<td bgcolor=%s>%4.2f<br>%s</td>' % ( col, float(i)/(n-1), col )
        return ret + '</tr></tbody></table>'
    
    html = '''
<!DOCTYPE html>
<head>
<meta charset=UTF-8>
<title>color test</title>
</head>
<style type="text/css">
table{
align: left;
}
td{
  width:  100px;
  text-align: center;
}
</style>
<body>
'''

    #html += test( (0,255,128), (255,0,0), 16 )
    #html += test( (0,128,255), (255,0,0), 16 )
    html += test( (30,128,255), (255,85,85), 30 )
    #html += test( (101,121,255), (255,15,5) ,30 )
    html += test( (148,160,255), (255,232,1) ,30 )
    html += test( (255,10,255) , (0,228,255), 30 )
    #html += test( (255,85,85), (3,200,136), 16 )

    # hsv
    html += HSV_test( (0.0, 1.0, 1.0), (0.66, 1.0, 1.0), 30 )
    html += HSV_test( (0.0, 1.0, 1.0), (1.0, 1.0, 1.0), 30 )
    html += HSV_test( (0.0, 0.9, 0.8), (1.0, 0.9, 0.8), 30 )
    
    html += '\n</body>'

    with open( 'test.html', 'w' ) as f:
        f.write( html )
