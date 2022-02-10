
import string
from tkinter import *
import threading
from subprocess import run
from tkinter import ttk,messagebox,filedialog


class downloader():

    def __init__(self):

    #    creates the main window
       self.m_window = Tk()                           
       self.m_window.title("youtube_to_mp3_converter")
       self.m_window.geometry('700x200')

       
       self.url = Label(self.m_window,text = 'Video link',font = ('Arial',12))
       self.url.place(x=30,y=40)
       self.entry_box = Entry(self.m_window,width = 70)
       self.entry_box.place(x=130,y=41)

    #    creates the input box
       self.f_path = StringVar()
       self.save_to = Label(self.m_window,text = 'Save mp3 file',font = ('Arial',12))
       self.save_to.place(x=30,y=80)
       self.save_box = Entry(self.m_window,width = 70,textvariable=self.f_path)
       self.save_box.place(x=130,y=81)

    #    creates browse button
       self.browseButton = Button(self.m_window,text= "Browse",command = self.browse_button)
       self.browseButton.place(x=600,y=81) 

    #    creates the download button
       self.down_bttn = Button(self.m_window,text = "Download",command = self.press_download)
       self.down_bttn.place(x=300,y=120)

    # creates progress bar
       self.progress_bar = ttk.Progressbar(self.m_window, orient = HORIZONTAL)
       self.progress_bar.pack(side = BOTTOM,fill=X)
       
       self.m_window.mainloop()


    def browse_button(self):
      self.filename = filedialog.askdirectory()
      self.f_path.set(self.filename)

    def donw_button(self,link,path):
        self.link = link
        self.path = path

        if self.path != None:
            run(f'youtube-dl --prefer-ffmpeg -o "{self.path}/%(title)s.%(ext)s" --extract-audio --audio-format mp3 {self.link}',
                 shell=True, capture_output=True, text=True).stdout
        else:
             run(f'youtube-dl --prefer-ffmpeg --extract-audio --audio-format mp3 {self.link}',
                 shell=True, capture_output=True, text=True).stdout

    def press_download(self):
        self.progress_bar.start()
        def call():
            self.url_t = self.entry_box.get()
            self.save = str(self.save_box.get())

            if self.url_t != None and (self.url_t.startswith('http') or self.url_t.startswith('www')):
                try:
                   
                    self.donw_button(self.url_t,self.save)
                    self.progress_bar.stop()
                    messagebox.showinfo(title = "Success",message = "Completed Downloading")
                   
                except:
                    self.progress_bar.stop()
                    messagebox.showerror(title = "Error",message = "Error please try again")

            else:
                self.progress_bar.stop()
                messagebox.showerror(title='Error', message='url not valid')
        
        self.thred = threading.Thread(target = call)
        self.thred.start()


if __name__ == '__main__':
    downloader() 

