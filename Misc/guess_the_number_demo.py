from Misc import guess_the_number as gtn

secret_number = gtn.get_number()
attempt = gtn.prompt_guess()

while not gtn.check_guess(attempt, secret_number):
    attempt = gtn.prompt_guess()
