from   pytube       import YouTube, Playlist
import sys

def help() -> "Exit":
    print(f"    Howdy, this what made'd by Ayc. pspsps2069@gmail.com for contact.")
    print(f"                    @       Help with args:")
    print(f"                   #*#      |--> -url=<url> will use the url in the context")
    print(f"                  *#*#*     |--> -p=<path> or --path=<path> will send the download to the path")
    print(f"                 #*#*#*#    |--> -s or --song will download only song")
    print(f"                *#*#*#*#*   |--> -v or --video will download only video")
    print(f"               #*#*#*#*#**  |--> -t=<type> or --type=<type> will use the type as reference to download songs")
    print(f"               #   @@@   &  |--> -l or --low will download with low resolution (480p)")
    print(f"               @   @@@      |--> -h or --high will download with high resolution (720p)")
    print(f"                   @@@@     |--> -y for playlist mode just download without asking")
    print(f"                @@@@@@@@    |--> -l=<K> or --limite=<K> will ask every K iterations if you want to continue")
    print(f"                            |--> -p or --playlist will consider the link as an playlist link")
    print(f"    LICENSE: Feel free to use this file as you want.")
    print(f"OBS: currently editing this, this was maded in 2 days. sorry for bugs :)")
    exit(0)

class downloadHandler:
    def __main__(self) -> "Select Mode":

        """ handle the modes the download will be able to download and how to """
        if   (self.playListMode  == True):   self.downloadPlaylist(self.link)
        elif (self.videoMode     == True):   self.downloadVideo(self.link)
        elif (self.songMode      == True):   self.downloadSong(self.link)
        # PLAYLIST MODE:  <09-04-22, pietra> #

    def downloadSong(self, link:str) -> "Optional Download":
        """ Inside streams ill filter only audio and only the extension of the
        managar class, then i'll take the first element and download. """
        print(f"|TARGET ==>\t{ YouTube(link).title}\n|->MODE: AUDIO\n|->STATUS: ", end="")
        try:    YouTube(link).streams.filter(only_audio=True,file_extension=self.type).first().download(self.path);print("OK\n",end="")
        except: print("ERROR\n",end="")
        print("|"+"-"*50)


    def downloadVideo(self, link:str) -> "Optional Download":

        """ Inside streams i'll filter the resolution and then download then
        take the first element then ill download""" 

        res = "480p"
        if (self.highMode == True): res = "720p"
        else:                       res = "360p"

        print(f"|TARGET ==>\t{ YouTube(link).title}\n|->MODE: [VIDEO, resolution: {res}]\n|->STATUS: ", end="")
        try:    YouTube(link).streams.order_by("resolution").filter(res=res).first().download(self.path);print("OK\n",end="")
        except: print("ERROR", end="")
        print("|"+"="*50)

    def downloadPlaylist(self, link:str) -> "Optional Download":
        for url in Playlist(link).video_urls:
            if      (self.IGNORE     != True):  self.checkLimiteDownload()
            if      (self.videoMode  == True):  self.downloadVideo(url)
            elif    (self.songMode   == True):  self.downloadSong(url)


    def checkLimiteDownload(self) -> "Optional Exit":
        self.INDEX += 1
        if (self.INDEX >= self.LIMITE):
            ask = input(f"Wanna download more {self.LIMITE} times? [y/n]")
            self.INDEX = 0
            if(ask.lower() == "n"):
                exit(0)

class manager(downloadHandler):
    """ Pre configuration for further use """
    highMode:       bool = False
    lowMode:        bool = False
    videoMode:      bool = False
    songMode:       bool = False
    showProgress:   bool = False
    IGNORE:         bool = False
    playListMode:   bool = False
    INDEX:          int  = 0
    LIMITE:         int  = 10
    type:           str  = "mp4"
    link:           str  = ""
    path:           str  = ""
    def runDownloaderContext(self) -> "Optional subclass Main function":
        """ test if the arguments var are ok, if yes then run. else raise
        exception """
        self.testConflicts()
        super().__main__()

    """ METHODS TO CONFIGURE THE CLASS """
    def setPath(self, path:str)     -> "Internal Config":   self.path           = path; return self
    def setType(self, Type:str)     -> "Internal Config":   self.type           = Type; return self
    def highMode(self)              -> "Internal Config":   self.highMode       = True; return self
    def lowMode(self)               -> "Internal Config":   self.lowMode        = True; return self
    def songMode(self)              -> "Internal Config":   self.songMode       = True; return self
    def showProgress(self)          -> "Internal Config":   self.showProgress   = True; return self
    def videoMode(self)             -> "Internal Config":   self.videoMode      = True; return self
    def ignoreMode(self)            -> "Internal Config":   self.IGNORE         = True; return self
    def playListMode(self)          -> "Internal Config":   self.playListMode   = True; return self
    def setLink(self, link:str)     -> "Internal Config":   self.link           = str(link); return self
    def setLimite(self, lim:int)    -> "Internal Config":   self.LIMITE         = int(lim);  return self


    def testConflicts(self) -> "Optional Exit":
        """ Test if some variables are ok for example video+song cant exist at
        same class!"""
        if  (self.songMode == True and self.videoMode == True):     print("[ERROR]: Can't use VIDEO MODE + SONG MODE"); exit(69)
        elif(self.lowMode  == True and self.highMode  == True):     print("[ERROR]: Can't use HIGHT MODE + LOW MODE");  exit(69)



""" MAIN FUNCTION """
if __name__ == "__main__":
    manager = manager()
    for arg in sys.argv:
        if  (arg in ["-H","--help"]):       help()
        elif(arg in ["-h", "--high"]):      manager.highMode()
        elif(arg in ["-l", "--low"]):       manager.lowMode()
        elif(arg in ["-s", "--song"]):      manager.songMode()
        elif(arg in ["-y",]):               manager.ignoreMode()
        elif(arg in ["-v", "--video"]):     manager.videoMode()
        elif(arg in ["-p", "--playlist"]):  manager.playListMode()
        elif(arg[0:5] in ["-url="]):        manager.setLink(arg[5:])
        elif(arg[0:3] in "-t="):            manager.setType(arg[3:])
        elif(arg[0:7] in "--type="):        manager.setType(arg[7:])
        elif(arg[0:3] in ["-l=",]):         manager.setLimite(arg[3:])
        elif(arg[0:9] in ["--limite=",]):   manager.setLimite(arg[9:])
        elif(arg[0:7] in ["--path=",]):        manager.setPath(f"{arg[7:]}/")
        elif(arg[0:3] in ["-p=",]):            manager.setPath(f"{arg[3:]}/")

    if (len(sys.argv) == 1):
        print("Download music mode", end="\n> ")
        link = input("Link: ")
        manager.songMode() \
            .showProgress() \
            .setLink(link)

    manager.runDownloaderContext()


