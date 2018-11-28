from tkinter import *
from tkinter import messagebox
import sys
from dataHandler import dataHandler


def handleStartBtn():
    uname1 = ents[0][1].get().strip()
    pwd1 = ents[1][1].get().strip()
    hashTag = ents[2][1].get().strip()
    userLmt = ents[3][1].get().strip()
    atMark = var1.get()
    isCommentedUser = var2.get()

    if uname1 and pwd1 and hashTag:
        dh = dataHandler()
        try:
            dh.login(uname1, pwd1)
            dh.getHashtagData(hashTag, userLmt, atMark, isCommentedUser)
        except Exception as e:
            print(e)
            dh.users_file.close()
            dh.loader.close()
            sys.exit()
    else:
        messagebox.showinfo("Error", "Provide username, password or hash tag.")


def startBtnClick():
    handleStartBtn()

def handleStopBtn():
    sys.exit()

def makeform(root):
    entries = []
    global var1, var2
    var1 = IntVar()
    var2 = IntVar()
    for field in range(1, 8):
        row = Frame(root)
        row.pack(side=TOP, padx=5, pady=2)
        if field == 1:
            userNameLab = Label(row, text="Username", fg="#383a39", font=("Helvetica", 12))
            userNameLab.pack(side=LEFT)
            userNameEnt = Entry(row, width=40)
            entries.append(('username' + str(field), userNameEnt))
            userNameEnt.pack(side=LEFT, fill=X)

        if field == 2:
            passwordLab = Label(row, text="Password", fg="#383a39", font=("Helvetica", 12))
            passworsEnt = Entry(row, width=40, show="*")
            entries.append(('password' + str(field), passworsEnt))
            passworsEnt.pack(side=RIGHT, fill=X)
            passwordLab.pack(side=RIGHT)

        if field == 3:
            filesLab = Label(row, text="Hash tag", fg="#383a39", font=("Helvetica", 12))
            filesEnt = Entry(row, width=60)
            filesEnt.pack(side=RIGHT, fill=X)
            entries.append(('hashTag' + str(field), filesEnt))
            filesLab.pack(side=RIGHT)

        if field == 4:
            userLmt = Label(row, text="User limit", fg="#383a39", font=("Helvetica", 12))
            userLmtEnt = Entry(row, width=20)
            userLmtEnt.pack(side=RIGHT, fill=X)
            entries.append(('limit' + str(field), userLmtEnt))
            userLmt.pack(side=RIGHT)

        if field == 5:
            chkBtn = Checkbutton(row, text="@", variable=var1)
            entries.append(('atMark' + str(field), chkBtn))
            chkBtn.pack()

        if field == 6:
            chkBtn1 = Checkbutton(row, text="Commented users of posts", variable=var2)
            entries.append(('isCommentedUser' + str(field), chkBtn1))
            chkBtn1.pack()

        if field == 7:
            b1 = Button(window, text='Download', command=startBtnClick)
            b1.pack(side=RIGHT, padx=5, pady=2)

    return entries

window = Tk()
window.title("InstaClient")

ents = makeform(window)

window.mainloop()