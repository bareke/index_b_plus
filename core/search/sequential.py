from django.conf import settings

"""
Sequential search of the product id
"""

def seq(product_id):
    position = 1
    with open(settings.PATH_FILE, 'r') as file:
        for line in file:
            if line.split()[0] == str(product_id):
                return product_id, line.split()[1], position
            position += 1
    return None


if __name__ == "__main__":
    product_id = 150

    product = seq(product_id)
    print("i got it!, id: {0}, price: {1}, and position: {2}".format(product[0], product[1], product[2]))
