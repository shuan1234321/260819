a = 123
print(a)

a = "a"
print(a)

a = 123 + 123
print(a)

a = [1123, "sasd", 3, 5+3]
print(a)

var1 = 10
var2 = 20

a = var1 + var2
print(a)

input_var = input("숫자 하나 입력")
print(input_var)

#dictionary

questions = {"question":"답을 구하시오", "answer":153,"score":5, "isMultipleChoise":False}

question1 = {"no":1, "question": "답을구하시오", "answer": 153, "score": 5, "isMultipleChoice": False}

questions = [{"no":1, "question": "답을구하시오", "answer": 153, "score": 5, "isMultipleChoice": False},
             {"no":2, "question": "답으로 올바른것을 고르시오", "answer": 3, "score": 5, "isMultipleChoice": True, "example": [50, 30, 35, 20, 40]},
             {"no":3, "question": "답을구하시오", "answer": 153, "score": 5, "isMultipleChoice": False},
             {"no":4, "question": "답을구하시오", "answer": 153, "score": 5, "isMultipleChoice": False},
             {"no":5, "question": "답을구하시오", "answer": 153, "score": 5, "isMultipleChoice": False}]
question1 = {"no":1, "question": "답을구하시오", "answer": 153, "score": 5, "isMultipleChoice": False}

print("답?", question1["answer"])
questions = [{"no":1, "question": "답을 구하시오", "answer": 153, "score": 5, "isMultipleChoice": False},
             {"no":2, "question": "답으로 올바른것을 고르시오", "answer": 3, "score": 5, "isMultipleChoice": True, "example": [50, 30, 35, 20, 40]},
             {"no":3, "question": "답으로 올바른것을 고르시오", "answer": 4, "score": 5, "isMultipleChoice": True, "example": [50, 30, 35, 20, 40]},
             {"no":4, "question": "답으로 올바른것을 고르시오", "answer": 3, "score": 5, "isMultipleChoice": True,  "example": [50, 30, 35, 20, 40]},
             {"no":5, "question": "답으로 올바른것을 고르시오", "answer": 1, "score": 5, "isMultipleChoice": True,  "example": [50, 30, 35, 20, 40]}]
print(questions[1])
print(questions[1]["example"])
print(questions[1]["example"][0])


