import logging


def main():

    # setup named logger
    logger = logging.getLogger("nk_logger")
    logger.setLevel(logging.DEBUG)

    # Logging messages
    logging.debug("This is a DEBUG message")
    logging.info("This is an INFO message")
    logging.warning("This is a WARNING message")
    logging.error("This is an ERROR message")
    logging.critical("This is a CRITICAL message")

    nadeem: dict = {"first_name": "Nadeem", "last_name": "Khalid"}
    inaaya: dict = {"first_name": "Inaaya", "last_name": "Khalid"}
    rashida: dict = {"first_name": "Rashida", "last_name": "Khalid"}
    tiger: dict = {"first_name": "Tiger", "last_name": "Khalid"}
    # list of dictionaries
    name_list: list[dict] = []
    name_list.append(nadeem)
    name_list.append(inaaya)
    name_list.append(rashida)
    name_list.append(tiger)

    print(name_list)
    
    for name in name_list:
        print(f"first name -> {name['first_name']}")
        print(f"last name -> {name['last_name']}")

    print(f"count -> {len(name_list)}")

    # pop out inaaya from the name_list
    # get index of inaaya
    index = name_list.index(inaaya) 
    name_list.pop(index)

    for name in name_list:
        print(f"first name -> {name['first_name']}")
        print(f"last name -> {name['last_name']}")

    print(f"count -> {len(name_list)}")


if __name__ == "__main__":
    main()
