class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        from sortedcontainers import SortedSet
        self.cuisines = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))
        self.food_to_cuisine = dict()
        self.food_to_rating = dict()
        
        for index in range(len(foods)):
            _cuisine, food, rating = cuisines[index], foods[index], ratings[index]
            
            self.cuisines[_cuisine].add((rating, food))
            self.food_to_cuisine[food] = _cuisine
            self.food_to_rating[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating = self.food_to_rating[food]
        cuisine = self.food_to_cuisine[food]
        
        self.cuisines[cuisine].discard((old_rating, food))
        self.cuisines[cuisine].add((newRating, food))
        self.food_to_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)