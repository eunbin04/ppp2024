class Cake:
    coat = "생크림"

    def __init__(self, topping, price, candles=0):
        self.topping = topping
        self.price = price
        self.candles = candles
 
    def describe(self):
        print(f"이 케잌은 {self.coat}으로 덮여 있다.")
        print(f"토핑은 {self.topping}을 올려 장식했다.")
        print(f"가격은 {self.price}원이다.")
        if self.candles>0:
            print(f"초가 {self.candles}개 꽂혀 있다.")


def main():
    cake_truck=[]

    cake_truck.append(Cake("눈사람 사탕", 10000))
    cake_truck.append(Cake("한라봉", 9000, 8))

    for cake in cake_truck:
        print(Cake)
        cake.describe()


if __name__ == "__main__":
    main()
