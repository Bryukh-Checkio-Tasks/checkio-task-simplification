"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "(x-1)*(x+1)",
            "answer": "x*x-1"
        },
        {
            "input": "(x+1)*(x+1)",
            "answer": "x*x+2*x+1"
        },
        {
            "input": "(x+3)*x*2-x*x",
            "answer": "x*x+6*x"
        },

        {
            "input": "x+x*x+x*x*x",
            "answer": "x*x*x+x*x+x"
        },
        {
            "input": "(2*x+3)*2-x+x*x*x*x",
            "answer": "x*x*x*x+3*x+6"
        },

        {
            "input": "3+4*x-2-2*x",
            "answer": "2*x+1"
        },

        {
            "input": "x*(x+1)*(x+1)",
            "answer": "x*x*x+2*x*x+x"
        },

        {
            "input": "x*x*x*x*x+10-2",
            "answer": "x*x*x*x*x+8"
        },
        {
            "input": "(x-100)*(x+100)",
            "answer": "x*x-10000"
        },
        {
            "input": "(x+2)*(x+2)*(x+2)",
            "answer": "x*x*x+6*x*x+12*x+8"
        }

],
    "Extra": [
        {
            "input": "(x-1)*(x-1)",
            "answer": "x*x-2*x+1"
        },
        {
            "input": "(x+3)*(x+3)",
            "answer": "x*x+6*x+9"
        },
        {
            "input": "(x+4)*x*3-x*x",
            "answer": "2*x*x+12*x"
        },

        {
            "input": "x+x*x+x*x*x*x",
            "answer": "x*x*x*x+x*x+x"
        },
        {
            "input": "2*(2*x+3)-x+x*x*x*x",
            "answer": "x*x*x*x+3*x+6"
        },

        {
            "input": "3+4*x-24-2*x",
            "answer": "2*x-21"
        },

        {
            "input": "(x+1)*x*(x+1)",
            "answer": "x*x*x+2*x*x+x"
        },

        {
            "input": "x*x*x*x*x+100-2",
            "answer": "x*x*x*x*x+98"
        },
        {
            "input": "(x-500)*(x+500)",
            "answer": "x*x-250000"
        },
        {
            "input": "(x-2)*(x+2)*(x+2)",
            "answer": "x*x*x+2*x*x-4*x-8"
        }

    ]
}
