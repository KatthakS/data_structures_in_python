class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d = {}
        for point in points:
            temp_tuple = (point[0], point[1])
            d[temp_tuple] = point[0] ** 2 + point[1] ** 2
        
        #dict(sorted(d.items(), key=lambda item: item[1]))
        print (d.keys())
        print(d)

        d= sorted(d.items(), key=lambda x: x[1])[:K]
        d = {k: v for k, v in d}
        return d.keys()