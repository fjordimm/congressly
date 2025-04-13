from congressQuery import get_bills
from supabaseInsert import send_bills

def main():
    bills = get_bills(1000)
    print(bills)
    send_bills(bills)

if __name__ == '__main__':
    main()
