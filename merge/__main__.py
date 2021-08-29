from tkinter import Tk, messagebox ,simpledialog  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def Merge():

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

    # set file name 
    outfilenameext = simpledialog.askstring("Filename", 'Choose a filename') + '.tap'
    # set Job name
    jobnamef = "(" + simpledialog.askstring("JobName", 'Choose a Jobname') + ")"

    filenames =[] # Creating a blank list for filenames

    finished = 0 # create finished indicator to create file selection loop

    while finished == 0:
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        print(filename)
        if filename != '':
            filenames.append(filename)
        else:
            a=1
        MsgBox = messagebox.askquestion ('More files','Do you want to merge any more files?',icon = 'warning')
        print(MsgBox)
        if MsgBox == 'yes':
            a=1
        else:
            finished = 1
        

    # Create and Open outfilenameext in write mode and add job name then tooling and gcode from each file


    with open(outfilenameext, 'w') as outfile:
        
        outfile.write(jobnamef)
        outfile.write("\n")

        for names in filenames:
            # Open each file in read mode identify tooling lines and append outfilenameext
            with open(names) as infile:
                Toolfinder = infile.readlines()
                tool = Toolfinder[4]
                outfile.write(tool)

        with open(filenames[1]) as infile:
            lines = infile.readlines()
            lines2 = lines[5:7]
            lines3 = lines[11:13]
            for line in lines2:
                outfile.write(line)
            for line in lines3:
                outfile.write(line)

        for names in filenames:
            with open(names) as infile:
                lines = infile.readlines()
                Counter = len(lines)
                delstart = Counter-6
                del lines[delstart:Counter]
                del lines[0:13]
                for line in lines:
                    outfile.write(line)

            outfile.write("\n")

        outfile.write('M30')

    print ("file: ", outfilenameext, " created.")
  