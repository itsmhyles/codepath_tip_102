'''
You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, where costs[i] is the cost of the ith supply item.
There is a special discount available during the expedition. If you purchase the ith item, you will receive a discount equivalent to costs[j], 
where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.
'''

def final_supply_costs(costs):
    final_costs = []
    
    for i in range(len(costs)):
        discounter = i+1
        if (discounter < len(costs)) and costs[discounter] < costs[i]:
            final_costs.append(costs[i]-costs[discounter])

        else:
            while len(final_costs) < i and discounter <len(costs):
                discounter +=1
                
                if costs[discounter] < costs[i]:
                    final_costs.append(costs[i]-costs[discounter])

                        
            final_costs.append(costs[i])
    
    return final_costs

print(final_supply_costs([8, 4, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6])) 