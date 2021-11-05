class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates_dict = {}
        for employee_id, manager_id in enumerate(manager):
            if manager_id in subordinates_dict:
                subordinates_dict[manager_id].append(employee_id)
            else:
                subordinates_dict[manager_id] = [employee_id]
        def get_time(manager_id):
            if manager_id in subordinates_dict:
                return informTime[manager_id] + max(get_time(subordinate_id) for subordinate_id in subordinates_dict[manager_id])
            return 0
        return get_time(headID)
