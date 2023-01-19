
'''

    This is a test demonstration of the starting pages of the capstone project

'''


from tkinter import *


# Windows
startWindow = Tk()
userAccountLoginCreateWindow = Toplevel(startWindow)
modulesMenuWindow = Toplevel(userAccountLoginCreateWindow)
schedulingAppointmentsWindow = Toplevel(userAccountLoginCreateWindow)
makeAReferralWindow = Toplevel(schedulingAppointmentsWindow)
orderALabWindow = Toplevel(makeAReferralWindow)
patientProviderCommunicationWindow = Toplevel(orderALabWindow)



# Colors
hintOfRed = "#F9F7F7"
botticelli = "#DBE2EF"
sanMarino = "#3F72AF"
blueZodiac = "#112D4E"
mirage = "#1B262C"

# Arrays
windows = [startWindow, userAccountLoginCreateWindow, modulesMenuWindow, schedulingAppointmentsWindow, makeAReferralWindow, orderALabWindow, patientProviderCommunicationWindow]
groupMemebers_A = ["Parker Phelps", "Jessica Weeks", "Christina Fortin", "Flora Cherotich"]
groupMemebers_B = ["Adia Chue", "Matthew Burrus", "Destan Hutcherson"]

# GLOBAL VARIABLES
userLoggedIn = False
invalidLogin = False
accountExists = False

# Functions
' ACROSS DIFFERENT WINDOWS '
# Window Setup
def windowSetup(window, width, height, titleTxt):

    window.geometry(str(width) + "x" + str(height))
    window.title(titleTxt)
    window.resizable(False, False)
    window.configure(bg=hintOfRed)

    if not window.winfo_viewable():
        window.deiconify()

# Center the window
def centerWindow(window, width, height):

    # Getting user screen measurements
    uW = window.winfo_screenwidth()
    uH = window.winfo_screenheight()

    # Getting x and y
    x = (uW/2) - (width/2)
    y = (uH/2) - (height/2)


    # Centering the window
    window.geometry('+%d+%d' % (x,y))

# Hide the windows
def hideAllWindows():
    for window in windows:
        window.withdraw()

# Exits the program
def exitProgram():
    for window in windows:
        window.quit()

# Creates a toolbar based on the window
def createWindowToolbar(window):

    if window == userAccountLoginCreateWindow:

        userAccountLoginCreateWindowToolbar = Frame(userAccountLoginCreateWindow)
        startMenuBtn = Button(userAccountLoginCreateWindowToolbar, text="START", command=enterStartWindow).pack(side=LEFT)
        exitBtn = Button(userAccountLoginCreateWindowToolbar, text="EXIT", command=exitProgram).pack(side=LEFT)
        userAccountLoginCreateWindowToolbar.pack(side=TOP, anchor=W)

    if window == modulesMenuWindow:

        modulesWindowToolbar = Frame(modulesMenuWindow)
        startMenuBtn = Button(modulesWindowToolbar, text="START", command=enterStartWindow).pack(side=LEFT)
        logoutBtn = Button(modulesWindowToolbar, text="LOGOUT", command=logoutUser).pack(side=LEFT)
        exitBtn = Button(modulesWindowToolbar, text="EXIT", command=exitProgram).pack(side=LEFT)

        modulesWindowToolbar.pack(side=TOP, anchor=W)

    if window == schedulingAppointmentsWindow:

        schedulingAppointmentsWindowToolbar = Frame(schedulingAppointmentsWindow)
        startMenuBtn = Button(schedulingAppointmentsWindowToolbar, text="START", command=enterStartWindow).pack(side=LEFT)
        modulesMenuBtn = Button(schedulingAppointmentsWindowToolbar, text="MODULES", command=enterModulesMenuWindow).pack(side=LEFT)
        logoutBtn = Button(schedulingAppointmentsWindowToolbar, text="LOGOUT", command=logoutUser).pack(side=LEFT)
        exitBtn = Button(schedulingAppointmentsWindowToolbar, text="EXIT", command=exitProgram).pack(side=LEFT)

        schedulingAppointmentsWindowToolbar.pack(side=TOP, anchor=W)

    if window == makeAReferralWindow:

        makeAReferralWindowToolbar = Frame(makeAReferralWindow)
        startMenuBtn = Button(makeAReferralWindowToolbar, text="START", command=enterStartWindow).pack(side=LEFT)
        modulesMenuBtn = Button(makeAReferralWindowToolbar, text="MODULES", command=enterModulesMenuWindow).pack(side=LEFT)
        logoutBtn = Button(makeAReferralWindowToolbar, text="LOGOUT", command=logoutUser).pack(side=LEFT)
        exitBtn = Button(makeAReferralWindowToolbar, text="EXIT", command=exitProgram).pack(side=LEFT)

        makeAReferralWindowToolbar.pack(side=TOP, anchor=W)

    if window == orderALabWindow:

        orderALabWindowToolbar = Frame(orderALabWindow)
        startMenuBtn = Button(orderALabWindowToolbar, text="START", command=enterStartWindow).pack(side=LEFT)
        modulesMenuBtn = Button(orderALabWindowToolbar, text="MODULES", command=enterModulesMenuWindow).pack(side=LEFT)
        logoutBtn = Button(orderALabWindowToolbar, text="LOGOUT", command=logoutUser).pack(side=LEFT)
        exitBtn = Button(orderALabWindowToolbar, text="EXIT", command=exitProgram).pack(side=LEFT)

        orderALabWindowToolbar.pack(side=TOP, anchor=W)

    if window == patientProviderCommunicationWindow:

        patientProviderCommunicationWindowToolbar = Frame(patientProviderCommunicationWindow)
        startMenuBtn = Button(patientProviderCommunicationWindowToolbar, text="START", command=enterStartWindow).pack(side=LEFT)
        modulesMenuBtn = Button(patientProviderCommunicationWindowToolbar, text="MODULES", command=enterModulesMenuWindow).pack(side=LEFT)
        logoutBtn = Button(patientProviderCommunicationWindowToolbar, text="LOGOUT", command=logoutUser).pack(side=LEFT)
        exitBtn = Button(patientProviderCommunicationWindowToolbar, text="EXIT", command=exitProgram).pack(side=LEFT)

        patientProviderCommunicationWindowToolbar.pack(side=TOP, anchor=W)


