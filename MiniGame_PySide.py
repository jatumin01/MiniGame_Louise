import sys
import getpass
userProfile = "C:/Users/"+getpass.getuser() + "Documents/Git/Minigame_louise"
if not userProfile in sys.path:
    sys.path.append(userProfile)

import Create_MiniGame_byPySide.MiniGame_Gui as miniGame
reload(miniGame)
