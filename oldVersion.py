#Para contato pspsps2069@gmail.com
#I can translate it for 50 bucks, via paypal.

import sys                           #para poder usar argumentos do tipo -arg na hora de chamar a função
from   pytube     import YouTube     #para baixar
from   pytube.cli import on_progress #mostrar progresso
from   pytube     import Playlist    # para downlaod de playlists
import moviepy.editor as mp          #video -> musica

link=[]
url=""
l_mode  =False
v_mode  =False
s_mode  =False
p_mode  =False
url_mode=False
ps_mode =False
def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc
def progress_function(self,stream, chunk,file_handle, bytes_remaining):
    size = stream.filesize
    p = 0
    while p <= 100:
        progress = p
        print (str(p)+'%')
        p = percent(bytes_remaining, size)
def help():
    print("Olá, bem-vinde a downloader de videos do youtube feito por Pedro Henrique Goffi de Paulo - Ayc.  ")
    print("A lista de todos os argumentos possiveis é:",arglist,"\n                                         ")
    print("                    @                                                                            ")
    print("                   #*#           -H ou --high para baixar em alta resolução                      ")
    print("                  *#*#*          -l ou --low para baixar em baixa resolução                      ")
    print("                 #*#*#*#         -url=<url> para inserir o link do video                         ")
    print("                *#*#*#*#*        -s ou --song para baixar em formato mp3                         ")
    print("               #*#*#*#*#**       -v ou --visual para visualizar o donwload em tempo real         ")
    print("                   @@@           -Pl ou --playlist para baixar no contexto de playlists          ")
    print("                   @@@           -PS mostrar todo conteudo da playlist antes de baixar <não dispnivel>           ")
    print("                   @@@                                                                           ")
    print("                   @@@           Obs, por padrão ira baixar: Alta resolução | Modo visual | video")
    quit()
 
for arg in sys.argv:
    if len(sys.argv)!=1:
        arglist = ["/home/pietra/Downloads/Pedro-YoutubeDownloader/ytb.py"    ,
                   "--help"    ,"-H" ,
                   "--high"    ,"-x" ,
                   "--visual"  ,"-v" ,
                   "--low"     ,"-l" ,
                   "--song"    ,"-s" ,
                   "--playlist","-Pl",
                   "-PS",
                   "-url="
                   ]
        
        
        
        if (arg == "-"):
            print("Argumento invalido")
            print("py arg.py --help para menu de ajuda")
            quit()


        if(arg=="-PS"):
            ps_mode=True
    
            
        if (arg == "-l" or arg=="--low"):
            
            l_mode=True
            
        if (arg == "-H" or arg=="--high"):
            
            if (l_mode!=False):
                print("ops, nao pode usar -H junto com -l")
                quit()
            else:
                l_mode=False
            
        if (arg == "-v" or arg=="--visual"):
            
            v_mode=True
            
        if (arg == "-s" or arg=="--song"):
            
            s_mode=True
            
        if (arg == "-h" or arg=="--help"):        
            help()
            

            
        if arg not in arglist:
            link.append(arg)
            for letter in link:
                if (str(letter[0:len(letter[0:5])]) == "-url="):
                    url_mode=True                                 
                    url=letter[5::]
                    print(url)                    
                    
                    
                else:
                    print("Argumento <"+letter+"> invalido")
                    print("py arg.py --help para menu de ajuda")
                    quit()

        
        if (arg=="-Pl" or arg=="--playlist"):
            print("ainda estou trabalhando em cima disto...")
        
            p_mode=True
    
    else:
        ps_mode=False
        l_mode=False
        v_mode=True

        

    
if url=="":
    url=input("Qual a url? ")
else:
    if (p_mode and url_mode):
        print("-"*50)
        print("ops, nao é possivel usar Pl + url")
        print("-"*50)
        quit()



#l_mode
#x_mode
#v_mode
#https://www.youtube.com/watch?v=5QKIexlas0g&list=OLAK5uy_ln4nbAeRhRf6PcQR_Sz73bZkwF5F_a5bE&index=10
if p_mode:
    v_mode=True
    print("Modo de playlist...")
    yt = Playlist(url)
    if(ps_mode):
        for url in yt.video_urls:
            print(YouTube(url).title)
            
    _choice=input("Continuar? sim/nao [Ss/Nn]: ")    
    if (str(_choice) == "S" or str(_choice) =="s"):
        pass
    elif (str(_choice) == "N" or str(_choice) =="n"):    
        quit()
    else:
        print("ops opção invalida...")
        quit()
    
    for url in yt.video_urls:        
        print("modo visual ativo automatico...")
        print("modo playlist alta qualidade automatico...")
        if(s_mode):
            print("EQWEQWEQWE")
            quit()
        else:
            print("poeqw")
            quit()

            
        

        #,on_progress_callback=on_progress
        
    quit()

        
        



        


if p_mode==False:
    
    if(v_mode):
        print("modo visual ativo...")
        yt = YouTube(url,on_progress_callback=on_progress)
        if(l_mode):
            v_file = yt.streams.filter(res="360p").first()
            print("Baixa resolução...")
        else:
            v_file = yt.streams.get_highest_resolution()
            print("Alta resolução...")
    else:
        yt = YouTube(url)
        if(l_mode):
            v_file = yt.streams.filter(res="360p").first()
            print("Baixa resolução...")
        else:
            v_file = yt.streams.get_highest_resolution()
            print("Alta resolução...")
            

    try:
        print("O titulo é este?")
        print(yt.title)
    except Exception as e:
        if str(e) =="regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*":
            print("Ops houve um erro...")
            print("Por favor verifique se o link que copiou esta correto!")
            quit()
        else:
            print("Opsie! erro "+str(e))
            quit()
        
    _choice=input("Continuar? sim/nao [Ss/Nn]: ")
    if (str(_choice) == "S" or str(_choice) =="s"):
        pass
    elif (str(_choice) == "N" or str(_choice) =="n"):    
        quit()
    else:
        print("ops opção invalida...")
        quit()
        
    if(s_mode):
        v_file = yt.streams.get_audio_only()
        try:
            v_file.download()
        except Exception as e:
            print("Erro: "+str(e))
        quit()
    try:
        v_file.download()
    except Exception as e:
        print("Ops, Erro: "+str(e))






