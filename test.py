import compute
import parser


def test_computation(inputstring, expected_output):
    # -- ast  is Abstract Syntax Tree
    ast = parser.parse(inputstring)
    actual_result = compute.compute(ast)
    print(f'{inputstring} should evaluate to {expected_output}, actual result is {actual_result}')
    assert actual_result == expected_output


if __name__ == "__main__":
    test_computation('1+1', 2)
    test_computation('1-1', 0)
    test_computation('3-2+1', 2)
    test_computation('8/4/2', 1)
    test_computation('1*2', 2)
    test_computation('(1+7)*(9+2)', 88)
    test_computation('(2+7)/4', 2.25)
    test_computation('7/4', 1.75)
    test_computation('2*3+4', 10)
    test_computation('2*(3+4)', 14)
    test_computation('2+3*4', 14)
    test_computation('2+(3*4)', 14)
    test_computation('2-(3*4+1)', -11)
    test_computation('2*(3*4+1)', 26)
    test_computation('8/((1+3)*2)', 1)

    print (' --- native units is mm ---')
    test_computation('1+22', 23)
    test_computation('1+1in', 26.4)
    test_computation('in(1)+10.4', 35.8)
    test_computation('1+in(3-2)', 26.4)
    test_computation('1\'+3"', 381)
    test_computation('1/4', 0.25)
    test_computation('1/4 in', 6.35)
    test_computation('1/4 ft', 76.2)
    test_computation('in(10+1/4)', 260.34999999999997)
    
#    try:
#        test_computation('1+1)', 1)
#        raised = False
#    except Exception:
#        raised = True
#    assert raised

print (' -- done -- ')
