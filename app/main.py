import os
from dotenv import load_dotenv

from services.service import QueryService

load_dotenv()


def main():
    print("🤖 AI CONTEXT ENGINE (Mini EricWise) 🤖")
    service = QueryService()
    while True:
        query = input("Enter your query or ('exit') :")
        if query.lower() == "exit":
            break
        response = service.process_query(query)
        if "error" in response:
            print("Error in the response: ", response["error"])
            continue
        print("Summary:", response["summary"])
        print("Dependencies:")
        for dep in response["dependencies"]:
            print("-", dep)

        print("Risks:", response["risks"])


if __name__ == "__main__":
    main()
