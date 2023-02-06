def solution(id_pw, db):
    answer = ''
    db_dict = dict(db)
    
    try_id, try_pwd = id_pw
    
    if db_dict.get(try_id) == None :
        answer = "fail" 
        return answer
    
    if db_dict.get(try_id) != try_pwd :
        answer = "wrong pw" 
        return answer
    else :
        answer = "login"
        return answer
    
# def solution(id_pw, db):
#     try_id, try_pwd = id_pw
#     db_dict = dict(db)
#     if db_pw := db_dict.get(try_id):
#         return "login" if db_pw == try_pwd else "wrong pw"
#     return "fail"
    