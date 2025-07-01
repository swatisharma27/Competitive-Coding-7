import heapq

def get_min_conference_rooms(meetings):
    """
    TC:O(n log n + n log k) = O(n log n)
    AS:O(n)

    """
    # meetings = [[0,30], [5,10], [15,20]]

    min_heap = []

    # sort the list by start time
    meetings.sort(key=lambda x: x[0])


    if len(meetings) > 0:
        heapq.heappush(min_heap, meetings[0][1])

    for i in range(1, len(meetings)):

        if min_heap[0] < meetings[i][0]:
            heapq.heappop(min_heap)
            
        heapq.heappush(min_heap, meetings[i][1])

    return len(min_heap)

if __name__ == "__main__":
    meetings = [[0,30], [5,10], [15,20]]
    print(get_min_conference_rooms(meetings))

    meetings2 = [[0,30], [5,10], [15,20], [5,15], [25,40]]
    print(get_min_conference_rooms(meetings2))