' ENTERING THE DIFFERENT WINDOWS '
# Enter Start Window
def enterStartWindow():

    hideAllWindows()
    windowSetup(startWindow, 1050, 1050, "Forsyth Family Practice Center - Medical Office Administration")
    centerWindow(startWindow, 1050, 1050)

# Enters either the user account login/create window or modules menu window
def enterEitherUSLCW_OR_MMW():

    global userLoggedIn

    if not userLoggedIn:
        enterUserAccountLoginCreateWindow()

    if userLoggedIn:
        enterModulesMenuWindow()

# Enter User Account Login/Create Window
def enterUserAccountLoginCreateWindow():
    hideAllWindows()
    windowSetup(userAccountLoginCreateWindow, 1100, 1100, "Forsyth Family Practice Center - Login/Create Account")
    centerWindow(userAccountLoginCreateWindow, 1100, 1100)

# Enters Module Menu Window
def enterModulesMenuWindow():
    hideAllWindows()
    windowSetup(modulesMenuWindow, 1100, 1100, "Forsyth Family Practice Center - Modules Menu")
    centerWindow(modulesMenuWindow, 1100, 1100)

# Enter Scheduling Appointments Window
def enterSchedulingAppointmentsWindow():
    hideAllWindows()
    windowSetup(schedulingAppointmentsWindow, 1000, 1000, "Forsyth Family Practice Center - Schedule An Appointment")
    centerWindow(schedulingAppointmentsWindow, 1000, 1000)

# Enter Make a Referral Window
def enterMakeAReferralWindow():
    hideAllWindows()
    windowSetup(makeAReferralWindow, 1000, 1000, "Forsyth Family Practice Center - Make a Referral")
    centerWindow(makeAReferralWindow, 1000, 1000)

# Enter Order a Lab Window
def enterOrderALabWindow():
    hideAllWindows()
    windowSetup(orderALabWindow, 1000, 1000, "Forsyth Family Practice Center - Order a Lab")
    centerWindow(orderALabWindow, 1000, 1000)

# Enter Patient/Provider Communication Window
def enterPatientProviderCommunicationWindow():
    hideAllWindows()
    windowSetup(patientProviderCommunicationWindow, 1000, 1000, "Forsyth Family Practice Center - Patient/Provider Comm.")
    centerWindow(patientProviderCommunicationWindow, 1000, 1000)

' ACCOUNT MANIPULATION '
# Login user
def loginUserBasedOnInputs():
    global userLoggedIn
    userLoggedIn = True

    if userLoggedIn:
        enterModulesMenuWindow()

# Logout user
def logoutUser():
    global userLoggedIn

    if userLoggedIn:
        userLoggedIn = False
        enterStartWindow()


