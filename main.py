from   pytube       import YouTube
import sys 
def help():
    print(f"    Howdy, this what made'd by Ayc. pspsps2069@gmail.com for contact.                                   ")
    print()
    print(f"                    @       Help with args:")
    print(f"                   #*#      |--> -url=<url> will use the url in the context")
    print(f"                  *#*#*     |--> -p=<path> or --path=<path> will send the download to the path.")
    print(f"                 #*#*#*#    |--> -s or --song will download only song")
    print(f"                *#*#*#*#*   |--> -v or --video will download only video")
    print(f"               #*#*#*#*#**  |--> -t=<type> or --type=<type> will use the type as reference to download songs")
    print(f"               #   @@@   &  |--> -l or --low will download with low resolution (480p)")
    print(f"               @   @@@      |--> -h or --high will download with high resolution (720p)")
    print(f"                   @@@@        ")
    print(f"                @@@@@@@@          ")
    print(f"    LICENSE: Feel free to use this file as you want.")
    print(f"TODO: playlist mode")
    exit(0)

class downloadHandler:
    def __main__(self):
        """ handle the modes the download will be able to download and how to """
        if self.videoMode   == True:    self.downloadVideo(self.link)
        elif self.songMode  == True:    self.downloadSong(self.link)
        # PLAYLIST MODE:  <09-04-22, pietra> #

    def downloadSong(self, link):
        """ Inside streams ill filter only audio and only the extension of the
        managar class, then i'll take the first element and download. """
        YouTube(self.link).streams.filter(only_audio=True,file_extension=self.type).first().download(self.path)

    def downloadVideo(self, link):
        """ Inside streams i'll filter the resolution and then download then
        take the first element then ill download"""
        if (self.highMode == True):
            res = "720p"
        else:
            res = "480p"
        YouTube(self.link).streams.order_by("resolution").filter(res=res).first().download(self.path)

class manager(downloadHandler):
    """ Pre configuration for further use """
    highMode:       bool = False
    lowMode:        bool = False
    videoMode:      bool = False
    songMode:       bool = False
    showProgress:   bool = False
    type:           str  = "mp4"
    link:           str  = ""
    path:           str  = ""
    def runDownloaderContext(self):
        """ test if the arguments var are ok, if yes then run. else raise
        exception """
        self.testConflicts()
        super().__main__()

    """ METHODS TO CONFIGURE THE CLASS """
    def setPath(self, path):    self.path           = path
    def setLink(self, link):    self.link           = link
    def highMode(self):         self.highMode       = True
    def lowMode(self):          self.lowMode        = True
    def songMode(self):         self.songMode       = True
    def showProgress(self):     self.showProgress   = True
    def setType(self, type):    self.type           = type
    def videoMode(self):        self.videoMode      = True

    def testConflicts(self):
        """ Test if some variables are ok for example video+song cant exist at
        same class!"""
        if(self.songMode == True and self.videoMode == True):
            print("[ERROR]: Can't use VIDEO MODE + SONG MODE")
            exit(69)
        elif(self.lowMode == True and self.highMode == True):
            print("[ERROR]: Can't use HIGHT MODE + LOW MODE")
            exit(69)





""" MAIN FUNCTION """
if __name__ == "__main__":
    manager = manager()
    for arg in sys.argv:
        if  (arg in ["-H","--help"]):   help()
        elif(arg[0:3] == "-p="):        manager.setPath(f"{arg[3:]}/")
        elif(arg[0:7] == "--path="):    manager.setPath(f"{arg[7:]}/")
        elif(arg in ["-h", "--high"]):  manager.highMode()
        elif(arg in ["-l", "--low"]):   manager.lowMode()
        elif(arg in ["-s", "--song"]):  manager.songMode()
        elif(arg in ["-v", "--video"]): manager.videoMode()
        elif(arg[0:5] in ["-url="]):    manager.setLink(arg[5:])
        elif(arg[0:3] in "-t="):        manager.setType(arg[3:])
        elif(arg[0:7] in "--type="):    manager.setType(arg[7:])

    if (len(sys.argv) == 1):
        print("Download music mode", end="\n> ")
        link = input("Link: ")
        manager.songMode()
        manager.showProgress()
        manager.setLink(link)

    manager.runDownloaderContext()
















