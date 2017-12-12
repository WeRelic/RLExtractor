# RL_ReplayExtractorUI.py

import RL_ReplayExtractor
import tkinter

    
        

class PathingPage( object ):
    def __init__( self, root ):
        self.replay_file_path = tkinter.StringVar()
        self.replay_json_path = tkinter.StringVar()
        
        self.replay_file_label = tkinter.Label(root,text="Replay File Path :")
        self.replay_json_label = tkinter.Label(root,text="Replay JSON path :")
    
        self.replay_file_entry = tkinter.Entry( root,textvariable = self.replay_file_path)
        self.replay_json_entry = tkinter.Entry( root,textvariable = self.replay_json_path )
            
    def Draw( self ):
        self.replay_file_label.grid(column=0,row=0,sticky='w',padx=5,pady=5)
        self.replay_json_label.grid(column=0,row=1,sticky='w',padx=5,pady=5)
        self.replay_file_entry.grid(column=1,row=0,sticky='w',columnspan=4,padx=5,pady=5)
        self.replay_json_entry.grid(column=1,row=1,sticky='w',columnspan=4,padx=5,pady=5)
        
        
        
class OverviewPage( object ):
    def __init__( self, root ):
        
        
if __name__ == "__main__":
    root = tkinter.Tk()
    pathpage = PathingPage(root)
    pathpage.Draw()
    root.mainloop()
    
    