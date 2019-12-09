#!/usr/bin/python


def recipe_batches(recipe, ingredients):

    batches = 0
    for item, needed in recipe.items():
        # If our recipe includes any ingredient not available, we can't make any batches
        if item not in ingredients:
            return 0

        # The amount we can make is determined by dividing what's on hand by what's needed
        amount = ingredients[item] // needed

        # If we don't have enough of any ingredient to make even one batch, return 0
        if amount == 0:
            return 0
        # If the amount we can make with the current ingredient is less than a previous one,
        # lower the number of batches we can make to the current amount. Or if batches is 0,
        # as when we first start, initialize batches to the first amount
        elif amount < batches or batches == 0:
            batches = amount

    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
