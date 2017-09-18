class Contact():
	name = ""
	phone = ""
	email = ""
	website = ""
	bday = ""
	linkedin = ""
	picture = ""

	def __init__(self):
		self._name = name
		self._phone = phone
		self._Email = email
		self._website = website
		self._bday = bday
		self._linkedin = linkedin
		self._picture = picture

print('WELCOME ON OUR CONTACT MANAGER \n YOU CAN ENJOY YOURSELF ;-) \n')
print('.: Please enter somme informations about your contact \n')

name = input('=> Enter your contact name :\n')
phone = input('\n=> Enter your contact phone :\n')
email = input('\n=> Enter your contact email :\n')
website = input('\n=> Enter your contact website :\n')
bday = input('\n=> Enter your contact bday :\n')
linkedin = input('\n=> Enter your contact linkedin :\n')
picture = input('\n=> Enter your picture name or link :\n')

print('The detail informations of your contact are :\n')
print('----------------------------------------\n########### CONTACT', name,' #############\n---------------------------------------')
print('\n #Name :', name,'\n #Phone :', phone,'\n #E-mail :', email,'\n #Website :', website,'\n #B-Day :', bday,'\n #Likedin :', linkedin,'\n #Picture :', picture,'\n================(^--^)================')

