from parseltongue import bionic_reading_html

def main():
    with open('test_text.txt', 'r') as f:
        text = f.read()

    result = bionic_reading_html(text)

    html_content = f"""
    <html>
    <head><title>Parseltongue Output</title></head>
    <body style="font-size: 24px; line-height: 1.6; font-family: Arial, sans-serif;">
    {result}
    </body>
    </html>
    """

    with open('output.html', 'w') as f:
        f.write(html_content)

    print("Output generated in output.html")

if __name__ == '__main__':
    main()
