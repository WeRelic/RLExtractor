# RL_Extractor_PlayerData.py


class RL_Player( object ):
    """
        Represents a single rocket league player within a replay.
    """
    def __init__( self, playername, car_data = None ):
        self.playername = playername
        self.car_data   = car_data
        
        
    def GetCarBody( self ):
        """ Get the name and color of the car body the player is using. """
        if self.car_data not None:
            return str(self.car_data.body)
        else:
            return None
            
    def GetCarDecal( self ):
        """ Get the name and color of the decal the player is using. """
        if self.car_data not None:
            return str(self.car_data.decal)
        else:
            return None
            
    def GetCarPrimaryColor( self ):
        """ Get the primary paint color of this player's car. """
        if self.car_data not None:
            return self.car_data.paint[0]
        else:
            return None
            
    def GetCarSecondaryColor( self ):
        """ Get the secondary paint color of this player's car. """
        if self.car_data not None:
            return self.car_data.paint[1]
        else:
            return None
            
    def GetCarWheels( self ):
        """ Get the wheel data of this player's car. """
        if self.car_data not None:
            return str(self.car_data.wheels)
        else:
            return None
            
    def GetCarTopper( self ):
        """ Get the topper data of this player's car. """
        if self.car_data not None:
            return str( self.car_data.topper )
        else:
            return None
            
    def GetCarBoost( self ):
        """ Get the boost data of this player's car. """
        if self.car_data not None:
            return str( self.car_data.boost )
        else:
            return None
            
    def GetCarTrail( self ):
        """ Get the trail data of this player's car. """
        if self.car_data not None:
            return self.car_data.trail
        else:
            return None
            
    def GetCarPrimaryPaint( self ):
        """ Get the primary paint type of this player's car. """
        if self.car_data not None:
            return self.car_data.paint[0]
        else:
            return None
            
    def GetCarSecondaryPaint( self ):
        """ Get the secondary paint type of this player's car. """
        if self.car_data not None:
            return self.car_data.paint[1]
        else:
            return None
            
    def GetGoalExplosion( self ):
        """ Get the goal explosion this player is using. """
        if self.car_data not None:
            return self.car_data.explosion
        else:
            return None
    
    
    