if __name__ == '__main__':


    ' Start Window '
    enterStartWindow()

    # Top text
    startWindowTextFrame = Frame(startWindow, bg=hintOfRed)
    startWindowMainHeading = Label(startWindowTextFrame, text="FORSYTH FAMILY PRACTICE CENTER", font=("Lato Bold", 24), fg=mirage, bg=hintOfRed).pack(pady=(0, 20))
    startWindowGroupName = Label(startWindowTextFrame, text="Medical Office Administration", font=("Lato", 18), fg=mirage, bg=hintOfRed).pack(pady=(0, 30))
    techUsedText = Label(startWindowTextFrame, text="Made with: Python (Tkinter)", font=("Lato", 10), fg=mirage, bg=hintOfRed).pack(side=BOTTOM, pady=(60,0))

    # Displaying group memeber names
    groupMemebers_A_Frame = Frame(startWindowTextFrame, bg=hintOfRed)
    groupMemebers_B_Frame = Frame(startWindowTextFrame, bg=hintOfRed)

    for memeber in groupMemebers_A:
         startWindowGroup_A = Label(groupMemebers_A_Frame, text=memeber, font=("Lato", 12), fg=blueZodiac, bg=hintOfRed).pack(side=LEFT, anchor=N, padx=(5, 5))

    for memeber in groupMemebers_B:
         startWindowGroup_B = Label(groupMemebers_B_Frame, text=memeber, font=("Lato", 12), fg=blueZodiac, bg=hintOfRed).pack(side=LEFT, anchor=N, padx=(5, 5))

    # Start window buttons
    startWindowBtns = Frame(startWindowTextFrame, bg=hintOfRed)
    startWindowEnterBtn = Button(startWindowBtns, text="ENTER", font=("Lato Bold", 12), activebackground=sanMarino, activeforeground=botticelli, bg=blueZodiac, fg=hintOfRed, bd=0, command=enterEitherUSLCW_OR_MMW, width=8, height=2)

    startWindowEnterBtn.pack(side=LEFT, padx=(10, 10))
    startWindowExitBtn = Button(startWindowBtns, text="CLOSE", font=("Lato Bold", 12), activebackground="black", activeforeground=hintOfRed, bg=mirage, fg=hintOfRed, bd=0, command=exitProgram, width=8, height=2)

    startWindowExitBtn.pack(side=RIGHT, padx=(10, 10))
    startWindowBtns.pack(side=BOTTOM, pady=(50, 0))


    groupMemebers_A_Frame.pack(side=TOP, pady=(10, 5))
    groupMemebers_B_Frame.pack(side=BOTTOM, pady=(5, 5))
    startWindowTextFrame.place(relx=.5, rely=.48, anchor=CENTER)


    ' User Account Login/Create Window '
    createWindowToolbar(userAccountLoginCreateWindow)

    userAccountLoginCreateBtn = Button(userAccountLoginCreateWindow, text="LOGIN/CREATE", command=loginUserBasedOnInputs).pack()


    ' Modules Menu '
    createWindowToolbar(modulesMenuWindow)

    modulesMenuWindowScheduleAppointmentBtn = Button(modulesMenuWindow, text="SCHEDULE AN APPOINTMENT", command=enterSchedulingAppointmentsWindow).pack(side=LEFT)
    modulesMenuWindowMakeAReferralBtn = Button(modulesMenuWindow, text="MAKE A REFERRAL", command=enterMakeAReferralWindow).pack(side=LEFT)
    modulesMenuWindowOrderALabBtn = Button(modulesMenuWindow, text="ORDER A LAB", command=enterOrderALabWindow).pack(side=LEFT)
    modulesMenuWindowPatientProviderCommunicationBtn = Button(modulesMenuWindow, text="PATIENT/PROVIDER COMM.", command=enterPatientProviderCommunicationWindow).pack(side=LEFT)


    ' Scheduling An Appointment Window '
    createWindowToolbar(schedulingAppointmentsWindow)



    ' Scheduling An Appointment Window '
    createWindowToolbar(makeAReferralWindow)



    ' Order a Lab Window '
    createWindowToolbar(orderALabWindow)



    ' Patient/Provider Communication Window '
    createWindowToolbar(patientProviderCommunicationWindow)



    # EXIT PROTOCOLS
    for window in windows:
        if window == startWindow:
            window.protocol("WM_DELETE_WINDOW", exitProgram)
        else:
            window.protocol("WM_DELETE_WINDOW", enterStartWindow)

    # Running the program
    startWindow.mainloop()
