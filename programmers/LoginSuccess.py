def solution(id_pw, db):
    answer = ''
    db_dict = dict(db)
    
    try_id, try_pwd = id_pw
    
    db_pw = db_dict.get(try_id)
    
    if db_pw :
        return "login" if db_pw == try_pwd else "wrong pw"

    return "fail"
    
# def solution(id_pw, db):
#     try_id, try_pwd = id_pw
#     db_dict = dict(db)
#     if db_pw := db_dict.get(try_id):
#         return "login" if db_pw == try_pwd else "wrong pw"
#     return "fail"
    