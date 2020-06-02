# taskcollector

a script to collect tasks from markdown files and write them to a new, collective file.

* **the problem**: you use my great script [wayd](https://github.com/spacekaila/wayd) (or something else that's not as cool), but now you have a markdown file with a ton of thoughts and tasks and it's a pain to separate them all
* **the solution**: use taskcollector! just supply it with your files and (optionally) where you want the new tasks written. taskcollector then parses the files to find your tasks and writes them all to a shiny new, collected file.

## to use
* download `taskcollector.py`
* run `python3 taskcollector.py -flag arg1 arg2 etc`

## notes
* you can run taskcollector with `-t` or no flags
* the `-t` option tells taskcollector that you want it to append your tasks to a previously existing file. taskcollector assumes you want your tasks written to the last file given in the arguments
* no flags tells taskcollector to create a new file and write your tasks there instead
* taskcollector can take (in theory) an unlimited number of files, but can only write to one taskfile (the last argument)

## how it works
taskcollector parses the lines in your given file(s) and looks for lines containing `[ ]` and `[x]`. It collects these lines along with the name of the file. It then either opens your specified task file (specified with the `-t` flag and the file as the last argument) and appends the tasks to it, or creates a new file named `taskcollector_YYYY-MM-DD.md` and writes the tasks there.

## examples
```
python3 taskcollector.py -t daily1.md daily2.md tasks.md
```
This tells taskcollector to look for tasks in `daily1.md` and `daily2.md` and append the tasks to `tasks.md`.

```
python3 taskcollector.py daily1.md daily2.md

```
This tells taskcollector to look for tasks in `daily1.md` and `daily2.md` and write the tasks to `taskcollector_yyyy-mm-dd.md`.

The output looks like this:

># dd.mm.yyyy
>daily1.md
>* [ ] task1
>* [x] task2
>* [ ] task3
>
>daily2.md
>* [x] task4
>* [x] task5
>* [ ] task6
