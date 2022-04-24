# Re

This package allows you to use regex in python.  
I just want to have a place where I can find all the included functions.  


## Compile
#### re.compile(pattern, flags)

Compiles a regular expression pattern into a regular expression object,  
which can be then used for matching using `match`, `search` or other methods.

The expression’s behaviour can be modified by specifying a flags value.  
Values can be any of the ones in my regex file, combined using bitwise OR (the | operator).
```py
prog = re.compile(pattern)
result = prog.match(string)
```

Which is the same as writing, but if you are going to use it several times, then it's better  
to use the other format.
```py
result = re.match(pattern, string)
```

## Search
#### re.search(pattern, string, flags)
Scans through **string** looking for the first location where the regular expression **patterns** produces a match.  
Returns a corresponding match object.  
Returns None if no position in the **string** matches the **patterns**.
  
    
    
## Match
#### re.match(pattern, string, flags)
This only looks for the **pattern** at the beggining of the **string**.
Returns the corresponding match object, or None if the **string** doesn't match.

It doesn't matter if you use a multiline, it only looks for a match at the beggining.
  
    
    
## Fullmatch
#### re.fullmatch(pattern, string, flags)
This finds out wether the whole **string** matches the **pattern**.
Returns the corresponding match object, or None if it doesn't match.
  
    
    
## Split
#### re.split(pattern, string, flags)
This looks for the **pattern** in the **string** and separates it. It will not include the pattern unless it is a group.
Returns a list with the separated words.

```py
re.split(r'\W+', 'word,..word, word,  .word')
```
This will return:
```py
['word', 'word', 'word', 'word']
```
  
    
    
## Findall
#### re.findall(pattern, string, flags)
Returns all non-overlapping matches of **pattern** in **string**, as a list of strings or tuples.  
The string is scanned left-to-right, and matches are returned in the order found.  
Empy matches are included in the result.  
  
    
    
## Sub
#### re.sub(pattern, replacement, string, count, flags)
Returns the string that results from replacing in **string** everywhere it finds the **pattern**, changing each for **replacement**.  
  
    
    
## Subn
#### re.subn(pattern, replacement, string, count, flags)
Does the same thing as `sub` but returns a tuple with the new text and the amount of changes it made.  
(new_text, n_changes)  
  
    
    
## Purge
#### re.purge()
Clear the regular expression cache.
