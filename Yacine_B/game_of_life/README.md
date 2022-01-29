# Game of Life

It's a cellular automaton.

Just create an initial configuration and observe how it evolves.

More information about the process on [Wikipedia](https://en.wikipedia.org/wiki/Conway's_Game_of_Life).


---

## ⚙️ Technologies employed   
   
\
 **tkinter**
: the standard Python interface to the Tk GUI toolkit.   
\
If not installed yet, run:

- on Linux

```
sudo apt-get install python-tk
```
For python 3 :
```
sudo apt-get install python3-tk
```

- on Windows

```
pip install python-tk
```
For python 3 :
```
pip install python3-tk
```

### ⚠️ Still not working ?
\
The *tkinter* module is not the same depending on your Python version. 

If you get this while running the script:
```
ImportError: No module named 'Tkinter'
```
then try this changes inside the code

| Python 2     | Python 3           |
|--------------|--------------------|
|Tkinter       | tkinter            |
|Tix           | tkinter.tix        |
|ttk           |tkinter.ttk         |
|tkMessageBox  |tkinter.messagebox  |
|tkColorChooser|tkinter.colorchooser|
|tkFileDialog  |tkinter.filedialog  |
|tkCommonDialog|tkinter.commondialog|
|tkSimpleDialog|tkinter.simpledialog|
|tkFont        |tkinter.font        |
|Tkdnd         |tkinter.dnd         |
|ScrolledText  |tkinter.scrolledtext|


---

## 🏷️ License
\
&copy; 2022 Yacine BOUKARI

This application is under MIT License.


Read the [LICENSE](LICENSE) for further details.

