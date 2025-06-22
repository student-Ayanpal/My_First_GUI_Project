import tkinter as tk 
from tkinter import messagebox
window=tk.Tk()
window.title("Mini project")
window.configure(bg="red")
def Input_Sentence():
    text="Enter the Sentence"
    sentence=T1.get("1.0","end-1c").strip()
    global sentence_list
    sentence_list=sentence.split()
    if  len(sentence_list)==0 or sentence==text:
       messagebox.showwarning("Missing Sentence", "Please enter a sentence in the first box.")
       return
def Input_word():
    text1="Enter one word which is present in the sentence"
    word=T2.get("1.0","end-1c").strip()
    global word_list
    word_list=word.split()
    if len(word_list)==0 or word==text1:
       messagebox.showwarning("Missing Word", "Please enter a word to remove in the second box.")
       return
    if len(word_list)>1:
       messagebox.showwarning("Multiple word","please enter a single word")
       return


def Show_Output():
    Input_Sentence()
    Input_word()
    word=word_list[0]
    if word not in sentence_list:
       messagebox.showwarning("Word Not Found", f"The word '{word}' was not found in the sentence.")
       return
   
    new_sentence=[]
    for i in range(len(sentence_list)):
        if sentence_list[i]!=word:
            new_sentence.append(sentence_list[i])
            
    T3.config(state=tk.NORMAL)
    T3.delete("1.0","end")
    T3.insert("1.0"," ".join(new_sentence))
    T3.config(state=tk.DISABLED)

def Clear_all():
    text="Enter the Sentence"
    T1.delete("1.0","end")
    T1.insert("1.0",text)
    
    text1="Enter one word which is present in the sentence"
    T2.delete("1.0","end")
    T2.insert("1.0",text1)
    
    text2="Output"
    T3.config(state=tk.NORMAL)
    T3.delete("1.0","end")
    T3.insert("1.0",text2)
    T3.config(state=tk.DISABLED)

def clear_on_click_t1(event):
    if T1.get("1.0", "end-1c") == text:
        T1.delete("1.0", "end")

def clear_on_click_t2(event):
    if T2.get("1.0", "end-1c") == text1:
        T2.delete("1.0", "end")

T1=tk.Text(window,height=5,width=50)
T1.pack(padx=50,pady=20)
text="Enter the Sentence"
T1.insert("1.0",text)

button1=tk.Button(window,text="Input Sentence",command=Input_Sentence)
button1.pack(padx=10,pady=20)


T2=tk.Text(window,height=5,width=50)
T2.pack(padx=50,pady=20)
text1="Enter one word which is present in the sentence"
T2.insert("1.0",text1)

button2=tk.Button(window,text="Input Word",command=Input_word)
button2.pack(padx=10,pady=20)


T3=tk.Text(window,height=5,width=50)
T3.pack(padx=50,pady=20)
text2="Output"
T3.insert("1.0",text2)
T3.config(state=tk.DISABLED)

T1.bind("<FocusIn>", clear_on_click_t1)
T2.bind("<FocusIn>", clear_on_click_t2)

button=tk.Button(window,text="Show Output",command=Show_Output)
button.pack(padx=10,pady=20)

clear_all_button=tk.Button(window,text="Clear All",command=Clear_all)
clear_all_button.pack(padx=10,pady=5)

Exit_button=tk.Button(window,text="Exit",command=window.destroy)
Exit_button.pack(side="bottom",pady=20)

window.mainloop()