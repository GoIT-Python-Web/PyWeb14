from my_task import add

if __name__ == '__main__':
    result = add.delay(5, 5)
    print(result.id)
