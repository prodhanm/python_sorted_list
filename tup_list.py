students = ("Gino", "Nora", "Talina", "Fanny", "Loretto", "Eric")

def alpha_sort(students):
    for name in sorted(students):
        return list(students)

def main():
    print(alpha_sort(students))

if __name__ == "__main__":
    main()