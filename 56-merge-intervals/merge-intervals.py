class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []

        for start, end in intervals:
            events.append((start, 'start'))
            events.append((end, 'end'))

        # Sort events — if same time, 'start' comes before 'end'
        events.sort(key=lambda x: (x[0], 0 if x[1] == 'start' else 1))

        merged = []
        active = 0
        start_time = None

        for time, typ in events:
            if typ == 'start':
                if active == 0:
                    start_time = time
                active += 1
            else:  # 'end'
                active -= 1
                if active == 0:
                    merged.append([start_time, time])

        return merged
