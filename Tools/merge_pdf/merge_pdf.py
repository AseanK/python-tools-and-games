import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from utils import package_installer
package_installer.install_dependencies()

from PyPDF2 import PdfWriter

'''
You have to install PyPDF2
command: pip install PyPDF2
'''

pdf_to_be_merged = [] #this list will contain all the select pdf files to be merged


'''
function openfile
opens a file manager dialog box, helps to select and open files to merged.
'''
def openFile():
    filename = filedialog.askopenfilename(title='Open PDF files', filetypes=[('PDF files', '*.pdf')])
    if filename:
        pdf_to_be_merged.append(filename)
        update_listbox()

'''
listbox will display all the files selected.
'''
def update_listbox():
    filenames_listbox.delete(0, tk.END)
    for pdf in pdf_to_be_merged:
        filenames_listbox.insert(tk.END, pdf)


'''
using move_up and move_down
we can select a pdf and can arrange the order in which it is to be merged.
'''
def move_up():
    selected_index = filenames_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        if selected_index > 0:
            pdf_to_be_merged[selected_index], pdf_to_be_merged[selected_index - 1] = \
                pdf_to_be_merged[selected_index - 1], pdf_to_be_merged[selected_index]
            update_listbox()

def move_down():
    selected_index = filenames_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        if selected_index < len(pdf_to_be_merged) - 1:
            pdf_to_be_merged[selected_index], pdf_to_be_merged[selected_index + 1] = \
                pdf_to_be_merged[selected_index + 1], pdf_to_be_merged[selected_index]
            update_listbox()



'''
merge function uses the list, pdf_to_be_merged and merge pdfs' using pyPDF2
after merging it will open up a file manager dialog box asking filename and location of stroing the merged pdf.
'''

def merge():
    try:
        if not pdf_to_be_merged:
            tk.messagebox.showwarning("No Files", "Please select PDF files to merge.")
            return

        merger = PdfWriter()
        for pdf in pdf_to_be_merged:
            merger.append(pdf)

        output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")],
                                              title="Save Merged PDF As")
        if output:
            with open(output, "wb") as output_file:
                merger.write(output_file)
            tk.messagebox.showinfo("Merge Complete", "PDF files merged successfully.")
        merger.close()
    except Exception as e:
        tk.messagebox.showinfo("Error happened.", f"Error happened please try again : error message - {str(e)}")


'''
reset function clears the pdf_to_merged and update_listbox, thus removing all the selected files.
'''
def reset():
    pdf_to_be_merged.clear()
    update_listbox()



root = tk.Tk()
root.title('PDF Merger')

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")

filenames_label = tk.Label(root, text='Selected PDF files:')
filenames_label.grid(row=0, column=0, columnspan=3, pady=5)

move_up_button = ttk.Button(root, text='Move Up', command=move_up)
move_up_button.grid(row=1, column=0, padx=5)

inputfiles_button = ttk.Button(root, text='Select PDF files', command=openFile)
inputfiles_button.grid(row=1, column=1, padx=5)

move_down_button = ttk.Button(root, text='Move Down', command=move_down)
move_down_button.grid(row=1, column=2, padx=5)

filenames_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=5)
filenames_listbox.grid(row=2, column=0, columnspan=3, pady=5)

mergepdf_button = ttk.Button(root, text='Merge PDF', command=merge)
mergepdf_button.grid(row=3, column=1, padx=10)

reset_button = ttk.Button(root, text='Reset', command=reset)
reset_button.grid(row=4, column=0, padx=5)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.grid(row=4, column=2, padx=5)

root.geometry("400x300") #intital dimensions of tkinter window




root.mainloop()
