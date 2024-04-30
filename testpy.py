def calculate_sum(numbers):
    total = sum(numbers)
    return total

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    numbers = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        num = float(input(f"Enter element {i+1}: "))
        numbers.append(num)

    sum_result = calculate_sum(numbers)
    average_result = calculate_average(numbers)

    print("Sum:", sum_result)
    print("Average:", average_result)

if __name__ == "__main__":
    main()


from django.http import HttpResponse


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator