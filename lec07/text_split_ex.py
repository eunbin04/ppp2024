def main():
    input_text="5,10,3,4,7"
    tokens=input_text.split(",")
    results=[]
    for token in tokens:
        results.append(int(token))
    print(sum(results))
    print(max(results))

    #results=[int(x) for x in input_text.split(",")]
    print(results)

if __name__=="__main__":
    main()