# RL_Extractor_CarData.py


class PaintedItem( object ):
    """ 
        Represents a painted or unpainted item in Rocket League.
        This includes decals, car bodies, rocket boosts, and toppers.
    """
    def __init__( self, name, painted_color = None ):
        self.name  = name
        self.color = painted_color
        
        
    def __str__( self ):
        if self.color == None:  
            return self.name
        else:
            return "{} {}".format(self.color, self.name)
            
            
class CarData( object ):
    """ 
        Represents all the customizations on a given rocket league player's car.
    """
    def __init__( self, 
            car_body, 
            decal, 
            primary_color, 
            secondary_color, 
            primary_paint, 
            secondary_paint,
            wheels, 
            boost, 
            trail, 
            goal_explosion, 
            topper ):
        self.body      = body
        self.decal     = decal
        self.colors    = [ primary_color, secondary_color ]
        self.paint     = [ primary_paint, secondary_paint ]
        self.boost     = boost
        self.trail     = trail
        self.explosion = goal_explosion
        self.topper    = topper
        self.wheels    = wheels
        
        
    def __str__( self ):
        s = self.body + "{\n"
        s = s + "\tDecal: {},\n\t\
Primary Color: {},\n\tSecondary Color: {},\
Primary Paint: {},\n\tSecondary Paint: {},\
\n\tRocket Boost: {},\n\tTrail: {},\n\t\
Goal Explosion: {},\n\tTopper: {}\n\tWheels: {}\n".format( self.decal, *self.colors, *self.paint, 
    self.boost, self.trail, self.explosion, self.topper, self.wheels )
        return s + "};"