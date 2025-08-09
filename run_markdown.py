from reader import bionic_reading

def main():
    with open('test_text.txt', 'r') as f:
        text = f.read()
    result = bionic_reading(text)
    print(result)

if __name__ == '__main__':
    main()
