def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = [[intervals['lesson'][0], intervals['lesson'][1]]]
    pupil = [[intervals['pupil'][i], intervals['pupil'][i + 1]] for i in range(0, len(intervals['pupil']), 2)]
    tutor = [[intervals['tutor'][i], intervals['tutor'][i + 1]] for i in range(0, len(intervals['tutor']), 2)]

    pupil_merged = merge_intervals(pupil)
    tutor_merged = merge_intervals(tutor)

    lesson_intervals = intersect_intervals(lesson, pupil_merged)
    final_intervals = intersect_intervals(lesson_intervals, tutor_merged)

    return sum(end - start for start, end in final_intervals)

def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

def intersect_intervals(intervals1, intervals2):
    i, j = 0, 0
    intersections = []
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]
        start_inter = max(start1, start2)
        end_inter = min(end1, end2)
        if start_inter < end_inter:
            intersections.append([start_inter, end_inter])
        if end1 < end2:
            i += 1
        else:
            j += 1
    return intersections

tests = [
    {'intervals': {
            'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {
            'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {
            'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'