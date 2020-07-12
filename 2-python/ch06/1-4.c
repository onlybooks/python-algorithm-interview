// C
bool isPalindrome(char *s) {
    int bias_left = 0;
    int bias_right = 1;

    int str_len = strlen(s);
    for (int i = 0; i < str_len; i++) {
        // 스킵 포인터 처리
        while (!isalnum(s[i + bias_left])) {
            bias_left++;
            if (i + bias_left == str_len)
                return true;
        }
        while (!isalnum(s[str_len - i - bias_right])) {
            bias_right++;
        }

        if (i + bias_left >= str_len - i - bias_right)
            break;
        // 팰린드롬 비교
        if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
            return false;
    }
    return true;
}