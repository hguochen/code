class PhoneNumber(object):
    """PhonNumber class is collection of name, phone_number key value stores"""
    def __init__(self, table={}):
        super(PhoneNumber, self).__init__()
        self.table = table
        
    def insert(self, name, number):
        if name in self.table:
            print "Element already exists."
            return
        self.table[name] = number
        return

    def delete(self, name):
        del self.table[name]
        return

    def find(self, name):
        return self.table[name]

    def print_numbers(self):
        if not self.table:
            return
        for name, number in self.table.iteritems():
            print name, number
        print ""
        return


def main():
    numbers = PhoneNumber()
    numbers.insert('gary', '1235678900')
    numbers.insert('roger', '53675473627')
    numbers.insert('david', '34576584572')
    numbers.print_numbers()

if __name__ == '__main__':
    main()