#create Contact class

class Contact(object):
    def __init__(self, first_name, last_name, mobile_number, work_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.email = email
    def add_contact_to_list(self):
        contact_list = []
        for self.info in Contact:
            contact_list.append(self.info)
            return contact_list
    def send_text(self, message):
        print "To: %s - %s" %(self.mobile_number, message)
        # if mobile_number == TRUE:
        #     print "To: %s - %s" %(self.mobile_number, message)
        # else:
        #     print "Please enter a valid mobile number."
#
# eileen = Contact("Eileen", "HS", "1231231234", "1231231234", "e@h.com")
#
# dave = Contact("D", "S", "7777777777", "7777777777", "d@s.com")
#
# print eileen.email
#
# print dave.first_name
# dave.send_text("hi Eileen!")

def main():

eileen = Contact("Eileen", "HS", "1231231234", "1231231234", "e@h.com")
dave = Contact("D", "S", "7777777777", "7777777777", "d@s.com")
chairman = Contact("The Cat", "Esq.", "5555555555", "5555555555", "chairman@cheezborger.com")

print add_contact_to_list

for 
print send_text


if __name__ == '__main__':
    main()
