# Signals from Outer Space

-------------------------------

## Directory Structure

```text
.
├── README.md -- Challenge intrustions 
├── signal.txt -- file containing raw signals. 
└── src
    └── main.py -- code file
```

## The Challenge

It’s finally happened. Earth’s radio waves have reached other sentient creatures far out in the universe, reaching the planet Dyslexia. They have reversed engineered English from our transmissions and have sent us a message of their own, which has been received together with other random space noise.  Unfortunately, the Dyslexians have substituted all the letters of the English language for other letters.  

For example (this is not the substitution, only an example) H to B, E to P, L to Q, O to M, so the word HELLO, would look like BPQQM. Fortunately, they have left spaces intact, so “BPQQM OMNCU” would be “HELLO WORLD”.

As NASA’s finest Pythonist, they have sent the gabled message to your office (a converted broom closet in Nasa’s utility building situated 3KM from the main campus). It is your responsibility to decipher this signal.

+ The Signal (see attachment) contains 64 KB of English uppercase letters and spaces.

+ The message is placed at a random place within the 64KB of text.

+ The length of the message is known, it’s 721 characters long.

+ The message is a substitution cipher encrypted English. The substitutions are stable (1 source letter maps to 1 destination letter).

+ The substitutions mapping is not known.

+ The top 10 English letters in the deciphered text by frequency is: E A T O I R S N H U

Add the first 9 words from the deciphered message to the top of your proposal. You get additional points for describing the process and well (human!) written python source code used to decipher.