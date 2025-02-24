import random

def naive_shuffle(cards):
    counts = {}
    for _ in range(1000000):  # 洗一百萬次牌
        shuffled = cards.copy()  
        # 執行naive洗牌
        for i in range(len(shuffled)):
            n = random.randint(0, len(shuffled) - 1)  # 隨機洗牌
            shuffled[i], shuffled[n] = shuffled[n], shuffled[i]  # 交換
        # 計算count
        counts[tuple(shuffled)] = counts.get(tuple(shuffled), 0) + 1
    return counts

def fisher_yates_shuffle(cards):
    counts = {}
    for _ in range(1000000):  # 洗衣百萬次牌
        shuffled = cards.copy()  #
        # 執行Fisher-Yates
        for i in range(len(shuffled) - 1, 0, -1):
            n = random.randint(0, i)  # 隨機拿牌
            shuffled[i], shuffled[n] = shuffled[n], shuffled[i]  # 交換
        # 計算
        counts[tuple(shuffled)] = counts.get(tuple(shuffled), 0) + 1
    return counts

# 四張牌要洗
cards = [1, 2, 3, 4]


naive_counts = naive_shuffle(cards)
fisher_yates_counts = fisher_yates_shuffle(cards)

# 印出結果
print("Naive algorithm:")
for combination, count in naive_counts.items():
    print(f"{list(combination)}: {count}")

print("\nFisher–Yates shuffle:")
for combination, count in fisher_yates_counts.items():
    print(f"{list(combination)}: {count}")
