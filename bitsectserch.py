def bisectserch(f, ng, ok):
    """ 
    :param func f :
        判定に使用する関数
    :param int ok: 
        解が存在するindex, 値
    :param int ng: 
        解が存在しない値
    :rytpe int:
    """ 
    while abs(ok - ng) > 1:
        mid = (ok + ng) / 2  # 必要に応じて / → //
        if f(mid):
            ok = mid
        else:
            ng = mid
    return ok
