# README #


# Setup

First download a wordlist. The example I use below uses [this one](http://www-personal.umich.edu/~jlawler/wordlist.html) which you can download from the terminal with:

```bash
wget http://www-personal.umich.edu/~jlawler/wordlist
```

You can use whatever wordlist you want, just make sure you change the ```WORDLIST_FILE``` variable in ```setup.py``` (and if you have a different format to your file, change how it loads in the words).

Then install the dependencies using ```pip```:

```bash
pip install fuzzywuzzy python-Levenshtein
```

# How to use

After you finished the setup, finally run the ```setup.py``` to generate the pickle files.

Then you can test the speed with

```bash
python test_string_matching WORD
```

For example, searching for "pellow":

```bash
python test_string_matching pillow

trying with pillow
checking if it is exactly in list...
not found exactly
trying list look-up took 1.59740447998e-05

searching through entire list...
Top 5 matches:  pillow(200.0)  billow(166.3)  willow(166.3)  pill(160.0)  plow(160.0)
Best match: Pillow
searching through entire list took 1.50267004967

searching through hashed list...
Top 5 matches:  pillow(200.0)  willow(166.3)  billow(166.3)  pill(160.0)  plow(160.0)
Best match: Pillow
searching through hashed list took 0.111702919006
```

Of course the fastest is direct lookup, but in this case "pillow" wasn't in the wordlist (it is actually "Pillow" in the list). Matching through the entire list takes 1.5 seconds, while the hashed version only takes 111 milliseconds! Way beter. The results for both are similar, as well, getting next results that make sense (billow, willow, pill).

What happens if you mispell a word?

```bash
python test_string_matching.py madgascar

trying with madgascar
checking if it is exactly in list...
not found exactly
trying list look-up took 1.50203704834e-05

searching through entire list...
Top 5 matches:  madagascar(189.7)  madagascan(168.2)  marasca(150.0)  mascara(150.0)  alnaschar(133.7)
Best match: Madagascar
searching through entire list took 1.39013600349

searching through hashed list...
Top 5 matches:  madagascar(189.7)  madagascan(168.2)  mascara(150.0)  marasca(150.0)  lascar(133.7)
Best match: Madagascar
searching through hashed list took 0.112021923065
```

Both full list method and the hash method got the right result, but again the hashed version was 14x faster!