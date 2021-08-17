# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")



def encode(l,s):
	if s<0:
		s=26+s
	if ord(l)<91 and ord(l)>64:
		if (ord(l)-64+s)==26:
			return 'Z'
		return chr(64+((ord(l)-64+s)%26))
	elif ord(l)>96 and ord(l)<123 :
		if (ord(l)-96+s)==26:
			return 'z'
		return chr(96+((ord(l)-96+s)%26))
	else:
		return l


def fun_applycaesarcipher(msg, shift):
	stri=""
	for i in msg:
		stri+=encode(i,shift)
	return stri

# print(ord('A'),ord('a'),ord('z'))




