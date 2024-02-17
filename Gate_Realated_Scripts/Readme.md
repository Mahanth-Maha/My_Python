### ResponseSheet.py

GATE 2024 Response sheet is released but its all jumbled, even the options,



So, I worte a script to correct it. this python script even separates Aptitude Questions in (1 - 10) , 1 Marks (11 - 35) and 2 Marks Question (36-65). it also maps the MSQs to the correct options as well.

Usage : save the response as html and pass it to the app.

```
python ResponseSheet.py -f <file_path>
```

Output : it should produce a csv with ordered response in same folder as script, with mapped Options.

this can be used to directly compare with the official key, if released.
