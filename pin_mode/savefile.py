# save seeds content to file
def saveSeeds(content, filename):
    with open(filename, 'w') as file:
        file.write(content)