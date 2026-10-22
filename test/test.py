import requests

banner = """TechDesk v1.0

[1] Create Ticket
[2] Update Ticket
[3] Search Ticket
[4] Exit
"""

host = "127.0.0.1:8000"

def main():
    print(banner)
    choose = str(input("Choose an option: "))

    if choose == "1":
        subject = "This is a subject."
        message = "This is a message."

        url = f"http://{host}/ticket/create?subject={subject}&message={message}"
        res = requests.post(url)
        print(res.json())


    if choose == "3":
        res = requests.get("http://127.0.0.1:8000/ticket")
        print(res.json())

main()