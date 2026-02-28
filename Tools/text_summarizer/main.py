import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from utils import package_installer
package_installer.install_dependencies()

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#please run: pip install nltk

import nltk

'''
if running nltk.download using jio wifi( Indian telecom service), please use a VPN or try using hotspot
refer to: https://github.com/nltk/nltk/issues/3140
'''
nltk.download('stopwords')
nltk.download('punkt')


text = ""
summaryx = ""

'''
open file function opens a dialog box, which allows text files to be selected
and data from text file is shown onto the screen.
'''
def openFile():
    global text
    filename = filedialog.askopenfilename(
        title='Open text files', filetypes=[('Text files', '*.txt')])

    with open(filename, 'r') as f:
        text_cur = f.read()

    text += text_cur
    T.delete('1.0', tk.END)
    T.insert(tk.END, text)

'''
reset button flushes out selected text files and currently generated summary.
'''
def reset():
    global text
    global summaryx
    text = ""
    summaryx = ""

    T.delete('1.0', tk.END)
    T_summary.delete('1.0', tk.END)



'''
summary function extracts the summary from the text.
methodology
1. create a word vectors list using word_tokenize from nltk, ignore all stop words.
2. create a sentence vector using sent_tokenize from nltk
3. give a importance value to sentences, by checking occurence of words in sentence.
4. calculate the average importance.
5. dispalyed sentences with higher importance than certain average.
'''
def summary():

    global text
    global summaryx

    stop_words = set(stopwords.words('english'))

    words = word_tokenize(text)

    words_freq = {}

    for word in words:
        if word in stop_words:
            continue
        elif word in words_freq:
            words_freq[word] += 1
        elif word not in words_freq:
            words_freq[word] = 1

    sentences = sent_tokenize(text)

    sentence_value = {}

    for sentence in sentences:
        for wordx, freq in words_freq.items():

            if wordx in sentence.lower():
                sentence_value[sentence] += freq
            else:
                sentence_value[sentence] = freq

    sum_val = 0
    for sentence in sentence_value:
        sum_val += sentence_value[sentence]

    average = sum_val // len(sentence_value)

    for sentence in sentences:
        if sentence in sentence_value and sentence_value[sentence] > (1.2 * average):
            summaryx += " " + sentence

    T_summary.delete('1.0', tk.END)
    T_summary.insert(tk.END, summaryx)


root = tk.Tk()
root.title('Text Summarizer')

# Text widget
T = tk.Text(root, height=20, width=52)
T.insert(tk.END, "Text here!")
T.grid(row=0, column=0, columnspan=3, pady=5, sticky="ew")

# Select Text file button
inputfiles_button = ttk.Button(root, text='Select Text file', command=openFile)
inputfiles_button.grid(row=1, column=0, columnspan=3,
                       padx=6, pady=6, sticky="nsew")

# Reset button
reset_button = ttk.Button(root, text='Reset', command=reset)
reset_button.grid(row=2, column=1, padx=5)

# Generate summary button
generate_summary_button = ttk.Button(
    root, text='Generate summary', command=summary)
generate_summary_button.grid(row=2, column=0, padx=5)

# Text widget for summary
T_summary = tk.Text(root, height=10, width=52)
T_summary.insert(tk.END, "summary......")
T_summary.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")

inputfiles_button = ttk.Button(root, text='Exit', command=root.destroy)
inputfiles_button.grid(row=4, column=0, columnspan=3,
                       padx=6, pady=6, sticky="nsew")

# Make the columns and rows resizable
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

root.mainloop()
