# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def count_self_murderers(n, beauty, intellect, richness):
    ladies = list(zip(beauty, intellect, richness))
    
    count = 0
    for i in range(n):
        is_self_murderer = False
        for j in range(n):
            if (ladies[j][0] > ladies[i][0] and 
                ladies[j][1] > ladies[i][1] and 
                ladies[j][2] > ladies[i][2]):
                is_self_murderer = True
                break
        if is_self_murderer:
            count += 1
            
    return count

def main():
    n = int(input())
    beauty = list(map(int, input().split()))
    intellect = list(map(int, input().split()))
    richness = list(map(int, input().split()))
    
    result = count_self_murderers(n, beauty, intellect, richness)
    print(result)

if __name__ == "__main__":
    main()