class ExpressionCalculator():

    def __init__(self):
        self.default_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.default_operators = ['+','-','*','/']


    def input_processing(self, my_string):

        my_numbers = []
        temp_str = ''

        for i in range(len(my_string)):
            # Сборка строки из принятых цифр
            if my_string[i] in self.default_numbers:
                temp_str += my_string[i]

                # Если последняя буква строки 
                if i == (len(my_string) - 1):
                    my_numbers.append(temp_str)

            elif (temp_str != ''):
                # Добавление оператора следующего за числом в список
                my_numbers.append(temp_str)
                my_numbers.append(my_string[i])
                temp_str = ''

        # Костыль, убирающий оператор после последнего числа списка, если он есть)
        last_index = len(my_numbers) - 1
        if not my_numbers[last_index].isnumeric():
            my_numbers.pop(last_index)

        return my_numbers


    def solve_expression(self, my_expression):
        """Принимает список, типа [операнд, оператор, операнд]"""
        expression = ''
        for one in my_expression:
            expression += one

        try:
            answer = eval(expression)
        except Exception:
            return "Что-то пошло не так. Попробуйте ввести другие данные!"
        else:
            return answer

