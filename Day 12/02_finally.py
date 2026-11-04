# finally block

def main():
    try:
        number = int(input('Enter a number please   :   '))
        print('The number is ',number)
    except Exception as e:
        print(e)
        return
# it will execute even when the function returns 
    finally:
        print('Inside the finally block')

main()