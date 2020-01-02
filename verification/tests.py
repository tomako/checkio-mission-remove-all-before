"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3,4,5], 3],
            "answer": [3, 4, 5],
            "explanation": "4 and 5 go after 3, which means should be removed"
        },
        {
            "input": [[1,1,2,2,3,3], 2],
            "answer": [2,2,3,3],
            "explanation": "only first '2' counts, the second '2' should be removed"
        },
        {
            "input": [[1,1,2,4,2,3,4], 2],
            "answer": [2,4,2,3,4],
        },
        {
            "input": [[1,1,5,6,7], 2],
            "answer": [1,1,5,6,7],
            "explanation": "Nothing should be removed if nothing is found"
        },
        {
            "input": [[], 0],
            "answer": [],
            "explanation": "Empty list stays unchanged"
        },
        {
            "input": [[7,7,7,7,7,7,7,7,7], 7],
            "answer": [7,7,7,7,7,7,7,7,7]
        }
    ],
    "Extra": [
        {
            "input": [[10, 1, 5, 6, 7, 10], 5],
            "answer": [5, 6, 7, 10],
        },
        {
            "input": [[1,2, 6,7,1,2,4,6,7,8,3,5,2,3], 6],
            "answer": [6,7,1,2,4,6,7,8,3,5,2,3],
        }
    ]
}
