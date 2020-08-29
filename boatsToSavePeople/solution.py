class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        weightMap = {}
        numberOfBoats = 0
        for person in people:
            if person > limit:
                continue
            if person == limit:
                numberOfBoats += 1
                continue
                
            secondperson = limit - person
            if secondperson in weightMap and weightMap[secondperson] >= 1:
                numberOfBoats += 1
                weightMap[secondperson] -= 1
            else:
                weightMap[person] = weightMap.get(person, 0) + 1
        
        for person in people:
            if person in weightMap and weightMap[person] > 0:
                weightMap[person] -= 1
                numberOfBoats += 1
        return numberOfBoats
                
            
        
#         for person in people:
#             weightMap[person] = weightMap.get(person,0) + 1
            
#         numberOfBoats = 0
        
#         for person in people:
#             if people > limit:
#                 continue
#             if people == limit:
#                 numberOfBoats += 1
#                 continue
            
#             secondperson = limit - person