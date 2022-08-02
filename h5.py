# 5) Poista tyhjät merkit ainoastaan seuraavan merkkijonon lopusta: "
# Alussa yksi tyhjä, lopussa kolme   ". Liitä merkkijonon perään "!"

# Eng: 5) Remove blanks only from the end of the following string:
# " One blank at the beginning, three " at the end. Append the string with a "!"

# Solution:

str = " One blank at the beginning, three at the end   "
print(str.rstrip() + "!")
