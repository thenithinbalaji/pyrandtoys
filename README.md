<h1 align = "center">PyRandToys</h1></center>

<p align = "center">

  <a href = "https://github.com/thenithinbalaji/pyrandtoys/releases">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/thenithinbalaji/pyrandtoys?color=blueviolet">
  </a>

  <a href = "https://github.com/thenithinbalaji/pyrandtoys/releases">
<img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/thenithinbalaji/pyrandtoys?color=blue">
  </a>

  <a href = "https://github.com/thenithinbalaji/pyrandtoys">
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/thenithinbalaji/pyrandtoys?color=red">
  </a>
  
<br>

  <a href = "https://github.com/thenithinbalaji/pyrandtoys/graphs/contributors">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/thenithinbalaji/pyrandtoys?color=ff69b4"> 
  </a>

  <a href = "https://github.com/thenithinbalaji/pyrandtoys/issues?q=is%3Aissue+is%3Aclosed">
<img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/thenithinbalaji/pyrandtoys?color=success">
  </a>

  <a href = "https://github.com/thenithinbalaji/pyrandtoys/blob/main/LICENSE.md">
<img alt="License" src="https://img.shields.io/github/license/thenithinbalaji/pyrandtoys"> 
  </a>
  
<br>
<code> pyrandtoys</code> is a python module containing probability-based toys' functions. <br> It works offline and is compatible with both Python 2 and 3. 

</p>

### 🔮 Installation

``` 
pip install pyrandtoys
```

### 🖥️ Usage

```
import pyrandtoys
print(pyrandtoys.coin()) #there are many other toys in pyrandtoys similar to coin, check below
```
## List of functions available in pyrandtoys module

### 🎲 Dice

**Optional:** Number of Dice `<int>`   
**Default:** Number of Dice = 1   
**Return Type:** `<tuple>`   
```
dice(number_of_dice)
```

### 🏆 Coin

**Optional:** Number of Coins `<int>`    
**Default:** Number of Coins = 1    
**Return Type:** `<tuple>`    
```
coin(number_of_coins)
```

### 🃏 Card
**Optional:** Number of Cards `<int>`    
**Default:** Number of Cards = 1    
**Return Type:** `<tuple>`    
```
card(number_of_cards)
```

### 🧮 Similar Toys

**Optional:** Number of Items `<int>`    
**Default:** Number of Items = 1    
**Return Type:** `<tuple>`    
```
dreidel(number_of_dreis)
cat(number_of_cats)
switch(number_of_switches)
```

### ⚖️ Spinner

**Required:** Lower & Upper Limits `<int>`    
**Default:** Lower Limit = 0    
**Return Type:** `<tuple>`    
```
spinner(lowerLimit, upperLimit) 
```

### 🥂 Toy Combinations
**Return Type:** `<tuple>`      
**Default:** Number of Toys = 0     
<br>
**If you want to use a combination of toys then,**        
**Required:** List of toys as `<list>`,`<tuple>`        
```
combi(("switch", "cat", "dice"))
combi(["dreidel", "coin", "coin", "cat"])
```

**For combination of x random toys,**    

```
combi(x)
```

### 📚 Project Links

+ PyPI [(https://pypi.org/project/pyrandtoys/)](https://pypi.org/project/pyrandtoys/)
+ GitHub [(https://github.com/thenithinbalaji/pyrandtoys)](https://github.com/thenithinbalaji/pyrandtoys)
