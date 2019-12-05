try:
    a_list_variable = []
    a_list_variable.extend(a_func_return_record())
except requests.ConnectionError as e:
    print("Упс!! Ошибка подключения к интернету.")
    print(str(e))
except requests.Timeout as e:
    print("Упс!! Время ожидания истекло.")
    print(str(e))
except requests.RequestException as e:
    print("Упс!! Возникла непредвиденная ошибка!")
    print(str(e))
except KeyboardInterrupt:
    print("Кто-то закрыл принудительно программу.")
finally:
    print("Total Records  = " + str(len(property_urls)))
    try:
        # файл для хранения URL
        record_file = open('records_file.txt', 'a+')
        record_file.write("\n".join(property_urls))
        record_file.close()
    except Exception as ex:
        print("Возникла ошибка при сохранении данных, текст ошибки:")
        print(str(e))