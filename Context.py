class Context:
    """ This shall manage personal functions inside a huge namespace """
    daysWorkingOn: int = 4
    ExitCode: str
    colors = {
        "OK":'\033[92m',
        "WARNING":'\033[93m',
        "FAIL":'\033[91m'
    }

    class std:
        """ standard functions will be activate when the program can proceed
        without any error. This class can be called by Context.std """
        HelpExitCode:      str = "You can contact me at: pedrohgdepauloc2@gmail.com"
        HighAndLowQuality: str = "Can't download with [--high] and [--low] flags"
        MusicAndVideo:     str = "Can't download with [--video] and [--music] flags"
        SucessEndRun:      str = "Thanks for using me"
        SucessfullRun:     str = "Sucessfully running"
        WarningRun:        str = "Something wen't wrong"
        FailRun:           str = "Error at runtime"

        def Exit(complement:str, colors:str = None) -> "Exit sucessfuly":
            """ The color shall be passed by argument and the complement as
            well then return """
            print(f"{Context.colors['OK']}{complement}")
            exit(0)
        def Display(color:str, complement:str, final:str=None) -> "Print with color":
            """ The color shall be passed by argument and the complement to
            print then return """
            if      color.lower() == "red":         tmp = Context.colors['FAIL']
            elif    color.lower() == "yellow":      tmp = Context.colors['WARNING']
            else:                                   tmp = Context.colors["OK"]

            print(f"{tmp}{complement}", end="" if final is not None else final)

    class Error:
        """ If some error rise when running this class shall be called by
        Context.Error """
        def Exit(ExitCode: int, complement:str) -> "Exit the program with warning or fail code":
            """ The color shall be passed by argument and the complement
                Note: this is only fail exit then the color will be or yellow
                or red for exit code 1 or 2"""
            if ExitCode == 1:
                COLOR       = Context.colors["WARNING"]
                message     = Context.std.WarningRun
            if ExitCode == 2:
                COLOR       = Context.colors["FAIL"]
                message     = Context.std.FailRun

            print(f"{COLOR}{message} | Complement: {complement}\nEXIT CODE: {ExitCode}")
            exit(ExitCode)
