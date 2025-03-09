def convert_to_plural(singular):
    if singular.endswith("us"):
        return singular[:-2] + "i"
    return singular

def main():
    t = int(input().strip())
    results = []
    
    for _ in range(t):
        singular = input().strip()
        plural = convert_to_plural(singular)
        results.append(plural)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()