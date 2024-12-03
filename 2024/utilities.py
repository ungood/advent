from IPython.display import display, Markdown

def display_puzzle(puzzle):
    display(Markdown(f"# Day {puzzle.day} - {puzzle.title}"))

    for i, example in enumerate(puzzle.examples):
        display(Markdown(f"## Example {i}"))
        print(example.input_data)
        
    display(Markdown(f"## Input Data"))
    print(puzzle.input_data)
        
def test_solution_a(puzzle, solution):
    pass