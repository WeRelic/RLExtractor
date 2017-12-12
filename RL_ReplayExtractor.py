import json, subprocess, tkinter, os, sys
import RL_Extractor_CarData


def PathLeaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
    


            
            
            


        
        
        
        
class MatchData( object ):
    def __init__( self, team1, team2, goals,
    
    
    
def GetRattleTrapVersion():
    if os.name == "linux":
        return "rattletrap-3.1.0-linux"
    elif os.name == "windows"
        return "rattletrap-3.1.0-windows-1"
    else:
        raise ValueError("Rattletrap does not support {}".format(os.name))


        
        
def RattleTrapDecodeCommand( replay_filepath = None ):
    if replay_file == None:
        return None
    else:
        return "{} decode {} > {}.json".format( GetRattleTrapVersion(), replay_filepath, PathLeaf(replay_filepath) )

        
        
        
def RattleTrapEncodeCommand( replay_jsonpath = None ):
    if replay_file == None:
        return None
    else:
        return "{} encode {} > {}.replay".format( GetRattleTrapVersion(), replay_jsonpath, PathLeaf(replay_jsonpath) )
        