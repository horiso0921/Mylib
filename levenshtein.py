def levenshtein(s1, s2, INSERT, ERASE, REPLACE):
    """
    aNとbMの編集距離:
    方法１：a1…aN という文字列を b1…bM−1 に編集してから bM を挿入
    方法２：a1…aN−1 の部分を b1…bM に編集してから末尾の aN を削除
    方法３：a1…aN−1 の部分を b1…bM−1 に編集してから末尾の aN を bM に置換。（aN=bM なら置換は不要）

    ERASE = 削除のコスト
    INSERT = 挿入のコスト
    REPLACE = 置換のコスト
    """
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i * INSERT

    for j in range(m + 1):
        dp[0][j] = j * ERASE

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else REPLACE
            dp[i][j] = min( dp[i - 1][j] + ERASE,     # 削除
                            dp[i][j - 1] + INSERT,    # 挿入
                            dp[i - 1][j - 1] + cost)  # 置換

    return dp[n][m]
