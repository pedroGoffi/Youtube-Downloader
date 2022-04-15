class Error:
    ExitCode: str 
    colors = {
        "OK":'\033[92m',
        "WARNING":'\033[93m',
        "FAIL":'\033[91m'
    }
   class std:
        HelpExitCode:      str = "You can contact me at: pedrohgdepauloc2@gmail.com"
        HighAndLowQuality: str = "Can't download with [--high] and [--low] flags"
        MusicAndVideo:     str = "Can't download with [--video] and [--music] flags"
        SucessEndRun:      str = "Thanks for using me"
        SucessfullRun:     str = "Sucessfully running"
        WarningRun:        str = "Something wen't wrong"
        FailRun:           str = "Error at runtime"
    class do:
        def Exit(ExitCode: int, complement:str):
            if ExitCode == 0: 
                COLOR = Error.colors["OK"]
                message = Error.std.SucessfullRun
            if ExitCode == 1: 
                COLOR = Error.colors["WARNING"]
                message = Error.std.WarningRun
            if ExitCode == 2: 
                COLOR = Error.colors["FAIL"]
                message = Error.std.FailRun
            print(f"{COLOR}{message} | Complement: {complement}\nEXIT CODE: {ExitCode}")
            exit(ExitCode)
