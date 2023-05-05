from expression_calculator import ExpressionCalculator

my_calculator = ExpressionCalculator()

while True:

    prompt = "Введите выражение, например '7+1*2', которое необходимо сосчитать.\n"
    prompt += "Выражение: "

    #input_string = '+++93+*323-1+6+++'

    input_string = input(prompt)
    processing_output = my_calculator.input_processing(input_string)
    result = my_calculator.solve_expression(processing_output)

    print(f"Результат: {result}")

    is_repeat = input("Повторить ? (нет - для выхода): ")
    if is_repeat.lower() == 'нет':
        break













