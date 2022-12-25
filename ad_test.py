import animedata as ad

if __name__ == "__main__":
    ad.dev_mode = True
    ad.update_anime_lib()
    json_dict = ad.load_json(True)
    ad.save_json(json_dict)
    json_dict_2 = ad.load_json(False)
    print(ad.check_dict(json_dict))
    print(ad.check_dict(json_dict_2))
    if json_dict != json_dict_2:
        print("Something went wrong ...")