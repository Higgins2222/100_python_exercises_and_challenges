
# Challenge 50 (Intermediate)
### https://www.reddit.com/r/dailyprogrammer/comments/teu9p/592012_challenge_50_intermediate/
**rya11111**

[5/9/2012] Challenge #50 [intermediate]

Given an absolute path, write a program that outputs an ASCII tree of that directory.

Example output here: HERE

Note: 'tree' utility is not allowed.

Extra credit: Limit the depth of the tree by variable n.

Thanks to jnaranjo for the challenge at r/dailyprogrammer_ideas ... LINK

**Resources**
[https://www.acooke.org/cute/UnixComman0.html]
[https://www.reddit.com/r/dailyprogrammer_ideas/]
[https://www.reddit.com/r/dailyprogrammer_ideas/comments/sbu4b/easy_generate_directory_tree_maps/]

**Solutions**

u/brbpizzatime
```c
#include <stdio.h>
#include <fts.h>
#include <string.h>

int main(int argc, char **argv) {
    FTS *dir = fts_open(argv + 1,  FTS_NOCHDIR, 0);
    FTSENT *file;
    while ((file = fts_read(dir))) {
        if (file->fts_info & FTS_F && file->fts_name[0] != '.') {
            printf("%s\n", file->fts_path);
        }
    }
    fts_close(dir);
    return 0;
}
```

u/kuzux
```haskell
import System.Directory (getDirectoryContents, doesDirectoryExist)
import System.FilePath ((</>), takeFileName, splitPath)
import System.Environment (getArgs)

data Entry = File FilePath
           | Directory FilePath [Entry]

showEntry :: Int -> Entry -> String
showEntry indent (File name) = (replicate indent ' ') ++ "+-" ++ name
showEntry indent (Directory name children) = (init . unlines) $ ((replicate indent ' ') ++ "+-" ++ name):(map (showEntry (indent+2)) children)

readDirectory :: FilePath -> IO Entry
readDirectory top = do isDir <- doesDirectoryExist top
                       if isDir then do
                           names <- getDirectoryContents top
                           let properNames = filter (`notElem` [".", ".."]) names
                           children <- mapM (\n -> readDirectory $ top</>n) properNames
                           return $ Directory (last . splitPath $ top) children
                        else return $ File (takeFileName top)

main :: IO()
main = do
    args <- getArgs
    if (null args) then error "pass directory path as argument"
        else do entry <- readDirectory (head args)
                putStrLn $ showEntry 0 entry
```

github\Higgins2222
```python
import os

dirs = os.scandir(path='..\\..\\')

def fetch_dirs(a):
    result = []

    for e in a:
        try:
            # Skip System Volume Information
            if e.name.startswith('System Volume Information'):
                continue
            # Skip these, recycle bin stuff
            if e.name.startswith('$'):
                continue
            # Append direntry to our return result and append a list of all subdirs, empty list if none exist
            # Don't follow symlinks, can cause inf loop
            if e.is_dir(follow_symlinks=False):
                result.append(e)
                result.append(fetch_dirs(os.scandir(e.path)))
        except PermissionError:
            # Skip directories that raise a permission error
            print(f"Permission denied: {e.path}")
        except FileNotFoundError:
            # Skip directories that no longer exist
            print(f"File not found: {e.path}")
    return result

def print_dirs(result, lvl=0):
    for e in result:
        if isinstance(e, os.DirEntry):
            if lvl == 0:
                print('\n', e.name)
            print(('  '+'--'*lvl)+':\\', end='')
            print(e.name)
        else:
            print_dirs(e, lvl+1)

result = fetch_dirs(dirs)
print_dirs(result)
```


u\theOnliest
```perl
use File::Find;

my $dir = $ARGV[0] ? shift @ARGV : '.';
my $slashBase = 0;
$slashBase++ while ($dir =~ m!/!g);
$slashBase = 1 if ($slashBase == 0);

find(\&wanted, $dir);

sub wanted {
  my $file = $File::Find::name;
  my $numSlash = 0;
  $numSlash++ while ($file =~ m!/!g);

  $file =~ s!.*/!!;
  $file = "|     "x($numSlash-$slashBase) . "|--$file";

  $numSlash ? print "$file\n" : print ".\n";
}
```

# Challenge 48 (Intermediate)
### reddit.com/r/dailyprogrammer/comments/t78lv/542012_challenge_48_intermediate/

[5/4/2012] Challenge #48 [intermediate]

Your task is to write a program that implements the Trabb Pardo Knuth algorithm.


**resources**
https://en.wikipedia.org/wiki/TPK_algorithm


```python
from math import sqrt
import random

def formula(x):
    return sqrt(abs(x)) + (5 * (x ** 3))

# Randomly generate 11 numbers
prompt = [round(random.random()*10, 2) for _ in range(0,11)]

# Iterate over the randomly generated numbers of prompt in reverse
for i, e in enumerate(prompt[::-1]):
    a = formula(e)
    print(f'({10 - i}, {a if a <= 400 else "TOO LARGE"})')
```

u/emcoffey3
```C#
  private static double F(double x)
  {
      return Math.Sqrt(Math.Abs(x)) + (5 * x * x * x);
  }
  public static void TPK()
  {
      double[] S = new double[11];
      for (int i = 0; i < S.Length; i++)
      {
          Console.Write("Please enter a number: ");
          if (!Double.TryParse(Console.ReadLine(), out S[i]))
              throw new IOException("Invalid user input. Please provide a number.");
      }
      S.Reverse().ToList().ForEach((x) =>
      {
          double y = F(x);
          Console.WriteLine("{0}", y > 400 ? "TOO LARGE" : y.ToString());
      });
  }
```

```rust
use std::{io, iter::zip};

fn f(t: f64) -> Option<f64> {
    let y = t.abs().sqrt() + 5.0 * t.powi(3);
    (y <= 400.0).then_some(y)
}

fn main() {
    let mut a = [0f64; 11];
    for (t, input) in zip(&mut a, io::stdin().lines()) {
        *t = input.unwrap().parse().unwrap();
    }

    a.iter().enumerate().rev().for_each(|(i, &t)| match f(t) {
        None => println!("{i} TOO LARGE"),
        Some(y) => println!("{i} {y}"),
    });
}
```

 # challenge #3 [difficult]
### https://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/
**u/nottoobadguy**

Welcome to cipher day!

For this challenge, you need to write a program that will take the scrambled words from this post, and compare them against THIS WORD LIST to unscramble them. For bonus points, sort the words by length when you are finished. Post your programs and/or subroutines!

Here are your words to de-scramble:

mkeart

sleewa

edcudls

iragoge

usrlsle

nalraoci

nsdeuto

amrhat

inknsy

iferkna

**Resources**
Word List: https://pastebin.com/jSD873gL

Check the timing of the one below, seems like it shouldn't be so bad, 6x worse than my first version (below that).

```python
import cProfile

WORDS_FILE = 'wordlist.txt'
WORD_COUNT = 0
WORDLIST_COUNT = 0
CHAR_COUNT = 0
INNER_COUNT = 0

def descramble(scrambled_word, wordlist):
    result = ''
    target_len = len(scrambled_word)
    global WORD_COUNT
    global WORDLIST_COUNT
    global CHAR_COUNT
    global INNER_COUNT

    WORD_COUNT += 1
    for word in wordlist:
        WORDLIST_COUNT += 1
        target = [0 for x in range(len(scrambled_word))]
        i = 0
        for c in scrambled_word:
            CHAR_COUNT += 1
            li = [(index, e) for index, e in enumerate(word) if index+1 not in [x for x in target]]
            for index, char in li:
                INNER_COUNT += 1
                # print(f'{index=} {char=} {c=}')
                if c == char:
                    target[i] = index+1
                    i += 1
                    break
                else:
                    continue
            else:
                break
        else:
            result = word
            break
    return result

def main():
    wordlist = []
    with open(WORDS_FILE, 'r') as file:
        for line in file:
            wordlist.append(line.strip())

    # print(wordlist)
    # 0g 1e 2o 3r 4g 5i 6a
    prompt = ['iragoge','iferkna','nsdeuto','sleewa','edcudls','mkeart','usrlsle','nalraoci','amrhat','inknsy']
    for word in prompt:

        print(descramble(word, wordlist))
    print(WORD_COUNT)
    print(WORDLIST_COUNT)
    print(CHAR_COUNT)
    print(INNER_COUNT)

cProfile.run('main()')
```

23687 function calls in 0.073 seconds

```python
WORDS_FILE = 'wordlist.txt'

def descramble(scrambled_word, wordlist):
    result = ''
    target_len = len(scrambled_word)
    for word in wordlist:
        if len(word) != target_len:
            continue
        test = list(word)
        for c in scrambled_word:
            if c in test:
                test.remove(c)
            else:
                break
        else:
            result = word

    return result

def main():
    wordlist = []
    with open(WORDS_FILE, 'r') as file:
        for line in file:
            wordlist.append(line.strip())

    # print(wordlist)
    prompt = ['iragoge','iferkna','nsdeuto','sleewa','edcudls','mkeart','usrlsle','nalraoci','amrhat','inknsy']
    for word in prompt:
        print(descramble(word, wordlist))
```

18021 function calls in 0.010 seconds

# Question 3 (Easy)
### reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
**u/nottoobadguy**

Welcome to cipher day!

write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore numbers, symbols, and whitespace.

for extra credit, add a "decrypt" function to your program!

**Resources**

The Caesar cipher is a type of substitution cipher, which means it substitutes one letter for another in a consistent fashion. It's one of the earliest known approaches to symmetric key cryptography. 
A common variation of the Caesar cipher is ROT13, which moves each letter of the alphabet 13 spots forward. ROT13 is convenient because applying another round of encryption with ROT13 also functions as decryption. 
The Caesar cipher is not widely used today because it is easy to break. Arab mathematician Al-Kindi broke the Caesar cipher using frequency analysis, which exploits patterns in letter frequencies. 

u/Higgins2222
```python
def shift_alpha(char, n):
    # Shifts an alpha char (+/-)n spaces forward in the alphabet, rotational
    # ord('a')=97, ord('b')=122
    value = ord(char.lower())
    if value < 97 or value > 122:
        return char
    return chr((value - 97 + n) % 26 + 97)

def ceaser_cipher(message, n=13):
    # Shift all letters in message n spaces
    result = []
    for c in message:
        result.append(shift_alpha(c, n))

    return ''.join([str(x) for x in result])

def ceaser_decrypt(coded_message, n=13):
    return ceaser_cipher(coded_message, -n)
```

```python
def rot13(text):
    """Encodes/decodes a string using ROT13 cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            char = chr(((ord(char) - base + 13) % 26) + base)
        result += char
    return result

text = "Hello, World!"
encoded = rot13(text)
print(encoded)  # Uryyb, Jbeyq!
decoded = rot13(encoded)
print(decoded)  # Hello, World!
```

u/Duncans_pumpkin
```c
for( char i; cin>>i; cout<<(char)((i-'@')%26+'A'));
```

u/gitah
```python
def rot_char(c,d):
    num = ord(c)
    if num >= ord('a') and num <= ord('z'):
        return chr(ord('a') + (num-ord('a')+d)%26)
    if num >= ord('A') and num <= ord('Z'):
        return chr(ord('A') + (num-ord('Z')+d)%26)
    return c

def rot(msg,d=13):
    """Preforms a rotational cipher on a message
        
       msg - the message to encrypt
       d - rotation size, 13 by default
    """
    arr = list(msg)
    for i,c in enumerate(arr):
        arr[i] = rot_char(c,d)
    return ''.join(arr)
```

u/garslo
```lisp
(defun encrypt (contents shift)
  (let ((contents-list (coerce contents 'list)))
    (concatenate 'string (mapcar #'(lambda (x) (code-char (+ shift (char-int x))))
                                 contents-list))))

(defun decrypt (contents shift)
  (encrypt contents (- shift)))

(decrypt (encrypt "My secret message" 4) 4) ; => "My secret message"
```

u/iostream3
```bash
echo str_rot13(fgets(STDIN));
```

```php
 <?php
echo str_rot13("Hello World");
echo "<br>";
echo str_rot13("Uryyb Jbeyq");
?> 
```

# Question 2
### reddit.com/r/dailyprogrammer/comments/pjbj8/easy_challenge_2/
**u/nottoobadguy**


Hello, coders! An important part of programming is being able to apply your programs, so your challenge for today is to create a calculator application that has use in your life. It might be an interest calculator, or it might be something that you can use in the classroom. For example, if you were in physics class, you might want to make a F = M * A calc.

EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!

**Resources**

**Solutions**

Solution: Python Force Calculator
github/Higgins2222
```python
def force_eq(force='', mass='', accel=''):
  # Returns (force, mass, accel) as a tuple if one of the params in left blank)
  # print(f'{force if force else '_'} {mass if mass else '_'} {accel if accel else '_'}')
  if mass and accel:
    return (mass*accel, mass, accel)
  elif force and mass:
    return (force, mass, force / mass)
  elif force and accel:
    return (force, force / accel, mass)
  else:
    return None
  return (force, mass, accel)

force = input('Enter force or leave blank to solve for force: ')
mass = input('Enter mass or leave blank to solve for mass: ')
accel = input('Enter accel or leave blank to solve for accel: ')
force = float(force) if force else ''
mass = float(mass) if mass else ''
accel = float(accel) if accel else ''
result = force_eq(force, mass, accel)
print(f'F={result[0]}, M={result[1]}, A={result[2]}')
```

Solution: Simple and Compound interest
u/InterestProgram
```python
def simpleInterest(capital, interestRate, time):
        answer = (capital * interestRate * time) / 100
        print(answer)

def compoundInterest(capital, interestRate, time):
        answer = capital * pow(1 + (interestRate / 100), time)
        print(answer)

print("1) Simple Interest")
print("2) Compound interest (annual)")
selection = input("Select 1 or 2: ")

if selection == "1" or selection == "simple interest":
    capital = float(input("Capital: "))
    interestRate = float(input("Interest rate (%): "))
    time = float(input("Time (years): "))
    
    simpleInterest(capital, interestRate, time)
elif selection == "2" or selection == "compound interest":
    capital = float(input("Capital: "))
    interestRate = float(input("Interest rate (%): "))
    time = float(input("Time (years): "))
    
    compoundInterest(capital, interestRate, time)
else:
    print("I didn't understand you!")
```

Solution: UTM Zone Locator
No Author
```python
import string

def long_to_utm(degrees):
    if degrees < -180 or degrees > 180:
        raise ValueError("Longitude out of bounds!")
    return int((degrees + 180) / 6) + 1
    
def lat_to_utm(degrees):
    char_list = string.ascii_uppercase[2:-2].replace('I', '').replace('O', '')
    if degrees < -90 or degrees > 90:
        raise ValueError("Latitude out of bounds!")
    if degrees < -80 or degrees >= 84:
        raise NotImplementedError("Have fun with polar coordinate systems!")
    if degrees >= 72:
        return 'X'
    return char_list[int((degrees + 80) / 8)]
    
def latlong_to_utm(latitude, longitude):
    zone = long_to_utm(longitude)
    band = lat_to_utm(latitude)
    # exception for Norway because Norway is silly
    if str(zone) + band == '31V' and longitude >= 3:
        zone = 32
    # exceptions for Svalbard (also owned by Norway, thus supporting the above assertion)
    if band == 'X' and zone in (32, 34, 36):
        if latitude < 9:
            zone = 31
        elif latitude < 21:
            zone = 33
        elif latitude < 33:
            zone = 35
        else:
            zone = 37
    return str(zone) + band
    
if __name__ == '__main__':
    while True:
        latitude = float(input("Enter latitude (N/S): "))
        longitude = float(input("Enter longitude (E/W): "))
        print("UTM Zone: %s" % latlong_to_utm(latitude, longitude))
```

Solution: Recipe Scaling Calculator!
```python
def recipe_calculator():
    print("Welcome to the Recipe Scaling Calculator!")
    print("1: Scale a recipe by a factor")
    print("2: Calculate ingredient quantities for a specific yield")
    print("3: Reverse calculate a recipe's scale factor")
    print("4: Quit")

    while True:
        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            base_yield = float(input("Enter the original yield of the recipe (e.g., servings): "))
            desired_yield = float(input("Enter the desired yield: "))
            factor = desired_yield / base_yield
            print(f"\nScale Factor: {factor:.2f}")
        
        elif choice == "2":
            base_amount = float(input("Enter the ingredient amount (e.g., cups, grams): "))
            scale_factor = float(input("Enter the scale factor: "))
            scaled_amount = base_amount * scale_factor
            print(f"\nScaled Ingredient Amount: {scaled_amount:.2f}")
        
        elif choice == "3":
            scaled_yield = float(input("Enter the scaled recipe yield: "))
            original_yield = float(input("Enter the original recipe yield: "))
            reverse_factor = scaled_yield / original_yield
            print(f"\nReverse Scale Factor: {reverse_factor:.2f}")
        
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

recipe_calculator()
```

Solution: Ideal Gas law calculator!
No Author
```java
import java.util.Scanner;


public class Driver {
  public static void main(String[] args){
    float R = 8.3145f;
    float n, v, t, p;
    String answer, units;
    
    Scanner scan = new Scanner(System.in);
    
    System.out.println("Ideal Gas law calculator!");
    System.out.println("What do you want to solve for? Moles = n, Volume = v, Temperature = t, Pressure = p");
    
    answer = scan.nextLine();
    
    if(answer.equalsIgnoreCase("n")){
      
      System.out.println("What is the volume?");
      v = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (mL or L only)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("ml")){
        v = v/1000;
      }
      
      System.out.println("What is the Temperature?");
      t = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (C or K only)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("C")){
        t = t + 273;
      }
      
      System.out.println("What is the Pressure?");
      p = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (kPa, Pa, mmHG, or atm)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("kPa")){
        p = (float) (p / 101.325);
      }
      else if(units.equalsIgnoreCase("Pa")){
        p = (float) (p / 101325);
      }
      else if(units.equalsIgnoreCase("mmHg")){
        p = (float) (p / 760);
      }
      
      n = (p*v)/(R*t);
      
      System.out.println("There are " + n + " moles!");
      
      
    }
    else if(answer.equalsIgnoreCase("v")){
      
      System.out.println("How many moles? (No scientific notation!)");
      n = Float.parseFloat(scan.nextLine());
      
      System.out.println("What is the Temperature?");
      t = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (C or K only)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("C")){
        t = t + 273;
      }
      
      System.out.println("What is the Pressure?");
      p = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (kPa, Pa, mmHG, or atm)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("kPa")){
        p = (float) (p / 101.325);
      }
      else if(units.equalsIgnoreCase("Pa")){
        p = (float) (p / 101325);
      }
      else if(units.equalsIgnoreCase("mmHg")){
        p = (float) (p / 760);
      }
      
      v = (n*R*t) / p;
      System.out.println("There are " + v + " Liters!");
      
    }
    else if(answer.equalsIgnoreCase("t")){
      
      System.out.println("How many moles? (No scientific notation!)");
      n = Float.parseFloat(scan.nextLine());
      
      System.out.println("What is the volume?");
      v = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (mL or L only)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("ml")){
        v = v/1000;
      }
      
      System.out.println("What is the Pressure?");
      p = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (kPa, Pa, mmHG, or atm)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("kPa")){
        p = (float) (p / 101.325);
      }
      else if(units.equalsIgnoreCase("Pa")){
        p = (float) (p / 101325);
      }
      else if(units.equalsIgnoreCase("mmHg")){
        p = (float) (p / 760);
      }
      
      t = ((p*v)/(n*R)) - 273;
      System.out.println("The temp is " + t + " degrees C!");
      
    }
    else if(answer.equalsIgnoreCase("p")){
      
      System.out.println("How many moles? (No scientific notation!)");
      n = Float.parseFloat(scan.nextLine());
      
      System.out.println("What is the volume?");
      v = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (mL or L only)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("ml")){
        v = v/1000;
      }
      
      System.out.println("What is the Temperature?");
      t = Float.parseFloat(scan.nextLine());
      
      System.out.println("What units are these in? (C or K only)");
      units = scan.nextLine();
      if(units.equalsIgnoreCase("C")){
        t = t + 273;
      }
      
      p = (n*R*t)/(v);
      System.out.println("The pressure is " + t + " atm!");
      
    }
    else{
      System.out.println("Invalid Entry. =[");
      
    }
  }
}
```

**Ideas**

*Meal Cost Breakdown Calculator*

**Purpose:** Calculate the cost of preparing a meal, including portioning per serving.
**Functions:**
Input the cost of ingredients and their quantities.
Divide the total cost by the number of servings to get cost-per-serving.
Optionally include labor and energy costs to calculate a full cost breakdown.


*Line Cook Workflow Timer*

**Purpose:** Help line cooks time multiple tasks to optimize prep and cooking processes.
**Functions:**
Set and start multiple timers for different tasks (e.g., boiling, chopping, frying).
Display timers in a dashboard, updating in real-time.
Alert the user when a timer finishes, with optional preparation steps displayed.

*Inventory Cost Calculator with Depreciation*

**Purpose:** Tracks the cost of inventory over time, accounting for depreciation (e.g., in a kitchen, ingredients like oils or spices may lose value if not used).
**Functions:**
Calculate the remaining value of inventory over a period of time using a depreciation rate.
Allow entry of new purchases and automatically update the total inventory value.
Forecast the date when inventory will reach a minimum value (e.g., when it’s no longer worth keeping).