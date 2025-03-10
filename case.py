import json
import os

def load_file():
    if os.path.exists("case.json"):
        with open("case.json","r") as file:
            return json.load(file)

def write_file(cases):
    with open("case.json","w") as file:
        json.dump(cases,file)

def view_all_cases(cases):
    if not cases:
        print("not cases found")
    else:
        for case_id,case_details in cases.items():
            print(f"Case ID : {case_id}")
            print(f"Title: {case_details['Title']}")
            print(f"Suspect:{', '.join(case_details['Suspects']) if case_details['Suspects'] else 'None'}")
            print(f"Status: {case_details['Status']}")
            
def add_new_case(cases):
    case_id = input()
    if case_id in cases:
        print("already exist")
        return
    title = input()
    suspects = input("coma sperated").split(",")
    status = input()
    cases[case_id] = {
        "Title" : title,
        "Suspects" : suspects,
        "Status" : status
    }
    write_file(cases)
    print("case added")

def update_case_status(cases):
    case_id = input()
    if case_id not in cases:
        print("not found")
        return
    new_status = input()
    cases[case_id]["Status"] = new_status
    write_file(cases)
    print("status updated")

def add_suspect(cases):
    case_id = input()
    if case_id not in cases:
        print("not found")
        return
    suspects = input().split(",")
    current_suspects = cases[case_id]["Suspects"]
    for suspect in suspects:
        if suspect in current_suspects:
            print("already exist")
            return
        cases[case_id]["Suspects"].append(suspects)
    write_file(cases)
    print("suspect added")

def remove_suspect(cases):
    case_id = input()
    if case_id not in cases:
        print("not found")
        return
    suspects = input().split(",")
    for suspect in suspects:
        if suspect not in cases[case_id]["Suspects"]:
            print("not found")
            return
        cases[case_id]["Suspects"].remove(suspect)
    write_file(cases)
    print("suspect removed")

def search_case(cases):
    case_id = input()
    if case_id not in cases:
        print("not found")
        return
    view_all_cases({case_id:cases[case_id]})

def search_open_cases(cases):
    # for case_id in cases:
    #     if cases[case_id]["Status"] == "open":
    #         view_all_cases({case_id:cases[case_id]})
    open_cases = {case_id:case_details for case_id,case_details in cases.items() if case_details["Status"] == "Open"}
    view_all_cases(open_cases)

def delete_case(cases):
    case_id = input()
    if case_id not in cases:
        print("not found")
        return
    del cases[case_id]
    write_file(cases)
    print("case deleted")

def find_case_by_suspect(cases):
    suspect = input()
    cases_with_suspect = {case_id:case_details for case_id,case_details in cases.items() if suspect in case_details["Suspects"]}
    view_all_cases(cases_with_suspect)

def main():
    cases = load_file()
    while True:
        choice = input()
        if choice == "1":
            view_all_cases(cases)
        elif choice == "2":
            add_new_case(cases)
        elif choice == "3":
            update_case_status(cases)
        elif choice == "4":
            add_suspect(cases)
        elif choice == "5":
            remove_suspect(cases)
        elif choice == "6":
            search_case(cases)
        elif choice == "7":
            search_open_cases(cases)
        elif choice == "8":
            delete_case(cases)
        elif choice == "9":
            find_case_by_suspect(cases)
        else:
            break
        
if __name__ == "__main__":
    main()