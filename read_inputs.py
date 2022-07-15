import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd

class Read_inputs:
  
    encrypt_file_path = ""
    decrypt_file_path = ""

    encryption_input_filename = ""
    decryption_input_filename = ""

    cipher = ""
    algoHash = ""
    itr = 0
    encrypt_password = ""
    decrypt_password = ""

    def getEncryptionInputs(self):
        
        return self.encryption_input_filename, self.encrypt_password, self.itr, self.algoHash, self.cipher
    
    def getDecryptionInputs(self):
        
        return self.decryption_input_filename, self.decrypt_password

    #Method to extract the filename and read contents of the inputted file to encrypt
    def get_encryption_file_name(self):
        
        self.confirm_lbl=Label(self.window1, text="File selected", fg='orange', font=("Helvetica", 13))
        self.confirm_lbl.place(x=400, y=52)
        
        #Copying the entire path of the selected file
        self.encrypt_file_path = fd.askopenfilename(initialdir = "/")
        
        #Copying the name of the file to encrypt from the path
        self.encryption_input_filename = os.path.basename(self.encrypt_file_path)

        #The dialogbox that displays the selected file
        showinfo(
            title='Selected File',
            message=self.encrypt_file_path
        )

    #Method to extract the filename and read contents of the inputted file to decrypt
    def get_decryption_file_name(self):
        
        self.confirm_lbl1=Label(self.window2, text="File selected", fg='orange', font=("Helvetica", 13))
        self.confirm_lbl1.place(x=400, y=52)
        
        #Copying the entire path of the selected file
        self.decrypt_file_path = fd.askopenfilename(initialdir = "/")

        #Copying the name of the file to decrypt from the path
        self.decryption_input_filename = os.path.basename(self.decrypt_file_path)

        #The dialogbox that displays the selected file
        showinfo(
            title='Selected File',
            message=self.decrypt_file_path
        )

    #Method that reads all inputs required for encryption from the GUI
    def read_inputs_for_encryption(self):
        
        self.encrypt_password = self.pass_txtfld.get()
        self.cipher = self.cip_cb.get()
        self.algoHash = self.hash_cb.get()
        self.itr = int(self.iter_txtfld.get())
        self.window1.destroy()

    
    #Method that reads all inputs required for decryption from the GUI
    def read_input_for_decryption(self):

        self.decrypt_password = self.pass_txtfld1.get()
        self.window2.destroy()

    #Encryption GUI 
    def gui_encrypt(self):
        self.window1=Tk()
        self.window1.title('CBC Encryption')
        
        open_button1 = ttk.Button(self.window1, text='Input a File', command=self.get_encryption_file_name)
        open_button1.place(x=380 , y=50)

        btn1=Button(self.window1, text="Encrypt", fg='green', command=self.read_inputs_for_encryption)
        btn1.place(x=240, y=335)

        enc_lbl=Label(self.window1, text="Select the file for encryption:", fg='green', font=("Helvetica", 16))
        enc_lbl.place(x=60, y=50)

        pass_lbl=Label(self.window1, text="Enter the Password:", fg='green', font=("Helvetica", 16))
        pass_lbl.place(x=60, y=100)

        cip_lbl=Label(self.window1, text="Select the cipher suite:", fg='green', font=("Helvetica", 16))
        cip_lbl.place(x=60, y=150)

        hash_lbl=Label(self.window1, text="Select the hashing algorithm:", fg='green', font=("Helvetica", 16))
        hash_lbl.place(x=60, y=200)

        iter_lbl=Label(self.window1, text="Enter the number of iterations:", fg='green', font=("Helvetica", 16))
        iter_lbl.place(x=60, y=265)

        self.pass_txtfld=Entry(self.window1, show='*', bg='black', fg='white', bd=5)
        self.pass_txtfld.place(x=280, y=98)

        self.iter_txtfld=Entry(self.window1, bg='black',fg='white', bd=5)
        self.iter_txtfld.place(x=360, y=265)

        var1 = StringVar()
        var1.set("AES128")
        data=("AES128", "AES256", "3DES")
        self.cip_cb=Combobox(self.window1, values=data)
        self.cip_cb.place(x=290, y=150)

        var2 = StringVar()
        var2.set("SHA256")
        data=("SHA256", "SHA512")
        self.hash_cb=Combobox(self.window1, values=data)
        self.hash_cb.place(x=340,y=200)

        self.window1.geometry("550x400+10+20")
        self.window1.mainloop() 

    #Decryption GUI
    def gui_decrypt(self):
        self.window2=Tk()
        self.window2.title('CBC Decryption')

        open_button2 = ttk.Button(self.window2, text='Input a File', command=self.get_decryption_file_name)
        open_button2.place(x=370 , y=50)

        btn2=Button(self.window2, text="Decrypt", fg='green', command=self.read_input_for_decryption)
        btn2.place(x=200, y=185)

        decr_lbl=Label(self.window2, text="Select the file for decryption:", fg='green', font=("Helvetica", 16))
        decr_lbl.place(x=70, y=50)

        pass_lb2=Label(self.window2, text="Enter the Password:", fg='green', font=("Helvetica", 16))
        pass_lb2.place(x=70, y=125)

        self.pass_txtfld1=Entry(self.window2, show='*', bg='black',fg='white', bd=5)
        self.pass_txtfld1.place(x=320, y=126)

        self.window2.geometry("510x280+10+20")
        self.window2.mainloop()