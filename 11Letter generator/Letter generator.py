'''Project File Structure:
Let us look at the flow of the project

Importing tkinter, requests, beautifulsoup and googleapiclient modules
Obtaining the key and creating a programmable search engine
Defining the lyrics extractor function.
Create the GUI.
Activating the function using a button.'''

from tkinter import * #Tkinter contains the GUI widgets to create the user interface
from tkinter import messagebox #To create prompts to alert the user, we use messagebox. It contains prompt to ask the user for yes or no questions, show a warning and errors etc
from tkinter import scrolledtext # The lyrics can be longer than the set dimensions of the window of the application. Hence we create a scrolling text widget to allow scrolling of the text widget and display the lyrics
from tkinter import StringVar
from tkinter import ttk

#Create the Song Lyrics extractor function using Python
def lyrics_extractor():
#Read the name of the song   
    song = song_entry.get()   
#Raise a warning if no input if given
    if len(song) <=0:
        messagebox.showerror(message = "Enter a song name" )
        return
    else:   
    #connect the API with the search engine
        lyric_object = build("customsearch", 'v1', developerKey=api_key).cse()
    #execute the search
        result = lyric_object.list(q=song, cx=cse_key).execute()
    #Obtain the first result of the 10 retrieved
        try: 
            first_value = next(iter(result["items"]))
        except:
            messagebox.showwarning(message = "Lyrics for "+song+" were not found" )
            return
    #Send a request link to extract contents of the first website
        result = requests.get(first_value["link"])
    #To obtain individual components in the html format
        soup_lyrics = BeautifulSoup(result.content, "html.parser")
    #Find the language using the link
        if ("tamil" in first_value["link"]) | ("hindi" in first_value["link"]):
        #if tamil, read the lyric from the div tag containing print-lyrics class
            lyrics = soup_lyrics.find(class_ = "print-lyrics")
        elif "azlyrics" in first_value["link"]:
        #if english, read the lyric from the div tag containing no class and id
            lyrics = soup_lyrics.find("div", {'class':'', 'id':''})      
    #Display the output
        display_lyrics = scrolledtext.ScrolledText(lyrics_app, width = 60, height=10, font=("Ubuntu Mono",10), bd=0, bg="darkgreen")
        display_lyrics.insert("1.0",lyrics.text)
        display_lyrics.config(state=DISABLED)
        display_lyrics.grid(row=2, column=0, columnspan=3)
        
#Create the user interface for the Python Extract Song Lyrics
lyrics_app = Tk()
lyrics_app.geometry("500x300")
lyrics_app.title("Bones's Lyrics extractor")
lyrics_app.config(bg="green")
#Specify the entry fields
song_label = Label(lyrics_app, text="Please, put song name: ",bg="green")
song_label.grid(row=0, column=0, padx=20, pady=20)
song_entry = Entry(lyrics_app, width=40)
song_entry.grid(row=0, column=1)

#Button for lyrics
get_lyrics_button = Button(lyrics_app, text="Get Lyrics", command=lyrics_extractor)
get_lyrics_button.grid(row=1, columnspan=2,pady=20)
# Create a Button exit
button_x = ttk.Button(lyrics_app, text='Close App',command=lyrics_app.destroy)
button_x.grid(
    column = 0,
    row = 4,
    padx = 5,
    pady = 5
)
button_x.bind(
    '<Button-1>'       
)
#Terminate the app upon closing
lyrics_app.mainloop()

